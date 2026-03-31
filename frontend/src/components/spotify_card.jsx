export default function SpotifyCard({ spotify }) {
  return (
    <section className="rounded-2xl row-span-2 col-span-2 border w-full border-white/10 bg-white/5 p-6 shadow-lg">
      <h2 className="mb-4 text-xl font-semibold">Now Playing</h2>

      {spotify ? (
        <div className="space-y-4">
          {spotify.album_image ? (
            <img
              src={spotify.album_image}
              alt={spotify.album_name || "Album cover"}
              className="h-full w-full rounded-xl object-cover"
            />
          ) : (
            <div className="flex h-64 w-full items-center justify-center rounded-xl bg-zinc-900 text-zinc-500">
              No Album Art
            </div>
          )}

          <div>
            <p className="text-2xl font-bold">{spotify.track_name || "No track"}</p>
            <p className="text-lg text-zinc-400">{spotify.artist || "Unknown artist"}</p>
            <p className="mt-1 text-lg text-zinc-500">{spotify.album_name || ""}</p>
          </div>

          <div className="rounded-lg bg-zinc-900 px-3 flex justify-between py-2 text-sm">
            {spotify.is_playing ? "Playing" : "Paused"}
            {spotify.volume_percent !== null && (
              <span className="ml-4 text-zinc-400">Volume: {spotify.volume_percent}%</span>
            )}
          </div>
        </div>
      ) : (
        <div className="rounded-xl bg-zinc-900 p-4 text-zinc-400">
          Spotify data unavailable
        </div>
      )}
    </section>
  );
}