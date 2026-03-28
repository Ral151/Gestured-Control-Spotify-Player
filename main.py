from fastapi import FastAPI
from camera import Camera
from yolo_detector import Gesture
from contextlib import asynccontextmanager
from spotify_controller import spotify_control as SpotifyController
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager    
async def lifespan(app: FastAPI):   
    camera.start()
    yield
    camera.stop()  

model = "YOLOv10n_gestures.pt"
camera = Camera(model)

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

spotify_controller = SpotifyController()

@app.get("/spotify/current")
def spotify_current():
    return spotify_controller.current_track()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/gesture")
def get_gesture():
    return {"Current Gesture": Gesture.current_gesture, "Stable Gesture": Gesture.stable_gesture, "Last Triggered": Gesture.last_gesture} 
