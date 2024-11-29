from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = Flask(__name__)

# Carregar o modelo YOLO
model = YOLO(r'yolo\best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    
    # Ler a imagem
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Fazer a predição
    results = model.predict(img, conf=0.19)

    # Extrair as caixas delimitadoras e informações de confiança
    detections = []
    for result in results:
        for box in result.boxes:
            if int(box.cls[0]) == 1:  # Filtrar apenas a classe 1
                detections.append({
                    'x1': float(box.xyxy[0][0]),
                    'y1': float(box.xyxy[0][1]),
                    'x2': float(box.xyxy[0][2]),
                    'y2': float(box.xyxy[0][3]),
                    'confidence': float(box.conf[0]),
                    'class': int(box.cls[0])
            })

    return jsonify(detections)

if __name__ == '__main__':
    app.run(debug=True)
