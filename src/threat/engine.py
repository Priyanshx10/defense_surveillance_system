import json
import time


class ThreatEngine:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            self.config = json.load(f)

        self.object_states = {}

    def _point_in_rect(self, x, y, rect):
        return (
            rect["x"] <= x <= rect["x"] + rect["width"] and
            rect["y"] <= y <= rect["y"] + rect["height"]
        )

    def evaluate(self, track_id, bbox):
        """
        bbox: (l, t, r, b)
        """
        current_time = time.time()
        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)

        if track_id not in self.object_states:
            self.object_states[track_id] = {
                "first_seen": current_time,
                "zone_entry_time": None
            }

        state = self.object_states[track_id]
        events = []

        for zone in self.config["restricted_zones"]:
            inside = self._point_in_rect(cx, cy, zone)

            if inside:
                if state["zone_entry_time"] is None:
                    state["zone_entry_time"] = current_time

                duration = current_time - state["zone_entry_time"]

                if (
                    self.config["loitering"]["enabled"]
                    and duration >= self.config["loitering"]["time_threshold_seconds"]
                ):
                    events.append({
                        "type": "LOITERING",
                        "zone": zone["id"],
                        "track_id": track_id,
                        "duration": round(duration, 2)
                    })
            else:
                state["zone_entry_time"] = None

        return events
