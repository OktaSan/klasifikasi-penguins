import pandas as pd
import numpy as np 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('data/penguins_cleaned.csv')

num_features = df.select_dtypes(include=['float64']).columns
cat_features = df.select_dtypes(include=['object']).columns


num_features