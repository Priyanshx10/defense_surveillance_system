from src.ingestion.video_reader import VideoReader
from src.detection.detector import ObjectDetector
from src.tracking.tracker import ObjectTracker
import cv2

VIDEO_PATH = "data/videos/sample.mp4"

def main():
    print("DSS: Starting Surveillance System (Detection + Tracking)")

    reader = VideoReader(VIDEO_PATH)
    detector = ObjectDetector()
    tracker = ObjectTracker()

    while True:
        frame = reader.read_frame()
        if frame is None:
            print("DSS: End of video stream")
            break

        results = detector.detect(frame)
        detections = detector.get_detections_for_tracker(results)

        tracks = tracker.update(detections, frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            l, t, r, b = map(int, track.to_ltrb())

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

        cv2.imshow("Defense Surveillance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    reader.release()
    cv2.destroyAllWindows()
    print("DSS: Shutdown Complete")

if __name__ == "__main__":
    main()
