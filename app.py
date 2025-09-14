import streamlit as st
import numpy as np
import pickle 
IMAGE_ADDRESS = "https://prdmspst.blob.core.windows.net/images/articles/swimming-walking-effectively-reduce-pain-for-fibromyalgia-e0c8628b-f81c-4688-baeb-1071f6e11065-thumbnail.jpg"

def run_app():
    st.title("Fibromyalgia Predicitons")
    st.subheader("Answer a few questions to find out if you have fibromyalgia")
    st.image(IMAGE_ADDRESS, caption = "Fibromyalgia")

run_app()