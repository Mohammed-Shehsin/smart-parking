
import time

class DwellTracker:
    def __init__(self, ttl=3.0):
        self.last_seen = {}
        self.entry = {}
        self.ttl = ttl
        self.events = []  # (plate, t_entry, t_exit, dwell_sec)

    def update(self, detected_plates):
        now = time.time()
        for p in detected_plates:
            if p not in self.entry:
                self.entry[p] = now
            self.last_seen[p] = now
        gone = [p for p, t in list(self.last_seen.items()) if now - t > self.ttl]
        for p in gone:
            t_entry = self.entry.pop(p, None)
            t_last  = self.last_seen.pop(p, None)
            if t_entry and t_last:
                self.events.append((p, t_entry, t_last, t_last - t_entry))
        return gone
