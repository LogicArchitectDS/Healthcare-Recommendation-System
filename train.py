import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_model():
    # Load dataset
    if not os.path.exists('Cleaned_Dataset.csv'):
        print("Error: Cleaned_Dataset.csv not found.")
        return

    df = pd.read_csv('Cleaned_Dataset.csv')

    # Define features and target
    features = ['fever', 'cough', 'fatigue', 'difficulty_breathing', 'age', 'gender', 'blood_pressure', 'cholesterol_level']
    target = 'disease'

    X = df[features].copy()
    y = df[target].copy()

    # Preprocessing
    encoders = {}
    categorical_cols = ['fever', 'cough', 'fatigue', 'difficulty_breathing', 'gender']
    
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        encoders[col] = le

    # Encode target variables
    le_disease = LabelEncoder()
    y_disease = le_disease.fit_transform(df['disease'])
    encoders['disease'] = le_disease

    le_risk = LabelEncoder()
    y_risk = le_risk.fit_transform(df['risk_level'])
    encoders['risk_level'] = le_risk

    # Split data
    X_train, X_test, y_disease_train, y_disease_test, y_risk_train, y_risk_test = train_test_split(
        X, y_disease, y_risk, test_size=0.2, random_state=42
    )

    # Train Disease Prediction Model
    disease_model = RandomForestClassifier(n_estimators=100, random_state=42)
    disease_model.fit(X_train, y_disease_train)

    # Train Risk Prediction Model
    risk_model = RandomForestClassifier(n_estimators=100, random_state=42)
    risk_model.fit(X_train, y_risk_train)

    # Evaluation - Disease
    y_disease_pred = disease_model.predict(X_test)
    disease_acc = accuracy_score(y_disease_test, y_disease_pred)
    print(f"Disease Model Accuracy: {disease_acc * 100:.2f}%")

    # Evaluation - Risk
    y_risk_pred = risk_model.predict(X_test)
    risk_acc = accuracy_score(y_risk_test, y_risk_pred)
    print(f"Risk Model Accuracy: {risk_acc * 100:.2f}%")

    # Save models and encoders
    joblib.dump(disease_model, 'disease_model.pkl')
    joblib.dump(risk_model, 'risk_model.pkl')
    joblib.dump(encoders, 'encoders.pkl')
    print("\nModels and encoders saved successfully.")

if __name__ == "__main__":
    train_model()
