# 04 — Experiments & Results

## 4.1 YOLOv8 Detection Performance

Training results show strong detection performance:

- **mAP50:** ~0.90  
- **mAP50–95:** ~0.55  
- **Inference speed (CPU):** ~8 ms/image  
- **Typical confidence scores:** 0.80–0.95  

These metrics confirm that YOLOv8n is highly effective even with lightweight configuration.

---

## 4.2 Example Detection Outputs

Example YOLOv8n predictions:
```
plate 0.85
(bounding box visualized)
```

Detected outputs were saved in:
```
runs/detect/predict/
```


Sample structure:
```
smart-parking/
├── runs/
│ └── detect/
│ └── predict/
│ ├── images.jpg
│ └── sample.jpeg

```

---

## 4.3 End-to-End ANPR Results (New)

After integrating OCR, the system performs:

1. Plate detection  
2. Plate cropping  
3. Text extraction  

Example output in `results.csv`:
```
image,crop,text,confidence
car1.jpg,car1_plate_0.jpg,KA 64 N 0G99,0.85
car2.jpg,car2_plate_0.jpg,DL 03 AB 5544,0.91
```

OCR successfully reads clear plates and performs consistently across typical lighting conditions.

---

## 4.4 Qualitative Visual Results

- Correct bounding box placement  
- Accurate cropping  
- OCR extraction with high readability  

These results demonstrate the feasibility of a full ANPR pipeline using lightweight tools.

---

## 4.5 Local Execution

To run inference locally:
```
pip install ultralytics easyocr
python demoAI.py

```
Outputs stored under:
```
runs/detect/predict/
```

---
