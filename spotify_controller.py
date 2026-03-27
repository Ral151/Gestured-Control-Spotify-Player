import os 
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class spotify_control:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope="user-modify-playback-state user-read-playback-state user-read-currently-playing streaming user-read-email user-read-private user-library-read user-library-modify",
            open_browser=True
        ))

    def play_pause(self):
        current_playback = self.sp.current_playback()
        if current_playback and current_playback["is_playing"] == True:
            self.sp.pause_playback()
            print("Playback paused")
        else:
            self.sp.start_playback()
            print("Playback started")

    def next_track(self):
        self.sp.next_track()
        print("Skipped to next track")

    def previous_track(self):
        self.sp.previous_track()
        print("Went back to previous track")
    
    def liked_song(self):
        current_track = self.sp.current_user_playing_track()
        if current_track and current_track["item"]:
            current_track_id = current_track["item"]["id"]
            current_track_name = current_track["item"]["name"]
            self.sp.current_user_saved_tracks_add([current_track_id])
            print(f"Liked '{current_track_name}'")
        else:
            print("No track is played")
     
    def volume_up(self):
        current_playback = self.sp.current_playback()
        if current_playback and current_playback["device"]:
            current_volume = current_playback["device"]["volume_percent"]
            if current_volume < 100:    
                percent_up = 10 if current_volume <= 90 else (100 - current_volume) 
                new_volume = current_volume + percent_up
                self.sp.volume(new_volume)
                print(f"Current Volume is {new_volume}")
            else:
                print("Volume is max")
        else:
            print("No active Spotify device")

    def volume_down(self):
        current_playback = self.sp.current_playback()
        if current_playback and current_playback["device"]:
            current_volume = current_playback["device"]["volume_percent"]
            if current_volume > 0:    
                percent_down = 10 if current_volume >= 10 else current_volume 
                new_volume = current_volume - percent_down
                self.sp.volume(new_volume)
                print(f"Current Volume is {new_volume}")
            else:
                print("Volume is min")
        else:
            print("No active Spotify device")