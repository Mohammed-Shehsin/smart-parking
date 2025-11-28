
# Smart Parking: Occupancy + License Plate Dwell Logging

Two-module AI project:

- **Occupancy per bay** (binary classification) using fixed bay polygons and a lightweight CNN.
- **License plate capture and dwell time** (YOLO plate detection → **PyTesseract** OCR primary; **OpenALPR OSS** optional baseline).

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Install Tesseract engine: Linux `sudo apt install tesseract-ocr`; macOS `brew install tesseract`; Windows installer.
```

### Run the PoC demo (plates + dwell)
Put a short video at `data/sample_parking.mp4` or use webcam (default fallback).

```bash
python app/demoAI.py
```

Outputs to `logs/events.csv`.

## Datasets (download separately)
- **PKLot**, **CNRPark-EXT** for occupancy (bay crops).
- **CCPD** (or similar) for plates.

## Structure
```
smart-parking/
├─ parking/     # occupancy classifier
├─ plates/      # plate detection + OCR
├─ app/         # demo app
├─ docs/        # writeups
└─ logs/        # outputs
```

## License
MIT
