from src.ingestion.video_reader import VideoReader
from src.detection.detector import ObjectDetector
import cv2

VIDEO_PATH = "data/videos/sample.mp4"

def main():
    print("DSS: Starting Surveillance System")

    reader = VideoReader(VIDEO_PATH)
    detector = ObjectDetector()

    while True:
        frame = reader.read_frame()

        if frame is None:
            print("DSS: End of video stream")
            break

        results = detector.detect(frame)

        annotated_frame = results[0].plot()

        latency = detector.get_latency_ms()
        fps = reader.get_fps()

        cv2.putText(
            annotated_frame,
            f"FPS: {fps} | Inference: {latency} ms",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Defense Surveillance System", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    reader.release()
    cv2.destroyAllWindows()

    print(f"DSS: Average FPS = {reader.get_fps()}")
    print("DSS: Shutdown Complete")

if __name__ == "__main__":
    main()
