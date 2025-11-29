# 04 — Experiments & Results


- **mAP50:** ~0.90
- **mAP50-95:** ~0.55
- **Confidence example:** `plate (0.85)`
- **Inference time:** ~8 ms / image on CPU

The model successfully detects vehicle license plates with high confidence.  
Below are sample results from YOLOv8n inference.

---

### 🖼️ Example Detections

```

plate 0.85

* bounding box visible

```

> The detection outputs are saved under:
```

runs/detect/predict/

```

Example repository directory view (results stored):
```

smart-parking/
├── runs/
│   └── detect/
│       └── predict/
│           ├── images.jpg
│           └── photo-1687039588464-09f1b52208c7.jpg

```

Sample input test images stored in:
```

smart-parking/images/
├── images.jpeg
└── photo-1687039588464-09f1b52208c7.jpeg

```

These files demonstrate successful inference and bounding box detection.
---

## 📸 Example Results

<p align="center">
  <img src="../images/images.jpeg" width="25%" />
  <img src="../runs/detect/predict/images.jpg" width="25%" />
</p>

<p align="center">
  <b>Left: Original Input | Right: YOLOv8n Detection</b>
</p>



---

## 🖥️ Running the Model Locally (Inference Only)

1. Place your trained model:
```

best.pt

````
in the main project folder.

---

### 1️⃣ Install Ultralytics

```bash
pip install ultralytics
````

---

### 2️⃣ Create `demoAI.py`

```python
from ultralytics import YOLO
from pathlib import Path

model = YOLO("best.pt")
image_dir = Path("images")

results = model.predict(source=str(image_dir), save=True)
print("Output saved in runs/detect/predict/")
```

---

### 3️⃣ Run the script

```bash
python demoAI.py
```

---

### 4️⃣ Output Location

All inference images will be saved automatically to:

```
runs/detect/predict/
```

You will see bounding boxes drawn directly onto the images.

---

## ✔️ Summary

* YOLOv8n performs well on license plate detection.
* Accuracy is high (mAP50 ≈ 0.90) even with a small dataset.
* Very fast inference and suitable for CPU deployment.
* Predictions saved automatically in the `runs/detect/predict/` directory.


---
