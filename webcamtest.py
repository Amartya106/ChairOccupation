import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/chair_detector_v13/weights/best.pt")

cap = cv2.VideoCapture(4)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    results = model.predict(source=frame, conf=0.7, stream=True)

    for result in results:
        annoted_frame = result.plot()
        cv2.imshow("Webcam", annoted_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()