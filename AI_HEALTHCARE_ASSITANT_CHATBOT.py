import streamlit as st
import time
import spacy

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

# Predefined medical responses with emoji
medical_responses = {
    # Common Symptoms
    "headache": "🤕 **Headache:** Headaches can be caused by stress, dehydration, or underlying health conditions. Try resting, drinking water, and avoiding screen time. If pain persists, consult a doctor.",
    "fever": "🌡️ Fever: A fever is often a sign of infection. Stay hydrated, get plenty of rest, and take over-the-counter medication if needed. If fever exceeds 102°F (39°C) or lasts more than 3 days, seek medical advice.",
    "cough": "🤧 Cough: A cough may be caused by colds, flu, allergies, or respiratory infections. Drink warm fluids, use a humidifier, and avoid smoking. If it persists for more than 2 weeks, consult a doctor.",
    "sore throat": "😖 Sore Throat: A sore throat can be due to a viral or bacterial infection. Gargle with warm salt water, drink honey tea, and avoid irritants like smoke.",
    "fatigue": "😴 Fatigue: Feeling tired all the time? It could be due to lack of sleep, stress, anemia, or an underlying condition. Try improving sleep habits and diet. If persistent, check with a doctor.",
    "nausea": "🤢 **Nausea:** Nausea can be caused by motion sickness, food poisoning, pregnancy, or gastrointestinal issues. Try eating small meals, drinking ginger tea, and staying hydrated.",
    "vomiting": "🤮 **Vomiting:** Stay hydrated with electrolyte drinks and avoid solid foods until you feel better. If vomiting persists for more than 24 hours, seek medical help.",
    "dizziness": "💫 **Dizziness:** Dizziness can be caused by dehydration, low blood pressure, or inner ear issues. Sit down, drink water, and avoid sudden movements.",
    "shortness of breath": "😮‍💨 **Shortness of Breath:** If you're having difficulty breathing, it could be due to asthma, anxiety, or a more serious condition. If severe, seek medical attention immediately.",
    "stomach pain": "🥴 **Stomach Pain:** It could be caused by indigestion, gas, or infection. Drink warm fluids and avoid spicy foods. If pain is severe or lasts more than 24 hours, consult a doctor.",
    
    # Chronic Conditions
    "diabetes": "🩸 **Diabetes:** Managing diabetes requires a healthy diet, regular exercise, and monitoring blood sugar levels. If you have concerns, talk to a healthcare provider.",
    "hypertension": "💓 **High Blood Pressure (Hypertension):** Reduce salt intake, exercise regularly, and manage stress to control your blood pressure. Consult a doctor for medication if needed.",
    "heart disease": "❤️ **Heart Disease:** Maintain a heart-healthy diet, exercise regularly, and avoid smoking. Seek immediate medical help if experiencing chest pain or irregular heartbeat.",
    "asthma": "🌬️ **Asthma:** Use prescribed inhalers, avoid allergens, and practice breathing exercises to manage symptoms. Seek medical help if breathing worsens.",
    "arthritis": "🦴 **Arthritis:** Joint pain and stiffness can be managed with physical activity, anti-inflammatory medication, and a balanced diet.",
    "obesity": "⚖️ **Obesity:** Maintaining a healthy weight requires a balanced diet, portion control, and regular exercise. Consult a nutritionist if needed.",
    
    # Mental Health
    "anxiety": "😟 **Anxiety:** Deep breathing, meditation, and talking to a therapist can help manage anxiety. If severe, consult a mental health professional.",
    "depression": "😞 **Depression:** If you're feeling persistently sad or hopeless, reach out to a therapist or trusted person for support. You're not alone, and help is available.",
    "stress": "💆 **Stress:** Managing stress involves relaxation techniques, exercise, and proper time management. Consider talking to someone if stress becomes overwhelming.",
    "insomnia": "🌙 **Insomnia:** Try maintaining a sleep schedule, avoiding screens before bed, and practicing relaxation techniques for better sleep.",
    
    # Skin & Allergies
    "allergy": "🤧 **Allergy:** Common allergens include pollen, dust, and certain foods. Avoid triggers, take antihistamines if needed, and seek medical help for severe reactions.",
    "rash": "🌿 **Rash:** Skin rashes can be caused by allergies, infections, or irritation. Keep the area clean, avoid scratching, and apply a soothing lotion.",
    "acne": "🧴 **Acne:** Keep your skin clean, avoid touching your face, and use acne treatments if needed. If severe, consult a dermatologist.",
    
    # Women's Health
    "pregnancy": "🤰 **Pregnancy:** Ensure a healthy diet, regular check-ups, and proper prenatal care. If you have concerns, consult a doctor.",
    "menstrual cramps": "🩸 **Menstrual Cramps:** Applying heat, staying hydrated, and taking pain relievers can help ease cramps.",
    "pcos": "⚕️ **PCOS (Polycystic Ovary Syndrome):** Managing PCOS involves a healthy diet, exercise, and sometimes medication. Consult a gynecologist for guidance.",
    
    # First Aid & Emergencies
    "burn": "🔥 **Burn:** For minor burns, cool the area with running water and apply aloe vera. For severe burns, seek emergency care.",
    "fracture": "🦴 **Fracture:** Keep the injured area immobilized and seek immediate medical help.",
    "choking": "🚑 **Choking:** Perform the Heimlich maneuver if someone is choking. Seek emergency help if breathing is obstructed.",
    "bleeding": "🩸 **Bleeding:** Apply firm pressure to stop the bleeding and seek medical help if necessary.",
    
    # COVID-19 & Infectious Diseases
    "covid": "🦠 **COVID-19:** Common symptoms include fever, cough, and loss of taste or smell. Get tested if symptoms persist and follow public health guidelines.",
    "flu": "🤒 **Flu:** Rest, drink fluids, and take fever-reducing medication if needed. Get a flu shot annually to reduce the risk.",
    
    # General Health & Advice
    "nutrition": "🥗 **Nutrition:** A balanced diet with plenty of fruits, vegetables, and whole grains is essential for overall health.",
    "exercise": "🏃 **Exercise:** Regular physical activity helps maintain a healthy weight and reduces the risk of many diseases.",
    "hydration": "💧 **Hydration:** Drink at least 8 glasses of water per day to stay hydrated and maintain body functions.",
    "sleep": "🛌 **Sleep:** Aim for 7-9 hours of sleep each night for optimal health and energy levels.",
    
    # Healthcare Services
    "doctor": "👨‍⚕️ **Doctor Consultation:** If you're feeling unwell, it's best to schedule a consultation with a doctor.",
    "appointment": "📅 **Appointment:** Would you like me to help you book a doctor's appointment?",
    "medication": "💊 **Medication:** Always take prescribed medications as directed. If you have concerns, speak with a healthcare provider.",
    "insurance": "📑 **Health Insurance:** Having health insurance ensures you have access to medical care when needed. Consider reviewing your coverage options.",
    
    # Emergency
    "emergency": "🚨 **Emergency:** If you're experiencing a life-threatening situation, call emergency services immediately (911 or your local emergency number).",
}


# Function to process user input
def healthcare_chatbot(user_input):
    doc = nlp(user_input.lower())

    # Check for keywords in predefined responses
    for word in doc:
        if word.text in medical_responses:
            return medical_responses[word.text]

    return "🤔 I'm not sure about that. Please consult a medical professional for accurate advice."

# Function to add a typing effect
def type_response(response):
    message = ""
    for char in response:
        message += char
        time.sleep(0.02)  # Adjust typing speed
        st.write(f"Chatbot: {message}", unsafe_allow_html=True)
        st.empty()  # Refresh the text dynamically
    st.write(f'<div class="bot-response">{response}</div>', unsafe_allow_html=True)

# Streamlit web app interface
def main():
    # Custom page configuration
    st.set_page_config(page_title="Healthcare Assistant", page_icon="💬", layout="centered")

    # Custom CSS for styling
    st.markdown("""
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
            }
            .main-container {
                max-width: 700px;
                margin: auto;
                padding: 20px;
                background: #1e293b;
                border-radius: 12px;
                box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.1);
            }
            h1 {
                text-align: center;
                color: #ff4b4b;
            }
            .stTextInput>div>div>input {
                background-color: #334155;
                color: white;
                padding: 12px;
                border-radius: 8px;
            }
            .stButton>button {
                background-color: #ff4b4b;
                color: white;
                border-radius: 8px;
                font-size: 16px;
                padding: 10px;
            }
            .stButton>button:hover {
                background-color: #ff0000;
            }
            .chat-container {
                margin-top: 20px;
            }
            .user-message {
                background-color: #2563eb;
                color: white;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 10px;
                text-align: right;
            }
            .bot-response {
                background-color: #64748b;
                color: white;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 10px;
                text-align: left;
            }
        </style>
    """, unsafe_allow_html=True)

    # Chatbot UI Layout
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("💡 AI Healthcare Assistant Chatbot")
    st.write("🤖 Ask me anything related to healthcare!")

    user_input = st.text_input("💬 Enter your question:")

    if st.button("Submit"):
        if user_input:
            st.markdown(f'<div class="user-message"> You: {user_input}</div>', unsafe_allow_html=True)
            response = healthcare_chatbot(user_input)
            st.markdown(f'<div class="bot-response">Chatbot: {response}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a query before submitting.")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
