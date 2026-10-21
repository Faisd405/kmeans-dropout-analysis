# kmeans-dropout-analysis

A Streamlit app that groups Indonesian regencies and cities by their number of school dropouts, using K-Means clustering. Built as a university data-mining assignment following CRISP-DM.

## Why

Dropout counts by region are easier to act on when similar regions are grouped together. The project clusters regencies/cities by their dropout profile across school levels (SD, SMP, SMA, SMK), so regions with similar patterns can be compared and discussed together.

## Dataset

- File: `jumlah-siswa-putus-sekolah-updated.xlsx` (the app reads this one). The same data is also in `.csv`.
- Columns: `No`, `Daerah` (region name), `Level` (`Provinsi` or `Kabupaten/Kota`), `SD`, `SMP`, `SMA`, `SMK` (dropout counts per school level).
- Coverage: 34 province rows and 514 regency/city rows across Indonesia. The data contains aggregate counts only, with no individual records.
- Only the `Kabupaten/Kota` rows are used for clustering.

## Method

1. Load the Excel sheet and keep the `Kabupaten/Kota` rows.
2. Features: `SD`, `SMP`, `SMA`, `SMK`, standardised with scikit-learn `StandardScaler`.
3. Elbow method: K-Means for k = 1..10 (`random_state=42`, `n_init=10`), with WCSS (inertia) plotted.
4. Clustering: K-Means with a user-selected k (slider 2-10, default 3). Cluster labels start at 1.
5. Evaluation: silhouette score on the scaled features, plus per-cluster totals and means.

The code does not handle missing values and adds no engineered features.

## App tabs

- **Data Siswa Putus Sekolah**: preview of the filtered data
- **Elbow Method**: WCSS plot for k = 1..10
- **Clustering K-Means**: k slider, region-to-cluster table, total dropouts per cluster
- **Evaluasi Data**: descriptive statistics, bar chart of totals per cluster, mean per cluster, silhouette score

## Tech stack

Python, Streamlit, pandas, NumPy, scikit-learn, seaborn, matplotlib, openpyxl (pinned in `requirements.txt`).

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Run from the repo root so `main.py` can find the Excel file. No environment variables are needed.

## Project structure

```
main.py                                    # whole app: load, preprocess, elbow, clustering, evaluation
jumlah-siswa-putus-sekolah-updated.xlsx    # dataset used by the app
jumlah-siswa-putus-sekolah-updated.csv     # same data as CSV
requirements.txt
```

## Testing

There are no automated tests. The app has only been checked by running it.

## Known gaps

- Clustering uses raw counts, so populous regions dominate. Per-capita rates would compare regions more fairly.
- The elbow plot and silhouette score are shown, but k is still chosen by hand.
- The dataset's original source and year are not documented in the repo.
