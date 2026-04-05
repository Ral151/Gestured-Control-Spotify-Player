# Gestured-Control-Spotify-Player

## Description

Repository for the controlling spotify player using hand gestures

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ral151/Gestured-Control-Spotify-Player.git
cd Gestured-Control-Spotify-Player
```

### 2. Backend setup

1. Install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#using-miniconda-in-a-commercial-setting)

2. Put YOLO Hagrid model (YOLOv10n_gestures.pt) on the root of this folder. Download the model on this link under model section https://github.com/hukenovs/hagrid?tab=readme-ov-file

3. Create and activate the Conda environment

```bash
conda env create -f environment.yml
conda activate Gesture-Spotify
```

4. Get your credential in this link https://developer.spotify.com/dashboard using your spotify account.

5. Create a `.env` file in the project root with your Spotify app credentials:

```env
SPOTIFY_CLIENT_ID="your_client_id"
SPOTIFY_CLIENT_SECRET="your_client_secret"
SPOTIFY_REDIRECT_URI="http://127.0.0.1:8888/callback"
```

6. Start the backend API

```bash
python -m uvicorn main:app --reload
```

Backend runs at `http://127.0.0.1:8000`.

### 3. Frontend setup

Open a new terminal and run:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Notes

- If `/spotify/profile` returns an error after scope changes, delete `.cache` in project root and restart backend to force Spotify re-auth.
- Make sure your Spotify app is opened with an active playback device.
- Confirm backend is running on `127.0.0.1:8000`.
- Confirm frontend is running on `localhost:5173`.
- Check CORS in `main.py` if frontend URL differs.

## Important Drawback of Current Development

Currently, the UI will call the API over and over again to get user's current playback, its volume, favorite playlists, etc which causes Spotify's API limit rate to be easily exceeded. To prevent this, it's better to just activate the backend directly without accessing the UI since it's made just to see the behavior of the YOLO Detector. 