from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=30,
            n_init=3,
            max_cosine_distance=0.3,
            nn_budget=None
        )

    def update(self, detections, frame):
        """
        detections format:
        [
          [x1, y1, x2, y2, confidence, class_id],
          ...
        ]
        """
        tracks = self.tracker.update_tracks(detections, frame=frame)
        return tracks
