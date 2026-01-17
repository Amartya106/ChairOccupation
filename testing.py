from ultralytics import YOLO

model = YOLO("runs/detect/chair_detector_v13/weights/best.pt")

results = model.predict(source="/home/amartya/Downloads/Testing-20260111T063440Z-1-001/Testing", conf=0.644, save=True)

for result in results:
    print(result.boxes.xyxy)
    print(result.boxes.conf)

