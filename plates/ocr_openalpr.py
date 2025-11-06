
# Optional baseline using OpenALPR CLI if installed.
import subprocess, cv2, os, uuid

def openalpr_ocr(bgr, country="eu"):
    tmp = f"/tmp/{uuid.uuid4().hex}.jpg"
    cv2.imwrite(tmp, bgr)
    try:
        out = subprocess.check_output(["alpr","-c",country,tmp]).decode("utf-8")
    except Exception:
        out = ""
    finally:
        if os.path.exists(tmp): os.remove(tmp)
    for line in out.splitlines():
        if line.strip().startswith("-") and len(line.split())>=2:
            return line.split()[1]
    return ""
