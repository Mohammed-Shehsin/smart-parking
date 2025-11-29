# 03 — Method & Design

This section describes the end-to-end architecture of the project, consisting of:

1. **YOLOv8-based plate detection**  
2. **OCR-based plate text recognition**  
3. **Batch-processing ANPR pipeline**

---

## 3.1 Why YOLOv8n?
YOLOv8n was chosen due to its:
- Lightweight architecture  
- Strong performance on small objects like license plates  
- Real-time inference capability  
- Easy integration and deployment  

It is ideal for both academic exploration and future embedded deployments.

---

## 3.2 Dataset Structure
Training used a YOLO-format dataset:
```
car_plate_data/
├── data.yaml
├── train/
│ ├── images/
│ └── labels/
└── test/
├── images/
└── labels/

```
```
path: car_plate_data
train: train/images
val: test/images
nc: 1
names: ['plate']
```
## 3.3 Model Architecture
YOLOv8 performs two key tasks:

Bounding box regression

Object classification

Its architecture includes:

C2f blocks for efficient feature reuse

Backbone CNN for visual feature extraction

PAN/FPN neck for multi-scale fusion

Detection head for bounding box prediction

## 3.4 Training Pipeline
Training was performed using Google Colab (T4 GPU):

Epochs: 30

Image size: 640×640

Batch size: 16

Optimizer: Adam

Loss: YOLOv8 detection loss

Command:

```
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="car_plate_data/data.yaml", epochs=30, imgsz=640, name="plate_yolov8n")
```
## 3.5 ANPR Pipeline (New Extension)
Following detection, cropped plate regions are passed into EasyOCR:

YOLO detects bounding box

Crop is extracted

OCR reads characters

Results saved in CSV + annotated image

This creates a full end-to-end ANPR solution.

## 3.6 Batch-Processing System
A dedicated script (anpr_batch.py) was designed to process entire folders:

Reads all images

Runs YOLO detection

Crops detected plates

Applies OCR

Saves results to:

``` 
anpr_results/
   crops/
   detections/
   results.csv 
   ```
This enables scalable processing across large datasets.


---
