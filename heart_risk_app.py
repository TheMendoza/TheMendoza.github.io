import streamlit as st

st.title('Cardiac Triage Questionnaire')

# Age category
age = st.radio('Please select your age category:', ['0-29', '30-49', '50-69', '70+'])
age_score = {'0-29': 0, '30-49': 1, '50-69': 2, '70+': 3}[age]

# Chest discomfort
chest_pain = st.radio('Do you suffer from chest discomfort, chest pain, or chest tightness?', ['Yes', 'No'])
chest_pain_score = 1 if chest_pain == 'Yes' else 0

# Symptoms at rest
symptoms_at_rest = st.radio('Do these symptoms occur at rest?', ['Yes', 'No'])
symptoms_at_rest_score = 2 if symptoms_at_rest == 'Yes' else 0

# Shortness of breath
shortness_of_breath = st.radio('Do you suffer from shortness of breath?', ['Yes', 'No'])
shortness_of_breath_score = 1 if shortness_of_breath == 'Yes' else 0

# Heart palpitations or dizzy spells
heart_palpitations = st.radio('Do you suffer from heart palpitation, heart racing or dizzy spells?', ['Yes', 'No'])
heart_palpitations_score = 1 if heart_palpitations == 'Yes' else 0

# Blacked out
blacked_out = st.radio('Have you ever blacked out, collapsed or lost consciousness?', ['Yes', 'No'])
blacked_out_score = 4 if blacked_out == 'Yes' else 0

# High blood pressure
high_blood_pressure = st.radio('Are you being referred for possible high blood pressure?', ['Yes', 'No'])
high_blood_pressure_score = 1 if high_blood_pressure == 'Yes' else 0

# Seen a heart specialist
heart_specialist = st.radio('Have you seen a heart specialist before?', ['Yes', 'No'])
heart_specialist_score = 0  # No score for this question

# Diagnosed with heart condition
heart_condition = st.radio('Were you diagnosed with a heart condition?', ['Yes', 'No'])
heart_condition_score = 1 if heart_condition == 'Yes' else 0

# Smoking history
smoked = st.radio('Have you ever smoked?', ['Yes', 'No'])
smoked_score = 2 if smoked == 'Yes' else 0

# Diabetic
diabetic = st.radio('Are you diabetic?', ['Yes', 'No'])
diabetic_score = 2 if diabetic == 'Yes' else 0

# Family history of heart disease
family_history = st.radio('Do you have a family history of heart disease?', ['Yes', 'No'])
family_history_score = 1 if family_history == 'Yes' else 0

# Calculate total score
total_score = (age_score + chest_pain_score + symptoms_at_rest_score + shortness_of_breath_score +
               heart_palpitations_score + blacked_out_score + high_blood_pressure_score +
               heart_specialist_score + heart_condition_score + smoked_score + diabetic_score +
               family_history_score)

st.write(f'Total Score: {total_score}')

if total_score > 4:
    st.write("A triage call will be arranged.")
else:
    st.write("Proceed to booking.")
