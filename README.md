# 🏥 Personalized Healthcare & Medicine Recommendation System

An AI-powered diagnostic and recommendation tool that predicts health conditions and provides personalized healthcare advice based on user symptoms and demographic data.

## 🌟 Features
- **Disease Prediction**: Uses a Random Forest Classifier to identify potential health conditions.
- **Risk Assessment**: Predicts the risk level (Low, Medium, High) associated with the symptoms.
- **Personalized Recommendations**: Provides specific precautions, over-the-counter medicine suggestions, and lifestyle advice.
- **Modern UI**: An interactive web interface built with Streamlit.
- **Medical Disclaimer**: Integrated safety notice for informational use.

## 📂 Project Structure
- `app.py`: The Streamlit web application.
- `train.py`: Data preprocessing and model training script.
- `recommendation.py`: Logic for generating personalized medical advice.
- `Cleaned_Dataset.csv`: The dataset used for training.
- `requirements.txt`: List of Python dependencies.
- `disease_model.pkl`: Trained model for disease prediction.
- `risk_model.pkl`: Trained model for risk level prediction.
- `encoders.pkl`: Serialized LabelEncoders for categorical data.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Clone this repository or navigate to the project directory and install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Training the Model
If you need to retrain the model or if the `.pkl` files are missing, run:
```bash
python train.py
```

### 4. Running the Web App
Start the Streamlit application:
```bash
streamlit run app.py
```

## 🛠️ Technology Stack
- **Language**: Python
- **Machine Learning**: Scikit-Learn (Random Forest)
- **Data Manipulation**: Pandas, Numpy
- **Web Framework**: Streamlit
- **Model Persistence**: Joblib

## ⚠️ Medical Disclaimer
This application is for **informational purposes only** and does not constitute professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

---
Built with ❤️ for a healthier future.
