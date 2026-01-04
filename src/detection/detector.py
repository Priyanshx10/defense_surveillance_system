import time
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", confidence=0.4):
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.last_inference_time = 0.0

    def detect(self, frame):
        start = time.time()

        results = self.model(
            frame,
            conf=self.confidence,
            verbose=False
        )

        self.last_inference_time = round((time.time() - start) * 1000, 2)
        return results

    def get_latency_ms(self):
        return self.last_inference_time
