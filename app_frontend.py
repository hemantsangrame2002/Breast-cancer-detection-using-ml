import streamlit as st
import requests
from PIL import Image
import base64

# ---- Set Page Config ----
st.set_page_config(
    page_title="Breast Cancer Detection",
    layout="centered",
    page_icon="🔬"
)

# ---- Background Image ----
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stButton > button {{
        background-color: #f63366;
        color: red;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-weight: bold;
    }}
    .stFileUploader, .stImage, .stMarkdown {{
        background: rgba(255, 0.8);
        padding: 1em;
        border-radius: 10px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background image (replace with your local image path or use online image)
set_background("background.png")  # Make sure you have 'background.png' in the same folder

# ---- UI Header ----
st.markdown("<h1 style='text-align: center; color: #f63366;'>🔬 Breast Cancer Detection App</h1>", unsafe_allow_html=True)
st.markdown("### 📸 Upload a breast X-ray image to detect cancer type:")

# ---- File Upload ----
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

# ---- Prediction ----
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing X-ray..."):
            try:
                files = {"file": uploaded_file.getvalue()}
                response = requests.post("http://127.0.0.1:5000/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    st.success(f"🧠 **Diagnosis:** `{result['diagnosis']}`")
                    
                    # Optional: if confidence is returned
                    if 'confidence' in result:
                        st.info(f"📊 Confidence: {result['confidence']}%")

                else:
                    st.error("❌ Error: Unable to get a valid response from the API.")

            except Exception as e:
                st.error(f"❌ Exception: {e}")
