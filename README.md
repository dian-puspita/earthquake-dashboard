# 🌋 Earthquake Risk Dashboard – Indonesia

**Dashboard interaktif berbasis Streamlit** untuk memvisualisasikan **probabilitas gempa bumi di Indonesia** berdasarkan data historis dan hasil prediksi model machine learning.

> Dibuat oleh: **Delastrada Dian Puspita** – 2025
> Dataset: BMKG dan data turunan hasil pemodelan
> Tools: `Python`, `Streamlit`, `Folium`, `Plotly`, `scikit-learn`

---

## Fitur Utama

* Tabel ringkasan probabilitas dan magnitudo per pulau
* Grafik bar interaktif untuk probabilitas model dan historis
* Perbandingan magnitudo prediksi vs historis
* **Peta interaktif** dengan popup informasi & label probabilitas
* Legenda visual untuk interpretasi warna ikon

---

## Struktur Proyek

```
earthquake-dashboard/
│
├── app.py                             # Aplikasi Streamlit utama
├── outputs/
│   └── probabilitas_dan_prediksi_magnitudo_per_pulau.csv
│
├── models/                            # (opsional) folder model .pkl jika dibutuhkan
│
├── requirements.txt                   # Daftar library Python
└── README.md                          # Dokumentasi proyek ini
```

---

## Cara Menjalankan

### 1. Clone repositori

```bash
git clone https://github.com/dian-puspita/earthquake-dashboard.git
cd earthquake-dashboard
```

### 2. Buat dan aktifkan environment (opsional)

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi Streamlit

```bash
streamlit run app.py
```

---

## Tentang Dataset

File CSV yang digunakan:
`outputs/probabilitas_dan_prediksi_magnitudo_per_pulau.csv`

Berisi kolom:

* `island`: Nama pulau
* `probability_model (%)`: Probabilitas gempa berdasarkan model (Random Forest)
* `probability_historis (%)`: Probabilitas berdasarkan frekuensi historis
* `avg_predicted_mag`: Rata-rata magnitudo hasil prediksi
* `avg_mag`: Rata-rata magnitudo historis
* `freq`: Jumlah kejadian gempa historis

---

## Visualisasi Peta

* Peta menggunakan **Folium** (leaflet.js).
* Setiap pulau diberi:

  * **Label angka**: menampilkan nilai probabilitas model
  * **Ikon berwarna**: menunjukkan tingkat risiko gempa (warna tergantung probabilitas)
  * **Popup**: menampilkan detail lengkap per pulau
* Legenda di bagian kiri bawah membantu interpretasi warna ikon.

---

## Ketergantungan

| Library            | Fungsi                                       |
| ------------------ | -------------------------------------------- |
| `streamlit`        | UI web app dashboard                         |
| `pandas`           | Manipulasi data CSV                          |
| `folium`           | Peta interaktif berbasis leaflet             |
| `plotly.express`   | Grafik interaktif (bar chart, grouped chart) |
| `streamlit-folium` | Integrasi peta Folium di Streamlit           |

---

## Lisensi

Proyek ini untuk keperluan edukasi dan penelitian. Silakan gunakan, modifikasi, dan kembangkan sesuai kebutuhan.

---
