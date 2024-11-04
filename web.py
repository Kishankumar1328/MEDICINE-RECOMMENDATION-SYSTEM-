import numpy as np
import streamlit as st
from pathlib import Path
import base64

# Function to convert image to bytes
def img_to_bytes(img_path):
    img_path = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_path).decode()
    return encoded

# Sidebar layout
def sidebar():
    st.sidebar.markdown(f"<img src='data:image/png;base64,{img_to_bytes('m.jpg')}' class='img-fluid' width=225 height=280>",
                        unsafe_allow_html=True)
    st.sidebar.markdown("""
       <div style="padding: 10px;">
           <h2 style="color: #1f77b4;">Medicine Recommendation System</h2>
           <p style="font-size: 14px;">
            This system is exclusively for doctors, offering support in analyzing patient data to recommend treatment options and improve clinical decision-making.
           </p>
       </div>
       """, unsafe_allow_html=True)

# Medications and associated diseases
medication_diseases = {
    "Aspirin": ["Pain", "Fever", "Inflammation"],
    "Paracetamol": ["Pain", "Fever"],
    "Ibuprofen": ["Pain", "Fever", "Inflammation"],
    "Amoxicillin": ["Bacterial Infections (e.g., Ear Infections, Sinus Infections, Pneumonia)"],
    "Ciprofloxacin": ["Bacterial Infections (e.g., Urinary Tract Infections, Respiratory Infections)"],
    "Metformin": ["Type 2 Diabetes"],
    "Insulin": ["Diabetes (Type 1 and Type 2)"],
    "Atorvastatin": ["High Cholesterol", "Heart Disease"],
    "Lisinopril": ["Hypertension", "Heart Failure"],
    "Amlodipine": ["Hypertension", "Angina"],
    "Hydrochlorothiazide": ["Hypertension", "Edema"],
    "Losartan": ["Hypertension", "Heart Failure"],
    "Omeprazole": ["Gastroesophageal Reflux Disease (GERD)", "Ulcers"],
    "Pantoprazole": ["GERD", "Ulcers"],
    "Ranitidine": ["GERD", "Ulcers"],
    "Simvastatin": ["High Cholesterol", "Heart Disease"],
    "Levothyroxine": ["Hypothyroidism"],
    "Warfarin": ["Blood Clots", "Stroke Prevention"],
    "Clopidogrel": ["Blood Clots", "Heart Attack Prevention"],
    "Metoprolol": ["Hypertension", "Angina", "Heart Failure"],
    "Prednisone": ["Inflammatory Conditions (e.g., Asthma, Rheumatoid Arthritis)"],
    "Cetirizine": ["Allergies", "Hay Fever"],
    "Loratadine": ["Allergies", "Hay Fever"],
    "Furosemide": ["Edema", "Heart Failure"],
    "Albuterol": ["Asthma", "Chronic Obstructive Pulmonary Disease (COPD)"],
    "Sertraline": ["Depression", "Anxiety Disorders"],
    "Fluoxetine": ["Depression", "Anxiety Disorders"],
    "Escitalopram": ["Depression", "Anxiety Disorders"],
    "Paroxetine": ["Depression", "Anxiety Disorders"],
    "Tramadol": ["Pain (Moderate to Severe)"],
    "Morphine": ["Severe Pain", "Palliative Care"],
    "Codeine": ["Mild to Moderate Pain", "Cough"],
    "Oxycodone": ["Moderate to Severe Pain"],
    "Gabapentin": ["Neuropathic Pain", "Seizures"],
    "Pregabalin": ["Neuropathic Pain", "Fibromyalgia"],
    "Aripiprazole": ["Schizophrenia", "Bipolar Disorder"],
    "Quetiapine": ["Schizophrenia", "Bipolar Disorder"],
    "Risperidone": ["Schizophrenia", "Bipolar Disorder"],
    "Alprazolam": ["Anxiety Disorders", "Panic Disorders"],
    "Diazepam": ["Anxiety Disorders", "Muscle Spasms", "Seizures"]
}

medication_diseases.update({
    "Doxycycline": ["Bacterial Infections", "Acne", "Lyme Disease", "Malaria Prevention"],
    "Azithromycin": ["Bacterial Infections", "Pneumonia", "Bronchitis", "Sinus Infections"],
    "Hydrocortisone": ["Inflammation", "Skin Conditions (e.g., Eczema)", "Allergic Reactions"],
    "Methotrexate": ["Rheumatoid Arthritis", "Psoriasis", "Certain Types of Cancer"],
    "Clonazepam": ["Seizures", "Panic Disorders", "Anxiety Disorders"],
    "Sitagliptin": ["Type 2 Diabetes"],
    "Dulaglutide": ["Type 2 Diabetes"],
    "Budesonide": ["Asthma", "Crohn's Disease", "Ulcerative Colitis"],
    "Baclofen": ["Muscle Spasms", "Spinal Cord Injury"],
    "Finasteride": ["Benign Prostatic Hyperplasia (BPH)", "Male Pattern Baldness"],
    "Tamsulosin": ["Benign Prostatic Hyperplasia (BPH)"],
    "Meloxicam": ["Osteoarthritis", "Rheumatoid Arthritis"],
    "Allopurinol": ["Gout", "Kidney Stones"],
    "Colchicine": ["Gout"],
    "Famotidine": ["GERD", "Ulcers", "Heartburn"],
    "Methadone": ["Severe Pain", "Opioid Dependence"],
    "Montelukast": ["Asthma", "Allergic Rhinitis"],
    "Duloxetine": ["Depression", "Anxiety Disorders", "Neuropathic Pain", "Fibromyalgia"],
    "Venlafaxine": ["Depression", "Anxiety Disorders"],
    "Topiramate": ["Seizures", "Migraine Prevention"],
    "Lamotrigine": ["Seizures", "Bipolar Disorder"],
    "Lithium": ["Bipolar Disorder"],
    "Lorazepam": ["Anxiety Disorders", "Seizures"],
    "Promethazine": ["Nausea", "Allergies", "Motion Sickness"],
    "Ondansetron": ["Nausea", "Vomiting", "Chemotherapy-Induced Nausea"],
    "Alendronate": ["Osteoporosis"],
    "Raloxifene": ["Osteoporosis", "Breast Cancer Prevention"],
    "Varenicline": ["Smoking Cessation"],
    "Naltrexone": ["Opioid Dependence", "Alcohol Dependence"],
    "Disulfiram": ["Alcohol Dependence"],
    "Propranolol": ["Hypertension", "Migraine Prevention", "Anxiety"],
    "Bisoprolol": ["Hypertension", "Heart Failure"],
    "Valsartan": ["Hypertension", "Heart Failure"],
    "Esomeprazole": ["GERD", "Ulcers"],
    "Famciclovir": ["Herpes Simplex Virus", "Shingles"],
    "Acyclovir": ["Herpes Simplex Virus", "Shingles", "Chickenpox"],
    "Oseltamivir": ["Influenza"],
    "Methimazole": ["Hyperthyroidism"],
    "Spironolactone": ["Hypertension", "Edema", "Heart Failure", "Acne"],
    "Apixaban": ["Blood Clots", "Stroke Prevention"],
    "Edoxaban": ["Blood Clots", "Stroke Prevention"],
    "Dabigatran": ["Blood Clots", "Stroke Prevention"],
    "Epinephrine": ["Severe Allergic Reactions (Anaphylaxis)"],
    "Donepezil": ["Alzheimer's Disease"],
    "Memantine": ["Alzheimer's Disease"],
    "Rivastigmine": ["Alzheimer's Disease", "Parkinson's Disease Dementia"],
    "Carbidopa/Levodopa": ["Parkinson's Disease"],
    "Amantadine": ["Parkinson's Disease", "Influenza"],
    "Levothyroxine": ["Hypothyroidism"]
})
# List of unique diseases
unique_diseases = sorted(list(set(disease for diseases in medication_diseases.values() for disease in diseases)))

# Medication-disease efficacy matrix
medication_data = np.array([
    [1 if disease in diseases else 0 for disease in unique_diseases]
    for diseases in medication_diseases.values()
])

# Recommendation system class
class MedicationRecommendation:
    def __init__(self, medication_data, num_factors=5, learning_rate=0.01, reg_param=0.01, num_epochs=100):
        self.medication_data = medication_data
        self.num_medications, self.num_diseases = medication_data.shape
        self.num_factors = num_factors
        self.learning_rate = learning_rate
        self.reg_param = reg_param
        self.num_epochs = num_epochs
        self.P = np.random.normal(scale=1./self.num_factors, size=(self.num_medications, self.num_factors))
        self.Q = np.random.normal(scale=1./self.num_factors, size=(self.num_diseases, self.num_factors))

    def train(self):
        for epoch in range(self.num_epochs):
            for i in range(self.num_medications):
                for j in range(self.num_diseases):
                    if self.medication_data[i][j] > 0:
                        eij = self.medication_data[i][j] - np.dot(self.P[i, :], self.Q[j, :].T)
                        self.P[i, :] += self.learning_rate * (eij * self.Q[j, :] - self.reg_param * self.P[i, :])
                        self.Q[j, :] += self.learning_rate * (eij * self.P[i, :] - self.reg_param * self.Q[j, :])
            if epoch % 10 == 0:
                print(f"Epoch: {epoch}, Error: {self.calculate_error()}")

    def calculate_error(self):
        errors = (self.medication_data - np.dot(self.P, self.Q.T)) ** 2
        return np.mean(errors[self.medication_data > 0])

    def get_recommendations(self, diseases, top_n=5):
        disease_indices = [unique_diseases.index(disease) for disease in diseases if disease in unique_diseases]
        if not disease_indices:
            return []
        scores = np.dot(self.P, self.Q[disease_indices].T)
        avg_scores = np.mean(scores, axis=1)
        top_medications = np.argsort(avg_scores)[::-1][:top_n]
        return [list(medication_diseases.keys())[i] for i in top_medications]

# Initialize and train the recommendation system
recommendation_system = MedicationRecommendation(medication_data)
with st.spinner("Training the recommendation model..."):
    recommendation_system.train()

# Streamlit app setup
st.title("Medicine Recommendation System")
sidebar()

# Disease selection dropdown
st.markdown("<h3>Select diseases:</h3>", unsafe_allow_html=True)
input_diseases = st.multiselect("Choose from the list:", unique_diseases)

# Button to get recommendations
if st.button("Get Recommendations"):
    if not input_diseases:
        st.warning("Please select at least one disease to get recommendations.")
    else:
        recommendations = recommendation_system.get_recommendations(input_diseases)
        if recommendations:
            st.write("Top medication recommendations:")
            for med in recommendations:
                st.markdown(f"<div style='background-color:#eaf4fc; padding:10px; margin:5px 0; border-radius:5px;'><strong>{med}</strong></div>", unsafe_allow_html=True)
        else:
            st.warning("No recommendations available for the selected diseases.")

# Custom CSS for consistent styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)


# Custom CSS for consistent styling of the disclaimer section
st.markdown("""
    <style>
    .disclaimer {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
        font-size: 14px;
        color: #721c24;
    }
    </style>
    """, unsafe_allow_html=True)

# Disclaimer for normal patients
st.markdown("""
    <div class="disclaimer">
        <strong>Disclaimer:</strong> This Allopathy Medicine Recommendation System is designed for educational and informational purposes only, and is intended for use by healthcare professionals. It is not a substitute for professional medical advice, diagnosis, or treatment. Patients should consult qualified healthcare providers before making any healthcare decisions. This tool should not be used for self-diagnosis or self-treatment.
    </div>
""", unsafe_allow_html=True)

