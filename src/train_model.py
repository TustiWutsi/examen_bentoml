import pandas as pd
import numpy as np
import bentoml
from sklearn.linear_model import LinearRegression

X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv')
y_test = pd.read_csv('data/processed/y_test.csv')

model = LinearRegression()
model.fit(X_train, y_train)
model.predict(X_test)
r2 = model.score(X_test, y_test)
print(f"Model R2 score: {r2}")

model_ref = bentoml.sklearn.save_model("admission_lr", model)
print(f"Modèle enregistré sous : {model_ref}")