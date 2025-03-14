import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset penguins.csv ke dalam DataFrame pandas
print("Memuat dataset...")
df = pd.read_csv('data/penguins_cleaned.csv')

# Menampilkan informasi dasar tentang DataFrame
print("\nInformasi Dasar Dataset:")
print("------------------------")
print("Tipe data dan jumlah non-null:")
print(df.info())  # Menampilkan tipe data setiap kolom dan jumlah nilai non-null
print("\nStatistik deskriptif:")
print(df.describe())  # Menampilkan statistik deskriptif untuk kolom numerik

# Visualisasi distribusi data menggunakan pair plot
print("\nMembuat visualisasi pair plot...")
sns.pairplot(df, hue='species')  # Membuat pair plot dengan warna berdasarkan spesies
plt.savefig("distribusi_data.png")  # Menyimpan plot ke file cek.png
print("Visualisasi pair plot berhasil disimpan sebagai cek.png!")

# Mengecek missing value di setiap kolom
print("\nJumlah Missing Value per Kolom:")
print("-----------------------------")
print(df.isnull().sum())  # Menampilkan jumlah missing value di setiap kolom
print("\nAnalisis selesai!")