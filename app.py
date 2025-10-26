# import streamlit as st
# import numpy as np
# import pickle 
# from sklearn.preprocessing import StandardScaler
# IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"
# def load_sklearn_model(model_path):
#     with open(model_path, "rb") as model_file:
#         final_model = pickle.load(model_file)
#     return final_model

# classification_model = load_sklearn_model("Fibromyalgia_app_model")

# def load_scaler(scalerpath):
#     with open(scalerpath, "rb") as scaler_file:
#        scaler = pickle.load(scaler_file)
#     return scaler
# scaler = load_scaler("standard_scaler")

# def run_app():
#     st.title("Fibromyalgia Predicitons")
#     st.subheader("Answer a few questions to find out if you have fibromyalgia")
#     st.image(IMAGE_ADDRESS, caption = "Fibromyalgia")
#     gender = st.radio("select gender", ("male", "female"))
#     gender_feature = 0 if gender == "male" else 1
#     age = st.number_input("enter age", min_value = 0, max_value = 120, value = 30)
#     CSI_total = st.number_input("enter CSI score", min_value = 0, value = 50)
#     SAT_total = st.number_input("enter SAT score", min_value = 0, value = 50)
#     SPS_total = st.number_input("enter SPS score", min_value = 0, value = 50)
#     SPSa_total = st.number_input("enter SPSa score", min_value = 0, value = 50)
#     SPSb_total = st.number_input("enter SPSb score", min_value = 0, value = 50)
#     features = np.array([[age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
#     scaled_features = scaler.transform(features)
#     final_features = np.hstack([[[gender_feature]],scaled_features])
#     if st.button("predict"):
#         model_predict = classification_model.predict(final_features)
#         result = model_predict[0]
#         if result == 1:
#             class_name = "fibromyalgia" 
#         else: class_name = "undercontrol"


#-------------------------------------------------------------------------------------------------------

import streamlit as st
import numpy as np
import pickle 
from sklearn.preprocessing import StandardScaler

# 🔹 NEW: Page setup and CSS styling
st.set_page_config(page_title="Fibromyalgia Predictions", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #E1E5EA;
    }
    .stButton>button {
        background-color: #2e8b57;
        color: white;
        border-radius: 8px;
        height: 2.5em;
        width: 8em;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #3cb371;
        color: white;
    }
    .card {
        background-color: rgba(255,255,255,0.05);
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    .center-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Original ML loading logic (unchanged)
IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"

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
# -------------------------------------------------------------------------

def run_app():
    # 🔹 NEW: Use container for a full-width layout
    with st.container():
        st.title("🩺 Fibromyalgia Predictions")
        st.subheader("Answer a few questions to find out if you have fibromyalgia")

        # 🔹 NEW: Add image spanning container width
        st.image(
            IMAGE_ADDRESS,
            caption="Fibromyalgia",
            use_container_width=True
        )

    # 🔹 NEW: Add instructions container
    with st.container():
        with st.expander("📋 Instructions", expanded=True):
            st.markdown("""
            **Before using this tool:**
            1. Visit the **[Fibromyalgia Survey Page](https://example.com/survey)** to obtain your scores.
            2. Fill out the survey and note your **CSI**, **SAT**, **SPS**, **SPSa**, and **SPSb** scores.
            3. Enter those scores below to get your prediction.
            4. You can learn more at:
               - [Fibromyalgia Info - WHO](https://www.who.int)
               - [Patient Resources](https://www.arthritis.org/diseases/fibromyalgia)
            """)

    st.markdown("<hr style='border:1px solid #444;'>", unsafe_allow_html=True)

    # 🔹 NEW: Input section in card style
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        gender = st.radio("Select gender", ("male", "female"))
        gender_feature = 0 if gender == "male" else 1

        age = st.number_input("Enter age", min_value=0, max_value=120, value=30)
        CSI_total = st.number_input("Enter CSI score", min_value=0, value=50)
        SAT_total = st.number_input("Enter SAT score", min_value=0, value=50)
        SPS_total = st.number_input("Enter SPS score", min_value=0, value=50)
        SPSa_total = st.number_input("Enter SPSa score", min_value=0, value=50)
        SPSb_total = st.number_input("Enter SPSb score", min_value=0, value=50)

        st.markdown("</div>", unsafe_allow_html=True)

    # Original feature scaling and prediction logic (unchanged)
    features = np.array([[age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
    scaled_features = scaler.transform(features)
    final_features = np.hstack([[[gender_feature]], scaled_features])

    # 🔹 NEW: Predict button in separate card
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if st.button("Predict"):
            model_predict = classification_model.predict(final_features)
            result = model_predict[0]
            if result == 1:
                class_name = "Fibromyalgia detected"
            else:
                class_name = "Under control"
            st.success(f"✅ **Prediction Result:** {class_name}")
        st.markdown("</div>", unsafe_allow_html=True)

# Run app
run_app()


