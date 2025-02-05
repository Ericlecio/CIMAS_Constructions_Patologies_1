from flask import Flask, render_template, request, jsonify, send_file
from ultralytics import YOLO
import cv2
import numpy as np
import os
import zipfile
import shutil
import uuid

app = Flask(__name__)

# Carregar o modelo YOLO
model = YOLO(r'yolo\best.pt')

# Diretório para salvar imagens processadas
OUTPUT_DIR = 'output_images'
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_images', methods=['POST'])
def process_images():
    if 'images' not in request.files:
        return jsonify({'error': 'Nenhuma imagem fornecida'}), 400

    images = request.files.getlist('images')
    detections = []

    for image in images:
        image_id = str(uuid.uuid4())
        img_path = os.path.join(OUTPUT_DIR, f'{image_id}.jpg')
        image.save(img_path)

        # Ler a imagem com OpenCV
        img = cv2.imread(img_path)
        results = model.predict(img, conf=0.19)

        for result in results:
            for box in result.boxes:
                if int(box.cls[0]) == 1:  # Detectando vegetação
                    x1, y1, x2, y2 = box.xyxy[0]
                    confidence = box.conf[0]
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 4)

                    detections.append({
                        'image': f'{image_id}.jpg',
                        'x1': float(x1),
                        'y1': float(y1),
                        'x2': float(x2),
                        'y2': float(y2),
                        'confidence': float(confidence),
                        'class': int(box.cls[0])
                    })
        
        # Salvar a imagem processada
        output_path = os.path.join(OUTPUT_DIR, f'{image_id}_processed.jpg')
        cv2.imwrite(output_path, img)
    
    return jsonify(detections)

@app.route('/download', methods=['GET'])
def download():
    zip_filename = 'imagens_processadas.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(OUTPUT_DIR):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    return send_file(zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
