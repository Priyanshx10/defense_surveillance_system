from src.ingestion.video_reader import VideoReader
from src.detection.detector import ObjectDetector
from src.tracking.tracker import ObjectTracker
from src.threat.engine import ThreatEngine
import cv2

VIDEO_PATH = "data/videos/sample.mp4"
CONFIG_PATH = "config/threat_config.json"
WINDOW_NAME = "Defense Surveillance System"


def main():
    print("DSS: Starting Surveillance System (Detection + Tracking + Threat Rules)")

    reader = VideoReader(VIDEO_PATH)
    detector = ObjectDetector()
    tracker = ObjectTracker()
    threat_engine = ThreatEngine(CONFIG_PATH)

    # Create a resizable window ONCE (correct way)
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, 960, 540)

    while True:
        frame = reader.read_frame()
        if frame is None:
            print("DSS: End of video stream")
            break

        # Detection
        results = detector.detect(frame)
        detections = detector.get_detections_for_tracker(results)

        # Tracking
        tracks = tracker.update(detections, frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            l, t, r, b = map(int, track.to_ltrb())

            # Draw tracked object
            cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"ID {track_id}",
                (l, t - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # Threat evaluation
            events = threat_engine.evaluate(track_id, (l, t, r, b))
            for event in events:
                print("THREAT DETECTED:", event)
                cv2.putText(
                    frame,
                    event["type"],
                    (l, b + 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2
                )

        # Telemetry overlay
        fps = reader.get_fps()
        latency = detector.get_latency_ms()

        cv2.putText(
            frame,
            f"FPS: {fps} | Inference: {latency} ms",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    reader.release()
    cv2.destroyAllWindows()
    print("DSS: Shutdown Complete")


if __name__ == "__main__":
    main()
