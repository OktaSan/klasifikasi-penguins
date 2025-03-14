import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data cleaned
df = pd.read_csv('data/engineered_penguins.csv')

num_df = df.select_dtypes(exclude=['object'])

# Tampilkan heatmap korelasi
plt.figure(figsize=(8,6))
sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('final_penguins_heatmap.png')
