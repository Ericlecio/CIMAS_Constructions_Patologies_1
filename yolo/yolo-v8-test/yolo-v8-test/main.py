from ultralytics import YOLO
import cv2
from windowcapture import WindowCapture
from collections import defaultdict
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

offset_x = 400  # 0
offset_y = 300  # 30
wincap = WindowCapture(size=(1366, 768), origin=(offset_x, offset_y))

model = YOLO("yolov8n.pt")

seguir = False

while True:

    sucess, img = capture.read()

    if sucess:
        if seguir:
            results = model.track(img, persist=True)
        else:
            results = model(img)

        for result in results:
            img = result.plot()

        cv2.imshow("tela", img)

    k = cv2.waitKey(1)
    if k == ord('k'):
        break

capture.release()
cv2.destroyAllWindows()
print("desligando")
