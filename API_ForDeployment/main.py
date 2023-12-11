# from joblib import load
import pickle
# from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Créer une instance FastAPI
app = FastAPI()

# Charger le modèle formé pour la classification des URL
loaded_model = pickle.load(open('phishingLR.pkl', 'rb'))

# Modèle de données pour la requête
class UrlRequest(BaseModel):
    url: str

# Définir le point de terminaison
@app.post("/predict-url")
def predict_url(data: UrlRequest):
    # Nouvelles données sur lesquelles on fait la prédiction
    new_data = [[data.url]]

    # Prédiction
    prediction = loaded_model.predict(new_data)[0]

    # Retourner le résultat de la prédiction
    return {'prediction': prediction}
