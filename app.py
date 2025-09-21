import streamlit as st
import numpy as np
import pickle 
IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"
def load_sklearn_model(model_path):
    with open(model_path, "rb") as model_file:
        final_model = pickle.load(model_file)
    return final_model

classification_model = load_sklearn_model("")

def run_app():
    st.title("Fibromyalgia Predicitons")
    st.subheader("Answer a few questions to find out if you have fibromyalgia")
    st.image(IMAGE_ADDRESS, caption = "Fibromyalgia")
    gender = st.radio("select gender", ("male", "female"))
    gender_feature = 0 if gender == "male" else 1
    age = st.number_input("enter age", min_value = 0, max_value = 120, value = 30)
    CSI_total = st.number_input("enter CSI score", min_value = 0, value = 50)
    SAT_total = st.number_input("enter SAT score", min_value = 0, value = 50)
    SPS_total = st.number_input("enter SPS score", min_value = 0, value = 50)
    SPSa_total = st.number_input("enter SPSa score", min_value = 0, value = 50)
    SPSb_total = st.number_input("enter SPSb score", min_value = 0, value = 50)
    features = np.array([[gender_feature, age, CSI_total, SAT_total, SPS_total, SPSa_total, SPSb_total]])
    if st.button("predict"):
        model_predict = classification_model.predict(features)
        result = model_predict[0]
        if result == 1:
            class_name = "fibromyalgia" 
        else: class_name = "undercontrol"
        st.success(f"predicition: {class_name}")

run_app()