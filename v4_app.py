# import streamlit as st
# import numpy as np
# import pickle
# from sklearn.preprocessing import StandardScaler

# # ---------- Load model and scaler ----------
# def load_sklearn_model(model_path):
#     with open(model_path, "rb") as model_file:
#         final_model = pickle.load(model_file)
#     return final_model

# classification_model = load_sklearn_model("Fibromyalgia_app_model")

# def load_scaler(scalerpath):
#     with open(scalerpath, "rb") as scaler_file:
#         scaler = pickle.load(scaler_file)
#     return scaler

# scaler = load_scaler("standard_scaler")

# IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"

# # ---------- MAIN APP ----------
# def run_app():
#     # 🌸 Page Styling (NEW)
#     st.set_page_config(page_title="Fibromyalgia Prediction", page_icon="💫", layout="centered")
#     st.markdown("""
#         <style>
#             .stApp {
#                 background-color: #f7f9fc;
#                 color: #222;
#                 font-family: 'Poppins', sans-serif;
#             }
#             h1, h2, h3 {
#                 text-align: center;
#                 color: #2e4053;
#             }
#             .stImage {
#                 display: flex;
#                 justify-content: center;
#             }
#             /* 🌈 Center image */
#             .st-emotion-cache-1v0mbdj img {
#                 display: block;
#                 margin-left: auto;
#                 margin-right: auto;
#                 border-radius: 12px;
#                 box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#             }
#             /* 💎 Stylish button */
#             div.stButton > button {
#                 background: linear-gradient(90deg, #667eea, #764ba2);
#                 color: white;
#                 border: none;
#                 padding: 0.6em 1.2em;
#                 border-radius: 10px;
#                 font-size: 1em;
#                 transition: all 0.3s ease;
#                 width: 100%;
#             }
#             div.stButton > button:hover {
#                 background: linear-gradient(90deg, #5a67d8, #6b46c1);
#                 transform: scale(1.03);
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # ---------- Page Content ----------
#     st.title("💫 Fibromyalgia Prediction Tool")
#     st.subheader("Answer a few questions to check your risk level")

#     # 🖼️ Centered Image
#     st.image(IMAGE_ADDRESS, caption="Fibromyalgia Awareness", use_container_width=True)

#     st.markdown("---")

#     gender = st.radio("Select Gender", ("Male", "Female"))
#     gender_feature = 0 if gender == "Male" else 1
#     age = st.number_input("Enter Age", min_value=0, max_value=120, value=30)
#     CSI_total = st.number_input("Enter CSI Score", min_value=0, value=50)
#     SAT_total = st.number_input("Enter SAT Score", min_value=0, value=50)
#     SPS_total = st.number_input("Enter SPS Score", min_value=0, value=50)
#     SPSa_total = st.number_input("Enter SPSa Score", min_value=0, value=50)
#     SPSb_total = st.number_input("Enter SPSb Score", min_value=0, value=50)

#     features = np.array([[age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
#     scaled_features = scaler.transform(features)
#     final_features = np.hstack([[[gender_feature]], scaled_features])

#     # 🌈 Predict button
#     if st.button("🔍 Predict"):
#         model_predict = classification_model.predict(final_features)
#         result = model_predict[0]

#         if result == 1:
#             class_name = "Fibromyalgia"
#             color = "#e74c3c"  # 🔴 red
#         else:
#             class_name = "Under Control"
#             color = "#27ae60"  # 🟢 green

#         # 🎨 Custom Result Strip (NEW)
#         st.markdown(f"""
#             <div style='padding:15px; background-color:{color}; border-radius:10px; text-align:center; color:white; font-weight:bold; font-size:18px;'>
#                 Prediction: {class_name}
#             </div>
#         """, unsafe_allow_html=True)

# # ---------- Run ----------
# run_app()
# -------------Final------------




import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# ---------- Load model and scaler ----------
def load_sklearn_model(model_path):
    with open(model_path, "rb") as model_file:
        final_model = pickle.load(model_file)
    return final_model

classification_model = load_sklearn_model("Fibromyalgia_app_model")

def load_scaler(scalerpath):
    with open(scalerpath, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    return scaler

scaler = load_scaler("standard_scaler")

IMAGE_ADDRESS = "https://coloradopaincare.com/wp-content/uploads/fibromyalgia-colorado-pain-care-moghim-krutsch-spine.jpg"
community_resources = [{"name": "National Fibromyalgia Association", "url": "https://www.fmaware.org"},
    {"name": "Fibromyalgia Action UK", "url": "https://www.fmauk.org"},
    {"name": "Reddit Fibromyalgia Community", "url": "https://www.reddit.com/r/Fibromyalgia"},
    {"name": "HealthUnlocked Fibromyalgia Forum", "url": "https://healthunlocked.com/fibromyalgia-action-uk"},
    {"name": "The Mighty Fibromyalgia Community", "url": "https://themighty.com/fibromyalgia"}]
feature_descriptions = {"CSI (Central Sensitization Inventory)": "Measures symptoms of central sensitization, which is common in fibromyalgia. Higher scores indicate greater sensitivity to pain and other stimuli.",
    "SAT (Symptom Assessment Tool)": "Assesses the severity of common fibromyalgia symptoms including pain, fatigue, and sleep disturbances.",
    "SPS (Symptom Pattern Score)": "Evaluates the pattern of symptoms to help identify fibromyalgia-specific symptom clusters.",
    "SPSa (Symptom Pattern Score - Affective)": "Focuses on the emotional and psychological aspects of fibromyalgia symptoms.",
    "SPSb (Symptom Pattern Score - Somatic)": "Measures physical symptoms and their impact on daily functioning."}
def show_feature_info():
    st.sidebar.title("Feature Information ℹ️")
    for feature, description in feature_descriptions.items():
        with st.sidebar.expander(feature):
            st.write(description)
def show_community_resources():
    st.subheader("Community Support and Resources")
    st.write("If you've been diagnosed with fibromyalgia or are experiencing symptoms, you're not alone. Here are some helpful resources:")
    cols = st.columns(2)
    for i, resource in enumerate(community_resources):
        with cols[i % 2]:
            st.markdown(f"🔹[{resource["name"]}]({resource["url"]})")
# ---------- MAIN APP ---------- (previous working version)
# def run_app():
#     # 🌙 Page Styling (Dark Theme)
#     st.set_page_config(page_title="Fibromyalgia Prediction", page_icon="💫", layout="centered")
#     st.markdown("""
#         <style>
#             .stApp {
#                 background-color: #0e1117;
#                 color: #f0f2f6;
#                 font-family: 'Poppins', sans-serif;
#             }
#             h1, h2, h3 {
#                 text-align: center;
#                 color: #f9fafc;
#             }
#             .st-emotion-cache-1v0mbdj img {
#                 display: block;
#                 margin-left: auto;
#                 margin-right: auto;
#                 border-radius: 12px;
#                 box-shadow: 0 4px 12px rgba(255,255,255,0.1);
#             }
#             /* 🌈 Stylish button */
#             div.stButton > button {
#                 background: linear-gradient(90deg, #ff8a00, #da1b60);
#                 color: white;
#                 border: none;
#                 padding: 0.7em 1.2em;
#                 border-radius: 10px;
#                 font-size: 1em;
#                 transition: all 0.3s ease;
#                 width: 100%;
#             }
#             div.stButton > button:hover {
#                 background: linear-gradient(90deg, #ff6a00, #c41c67);
#                 transform: scale(1.03);
#             }
#             /* 📦 Collapsible expander background */
#             [data-testid="stExpander"] {
#                 background-color: #1c1f26;
#                 border-radius: 10px;
#                 color: #f0f2f6;
#             }
#             /* 🎨 Number input boxes */
#             input {
#                 background-color: #1c1f26 !important;
#                 color: #f0f2f6 !important;
#                 border-radius: 6px;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # ---------- Header ----------
#     st.title("💫 Fibromyalgia Prediction Tool")
#     st.subheader("Answer a few questions to check your risk level")

#     # ---------- Instructions Section (NEW) ----------
#     with st.expander("📘 Instructions & Important Links", expanded=True):
#         st.markdown("""
#         THIS IS A TEST TO DETERMINE WHETHER YOU HAVE FIBROMYALGIA OR NOT!!
#         Symptoms: 
#         - Muscle pain or tenderness
#         - Fatigue
#         - Face and jaw pain (temporomandibular joint disorders)
#         - Headaches and migraines
#         - Digestive problems, including diarrhea and constipation
#         - Bladder control issues
#         Follow these steps before you begin:
#         1. **Visit the [Survey Page](https://example.com/survey)** — Fill out the surveys to get your CSI, SAT, SPS, SPSa, and SPSb scores. (These tests are for scoring your senstivity and pain levels)  
#         2. **Return here** and enter those scores below.
#         3. Click on **Predict** to know whether you may be under control or at risk for Fibromyalgia.

#         🔗 **Helpful Resources:**
#         - [Fibromyalgia Awareness Article](https://www.cdc.gov/arthritis/basics/fibromyalgia.htm)
#         - [How to Interpret CSI Scores](https://www.mdcalc.com/)
#         - [Support Communities](https://www.fmaware.org/)

#         NOTE: This app is solely for detection of fibromyalgia and can be prone to errors. DO NOT solely rely on the results of this app, please confront your doctor if you have any symptoms. 
#         """)
    
#     st.image(IMAGE_ADDRESS, caption="Fibromyalgia Awareness", use_container_width=True)

#     st.markdown("---")

#     # ---------- Inputs ----------
#     gender = st.radio("Select Gender", ("Male", "Female"))
#     gender_feature = 0 if gender == "Male" else 1
#     age = st.number_input("Enter Age", min_value=0, max_value=120, value=30)
#     CSI_total = st.number_input("Enter CSI Score", min_value=0, value=50)
#     SAT_total = st.number_input("Enter SAT Score", min_value=0, value=50)
#     SPS_total = st.number_input("Enter SPS Score", min_value=0, value=50)
#     SPSa_total = st.number_input("Enter SPSa Score", min_value=0, value=50)
#     SPSb_total = st.number_input("Enter SPSb Score", min_value=0, value=50)

#     features = np.array([[age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
#     scaled_features = scaler.transform(features)
#     final_features = np.hstack([[[gender_feature]], scaled_features])

#     # ---------- Predict Button ----------
#     if st.button("🔍 Predict"):
#         model_predict = classification_model.predict(final_features)
#         result = model_predict[0]

#         if result == 1:
#             class_name = "Fibromyalgia Detected"
#             color = "#e74c3c"  # 🔴 red/orange
#         else:
#             class_name = "Under Control"
#             color = "#27ae60"  # 🟢 green

#         # 🎨 Custom Result Strip (NEW)
#         st.markdown(f"""
#             <div style='padding:15px; background-color:{color}; border-radius:10px; text-align:center; 
#             color:white; font-weight:bold; font-size:18px; margin-top:20px;'>
#                 Prediction: {class_name}
#             </div>
#         """, unsafe_allow_html=True)

# # ---------- Run ----------
# run_app()

def run_app():
    show_feature_info()
    st.title("Fibromyalgia Prediction Tool")
    st.write(("""
    This tool helps predict the likelihood of fibromyalgia based on standardized assessment scores. 
    Please enter your information below.
    """))
    st.image(IMAGE_ADDRESS, caption = "Managing Fibromyalgia with appropriate care and support.")
    with st.form("Prediction Form"):
        st.subheader("Patient Information")
        col1, col2 = st.columns(2)
        with col1:
            gender = st.radio("Gender", ("Male", "Female"), horizontal = True)
        with col2:
            age = st.number_input("Age", min_value = 0, max_value = 120, value = 30)
        st.markdown("---")
        st.subheader("Assessment Scores")
        st.write("Enter your assessment scores (hover over ℹ️ in the sidebar for more information about each score)")
        CSI_total = st.slider("CSI Total Score", min_value = 0, max_value = 100, value = 50, help = "Central Sensitization Inventory(0-100)")
        SAT_total = st.slider("SAT Total Score", min_value = 0, max_value = 100, value = 50, help = "Symptom Assessment Tool (0-100)")
        SPS_total = st.slider("SPS Total Score", min_value = 0, max_value = 100, value = 50, help = "Symptom Pattern Score(0-100)")
        SPSa_total = st.slider("SPSa Total Score", min_value = 0, max_value = 100, value = 50, help = "Symptom Pattern Score - Affective(0-100)")
        SPSb_total = st.slider("SPSb Total Score", min_value = 0, max_value = 100, value = 50, help = "Symptom Pattern Score - Somatic(0-100)")
        submit_button = st.form_submit_button("Predict")
    gender_feature = 0 if gender == "Male" else 1
    if 'submit_button' in locals() and submit_button:
        with st.spinner('Analyzing your information...'):
            # Feature values input
            features = np.array([[age, csi_total, sat_total, sps_total, spsa_total, spsb_total]])
            
            # Normalize the features except gender
            scaled_features = scaler.transform(features)
            
            # Combine the gender feature with the scaled features
            final_features = np.hstack([[[gender_feature]], scaled_features])
            
            # Make prediction
            model_predict = classification_model.predict(final_features)
            result = model_predict[0]
            
            # Display results
            st.markdown("---")
            st.subheader("🔍 Prediction Results")
            
            if result == 1:
                st.error("## 🚨 Fibromyalgia Detected")
                st.write("""
                Based on the provided information, the model predicts a likelihood of fibromyalgia. 
                Please consult with a healthcare professional for a comprehensive evaluation.
                """)
                show_community_resources()
            else:
                st.success("## ✅ No Fibromyalgia Detected")
                st.write("""
                Based on the provided information, the model does not detect signs of fibromyalgia.
                However, if you're experiencing symptoms, please consult with a healthcare professional.
                """)
            
            # Disclaimer
            st.markdown("---")
            st.warning("""
            **Disclaimer:** This tool is for informational purposes only and is not a substitute for 
            professional medical advice, diagnosis, or treatment. Always seek the advice of your 
            physician or other qualified health provider with any questions you may have regarding 
            a medical condition.
            """)

run_app()
