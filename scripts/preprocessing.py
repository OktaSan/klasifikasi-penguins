import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load data engineered
data = pd.read_csv('data/engineered_penguins.csv')

# Fitur numerik dan kategori
num_features = ['bill_length_mm', 'flipper_length_mm', 'body_mass_g', 'bill_ratio']
cat_features = ['island', 'sex']

# Pipeline untuk scaling dan encoding
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first'), cat_features)
])

# Fit & transform data
X = data.drop('species', axis=1)
y = data['species']

X_transformed = preprocessor.fit_transform(X)

# Convert hasilnya ke DataFrame
final_data = pd.DataFrame(X_transformed, columns=preprocessor.get_feature_names_out())
final_data['species'] = y

# Simpan ke final_penguins.csv
final_data.to_csv('data/final_penguins.csv', index=False)