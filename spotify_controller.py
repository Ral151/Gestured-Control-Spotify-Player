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
            scope="user-modify-playback-state user-read-playback-state user-read-currently-playing streaming user-read-email user-read-private user-library-read user-library-modify user-read-recently-played user-top-read",
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
    
    def current_track(self):
        playback = self.sp.current_playback()
        if not playback or not playback.get("item"):
            return {
                "is_playing": False,
                "track_name": None,
                "artist": None,
                "album_name": None,
                "album_image": None,
                "volume_percent": None
            }

        item = playback["item"]
        images = item["album"]["images"]
        volume = playback["device"]["volume_percent"]

        return {
            "is_playing": playback.get("is_playing", False),
            "track_name": item.get("name"),
            "artist": ", ".join(artist["name"] for artist in item.get("artists", [])),
            "album_name": item["album"].get("name"),
            "album_image": images[0]["url"] if images else None,
            "volume_percent": volume if volume else None,
        }
    
    def user_profile(self):
        profile = self.sp.current_user()
        user_recently_played = self.sp.current_user_recently_played(limit=4)
        user_top_artist = self.sp.current_user_top_artists(limit=3)

        played_items = user_recently_played.get("items", [])
        top_artist = user_top_artist.get("items", [])

        return {
            "user": profile,
            "recently_played": played_items,
            "top_artists": top_artist,
            "profile_image": profile.get("images", [])
        }