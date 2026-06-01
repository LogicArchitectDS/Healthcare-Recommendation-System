import streamlit as st
import pandas as pd
import joblib
import os
from recommendation import get_recommendation

# Page configuration
st.set_page_config(page_title="Personalized Healthcare Recommendation System", layout="wide")

st.title("🏥 Personalized Healthcare & Medicine Recommendation System")
st.markdown("""
Predict potential health conditions based on symptoms and demographic data. 
*Note: This is an AI-powered tool for informational purposes only.*
""")

# Load model and encoders
@st.cache_resource
def load_assets():
    if os.path.exists('disease_model.pkl') and os.path.exists('risk_model.pkl') and os.path.exists('encoders.pkl'):
        d_model = joblib.load('disease_model.pkl')
        r_model = joblib.load('risk_model.pkl')
        encoders = joblib.load('encoders.pkl')
        return d_model, r_model, encoders
    return None, None, None

d_model, r_model, encoders = load_assets()

if d_model is None:
    st.error("Model files not found. Please run 'train.py' first to train and save the model.")
else:
    # Sidebar for inputs
    st.sidebar.header("User Information & Symptoms")
    
    with st.sidebar.form("input_form"):
        age = st.number_input("Age", min_value=0, max_value=120, value=25)
        gender = st.selectbox("Gender", options=["male", "female"])
        
        st.subheader("Symptoms")
        fever = st.selectbox("Fever", options=["Yes", "No"])
        cough = st.selectbox("Cough", options=["Yes", "No"])
        fatigue = st.selectbox("Fatigue", options=["Yes", "No"])
        difficulty_breathing = st.selectbox("Difficulty Breathing", options=["Yes", "No"])
        
        st.subheader("Vitals")
        blood_pressure = st.select_slider("Blood Pressure Level (0=Low, 1=Normal, 2=High)", options=[0, 1, 2], value=1)
        cholesterol_level = st.select_slider("Cholesterol Level (0=Low, 1=Normal, 2=High)", options=[0, 1, 2], value=1)
        
        submit_button = st.form_submit_button("Predict Disease")

    if submit_button:
        # Prepare input data
        input_data = pd.DataFrame({
            'fever': [fever],
            'cough': [cough],
            'fatigue': [fatigue],
            'difficulty_breathing': [difficulty_breathing],
            'age': [age],
            'gender': [gender],
            'blood_pressure': [blood_pressure],
            'cholesterol_level': [cholesterol_level]
        })

        # Encode categorical inputs
        try:
            for col in ['fever', 'cough', 'fatigue', 'difficulty_breathing', 'gender']:
                le = encoders[col]
                input_data[col] = le.transform(input_data[col])
            
            # Predictions
            disease_idx = d_model.predict(input_data)[0]
            predicted_disease = encoders['disease'].inverse_transform([disease_idx])[0]
            
            risk_idx = r_model.predict(input_data)[0]
            predicted_risk = encoders['risk_level'].inverse_transform([risk_idx])[0]
            
            # Display Results
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.success(f"### Predicted Health Condition: **{predicted_disease}**")
            with col_res2:
                risk_color = "red" if predicted_risk == "High" else "orange" if predicted_risk == "Medium" else "green"
                st.markdown(f"### Risk Level: <span style='color:{risk_color}'>**{predicted_risk}**</span>", unsafe_allow_html=True)
            
            st.divider()
            
            # Recommendations
            st.subheader("📋 Personalized Recommendations")
            rec, disclaimer = get_recommendation(predicted_disease)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info("**General Precautions**")
                st.write(rec['Precautions'])
            with col2:
                st.warning("**Medicine Suggestions**")
                st.write(rec['Medicine'])
            with col3:
                st.success("**Lifestyle Advice**")
                st.write(rec['Lifestyle'])
                
            st.markdown(disclaimer)

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit and Scikit-Learn")
