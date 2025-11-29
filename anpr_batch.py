import cv2
import os
from ultralytics import YOLO
import easyocr
from pathlib import Path
import csv

# -----------------------------
# CONFIGURATION
# -----------------------------
MODEL_PATH = "best.pt"
INPUT_FOLDER = "images"              # folder with your car images
OUTPUT_FOLDER = "anpr_results"       # main output directory

CROPS_FOLDER = f"{OUTPUT_FOLDER}/crops"
DETECTIONS_FOLDER = f"{OUTPUT_FOLDER}/detections"
TEXT_FILE = f"{OUTPUT_FOLDER}/results.csv"

# -----------------------------
# SETUP
# -----------------------------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(CROPS_FOLDER, exist_ok=True)
os.makedirs(DETECTIONS_FOLDER, exist_ok=True)

detector = YOLO(MODEL_PATH)
ocr_reader = easyocr.Reader(['en'])

# -----------------------------
# FUNCTION: OCR + DETECTION
# -----------------------------
def process_image(img_path):
    img = cv2.imread(img_path)

    # Run YOLO
    results = detector.predict(img, verbose=False)
    res = results[0]

    boxes = res.boxes.xyxy.cpu().numpy()
    scores = res.boxes.conf.cpu().numpy()

    output_entries = []

    for i, (box, score) in enumerate(zip(boxes, scores)):
        x1, y1, x2, y2 = box.astype(int)

        # Crop plate
        crop = img[y1:y2, x1:x2]

        crop_name = f"{Path(img_path).stem}_plate_{i}.jpg"
        crop_path = f"{CROPS_FOLDER}/{crop_name}"
        cv2.imwrite(crop_path, crop)

        # OCR
        text_list = ocr_reader.readtext(crop, detail=0)
        text = " ".join(text_list).strip()

        output_entries.append({
            "image": Path(img_path).name,
            "crop": crop_name,
            "text": text,
            "confidence": float(score)
        })

        # Draw bounding box on main image
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2)

    # Save annotated detection image
    output_img_path = f"{DETECTIONS_FOLDER}/{Path(img_path).name}"
    cv2.imwrite(output_img_path, img)

    return output_entries


# -----------------------------
# MAIN EXECUTION
# -----------------------------
all_results = []

image_files = [f for f in os.listdir(INPUT_FOLDER)
               if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

print(f"Found {len(image_files)} images. Processing...")

for img_file in image_files:
    full_path = f"{INPUT_FOLDER}/{img_file}"
    print(f"Processing: {img_file}")

    results = process_image(full_path)
    all_results.extend(results)

# -----------------------------
# SAVE RESULTS TO CSV
# -----------------------------
with open(TEXT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["image", "crop", "text", "confidence"])
    writer.writeheader()
    for row in all_results:
        writer.writerow(row)

print("\nDone!")
print(f"Results saved to: {OUTPUT_FOLDER}")
print(f"- Crops: {CROPS_FOLDER}")
print(f"- Annotated images: {DETECTIONS_FOLDER}")
print(f"- Text results: {TEXT_FILE}")
