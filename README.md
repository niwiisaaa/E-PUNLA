# E-PUNLA 🌱

**E-PUNLA** is a machine learning–based leaf disease prediction system developed as an academic project for Sofware Engineering 1. The application aims to assist in the early detection of plant diseases by analyzing leaf images and providing fast, accessible predictions.

---

## 📌 Overview

E-PUNLA leverages image classification techniques to identify common plant leaf diseases. By integrating a trained machine learning model into a web-based application, the project demonstrates the practical use of artificial intelligence in agriculture and environmental sustainability.

---

## ✨ Features

- **Leaf Image Upload** – Users can upload plant leaf images for analysis  
- **Disease Prediction** – Automatically predicts possible leaf diseases  
- **Web-Based Interface** – Simple and user-friendly design  
- **Fast Results** – Displays prediction output in real time  
- **Academic-Oriented** – Designed for learning, demonstration, and research  

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher  
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/niwiisaaa/E-PUNLA.git
cd E-PUNLA
```

2. (Optional but recommended) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to:
```
http://localhost:5000
```

---

## 📂 Project Structure

```
E-PUNLA/
├── model/
│   └── trained_model.h5     # Pre-trained ML model
├── static/
│   ├── css/                 # Stylesheets
│   └── uploads/             # Uploaded leaf images
├── templates/
│   ├── index.html           # Main upload page
│   └── result.html          # Prediction results page
├── app.py                   # Flask application entry point
├── requirements.txt         # Project dependencies
└── README.md
```

---

## Usage Guide

1. Launch the application in your browser  
2. Upload a clear image of a plant leaf  
3. Submit the image for processing  
4. View the predicted disease result  

---

## 🛠 Technologies Used

- **Language**: Python  
- **Web Framework**: Flask  
- **Machine Learning**: TensorFlow / Keras  
- **Frontend**: HTML, CSS  
- **Image Processing**: OpenCV / PIL  
