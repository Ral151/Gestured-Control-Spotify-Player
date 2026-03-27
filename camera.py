import cv2
from yolo_detector import YoloDetector, GestureStabilizer, Gesture
from spotify_controller import spotify_control
import threading 

class Camera:
    def __init__(self, model_path):
        self.detector = YoloDetector(model_path)
        self.stabilizer = GestureStabilizer()
        self.thread = None
        self.running = False
        self.spotify_controller = spotify_control()
    def start(self):
        if self.running:
            return 
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True) 
        self.thread.start()

    def handle_gesture(self, gesture):
        try:
            if gesture == "palm":
                self.spotify_controller.play_pause()
            elif gesture == "call":
                self.spotify_controller.next_track()
            elif gesture == "gun":
                self.spotify_controller.previous_track()
            elif gesture == "like":
                self.spotify_controller.liked_song()
            elif gesture == "one":
                self.spotify_controller.volume_up()
            elif gesture == "two":
                self.spotify_controller.volume_down()
        except Exception as error:
            print(f"Gesture action failed: {error}")
    
    def run(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Could not open webcam")
        
        while self.running:
            success, frame = cap.read()
            if not success:
                print("Failed to open camera")
                break
            
            detection, result = self.detector.detect_gestures(frame)

            top_label = None
            if detection:
                top_label = detection[0]["label"]

            stable_gesture, trigger = self.stabilizer.update(top_label)

            Gesture.stable_gesture = stable_gesture 
            Gesture.current_gesture = top_label
            if trigger and stable_gesture:
                Gesture.last_gesture = stable_gesture
                self.handle_gesture(stable_gesture)
        cap.release()

    def stop(self):
        self.running = False
