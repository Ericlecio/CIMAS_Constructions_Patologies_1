from ultralytics import YOLO

# para marcar as imagens
# https://www.makesense.ai/


def main():
    # Load a model
    # model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="crack.yaml", epochs=30, device="0",amp=False)  # , device=0)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    results = model("crack.jpg")  # predict on an image
    path = model.export(format="onnx")  # export the model to ONNX format
    print("path", path)


if __name__ == '__main__':
    # freeze_support()
    main()
