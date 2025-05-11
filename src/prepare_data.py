import pandas as pd
import numpy as np
#import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('./data/raw/admission.csv')

df.drop(["Serial No."], axis=1, inplace=True)
df.dropna(inplace=True)

X = df.drop(["Chance of Admit "], axis=1)
y = df['Chance of Admit ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler().fit(X_train)
X_train = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

#scaler_path = 'src/artifacts/scaler.joblib'
#os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
#joblib.dump(scaler, 'src/artifacts/scaler.joblib')
#print("StandardScaler saved to src/artifacts/scaler.joblib")

X_train.to_csv("./data/processed/X_train.csv", index=False)
print('X_train saved to data/processed/X_train.csv')

X_test.to_csv("./data/processed/X_test.csv", index=False)
print('X_test saved to data/processed/X_test.csv')

y_train.to_csv("./data/processed/y_train.csv", index=False)
print('y_train saved to data/processed/y_train.csv')

y_test.to_csv("./data/processed/y_test.csv", index=False)
print('y_test saved to data/processed/y_test.csv')