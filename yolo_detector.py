import cv2
from ultralytics import YOLO
from collections import Counter
import time

class YoloDetector:
    """YOLO Object Detector for hand gestures"""
    def __init__ (self, model_path='YOLOv10n_gestures.pt', confidence_threshold=0.5):
        self.model= YOLO(model_path)
        self.confidence_threshold = confidence_threshold
    
    def detect_gestures(self, frame):
        res = self.model.predict(frame, conf=self.confidence_threshold, verbose=False)
        res = res[0]
        boxes = res.boxes
        names = res.names

        detections = []
        if boxes is None or len(boxes) < 1:
            return detections, res
        else:
            for box in boxes:
                class_id= int(box.cls[0])
                confidence = float(box.conf[0])
                x1,y1,x2,y2 = box.xyxy[0].tolist()

                detections.append({
                    "label": names[class_id],
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                })
            
            detections.sort(key=lambda x: x['confidence'], reverse=True)
            return detections, res  

class GestureStabilizer:
    """Stabilizing gesture logic to prevent rapid changes and false positives"""
    def __init__(self, window_size: int = 5, min_count: int = 3, cooldown_seconds: float = 1.5):
        self.window = list(window_size * [None])
        self.min_count = min_count
        self.cooldown_seconds = cooldown_seconds
        self.last_trigger_time = 0.0
        self.last_triggered_gesture = None

    def update(self, gesture_label: str | None):
        self.window.append(gesture_label)
        self.window.pop(0)

        valid_gestures = [g for g in self.window if g is not None]
        if not valid_gestures:
            return None, False

        counter = Counter(valid_gestures)
        best_gesture, count = counter.most_common(1)[0]

        if count >= self.min_count:
            is_stable = True
        else:
            is_stable = False
        if not is_stable:
            return None, False

        now = time.time()
        in_cooldown = (now - self.last_trigger_time) < self.cooldown_seconds

        if in_cooldown and best_gesture == self.last_triggered_gesture:
            return best_gesture, False

        self.last_trigger_time = now
        self.last_triggered_gesture = best_gesture
        return best_gesture, True
    
class Gesture:
    current_gesture = None
    last_gesture = None
    stable_gesture = None
