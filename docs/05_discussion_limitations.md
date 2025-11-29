# 05 — Discussion & Limitations

While YOLOv8n achieves strong detection accuracy, several practical limitations remain.

## 5.1 Discussion
The implemented system successfully performs:
- Plate detection  
- Plate cropping  
- Text extraction via OCR  
- Batch processing across entire folders  

This demonstrates that a lightweight model such as YOLOv8n can serve as the backbone of a functional ANPR pipeline.

---

## 5.2 Limitations

### 1. Dataset scope
The dataset primarily contains plates from specific regions.  
Generalization to other countries may be limited.

### 2. Small or distant plates
Detection quality degrades when the plate occupies only a few pixels.

### 3. OCR sensitivity
Although EasyOCR is robust, it struggles with:
- Motion blur  
- Low-light images  
- High glare or reflections  
- Non-standard fonts  

### 4. No temporal consistency
The pipeline currently processes **images only**, not video.  
Repeated detections in sequential frames are not tracked.

---

## 5.3 Future Work

### 1. Enhanced OCR Integration
Use advanced models such as:
- CRNN  
- PaddleOCR  
- Transformer-based text recognition  

### 2. Multi-country dataset expansion
Incorporate plates from:
- EU  
- Asia  
- Middle East  
- North America  

### 3. Edge deployment
Optimize the model for:
- Raspberry Pi 4/5  
- Jetson Nano / Xavier  
- ARM devices  
Using quantization (INT8) for speed.

### 4. Full ANPR Pipeline
Implement:
1. YOLO detection  
2. OCR  
3. Regex-based text post-processing  
4. Vehicle tracking  
5. API/database integration  

### 5. Multi-object tracking for video
Integrate trackers such as:
- ByteTrack  
- DeepSORT  
- BoT-SORT  

---

## 5.4 Summary
The current system performs reliable license plate detection and OCR-based text recognition.  
With dataset expansion, improved OCR, and edge optimization, the project can evolve into a **production-grade ANPR system** suitable for real-world deployments.
