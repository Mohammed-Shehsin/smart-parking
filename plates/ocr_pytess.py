
import cv2, pytesseract
from PIL import Image
import numpy as np

ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def preprocess_plate(plate_bgr):
    gray = cv2.cvtColor(plate_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    return th

def ocr_plate(plate_bgr):
    img = preprocess_plate(plate_bgr)
    config = (
        "--oem 1 --psm 7 "
        f"-c tessedit_char_whitelist={ALNUM} "
        "-c load_system_dawg=0 -c load_freq_dawg=0"
    )
    text = pytesseract.image_to_string(Image.fromarray(img), config=config)
    text = ''.join([c for c in text if c.upper() in ALNUM]).upper()
    return text
