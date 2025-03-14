# **Analisis Data Penguin**

## **Deskripsi Proyek**
Repositori ini berisi analisis data mengenai spesies penguin yang ditemukan di Antartika, menggunakan dataset yang mencakup berbagai fitur terkait fisik penguin dan lokasi pengamatan mereka. Tujuan utama dari proyek ini adalah untuk mengeksplorasi dataset menggunakan analisis eksplorasi data (EDA), memvisualisasikan hubungan antar fitur, serta membangun model prediksi untuk mengidentifikasi spesies penguin berdasarkan karakteristik fisiknya.

## **Fitur Utama**
- **Eksplorasi Data**: Menyediakan analisis deskriptif dan statistik dasar dari dataset penguin, termasuk pencarian nilai yang hilang dan analisis outlier.
- **Visualisasi Data**: Menggunakan berbagai teknik visualisasi seperti histogram, boxplot, bar chart, scatter plot, dan heatmap untuk memahami distribusi data dan hubungan antar fitur.

## **Struktur Repository**
```
penguins-analysis/
│
├── data/
│   ├── penguins.csv          # Dataset asli penguin
│   ├── penguins_cleaned.csv  # Dataset yang telah dibersihkan dan diproses
│   ├── engineered_penguins.csv # Dataset yang telah ditambahkan features baru
│   ├── final_penguins.csv # Dataset final yang siap digunakan untuk Machine Learning
├── notebooks/
│   ├── EDA.py             # Notebook untuk eksplorasi data awal
│
├── scripts/
│   ├── cleaning.py      # Skrip untuk pembersihan dan persiapan data
│
├── reports/
│
└── README.md                 # Deskripsi proyek dan instruksi penggunaan
```

## **Instalasi**
Untuk menjalankan proyek ini, pastikan kamu memiliki Python dan beberapa library utama yang digunakan dalam analisis data. Berikut adalah instruksi untuk menginstal dependensi:

1. **Clone repository**:
   ```bash
   git clone https://github.com/OktaSan/klasifikasi-penguins.git
   cd klasifikasi-penguins
   ```

2. **Buat virtual environment dan aktifkan**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/MacOS
   venv\Scripts\activate     # Untuk Windows
   ```

## **Dependensi**
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## **Hasil dan Rekomendasi**
Hasil analisis menunjukkan bahwa terdapat hubungan yang signifikan antara panjang flipper, panjang bill, dan berat tubuh dengan spesies penguin. Berdasarkan eksplorasi data dan pelatihan model, rekomendasi utama adalah untuk menggunakan model Random Forest untuk prediksi spesies penguin, yang memberikan hasil yang lebih baik dibandingkan model lain yang diuji.
