from ultralytics import YOLO
import easyocr
import cv2
import numpy as np

# 1. Load models
detector = YOLO("best.pt")          # your trained YOLOv8 plate detector
reader = easyocr.Reader(['en'])     # language for OCR (adjust if needed)

# 2. Load image
img_path = "images/images.jpeg"
img = cv2.imread(img_path)

# 3. Run detection
results = detector.predict(source=img, verbose=False)

# 4. Take first result (one image)
res = results[0]
boxes = res.boxes.xyxy.cpu().numpy()      # [x1, y1, x2, y2]
scores = res.boxes.conf.cpu().numpy()

plate_texts = []

for box, score in zip(boxes, scores):
    x1, y1, x2, y2 = box.astype(int)

    # 5. Crop the plate region
    crop = img[y1:y2, x1:x2]

    # 6. Run OCR on the cropped plate
    ocr_result = reader.readtext(crop, detail=0)   # detail=0 → only text strings
    text = " ".join(ocr_result).strip()

    plate_texts.append({
        "bbox": (x1, y1, x2, y2),
        "det_conf": float(score),
        "text": text
    })

print(plate_texts)
