from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('your_model.pkl')  # Ensure this path is correct

@app.route('/')
def home():
    return render_template('index.html')  # Serve the existing HTML file

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.json
        age = data['age']
        temperature = data['temperature']
        pulse = data['pulse']
        ecg = data['ecg']
        
        # Prepare the input for the model
        input_data = np.array([[age, temperature, pulse, ecg]])
        
        # Get prediction from the model
        prediction = model.predict(input_data)
        
        # Convert prediction to a standard Python type
        diagnosis = int(prediction[0])

        # Generate suggestions based on the vitals
        suggestions = generate_suggestions(age, temperature, pulse, ecg)

        return jsonify({'diagnosis': diagnosis, 'suggestions': suggestions})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def generate_suggestions(age, temperature, pulse, ecg):
    suggestions = []

    # Age-based suggestions
    if age < 18:
        suggestions.append("The patient is a minor. Ensure parental consent for any medical procedures or treatments. Regular pediatric check-ups are recommended to monitor growth and development.")
    elif age < 65:
        suggestions.append("The patient is an adult. Encourage regular health screenings, including blood pressure checks, cholesterol levels, and diabetes screenings, to maintain optimal health.")
    else:
        suggestions.append("The patient is a senior. Geriatric assessments are important to evaluate cognitive function, mobility, and the risk of falls. Regular screenings for conditions such as osteoporosis and heart disease are advised.")

    # Temperature-based suggestions
    if temperature < 97.0:
        suggestions.append("The patient has a low body temperature, which may indicate hypothermia or other underlying health issues. It is important to monitor the patient closely and consider warming measures if necessary.")
    elif 97.0 <= temperature <= 98.6:
        suggestions.append("The patient's temperature is within the normal range. This is a positive sign, indicating that there are no immediate concerns regarding fever or infection.")
    elif 98.6 < temperature < 100.4:
        suggestions.append("The patient has a mild fever, which could be a sign of a viral infection or other mild illness. Recommend rest, increased fluid intake, and monitoring for any additional symptoms. If the fever persists, further evaluation may be necessary.")
    else:
        suggestions.append("The patient has a high fever, which may indicate a more serious infection or illness. Immediate medical evaluation is recommended to determine the cause of the fever and appropriate treatment options.")

    # Pulse-based suggestions
    if pulse < 60:
        suggestions.append("The patient has a low pulse rate (bradycardia). This could be a sign of an underlying heart condition or the effects of certain medications. Continuous monitoring is essential, and further cardiac evaluation may be warranted.")
    elif 60 <= pulse <= 100:
        suggestions.append("The patient's pulse is within the normal range, which is a good indicator of cardiovascular health. Encourage regular physical activity and a heart-healthy diet to maintain this status.")
    else:
        suggestions.append("The patient has a high pulse rate (tachycardia). This could be due to stress, anxiety, dehydration, or an underlying medical condition. Recommend monitoring the patient's heart rate and consider further investigation if symptoms persist.")

    # ECG-based suggestions
    if ecg < 0.4:
        suggestions.append("The ECG value is low, which may indicate potential cardiac issues. It is advisable to conduct further cardiac evaluations, including echocardiograms or stress tests, to assess heart function.")
    elif 0.4 <= ecg <= 0.7:
        suggestions.append("The ECG value is within the normal range, suggesting that the heart is functioning properly. Regular monitoring and maintaining a healthy lifestyle are recommended to support cardiovascular health.")
    else:
        suggestions.append("The ECG value is elevated, which may indicate the presence of cardiac stress or other heart-related issues. Recommend further cardiac assessment and possibly a referral to a cardiologist for specialized care.")

    # Combine suggestions into a detailed response
    return " ".join(suggestions)

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development