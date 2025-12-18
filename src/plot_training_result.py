import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# CONFIG
# -----------------------------
ANPR_CSV = "anpr_results/results.csv"

# Optional: YOLO training metrics CSV (ONLY if you trained locally and have this file)
# Example paths:
#   runs/detect/plate_yolov8n/results.csv
#   runs/detect/train/results.csv
YOLO_TRAIN_CSV = None  # e.g. "runs/detect/plate_yolov8n/results.csv"

OUT_DIR = "anpr_results/plots"
os.makedirs(OUT_DIR, exist_ok=True)


# -----------------------------
# HELPERS
# -----------------------------
def safe_savefig(path: str):
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"[OK] Saved: {path}")


def load_csv_strict(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV not found: {path}")
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"CSV is empty: {path}")
    return df


# -----------------------------
# PART A: ANPR INFERENCE PLOTS
# -----------------------------
def plot_anpr_inference(anpr_csv: str):
    df = load_csv_strict(anpr_csv)

    # Validate required columns
    required_cols = {"image", "crop", "text", "confidence"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in {anpr_csv}: {missing}")

    # Clean
    df["confidence"] = pd.to_numeric(df["confidence"], errors="coerce")
    df["text"] = df["text"].fillna("").astype(str)
    df = df.dropna(subset=["confidence"])

    if df.empty:
        raise ValueError("No valid confidence values found after cleaning. Check your CSV.")

    # 1) Confidence histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["confidence"], bins=20)
    plt.xlabel("YOLO Detection Confidence")
    plt.ylabel("Count")
    plt.title("Distribution of License Plate Detection Confidence")
    plt.grid(True)
    safe_savefig(os.path.join(OUT_DIR, "01_confidence_hist.png"))

    # 2) Average confidence per image
    avg_conf = df.groupby("image")["confidence"].mean().sort_values(ascending=False)
    plt.figure(figsize=(max(10, len(avg_conf) * 0.6), 5))
    avg_conf.plot(kind="bar")
    plt.ylabel("Average Confidence")
    plt.title("Average Detection Confidence per Image")
    plt.grid(True)
    safe_savefig(os.path.join(OUT_DIR, "02_avg_confidence_per_image.png"))

    # 3) Detections per image
    det_count = df["image"].value_counts()
    plt.figure(figsize=(max(10, len(det_count) * 0.6), 5))
    det_count.plot(kind="bar")
    plt.ylabel("Detections (plates) per image")
    plt.title("Number of Detected Plates per Image")
    plt.grid(True)
    safe_savefig(os.path.join(OUT_DIR, "03_detections_per_image.png"))

    # 4) OCR text length vs confidence (sanity check)
    df["text_len"] = df["text"].str.replace(" ", "", regex=False).str.len()
    plt.figure(figsize=(7, 5))
    plt.scatter(df["confidence"], df["text_len"])
    plt.xlabel("Detection Confidence")
    plt.ylabel("OCR Text Length (no spaces)")
    plt.title("OCR Output Length vs Detection Confidence")
    plt.grid(True)
    safe_savefig(os.path.join(OUT_DIR, "04_ocr_length_vs_confidence.png"))

    # Bonus: Save a summary CSV (optional)
    summary_path = os.path.join(OUT_DIR, "summary_stats.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("ANPR Inference Summary\n")
        f.write("=====================\n\n")
        f.write(f"Total detections: {len(df)}\n")
        f.write(f"Unique images: {df['image'].nunique()}\n")
        f.write(f"Mean confidence: {df['confidence'].mean():.4f}\n")
        f.write(f"Median confidence: {df['confidence'].median():.4f}\n")
        f.write(f"Min confidence: {df['confidence'].min():.4f}\n")
        f.write(f"Max confidence: {df['confidence'].max():.4f}\n")
        f.write("\nTop images by avg confidence:\n")
        f.write(avg_conf.head(10).to_string())
        f.write("\n")
    print(f"[OK] Saved: {summary_path}")

    print("\n✅ ANPR inference plots generated successfully.")


# -----------------------------
# PART B: YOLO TRAINING PLOTS (OPTIONAL)
# -----------------------------
def plot_yolo_training(train_csv: str):
    df = load_csv_strict(train_csv)

    # Ultralytics training csv typically has columns like:
    # epoch, train/box_loss, val/box_loss, metrics/mAP50, metrics/mAP50-95, metrics/precision, metrics/recall
    if "epoch" not in df.columns:
        raise ValueError("This does not look like a YOLO training results.csv (missing 'epoch').")

    # Plot mAP vs epoch if available
    if "metrics/mAP50" in df.columns and "metrics/mAP50-95" in df.columns:
        plt.figure(figsize=(8, 5))
        plt.plot(df["epoch"], df["metrics/mAP50"], label="mAP@50")
        plt.plot(df["epoch"], df["metrics/mAP50-95"], label="mAP@50-95")
        plt.xlabel("Epoch")
        plt.ylabel("mAP")
        plt.title("YOLO Training: Validation mAP vs Epoch")
        plt.legend()
        plt.grid(True)
        safe_savefig(os.path.join(OUT_DIR, "10_yolo_map_vs_epoch.png"))
    else:
        print("[WARN] mAP columns not found in training CSV. Skipping mAP plot.")

    # Plot training vs validation box loss if available
    if "train/box_loss" in df.columns and "val/box_loss" in df.columns:
        plt.figure(figsize=(8, 5))
        plt.plot(df["epoch"], df["train/box_loss"], label="train/box_loss")
        plt.plot(df["epoch"], df["val/box_loss"], label="val/box_loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("YOLO Training: Box Loss vs Epoch")
        plt.legend()
        plt.grid(True)
        safe_savefig(os.path.join(OUT_DIR, "11_yolo_box_loss_vs_epoch.png"))
    else:
        print("[WARN] box_loss columns not found. Skipping loss plot.")

    # Optional: precision/recall if available
    if "metrics/precision" in df.columns and "metrics/recall" in df.columns:
        plt.figure(figsize=(8, 5))
        plt.plot(df["epoch"], df["metrics/precision"], label="precision")
        plt.plot(df["epoch"], df["metrics/recall"], label="recall")
        plt.xlabel("Epoch")
        plt.ylabel("Value")
        plt.title("YOLO Training: Precision/Recall vs Epoch")
        plt.legend()
        plt.grid(True)
        safe_savefig(os.path.join(OUT_DIR, "12_yolo_precision_recall_vs_epoch.png"))
    else:
        print("[WARN] precision/recall columns not found. Skipping precision/recall plot.")

    print("\n✅ YOLO training plots generated successfully.")


# -----------------------------
# MAIN
# -----------------------------
def main():
    print("=== Plot Generator ===")
    print(f"ANPR CSV: {ANPR_CSV}")
    print(f"Output folder: {OUT_DIR}\n")

    # A) Always generate ANPR inference plots
    plot_anpr_inference(ANPR_CSV)

    # B) Optionally generate YOLO training plots
    if YOLO_TRAIN_CSV:
        print(f"\nYOLO training CSV: {YOLO_TRAIN_CSV}")
        plot_yolo_training(YOLO_TRAIN_CSV)
    else:
        print("\n[INFO] YOLO_TRAIN_CSV not set. Skipping training-performance plots.")
        print("      If you have training logs, set YOLO_TRAIN_CSV to runs/detect/<run>/results.csv")

    print("\nDone ✅")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)
