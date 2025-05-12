import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import bentoml

df = pd.read_csv('./data/raw/admission.csv')

df = df.rename(columns={
    "Chance of Admit ": "Chance of Admit",
    "GRE Score": "GRE_Score",
    "TOEFL Score": "TOEFL_Score",
    "University Rating": "University_Rating",
    "LOR ": "LOR"
})

df.drop(["Serial No."], axis=1, inplace=True)
df.dropna(inplace=True)

X = df.drop(["Chance of Admit"], axis=1)
y = df["Chance of Admit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler().fit(X_train)
X_train = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

X_train.to_csv("./data/processed/X_train.csv", index=False)
print('X_train saved to data/processed/X_train.csv')

X_test.to_csv("./data/processed/X_test.csv", index=False)
print('X_test saved to data/processed/X_test.csv')

y_train.to_csv("./data/processed/y_train.csv", index=False)
print('y_train saved to data/processed/y_train.csv')

y_test.to_csv("./data/processed/y_test.csv", index=False)
print('y_test saved to data/processed/y_test.csv')

scaler_ref = bentoml.sklearn.save_model("standard_scaler", scaler)
print(f"Modèle enregistré sous : {scaler_ref}")