import pandas as pd
import numpy as np

# 1. Memuat Dataset
print("Memuat dataset penguins.csv...")
df = pd.read_csv('data/penguins.csv')
print("Dataset berhasil dimuat.")

# 2. Menghapus Nilai Null (Missing Values)
print("\nMenghapus baris dengan nilai null...")
df_cleaned = df.dropna()  
print("Baris dengan nilai null telah dihapus.")

# 3. Menampilkan Jumlah Nilai Null Setelah Penghapusan
print("\nJumlah nilai null setelah penghapusan:")
print(df_cleaned.isnull().sum())  

# 4. Menghapus Baris Duplikat
print("\nMenghapus baris duplikat...")
df_cleaned = df_cleaned.drop_duplicates()  
print("Baris duplikat telah dihapus.")

# 5. Menampilkan Jumlah Baris Duplikat Setelah Penghapusan
print("\nJumlah baris duplikat setelah penghapusan:")
print(df_cleaned.duplicated().sum())  

# 6. Menghapus featrures yang tidak penting
print("\nHapus features yang tidak penting:")
df_cleaned = df_cleaned.drop(df_cleaned[['id', 'year']], axis=1)
print(df_cleaned.head())

# 7. Menyimpan DataFrame yang Sudah Dibersihkan ke File CSV Baru
print("\nMenyimpan DataFrame yang sudah dibersihkan ke penguins_cleaned.csv...")
df_cleaned.to_csv('data/penguins_cleaned.csv', index=False)  
print("DataFrame berhasil disimpan ke penguins_cleaned.csv.")

print("\nPembersihan data selesai.")