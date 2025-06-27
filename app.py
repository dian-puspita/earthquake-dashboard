import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.features import DivIcon
from streamlit_folium import st_folium
from branca.element import MacroElement
from jinja2 import Template

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Gempa Indonesia", layout="wide")

# Judul
st.title("🌋 Dashboard Risiko Gempa di Indonesia per Pulau")

# Load data hasil
df = pd.read_csv('outputs/probabilitas_dan_prediksi_magnitudo_per_pulau.csv')

# Sidebar: Filter Pulau
selected_islands = st.sidebar.multiselect(
    "Pilih pulau yang ingin ditampilkan:",
    df['island'].unique(),
    default=df['island'].unique()
)
filtered_df = df[df['island'].isin(selected_islands)]

# TABEL HASIL
st.subheader("📊 Ringkasan Probabilitas & Magnitudo per Pulau")
st.dataframe(
    filtered_df.style.format({
        'probability_model (%)': '{:.2f}%',
        'probability_historis (%)': '{:.2f}%',
        'avg_predicted_mag': '{:.2f}',
        'avg_mag': '{:.2f}',
        'freq': '{:,.0f}'
    }),
    use_container_width=True
)

# GRAFIK PROBABILITAS
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🔮 Probabilitas Model")
    fig_model = px.bar(filtered_df.sort_values('probability_model (%)', ascending=True),
                       x='probability_model (%)', y='island',
                       orientation='h', color='probability_model (%)',
                       color_continuous_scale='Reds')
    st.plotly_chart(fig_model, use_container_width=True)

with col2:
    st.markdown("### 🧾 Probabilitas Historis")
    fig_hist = px.bar(filtered_df.sort_values('probability_historis (%)', ascending=True),
                      x='probability_historis (%)', y='island',
                      orientation='h', color='probability_historis (%)',
                      color_continuous_scale='Blues')
    st.plotly_chart(fig_hist, use_container_width=True)

# GRAFIK MAGNITUDO
st.markdown("### 📈 Rata-Rata Magnitudo: Prediksi vs Historis")
fig_mag = px.bar(filtered_df,
                 x='island',
                 y=['avg_predicted_mag', 'avg_mag'],
                 barmode='group',
                 labels={'value': 'Magnitudo', 'variable': 'Tipe'},
                 text_auto=True)
st.plotly_chart(fig_mag, use_container_width=True)

# PETA INTERAKTIF
st.subheader("🗺️ Peta Interaktif Risiko Gempa per Pulau")

# Koordinat tengah tiap pulau
island_coords = {
    'Sumatera': [-0.5, 102],
    'Jawa': [-7.0, 111],
    'Bali': [-8.34, 115.09],
    'Nusa Tenggara': [-8.6, 119],
    'Kalimantan': [0.5, 114],
    'Sulawesi': [-1.5, 121.5],
    'Maluku': [-3.0, 129],
    'Papua': [-4.0, 138.5],
}

# Fungsi warna ikon
def get_icon_color(prob):
    if prob >= 25:
        return "darkred"
    elif prob >= 15:
        return "orange"
    elif prob >= 5:
        return "green"
    else:
        return "blue"

# Inisialisasi peta
m = folium.Map(location=[-2.5, 117], zoom_start=5, tiles="CartoDB positron")

# Tambah marker dan label
for _, row in filtered_df.iterrows():
    island = row['island']
    lat, lon = island_coords.get(island, [None, None])
    if lat is None: continue

    prob = row['probability_model (%)']
    icon_color = get_icon_color(prob)

    # Label angka %
    folium.Marker(
        location=[lat + 0.7, lon],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(0, 0),
            html=f"""
                <div style='font-size:13px;
                            color:black;
                            font-weight:bold;
                            text-shadow: 0px 0px 2px #fff'>
                    {prob:.1f}%
                </div>
            """
        )
    ).add_to(m)

    # Popup
    popup_text = (
        f"<b>{island}</b><br>"
        f"Probabilitas Model: <b>{prob:.2f}%</b><br>"
        f"Probabilitas Historis: {row['probability_historis (%)']:.2f}%<br>"
        f"Magnitudo Prediksi: {row['avg_predicted_mag']:.2f}<br>"
        f"Magnitudo Historis: {row['avg_mag']:.2f}<br>"
        f"Frekuensi Gempa: {int(row['freq'])}"
    )

    # Ikon warna + popup
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(icon='globe', prefix='fa', color=icon_color),
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(m)

# Tambahkan Legenda
legend_html = """
<div style="
    position: fixed; 
    bottom: 20px; left: 50px; width: 220px; z-index:9999; 
    background-color: white;
    border: 2px solid grey;
    border-radius: 8px;
    padding: 10px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    font-size: 13px;
    color: black;
">
    <b>🌍 Legenda Warna Ikon</b><br>
    <svg width="12" height="12"><circle cx="6" cy="6" r="6" fill="darkred" /></svg> &nbsp; ≥ 25% (Sangat Tinggi)<br>
    <svg width="12" height="12"><circle cx="6" cy="6" r="6" fill="orange" /></svg> &nbsp; 15–24% (Tinggi)<br>
    <svg width="12" height="12"><circle cx="6" cy="6" r="6" fill="green" /></svg> &nbsp; 5–14% (Sedang)<br>
    <svg width="12" height="12"><circle cx="6" cy="6" r="6" fill="blue" /></svg> &nbsp; &lt; 5% (Rendah)
</div>
"""

class FloatLegend(MacroElement):
    def __init__(self, html):
        super().__init__()
        self._template = Template("""
            {% macro html(this, kwargs) %}
            """ + html + """
            {% endmacro %}
        """)

m.get_root().add_child(FloatLegend(legend_html))

# Tampilkan peta
st_data = st_folium(m, width=800, height=500)

# Footer
st.markdown("---")
st.markdown("📍 Dibuat oleh: Delastrada Dian Puspita — 2025")
