export default function UserProfile({ user }) {
  const profile = user?.user || {};
  const profileImage = user?.profile_image?.[0]?.url || null;
  const recentlyPlayed = user?.recently_played || [];
  const topArtists = user?.top_artists || [];

  return (
    <div className="bg-gray-800 p-4 rounded-lg">
      <div className="flex items-center space-x-4">
        {profileImage ? (
          <img
            src={profileImage}
            alt="Profile"
            className="w-16 h-16 rounded-full object-cover"
          />
        ) : (
          <div className="w-16 h-16 rounded-full bg-gray-700" />
        )}
        <div>
          <h2 className="text-xl font-bold">{profile.display_name || "Spotify User"}</h2>
        </div>
      </div>

      <div className="mt-4">
        <h3 className="text-lg font-semibold">Recently Played</h3>
        <ul className="space-y-2">
          {recentlyPlayed.map((item) => (
            <li key={item?.track?.id || item?.played_at} className="text-gray-300">
              {item?.track?.name || "Unknown track"} - {item?.track?.artists?.[0]?.name || "Unknown artist"}
            </li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h3 className="text-lg font-semibold">Top Artists</h3>
        <ul className="space-y-2">
          {topArtists.map((artist) => (
            <li key={artist?.id || artist?.name} className="text-gray-300">
              {artist?.name || "Unknown artist"}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}