import os
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import logging
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path ke model H5
MODEL_PATH = './model.h5'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
logger.info(f"Loading model from {MODEL_PATH}")

# Muat model TensorFlow
model = tf.keras.models.load_model(MODEL_PATH)

# Daftar nama kelas
class_names = [
    'AvocadoQ_Fresh', 'AvocadoQ_Mild', 'AvocadoQ_Rotten', 
    'BananaDB_Fresh', 'BananaDB_Mild', 'BananaDB_Rotten',
    'CucumberQ_Fresh', 'CucumberQ_Mild', 'CucumberQ_Rotten',
    'GrapefruitQ_Fresh', 'GrapefruitQ_Mild', 'GrapefruitQ_Rotten',
    'KakiQ_Fresh', 'KakiQ_Mild', 'KakiQ_Rotten',
    'PapayaQ_Fresh', 'PapayaQ_Mild', 'PapayaQ_Rotten',
    'PeachQ_Fresh', 'PeachQ_Mild', 'PeachQ_Rotten',
    'tomatoQ_Fresh', 'tomatoQ_Mild', 'tomatoQ_Rotten'
]

# Buat folder untuk menyimpan file sementara
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET'])
def hello():
    return "Hello, world!"

def load_and_preprocess_image(image, img_size=(224, 224)):
    """
    Preprocess an image for model prediction.

    Args:
        image (PIL.Image): Input image
        img_size (tuple): Target image size

    Returns:
        numpy.ndarray: Preprocessed image array
    """
    img = image.resize(img_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint untuk klasifikasi gambar."""
    if 'file' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['file']
    if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        try:
            image = Image.open(file_path)
            processed_image = load_and_preprocess_image(image)
            logger.info(f"Processed image shape: {processed_image.shape}")

            predictions = model.predict(processed_image)
            logger.info(f"Raw predictions: {predictions}")

            predicted_class_idx = np.argmax(predictions, axis=1)[0]
            confidence = float(np.max(predictions))
            predicted_class_name = class_names[predicted_class_idx]

            os.remove(file_path)  # Bersihkan file sementara

            return jsonify({
                'class': predicted_class_name,
                'confidence': confidence
            })

        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid image file format'}), 400

if __name__ == '__main__':
    # Create uploads folder if not exists
    os.makedirs('uploads', exist_ok=True)
    pass
    # app.run(debug=True, host='0.0.0.0', port=5000)