import numpy as np
import joblib

pca = joblib.load(
    "models/pca_model.pkl"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

def reduce_dimension(
    age,
    income,
    score
):

    data = np.array(
        [
            [age, income, score]
        ]
    )

    scaled_data = scaler.transform(data)

    transformed = pca.transform(
        scaled_data
    )

    return transformed[0]