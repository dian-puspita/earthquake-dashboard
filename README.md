# 🌋 Earthquake Risk Dashboard – Indonesia

🔗 **[Demo Langsung – Streamlit App](https://earthquake-dashboard.streamlit.app/)**

**Dashboard interaktif berbasis Streamlit** untuk memvisualisasikan **probabilitas dan magnitudo gempa bumi di Indonesia** berdasarkan data historis dan hasil prediksi model machine learning.

> Dibuat oleh: **Delastrada Dian Puspita** – 2025  
> Dataset: BMKG (2015–2023) dan data turunan hasil pemodelan  
> Tools: `Python`, `Streamlit`, `Folium`, `Plotly`, `scikit-learn`

---

## Tujuan

Proyek ini bertujuan untuk:

- Memprediksi **rata-rata magnitudo** gempa berdasarkan lokasi (`latitude`, `longitude`, `depth`)
- Menghitung **probabilitas kejadian gempa** di setiap pulau besar di Indonesia melalui dua pendekatan:
  - **Random Forest Classifier** (prediksi probabilitas berdasarkan model)
  - **Perhitungan historis** (proporsi frekuensi gempa per pulau)

---

## Struktur Proyek

```

earthquake-dashboard/
│
├── app.py                             # Aplikasi Streamlit utama
├── outputs/
│   └── probabilitas\_dan\_prediksi\_magnitudo\_per\_pulau.csv
│
├── models/                            # (opsional) model RF pickle
├── requirements.txt                   # Daftar library Python
└── README.md                          # Dokumentasi proyek ini

````

---

## Cara Menjalankan

```bash
# Clone repo
git clone https://github.com/dian-puspita/earthquake-dashboard.git
cd earthquake-dashboard

# (Opsional) Buat environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependensi
pip install -r requirements.txt

# Jalankan Streamlit
streamlit run app.py
````

---

## Fitur Utama

* Tabel ringkasan probabilitas & magnitudo per pulau
* Grafik bar interaktif (probabilitas model vs historis)
* Perbandingan magnitudo prediksi vs historis
* **Peta interaktif**: label & ikon warna sesuai risiko
* Legenda visual untuk interpretasi risiko gempa

---

## Penjelasan Metodologi

* `Random Forest Regressor`: memprediksi magnitudo dari fitur spasial
* `Random Forest Classifier`: estimasi probabilitas gempa berdasarkan fitur input
* **Probabilitas Historis** dihitung manual:

  ```
  Probabilitas (%) = (Jumlah Gempa di Pulau X / Total Seluruh Gempa) × 100%
  ```

---

## Keterkaitan dengan Artikel Ilmiah

📄 Artikel ilmiah terkait:
**"Random Forest Analysis for Predicting the Probability of Earthquake in Indonesia"**
📰 Jurnal: *Social Science and Humanities Journal, Vol. 09 (2025)*
🔗 [Baca Artikel (Open Access)](https://doi.org/10.18535/sshj.v9i01.1574)

🧩 Penjelasan:

* Dalam artikel ilmiah, **Random Forest digunakan untuk memprediksi magnitudo gempa (regresi)**.
* Pada dashboard ini, **probabilitas gempa per pulau** ditampilkan menggunakan:

  * Hasil klasifikasi (model)
  * Frekuensi historis
* Visualisasi pada dashboard merupakan perluasan dari hasil ilmiah tersebut.

---

## 📦 Dataset yang Digunakan

File utama: `outputs/probabilitas_dan_prediksi_magnitudo_per_pulau.csv`
Berisi kolom:

| Kolom                      | Keterangan                                    |
| -------------------------- | --------------------------------------------- |
| `island`                   | Nama pulau                                    |
| `probability_model (%)`    | Probabilitas model (Random Forest Classifier) |
| `probability_historis (%)` | Probabilitas dari data historis               |
| `avg_predicted_mag`        | Prediksi magnitudo rata-rata (Random Forest)  |
| `avg_mag`                  | Rata-rata magnitudo historis                  |
| `freq`                     | Jumlah gempa historis                         |

---

## 📍 Visualisasi Peta

* Dibangun menggunakan `Folium`
* Menampilkan:

  * Label angka (nilai probabilitas)
  * Ikon warna berdasarkan tingkat risiko
  * Popup informasi per pulau
* Legenda visual membantu interpretasi tingkat risiko:

  * 🔴 Sangat Tinggi ≥ 25%
  * 🟠 Tinggi 15–24%
  * 🟢 Sedang 5–14%
  * 🔵 Rendah < 5%

---

## 📚 Ketergantungan

| Library            | Fungsi                                |
| ------------------ | ------------------------------------- |
| `streamlit`        | UI dashboard web                      |
| `pandas`           | Manipulasi data                       |
| `plotly.express`   | Visualisasi grafik interaktif         |
| `folium`           | Peta interaktif                       |
| `streamlit-folium` | Integrasi peta ke dashboard Streamlit |

---

## ⚖️ Lisensi

Proyek ini untuk keperluan edukasi dan penelitian.
Lisensi: [MIT License](LICENSE)

Silakan gunakan, modifikasi, dan kembangkan proyek ini sesuai kebutuhan.
Mohon tetap mencantumkan atribusi yang sesuai.
