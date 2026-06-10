import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv(
    "data/processed/cleaned_data.csv"
)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(df)

pca = PCA(
    n_components=2
)

pca.fit(X_scaled)

joblib.dump(
    pca,
    "models/pca_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("PCA model trained successfully.")