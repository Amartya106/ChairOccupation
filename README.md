# Chair Occupation Detection
This project uses YOLOv8 for detection of a specific chair(small dataset used). Currently it only detects an unoccupied chair in real time and in the future is intended to distinguish between occupied and unccupied chairs using the Arduino UNO Q.

## Performance Metrics
* **Accuracy:** 99.5% mAP50
* **Optimal Confidence Threshold:** 0.644 (based on F1-Confidence Curve)

![F1-Confidence Curve](https://github.com/user-attachments/assets/ce728a33-e096-4340-88d7-6711b52cec50)


## 📊 Project Progress

| Class Name | Status | Accuracy (mAP50) |
| :--- | :--- | :--- |
| **Unoccupied Chair** | ✅ Completed | 99.5% |
| **Occupied Chair** | 🏗️ In Progress | TBD |


## Technical Choice
### Why YOLOv8 over YOLOv11?
After comparing results from both,  **YOLOv8** was selected because:
* **Stability:** v8 demonstrated a more robust F1-Confidence curve (peak at 0.644 compared to 0.357 for v11)
* **Bounding Boxes:** Observed tighter and more consistent bounding boxes on the target object with v8
