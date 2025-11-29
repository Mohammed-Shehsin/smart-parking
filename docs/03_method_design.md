# 03 — Method & Design


## 🚀 Why YOLOv8n?

- **Lightweight & fast**
- **Very high accuracy for single-class detection**
- **Perfect for student projects**
- **Easy deployment on CPU**
- **Excellent documentation & tooling**



## 📁 Dataset

### Dataset structure (YOLO format)

```

car_plate_data/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
└── test/
├── images/
└── labels/

````

### data.yaml

```yaml
path: car_plate_data
train: train/images
val: test/images

nc: 1
names: ['plate']
````

---

## 🧠 Model Architecture

YOLOv8 performs **two tasks simultaneously**:

* **Bounding box regression**
* **Object classification**

Internally handled by:

* **C2f blocks** (efficient residual/feature reuse)
* **Convolutional backbone**
* **PAN/FPN neck** (multi-scale feature fusion)
* **Detection head**

This produces real-time, single-stage predictions without region proposals.

---

## 🛠️ Training Setup

* **Platform:** Google Colab (T4 GPU)
* **Epochs:** 30
* **Image size:** 640×640
* **Batch size:** 16
* **Optimizer:** Adam
* **Loss:** YOLO detection loss

---

## ▶️ Training Command

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="car_plate_data/data.yaml",
    epochs=30,
    imgsz=640,
    name="plate_yolov8n"
)
```



