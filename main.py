from fastapi import FastAPI
from camera import Camera
from yolo_detector import Gesture
from contextlib import asynccontextmanager


@asynccontextmanager    
async def lifespan(app: FastAPI):   
    camera.start()
    yield
    camera.stop()  

model = "YOLOv10n_gestures.pt"
camera = Camera(model)

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/gesture")
def get_gesture():
    return {"Current Gesture": Gesture.current_gesture, "Stable Gesture": Gesture.stable_gesture, "Last Triggered": Gesture.last_gesture} 
