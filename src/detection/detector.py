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

    def get_detections_for_tracker(self, results):
        """
        Convert YOLO detections to DeepSORT format.

        DeepSORT expects:
        [([x, y, w, h], confidence, class_id), ...]
        """
        detections = []

        boxes = results[0].boxes
        if boxes is None:
            return detections

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            w = x2 - x1
            h = y2 - y1

            conf = float(box.conf[0])
            cls = int(box.cls[0])

            detections.append(([x1, y1, w, h], conf, cls))

        return detections
