import { Music2, Cpu } from "lucide-react";

export default function Navbar({ backendStatus }) {
  return (
    <header className= "border-b border-white/10 bg-white/5 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6">
        <div>
          <h1 className="text-2xl font-bold">Gesture Spotify</h1>
        </div>

        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 rounded-full border border-white/10 bg-zinc-900 px-3 text-sm">
            <Cpu size={16} />
            <span>{backendStatus ? "Backend Online" : "Backend Offline"}</span>
          </div>
          <div className="flex items-center gap-2 rounded-full border border-white/10 bg-zinc-900 px-3 text-sm">
            <Music2 size={16} />
            <span>Spotify Control</span>
          </div>
        </div>
      </div>
    </header>
  );
}