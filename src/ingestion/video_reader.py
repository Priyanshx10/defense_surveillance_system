import cv2
import time

class VideoReader:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            raise RuntimeError("ERROR: Cannot open video source")

        self.frame_count = 0
        self.start_time = time.time()

    def read_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        self.frame_count += 1
        return frame

    def get_fps(self):
        elapsed = time.time() - self.start_time
        if elapsed == 0:
            return 0
        return round(self.frame_count / elapsed, 2)

    def release(self):
        self.cap.release()
