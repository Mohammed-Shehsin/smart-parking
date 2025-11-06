
import cv2, csv, os
from plates.detect_yolo import PlateDetector
from plates.ocr_pytess import ocr_plate
from plates.track import DwellTracker

VIDEO_PATH = os.environ.get("SP_VIDEO", "data/sample_parking.mp4")
WEIGHTS    = os.environ.get("SP_WEIGHTS", "weights/plate_yolo.pt" )

def main():
    det = PlateDetector(WEIGHTS, conf=0.25)
    trk = DwellTracker(ttl=2.5)

    cap = cv2.VideoCapture(VIDEO_PATH if os.path.exists(VIDEO_PATH) else 0)
    os.makedirs("logs", exist_ok=True)
    with open("logs/events.csv","w",newline="") as f:
        wr = csv.writer(f); wr.writerow(["plate","t_entry","t_exit","dwell_sec"])
        while True:
            ok, frame = cap.read()
            if not ok: break
            boxes = det.detect(frame)
            plates = []
            for (x1,y1,x2,y2,conf) in boxes:
                crop = frame[y1:y2, x1:x2]
                plate_txt = ocr_plate(crop)
                if plate_txt:
                    plates.append(plate_txt)
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.putText(frame, plate_txt, (x1, y1-8), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2)
            gone = trk.update(plates)
            while trk.events:
                p, t_in, t_out, dwell = trk.events.pop(0)
                wr.writerow([p, int(t_in), int(t_out), int(dwell)])
            cv2.imshow("Smart Parking - Plates", frame)
            if cv2.waitKey(1) & 0xFF == 27: break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
