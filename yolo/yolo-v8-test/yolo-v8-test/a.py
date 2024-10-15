from ultralytics import YOLO
import mss
import cv2
import numpy as np

# Carregar o modelo treinado YOLOv8
model = YOLO(r'C:\yolo\yolo-v8-test\yolo-v8-test\runs\detect\train5\weights\best.pt')

# Configurar a captura de tela com mss
sct = mss.mss()
# monitor = sct.monitors[1]  # Seleciona o monitor principal (alterar caso tenha mais de um)
monitor = {'top': 0, 'left': 0, 'width': 800, 'height': 600}
while True:
    # Capturar a tela
    screenshot = sct.grab(monitor)

    # Converter o screenshot para numpy array
    frame = np.array(screenshot)

    # Remover o canal alfa (se necessário, em alguns casos a tela captura com 4 canais)
    frame = frame[:, :, :3]

    # Fazer a detecção no frame capturado
    results = model.predict(source=frame, show=True)

    # Exibir a tela com as detecções
    cv2.imshow('YOLOv8 - Deteccao de Objetos na Tela', frame)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fechar janelas
cv2.destroyAllWindows()