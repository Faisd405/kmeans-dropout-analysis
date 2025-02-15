# Data Mining
Analisis Clustering Jumlah Siswa Putus Sekolah di Indonesia Menggunakan Metode K-Means Berbasis CRISP-DM

## 📋 Deskripsi
Aplikasi ini bertujuan untuk menganalisis dan mengelompokkan jumlah siswa putus sekolah di Indonesia menggunakan metode K-Means Clustering berdasarkan pendekatan CRISP-DM. Dengan menggunakan dataset yang relevan, aplikasi ini dapat membantu dalam memahami pola dan tren dari data siswa putus sekolah.

## 🚀 Fitur Utama
- **Preprocessing Data**: Pembersihan dan transformasi data sebelum analisis.
- **Clustering dengan K-Means**: Mengelompokkan data berdasarkan karakteristik tertentu.
- **Visualisasi Data**: Menampilkan hasil clustering dalam bentuk grafik dan diagram.
- **Evaluasi Model**: Menggunakan metode evaluasi seperti elbow method dan silhouette score.
- **Aplikasi Interaktif**: Antarmuka berbasis Streamlit untuk eksplorasi data.

## 💻 Teknologi yang Digunakan
- Python 3.12+
- Streamlit
- Scikit-learn
- Pandas
- Numpy
- Seaborn
- Matplotlib

## 📦 Cara Instalasi

### 1. Clone Repository
```bash
git clone [URL_REPOSITORY_ANDA]
cd [NAMA_FOLDER_PROJECT]
```

### 2. Buat Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run main.py
```

## 📊 Struktur Data
Data yang digunakan mencakup informasi jumlah siswa putus sekolah berdasarkan berbagai kategori, seperti:
- Provinsi
- Jenis Kelamin
- Tahun Ajaran
- Tingkat Pendidikan (SD, SMP, SMA)

## 📈 Metodologi
Aplikasi menggunakan pendekatan **CRISP-DM** (Cross-Industry Standard Process for Data Mining) yang terdiri dari:
1. **Business Understanding**: Memahami permasalahan dan tujuan analisis.
2. **Data Understanding**: Mengumpulkan dan mengeksplorasi data.
3. **Data Preparation**: Pembersihan dan transformasi data.
4. **Modeling**: Menerapkan algoritma K-Means Clustering.
5. **Evaluation**: Menilai performa model clustering.
6. **Deployment**: Menyediakan hasil analisis dalam bentuk aplikasi interaktif.

## 📱 Tampilan Aplikasi
Aplikasi ini terdiri dari beberapa tab utama:
- **Dashboard**: Visualisasi data dan clustering.
- **Eksplorasi Data**: Statistik dan informasi dasar tentang dataset.
- **Modeling**: Konfigurasi dan hasil dari model clustering.
- **Evaluasi Model**: Metrik evaluasi seperti elbow method dan silhouette score.

## ⚙️ Requirements
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.2.0
seaborn>=0.12.0
matplotlib>=3.6.0
```

## 🤝 Kontribusi
Silakan berkontribusi dengan:
1. Fork repository
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 🙏 Ucapan Terima Kasih
- **Streamlit** untuk framework visualisasi interaktif.
- **Scikit-learn** untuk implementasi K-Means Clustering.
- **Pandas & Numpy** untuk manipulasi data.
- **Seaborn & Matplotlib** untuk visualisasi data.

## 📚 Teori dan Metodologi

### 1. Clustering dengan K-Means
K-Means adalah metode unsupervised learning yang digunakan untuk mengelompokkan data berdasarkan kesamaan fitur.

#### Rumus Dasar K-Means:
```
J = Σ Σ || x_i - c_j ||²
```
Dimana:
- `x_i` adalah data ke-i
- `c_j` adalah centroid cluster j
- `J` adalah fungsi objektif yang diminimalkan

#### Langkah-langkah K-Means:
1. Pilih jumlah cluster `k`.
2. Inisialisasi centroid secara acak.
3. Hitung jarak setiap titik data ke centroid.
4. Kelompokkan data berdasarkan centroid terdekat.
5. Perbarui centroid berdasarkan rata-rata titik dalam cluster.
6. Ulangi langkah 3-5 hingga konvergen.

### 2. Evaluasi Model

#### 1. Elbow Method
Digunakan untuk menentukan jumlah cluster optimal dengan melihat perubahan inertia:
```
Inertia = Σ || x_i - c_j ||²
```
Jika perubahan inertia mulai melambat pada titik tertentu, jumlah cluster tersebut dianggap optimal.

#### 2. Silhouette Score
Mengukur seberapa baik setiap titik dalam cluster dibandingkan dengan cluster lain.
```
S = (b - a) / max(a, b)
```
Dimana:
- `a` = rata-rata jarak ke anggota cluster yang sama.
- `b` = rata-rata jarak ke anggota cluster terdekat lainnya.

Silhouette Score berkisar antara -1 hingga 1, di mana nilai mendekati 1 menunjukkan cluster yang baik.

### 3. Pra-pemrosesan Data
- **Mengatasi Missing Values**: Menggunakan imputasi mean atau median.
- **Normalisasi Data**: Standarisasi menggunakan Min-Max Scaling atau Z-score.
- **Pembuatan Fitur**: Menambah fitur baru untuk meningkatkan akurasi model.

### 4. Visualisasi Data
- **Scatter Plot** untuk melihat distribusi cluster.
- **Heatmap** untuk melihat korelasi antar fitur.
- **Histogram** untuk distribusi fitur individu.

## 🎯 Kesimpulan
- K-Means berhasil mengelompokkan data siswa putus sekolah dengan pola yang dapat dianalisis lebih lanjut.
- Evaluasi menggunakan Elbow Method dan Silhouette Score membantu dalam pemilihan jumlah cluster optimal.
- Visualisasi data memberikan wawasan yang lebih mendalam tentang tren dan pola dalam dataset.
