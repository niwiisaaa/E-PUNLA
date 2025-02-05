from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import uuid
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'secret_key_here'

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model
try:
    model = load_model('leaf_model.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class_indices = {'HEALTHY': 0, 'UNHEALTHY': 1, 'Class3': 2}
class_labels = {v: k for k, v in class_indices.items()}

# Helper function to predict the class of an image
def predict_image(img_path, model, class_labels):
    try:
        img = image.load_img(img_path, target_size=(150, 150))  # Ensure this matches your model's input size
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        return class_labels[predicted_class]
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error during prediction"

@app.route('/')
def dashboard():
    # Sample data to render dynamically
    weather = {"temperature": "32°C", "location": "Camarines Sur"}
    insight = {"planting_calendar": 40, "soil_conditions": 70, "recommendations": 90}
    return render_template('dashboard.html', weather=weather, insight=insight)

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request.', 'danger')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading.', 'danger')
            return redirect(request.url)

        if file:
            # Secure the file name and save it
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)

            # Make a prediction
            if model:
                prediction = predict_image(file_path, model, class_labels)
            else:
                prediction = "Model not loaded. Please check the model file."

            # Return the result
            return render_template('result.html', prediction=prediction, image_path=file_path)

    return render_template('upload.html')

# Main entry point
if __name__ == '__main__':
    # Create upload folder if it does not exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Run the application in debug mode for development
    app.run(debug=True)
