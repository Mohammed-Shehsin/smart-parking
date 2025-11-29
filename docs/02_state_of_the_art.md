# 02 — State of the Art

This section reviews existing academic and industrial approaches to license plate detection and recognition. Three primary categories were evaluated.

## 2.1 Classical Computer Vision (Haar Cascades)
Early ANPR relied on handcrafted feature extractors such as Haar cascades, edge detection, and morphology-based segmentation.

### Strengths
- Very fast and lightweight  
- Works on low-power embedded hardware  
- Simple to implement  

### Weaknesses
- Fails under variations in lighting, angle, shadow, or noise  
- Highly sensitive to plate design diversity  
- Poor generalization across countries  

Although historically important, classical CV is **insufficient for modern ANPR workloads**.

---

## 2.2 CNN-based Detectors (Faster R-CNN, YOLOv3/v5)
The introduction of deep convolutional networks significantly improved detection accuracy.

### Strengths
- Good robustness to noise and illumination  
- Reasonable generalization to different plate styles  
- Strong academic benchmark performance  

### Weaknesses
- Relatively slower inference  
- Computationally expensive  
- More complex training pipelines  

---

## 2.3 Single-Shot Detectors: YOLOv7 / YOLOv8
YOLOv8 represents the latest generation of one-stage object detectors, optimized for both accuracy and real-time performance.

### Strengths
- Excellent inference speed  
- High accuracy even with lightweight models  
- Easy training and deployment  
- Suitable for edge devices  

### Weaknesses
- Requires high-quality labeled datasets  
- Detection alone is insufficient for full ANPR (needs OCR)  

---

## 2.4 OCR Approaches
License plate reading requires a second stage: text recognition. Three OCR families were analyzed:

| Method | Description | Pros | Cons |
|-------|-------------|------|------|
| **Tesseract** | Classical OCR using rule-based segmentation | Lightweight | Poor on noisy/angled plates |
| **EasyOCR** | CNN-based deep learning OCR | Strong generalization, multilingual | Slightly slower |
| **CRNN / LSTM Models** | End-to-end trainable recognition | Highest performance | Requires large training datasets |

**EasyOCR** was selected for this project due to simplicity, robustness, and ability to process real-world plates without retraining.

---
