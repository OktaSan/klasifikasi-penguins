import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# 1. Memuat Dataset yang Sudah Dibersihkan
df = pd.read_csv('data/penguins_cleaned.csv')

# 2. Mengidentifikasi Fitur Numerik dan Kategorikal
num_features = df.select_dtypes(include=['float64']).columns  
cat_features = df.select_dtypes(include=['object']).columns   

# 3. Membuat Pipeline untuk Fitur Numerik
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# 4. Membuat Pipeline untuk Fitur Kategorikal
cat_pipeline = Pipeline([
    ('encoder', OneHotEncoder(drop='first'))
])

# 5. Membuat Pipeline Lengkap dengan ColumnTransformer
full_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

# 6. Melakukan Preprocessing Data
data_preprocessed = full_pipeline.fit_transform(df)

# 7. Membuat DataFrame dari Hasil Preprocessing
data_final = pd.DataFrame(data_preprocessed)

# 8. Menyimpan DataFrame Hasil Preprocessing ke File CSV
data_final.to_csv('data/penguins_final.csv', index=False)

# 9. Menyimpan Model Pipeline untuk Penggunaan Selanjutnya
joblib.dump(full_pipeline, 'models/penguins_pipeline.pkl')