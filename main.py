import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

#==============================================================================
# BUSINESS UNDERSTANDING
#==============================================================================
# Tujuan:
# - Mengelompokkan daerah berdasarkan jumlah siswa putus sekolah.
# - Menentukan pola yang dapat digunakan untuk intervensi kebijakan pendidikan.
#==============================================================================

def load_data():  
    #==============================================================================
    # DATA UNDERSTANDING
    #==============================================================================
    # Tujuan:
    # - Memahami struktur data yang berisi jumlah siswa putus sekolah di Indonesia.
    # - Data mencakup jumlah siswa putus sekolah per level pendidikan (SD, SMP, SMA, SMK).
    #==============================================================================
    file_path = "jumlah-siswa-putus-sekolah-updated.xlsx"
    data = pd.read_excel(file_path, sheet_name='Sheet1')
    
    return data

def preprocess_data(data):
    #==============================================================================
    # DATA PREPARATION
    #==============================================================================
    # Tujuan:
    # - Membersihkan dan menyiapkan data untuk analisis.
    # - Memilih data dari level Kabupaten/Kota.
    # - Mengganti nama kolom agar lebih representatif.
    #==============================================================================
    data = data[data['Level'] == 'Kabupaten/Kota']
    data = data.rename(columns={
        'Nama Kabupaten/Kota': 'Daerah',
        'Jumlah Putus SD': 'SD',
        'Jumlah Putus SMP': 'SMP',
        'Jumlah Putus SMA': 'SMA',
        'Jumlah Putus SMK': 'SMK'
    })
    return data

def perform_elbow_method(X):
    #==============================================================================
    # MODELING - Elbow Method
    #==============================================================================
    # Tujuan:
    # - Menentukan jumlah cluster optimal menggunakan metode Elbow.
    # - Menggunakan Within-Cluster Sum of Squares (WCSS) untuk evaluasi.
    #==============================================================================
    wcss = []
    k_range = range(1, 11)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    return k_range, wcss

def perform_clustering(X, k):
    #==============================================================================
    # MODELING - K-Means Clustering
    #==============================================================================
    # Tujuan:
    # - Mengelompokkan daerah berdasarkan jumlah siswa putus sekolah.
    # - Menggunakan algoritma K-Means untuk menentukan cluster terbaik.
    # - Menambahkan hasil cluster ke dalam dataset.
    #==============================================================================
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X)
    return clusters + 1  # Agar cluster dimulai dari 1

def main(): 
    st.set_page_config(
        page_title="Clustering Jumlah Siswa Putus Sekolah",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.title("Analisis Clustering Jumlah Siswa Putus Sekolah di Indonesia")

    datasetTab, elbowTab, clusteringTab, evaluationTab = st.tabs([
        "Data Siswa Putus Sekolah",
        "Elbow Method",
        "Clustering K-Means",
        "Evaluasi Data"
    ])

    raw_data = load_data()
    df = preprocess_data(raw_data)
    features = ['SD', 'SMP', 'SMA', 'SMK']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    with datasetTab:
        #==============================================================================
        # EVALUATION - Tinjauan Data
        #==============================================================================
        # Tujuan:
        # - Menampilkan data awal siswa putus sekolah untuk memahami distribusinya.
        #==============================================================================
        st.header("Data Siswa Putus Sekolah")
        st.dataframe(df.head())

    with elbowTab:
        st.header("Elbow Method")
        k_range, wcss = perform_elbow_method(X_scaled)
        
        fig, ax = plt.subplots()
        ax.plot(k_range, wcss, marker='o', linestyle='--')
        ax.set_xlabel('Jumlah Cluster')
        ax.set_ylabel('WCSS')
        ax.set_title('Elbow Method untuk Menentukan K Optimal')
        st.pyplot(fig)

    with clusteringTab:
        st.header("Clustering K-Means")
        k_optimal = st.slider("Pilih jumlah cluster", 2, 10, 3)
        df['Cluster'] = perform_clustering(X_scaled, k_optimal)
        st.write("## Hasil Clustering")
        st.dataframe(df[['Daerah', 'Cluster']])
        
        #==============================================================================
        # DEPLOYMENT - Menampilkan Hasil Clustering
        #==============================================================================
        # Tujuan:
        # - Menampilkan hasil clustering dalam bentuk tabel agregat.
        # - Membantu dalam analisis kebijakan pendidikan.
        #==============================================================================
        st.write("### Total Jumlah Siswa Putus Sekolah per Cluster")
        cluster_totals = df.groupby('Cluster')[features].sum()
        cluster_totals['Total'] = cluster_totals.sum(axis=1)
        st.dataframe(cluster_totals)
    
    with evaluationTab:
        st.header("Evaluasi Data")
        
        st.write("### Statistik Deskriptif")
        st.dataframe(df.describe())
        
        st.write("### Distribusi Data per Cluster")
        fig, ax = plt.subplots()
        sns.barplot(x=cluster_totals.index, y=cluster_totals["Total"], ax=ax)
        ax.set_xlabel("Cluster")
        ax.set_ylabel("Total Siswa Putus Sekolah")
        ax.set_title("Total Siswa Putus Sekolah per Cluster")
        st.pyplot(fig)
        
        st.write("### Rata-rata Jumlah Putus Sekolah per Cluster")
        cluster_means = df.groupby('Cluster')[features].mean()
        st.dataframe(cluster_means)

        # Hitung Silhouette Score
        silhouette_avg = silhouette_score(X_scaled, df['Cluster'])

        st.write(f"### Silhouette Score: {silhouette_avg:.3f}")

if __name__ == "__main__":
    main()
