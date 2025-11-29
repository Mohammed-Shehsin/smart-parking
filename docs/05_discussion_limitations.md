# 05 — Discussion & Limitations

While YOLOv8n demonstrates high detection performance, the current implementation has notable constraints:

- **Dataset scope:**  
  The dataset is limited to specific countries' plate formats.  
  Models trained on narrow domains generalize poorly to unfamiliar styles.

- **Small or distant plates:**  
  Performance drops when license plates occupy very few pixels.  
  Detection confidence decreases significantly for plates far from the camera.

- **No OCR Pipeline:**  
  This system **detects plates only**.  
  It does not extract or read the alphanumeric characters (no ANPR).

- **Environmental interference:**  
  Strong shadows, reflections, motion blur, and angled plates may still cause detection failures.

---

## 🔮 7. Future Work

To evolve this project into a full ANPR (Automatic Number Plate Recognition) system, the following upgrades are recommended:

### 📌 1. Integrate OCR
Convert detected bounding box regions into text using:
- **EasyOCR**
- **Tesseract**
- **CRNN (Convolutional Recurrent Neural Network)**
- **PaddleOCR**

YOLO → Crop ROI → OCR → Text Output

---

### 📌 2. Expand Dataset Coverage
Train or fine-tune with:
- Multi-country plates
- Diverse fonts and languages
- Varying sizes and aspect ratios
- Different weather, day/night, and camera angles

Improves robustness for real-world deployment.

---

### 📌 3. Edge Deployment
Optimize for embedded devices:
- **Raspberry Pi 4 / Pi 5**
- **Jetson Nano / Xavier / Orin**

Quantization (INT8) and model pruning can support real-time inference at low power.

---

### 📌 4. Full ANPR Pipeline
End-to-end architecture:
1. Detection (YOLO)
2. ROI cropping
3. OCR
4. Post-processing (regex, formatting, validation)
5. Storage (CSV, SQL, API)

Useful for parking, toll systems, or traffic monitoring.

---

### 📌 5. Multi-Object Tracking
Add temporal tracking for video streams:
- **ByteTrack**
- **BoT-SORT**
- **DeepSORT**

This avoids re-identifying the same car plate for each frame.

---

## 🌱 Summary
The current implementation performs real-time **plate detection only**.  
To achieve commercial-grade ANPR, OCR integration, dataset expansion, and hardware-level optimization are essential.
