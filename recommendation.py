def get_recommendation(disease):
    """
    Returns personalized healthcare recommendations based on the predicted disease.
    """
    recommendations = {
        "Influenza": {
            "Precautions": "Rest, stay hydrated, and avoid contact with others to prevent spreading.",
            "Medicine": "Over-the-counter pain relievers (e.g., acetaminophen, ibuprofen). Consult a doctor for antivirals if symptoms are severe.",
            "Lifestyle": "Ensure adequate sleep and eat nutrient-rich foods."
        },
        "Common Cold": {
            "Precautions": "Wash hands frequently and use tissues when sneezing or coughing.",
            "Medicine": "Decongestants, cough suppressants, and throat lozenges.",
            "Lifestyle": "Drink warm fluids like tea or soup and get plenty of rest."
        },
        "Asthma": {
            "Precautions": "Avoid known triggers like dust, pollen, and smoke.",
            "Medicine": "Keep a rescue inhaler (e.g., albuterol) available at all times as prescribed.",
            "Lifestyle": "Practice breathing exercises and monitor air quality."
        },
        "Diabetes": {
            "Precautions": "Monitor blood glucose levels regularly and care for your feet.",
            "Medicine": "Follow the prescribed insulin or oral medication regimen strictly.",
            "Lifestyle": "Maintain a balanced low-glycemic diet and exercise regularly."
        },
        "Hypertension": {
            "Precautions": "Monitor blood pressure at home and reduce salt intake.",
            "Medicine": "Take prescribed antihypertensive medications consistently.",
            "Lifestyle": "Incorporate cardiovascular exercises and manage stress through meditation or yoga."
        },
        "Dengue Fever": {
            "Precautions": "Use mosquito nets and repellents; remove stagnant water around the house.",
            "Medicine": "Pain relievers like acetaminophen; avoid aspirin or ibuprofen as they can increase bleeding risk.",
            "Lifestyle": "Complete bed rest and high fluid intake."
        }
    }

    # Default recommendation for diseases not specifically mapped
    default_rec = {
        "Precautions": "Consult a healthcare professional for a detailed diagnosis and follow-up.",
        "Medicine": "Do not self-medicate. Follow the treatment plan provided by your doctor.",
        "Lifestyle": "Maintain a healthy diet, stay hydrated, and monitor your symptoms closely."
    }

    res = recommendations.get(disease, default_rec)
    
    disclaimer = (
        "\n\n**MEDICAL DISCLAIMER:** This recommendation is for informational purposes only and is not a "
        "substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of "
        "your physician or other qualified health provider with any questions you may have regarding a medical condition."
    )
    
    return res, disclaimer
