import pandas as pd

df = pd.read_csv('data/penguins_cleaned.csv')

# buat fitur baru rasio panjang paruh
df['bill_ratio'] = df['bill_length_mm'] / df['bill_depth_mm']

# ambil fitur yang berkorelasi tinggi
update_features = [
    'bill_length_mm',
    'flipper_length_mm',
    'body_mass_g',
    'bill_ratio',
    'species',
    'island',
    'sex' 
]

df_engineering = df[update_features]

# Simpan hasilnya
df_engineering.to_csv('data/engineered_penguins.csv', index=False)