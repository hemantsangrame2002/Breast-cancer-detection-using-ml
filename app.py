from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

# Load Pre-trained VGG16 Model
model = VGG16(weights="imagenet", include_top=False, pooling="avg")

@app.route("/")
def home():
    return "Breast Cancer X-ray Detection API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if an image is uploaded
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        img = Image.open(io.BytesIO(file.read())).convert("RGB")

        # Preprocess image
        img = img.resize((224, 224))  # Resize for VGG16
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Get prediction (placeholder: replace with actual model)
        prediction = model.predict(img_array)
        diagnosis = "⚠️ Cancer Detected! ⚠️\n\nOur AI model has detected signs of potential breast cancer in the uploaded X-ray. Please consult a medical professional for further evaluation and diagnosis. Early detection is crucial for effective treatment. Stay strong, and seek medical advice at the earliest." if np.mean(prediction) > 0.5 else "✅ No Cancer Detected ✅\n\nOur AI model did not detect any signs of breast cancer in the uploaded X-ray. However, this is not a substitute for a professional medical diagnosis. If you have any concerns or symptoms, consider consulting a doctor for a thorough check-up."

        return jsonify({"diagnosis": diagnosis})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
