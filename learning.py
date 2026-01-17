from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data = '/home/amartya/Desktop/ChairProj/data.yaml',
    epochs = 100,
    imgsz = 640,
    batch=16,
    name='chair_detector_v1',
    hsv_s = 0.7,
    hsv_v = 0.4,
    mosaic = 1.0,
    mixup = 0.1,
    perspective = 0.001,
    scale = 0.5,
    fliplr = 0.5
)

