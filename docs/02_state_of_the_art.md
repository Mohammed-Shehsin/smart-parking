# 02 — State of the Art


```markdown
# License Plate Detection Project — YOLOv8n

This project reviews three AI approaches for license plate detection and implements a modern lightweight YOLOv8 model for real-world performance.

---

## 📦 Approaches Reviewed

### 1. Classical Computer Vision (Haar Cascades)

**How it works:**  
Uses handcrafted features (Haar filters) and AdaBoost classifier.

**Strengths**
- Very fast
- Low computational cost
- Easy to implement

**Weaknesses**
- Extremely sensitive to lighting, angle, blur
- Fails for modern diverse plate designs
- Outdated for real-world use

---

### 2. Deep Learning CNN Detectors (Faster R-CNN, YOLOv3/v5)

**How it works:**  
CNN backbone extracts features → region proposals → bounding box classification.

**Strengths**
- Good accuracy
- Robust to lighting and rotation
- Works on standard datasets

**Weaknesses**
- Heavier model, slower
- Training requires GPU
- Complex pipeline

---

### 3. Modern YOLO Architectures (YOLOv7, YOLOv8)

**How it works:**  
One-stage end-to-end object detection (no region proposal stage).

**Strengths**
- State-of-the-art performance
- Very fast inference
- Excellent for real-time systems
- Clean training pipeline

**Weaknesses**
- Requires annotated dataset
- GPU highly recommended for training
- Detects object only — OCR still needed

---

## 🚀 Chosen Implementation: YOLOv8n (Ultralytics)

**Why YOLOv8n?**
- Lightweight & fast
- Very high accuracy for single-class detection
- Perfect for student projects
- Easy deployment on CPU
- Excellent documentation & tooling

---

## 📁 Dataset Format (YOLO)

```

car_plate_data/
│
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
└── test/
├── images/
└── labels/

````

### Example `data.yaml`

```yaml
path: car_plate_data
train: train/images
val: test/images

nc: 1
names: ['plate']
````

YOLO label format:

```
class x_center y_center width height
```

All values are normalized (0–1).

---

## 🧠 Model Architecture

YOLOv8 performs two tasks in a single forward pass:

* **Bounding box regression**
* **Object classification**

Key components:

* **Convolutional backbone**
* **C2f blocks (improved CSPNet-like)**
* **PAN/FPN neck**
* **Detection head**

Advantages:

* High resolution multi-scale feature fusion
* Extremely fast inference
* Minimal post-processing overhead

---

## 🛠️ Training Setup

**Platform:** Google Colab (T4 GPU)
**Epochs:** 30
**Image size:** 640×640
**Batch size:** 16
**Optimizer:** Adam
**Loss:** YOLO detection loss

---

## ▶️ Training Command

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="car_plate_data/data.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    name="plate_yolov8n"
)
```

---

## 🔎 Inference Example

```python
from ultralytics import YOLO

model = YOLO("runs/detect/plate_yolov8n/weights/best.pt")
results = model("test/images/sample.jpg")
results.show()
```

---

## 📊 Evaluation Metrics

Recommended metrics:

* mAP@0.5
* mAP@0.5:0.95
* Precision
* Recall
* FPS / latency

---

## 📌 OCR Integration (Future Work)

Detection provides the bounding box of the plate.
To extract the text, integrate OCR:

Options:

* EasyOCR
* Tesseract OCR
* PaddleOCR

**Pipeline:**

1. Detect license plate → crop region
2. Run crop through OCR model
3. Clean/validate detected string

---

## 🛠️ Deployment Notes

* YOLOv8n can run on CPU
* Export formats supported:

  * ONNX
  * TensorRT
  * CoreML
  * OpenVINO

Example export command:

```bash
yolo export model=runs/detect/plate_yolov8n/weights/best.pt format=onnx
```

---

## 📜 License

Educational project.
All datasets and pretrained models are subject to their respective licenses.

---

## 🙏 Acknowledgements

* Ultralytics YOLOv8
* Google Colab GPU
* Dataset contributors

```
```
