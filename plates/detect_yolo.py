
from ultralytics import YOLO

class PlateDetector:
    def __init__(self, weights="weights/plate_yolo.pt", conf=0.25, imgsz=640):
        self.model = YOLO(weights)
        self.conf = conf
        self.imgsz = imgsz

    def detect(self, frame):
        results = self.model.predict(source=frame, imgsz=self.imgsz, conf=self.conf, verbose=False)
        boxes = []
        for r in results:
            for b in r.boxes:
                x1,y1,x2,y2 = map(int, b.xyxy[0].tolist())
                conf = float(b.conf[0])
                boxes.append((x1,y1,x2,y2,conf))
        return boxes
