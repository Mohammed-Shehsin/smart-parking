# scripts/make_ccpd_like_sample.py
# Creates a tiny "ccpd-like" sample dataset from a video using your detector,
# saving plate crops + a CSV of detections for quick experiments.

import os, csv, cv2
from ultralytics import YOLO
from plates.ocr_pytess import ocr_plate

VIDEO = os.environ.get("SP_VIDEO", "data/sample_parking.mp4")  # change if needed
OUT   = "data/ccpd_like_sample"
MODEL = os.environ.get("SP_WEIGHTS", "keremberke/yolov8n-license-plate")

os.makedirs(OUT, exist_ok=True)
os.makedirs(f"{OUT}/images", exist_ok=True)
csv_path = f"{OUT}/labels.csv"

det = YOLO(MODEL)
cap = cv2.VideoCapture(0 if not os.path.exists(VIDEO) else VIDEO)

with open(csv_path, "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["img_path","x1","y1","x2","y2","plate_text"])
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok: break
        results = det.predict(source=frame, imgsz=640, conf=0.25, verbose=False)
        saved = False
        for r in results:
            for b in r.boxes:
                x1,y1,x2,y2 = map(int, b.xyxy[0].tolist())
                crop = frame[y1:y2, x1:x2]
                if crop.size == 0: 
                    continue
                txt = ocr_plate(crop)
                # save whole frame so you can reuse it later
                img_name = f"frame_{idx:06d}.jpg"
                if not saved:
                    cv2.imwrite(f"{OUT}/images/{img_name}", frame)
                    saved = True
                wr.writerow([f"images/{img_name}", x1,y1,x2,y2, txt])
        idx += 1
cap.release()
print(f"Saved small sample to {OUT}")
