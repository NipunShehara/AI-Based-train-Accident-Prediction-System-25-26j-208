from ultralytics import YOLO
import cv2
import os

MODEL_PATH = "runs/detect/train/weights/best.pt"
IMAGE_PATH = "test_media/images/test.jpg"   # put a test image here

def main():
    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Model not found: {MODEL_PATH}")
        print("Train first: yolo detect train data=dataset_yolo/data.yaml model=yolov8n.pt epochs=50 imgsz=640")
        return

    if not os.path.exists(IMAGE_PATH):
        print(f"[ERROR] Test image not found: {IMAGE_PATH}")
        print("Put a file named test.jpg inside test_media/images/")
        return

    model = YOLO(MODEL_PATH)
    img = cv2.imread(IMAGE_PATH)

    results = model(img)
    annotated = results[0].plot()

    out_path = "test_media/images/output_test.jpg"
    cv2.imwrite(out_path, annotated)
    print(f"[OK] Saved result image: {out_path}")

if __name__ == "__main__":
    main()
