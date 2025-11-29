from ultralytics import YOLO
from pathlib import Path

def main():
    # Load trained model
    model = YOLO("best.pt")

    # Folder with test images
    image_dir = Path("images")

    # Run detection on all jpg/pngs in images/
    results = model.predict(
        source=str(image_dir),
        imgsz=640,
        conf=0.25,
        save=True
    )

    print("Done. Check 'runs/detect/predict' for output images.")

if __name__ == "__main__":
    main()
