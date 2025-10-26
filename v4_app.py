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

IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"

# ---------- MAIN APP ----------
def run_app():
    # 🌸 Page Styling (NEW)
    st.set_page_config(page_title="Fibromyalgia Prediction", page_icon="💫", layout="centered")
    st.markdown("""
        <style>
            .stApp {
                background-color: #f7f9fc;
                color: #222;
                font-family: 'Poppins', sans-serif;
            }
            h1, h2, h3 {
                text-align: center;
                color: #2e4053;
            }
            .stImage {
                display: flex;
                justify-content: center;
            }
            /* 🌈 Center image */
            .st-emotion-cache-1v0mbdj img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            /* 💎 Stylish button */
            div.stButton > button {
                background: linear-gradient(90deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 0.6em 1.2em;
                border-radius: 10px;
                font-size: 1em;
                transition: all 0.3s ease;
                width: 100%;
            }
            div.stButton > button:hover {
                background: linear-gradient(90deg, #5a67d8, #6b46c1);
                transform: scale(1.03);
            }
        </style>
    """, unsafe_allow_html=True)

    # ---------- Page Content ----------
    st.title("💫 Fibromyalgia Prediction Tool")
    st.subheader("Answer a few questions to check your risk level")

    # 🖼️ Centered Image
    st.image(IMAGE_ADDRESS, caption="Fibromyalgia Awareness", use_container_width=True)

    st.markdown("---")

    gender = st.radio("Select Gender", ("Male", "Female"))
    gender_feature = 0 if gender == "Male" else 1
    age = st.number_input("Enter Age", min_value=0, max_value=120, value=30)
    CSI_total = st.number_input("Enter CSI Score", min_value=0, value=50)
    SAT_total = st.number_input("Enter SAT Score", min_value=0, value=50)
    SPS_total = st.number_input("Enter SPS Score", min_value=0, value=50)
    SPSa_total = st.number_input("Enter SPSa Score", min_value=0, value=50)
    SPSb_total = st.number_input("Enter SPSb Score", min_value=0, value=50)

    features = np.array([[age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
    scaled_features = scaler.transform(features)
    final_features = np.hstack([[[gender_feature]], scaled_features])

    # 🌈 Predict button
    if st.button("🔍 Predict"):
        model_predict = classification_model.predict(final_features)
        result = model_predict[0]

        if result == 1:
            class_name = "Fibromyalgia"
            color = "#e74c3c"  # 🔴 red
        else:
            class_name = "Under Control"
            color = "#27ae60"  # 🟢 green

        # 🎨 Custom Result Strip (NEW)
        st.markdown(f"""
            <div style='padding:15px; background-color:{color}; border-radius:10px; text-align:center; color:white; font-weight:bold; font-size:18px;'>
                Prediction: {class_name}
            </div>
        """, unsafe_allow_html=True)

# ---------- Run ----------
run_app()
