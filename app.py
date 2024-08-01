import streamlit as st
from utils import model_prediction
import requests

# set the page config
st.set_page_config(page_title="Sentence Correction", page_icon="📝", layout="centered")

# set the title
st.title("Sentence Correction")

user_input=st.text_area("Enter text: ")

if st.button("Remove Error"):
    with st.status("Hitting the api please wait...."):
        try:
            response=requests.post("http://localhost:8000/predict", json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                st.error(f"Original Text: {result['original_text']}")
                st.success(f"Model Prediction: {result['corrected_text']}")
                # st.json(result)
            else:
                st.error("Error in fetching prediction from the API.")
        except Exception as e:
            st.write(f"There should be some issue in the api serving {e}")



