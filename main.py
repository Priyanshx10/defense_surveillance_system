from src.ingestion.video_reader import VideoReader
import cv2

VIDEO_PATH = "data/videos/sample.mp4"

def main():
    print("DSS: Starting Video Ingestion")

    reader = VideoReader(VIDEO_PATH)

    while True:
        frame = reader.read_frame()

        if frame is None:
            print("DSS: End of video stream")
            break

        cv2.imshow("Defense Surveillance Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    fps = reader.get_fps()
    print(f"DSS: Average FPS = {fps}")

    reader.release()
    cv2.destroyAllWindows()
    print("DSS: Video Ingestion Shutdown Complete")

if __name__ == "__main__":
    main()
