from ultralytics import YOLO

# Carregar o modelo YOLOv8 treinado
model = YOLO(r'C:\yolo\yolo-v8-test\yolo-v8-test\runs\detect\train48\weights\best.pt')

# Fazer a previsão em uma imagem
results = model.predict(source=r'crack.jpg', show=True)

# Exibir as detecções
for result in results:
    result.show()