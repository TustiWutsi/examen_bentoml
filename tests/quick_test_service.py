import requests
import jwt
from datetime import datetime, timedelta

# The URL of the login and prediction endpoints
login_url = "http://127.0.0.1:3000/login"
predict_url = "http://127.0.0.1:3000/v1/models/admission_lr/predict"

# Credentials & tokens information
credentials = {
    "username": "arthurbastide",
    "password": "helloworld"
}

# Data to be sent to the prediction endpoint
data = {
    "GRE_Score": 327,
    "TOEFL_Score": 107,
    "University_Rating": 3,
    "SOP": 3.5,
    "LOR": 4.5,
    "CGPA": 7.1,
    "Research": 1,
}

# Send a POST request to the login endpoint
login_response = requests.post(
    login_url,
    headers={"Content-Type": "application/json"},
    json=credentials
)

# Check if the login was successful
if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Token JWT obtenu:", token)

    # Send a POST request to the prediction
    response = requests.post(
        predict_url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        json=data
    )

    print("Réponse de l'API de prédiction:", response.text)
else:
    print("Erreur lors de la connexion:", login_response.text)