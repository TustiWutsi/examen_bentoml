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

wrong_credentials = {
    "username": "wrong",
    "password": "wrong"
}

JWT_SECRET_KEY = "your_jwt_secret_key_here"
JWT_ALGORITHM = "HS256"

invalid_token = "invalid_token"

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

invalid_data = {
    "GRE_Score": 300,
    "TOEFL_Score": 100,
    "University_Rating": 5,
}

# Unit tests
def test_login_success():
    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failure():
    response = requests.post(login_url, json=wrong_credentials)
    assert response.status_code != 200
    #assert response.json()["detail"] == "Invalid credentials"

def test_predict_no_token():
    response = requests.post(predict_url, json={})
    assert response.status_code == 401
    assert response.json()["detail"] == "Missing authentication token"

def test_predict_invalid_token():
    headers = {f"Authorization": "Bearer {invalid_token}"}
    response = requests.post(predict_url, headers=headers, json={})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid token"

def test_predict_expired_token():
    expired_token = jwt.encode({
        "sub": "arthurbastide",
        "exp": datetime.utcnow() - timedelta(hours=1)
    }, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    headers = {"Authorization": f"Bearer {expired_token}"}
    response = requests.post(predict_url, headers=headers, json={})
    assert response.status_code == 401
    assert response.json()["detail"] == "Token has expired"

def test_predict_valid_request():
    login_response = requests.post(login_url, json=credentials)
    assert login_response.status_code == 200
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(predict_url, headers=headers, json=data)
    assert response.status_code == 200
    result = response.json()
    assert "prediction" in result
    assert "user" in result
    assert isinstance(result["prediction"], list)
    assert result["user"] == "arthurbastide"

def test_predict_invalid_payload():
    token = jwt.encode({
        "sub": "arthurbastide",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(predict_url, headers=headers, json=invalid_data)
    assert response.status_code == 400