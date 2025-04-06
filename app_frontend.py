import streamlit as st
import requests

st.title("🔬 Breast Cancer X-ray Detection Web App")
st.markdown("### Upload a breast X-ray image for diagnosis:")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    if st.button("🔍 Predict"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:5000/predict", files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"**Diagnosis:** {result['diagnosis']}")
        else:
            st.error("Error: Could not get a valid response from the API.")
