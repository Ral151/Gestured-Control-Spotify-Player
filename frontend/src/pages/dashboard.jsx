import { useEffect, useState } from "react";
import { fetchGesture, fetchHealth, fetchSpotifyCurrent } from "../api/yolo_predict";
import Navbar from "../components/navbar";
import GestureCard from "../components/gesture_card";
import SpotifyCard from "../components/spotify_card";
import CommandGuide from "../components/command_guide";
import ActivityLog from "../components/activity_log";

export default function Dashboard() {
  const [health, setHealth] = useState(null);
  const [gesture, setGesture] = useState({
    current: null,
    stable: null,
    last_trigger: null,
  });
  const [spotify, setSpotify] = useState(null);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const load = async () => {
      try {
        const [healthData, gestureData, spotifyData] = await Promise.all([
          fetchHealth(),
          fetchGesture(),
          fetchSpotifyCurrent().catch(() => null),
        ]);

        setHealth(healthData);
        setGesture(gestureData);
        setSpotify(spotifyData);

        if (gestureData?.last_trigger) {
          setLogs((prev) => {
            const next = [
              {
                id: Date.now(),
                label: gestureData.last_trigger,
                time: new Date().toLocaleTimeString(),
              },
              ...prev,
            ];

            const deduped = [];
            const seen = new Set();

            for (const item of next) {
              const key = `${item.label}-${item.time}`;
              if (!seen.has(key)) {
                seen.add(key);
                deduped.push(item);
              }
            }

            return deduped.slice(0, 8);
          });
        }
      } catch (err) {
        console.error(err);
      }
    };

    load();
    const interval = setInterval(load, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-black text-white">
      <Navbar backendStatus={health?.status === "ok"} />

      <main className="mx-auto max-w-7xl px-6 py-6">
        <div className="grid gap-6 lg:grid-cols-3">
          <GestureCard gesture={gesture} />
          <SpotifyCard spotify={spotify} />
          <CommandGuide />
        </div>

        <div className="mt-6">
          <ActivityLog logs={logs} />
        </div>
      </main>
    </div>
  );
}