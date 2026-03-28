export default function GestureCard({ gesture }) {
  return (
    <section className="rounded-2xl border border-white/10 bg-white/5 p-6 shadow-lg">
      <h2 className="mb-4 text-xl font-semibold">Gesture Status</h2>

      <div className="space-y-4">
        <div>
          <p className="text-sm text-zinc-400">Current</p>
          <p className="text-2xl font-bold">{gesture?.current || "None"}</p>
        </div>

        <div>
          <p className="text-sm text-zinc-400">Stable</p>
          <p className="text-2xl font-bold text-cyan-300">{gesture?.stable || "None"}</p>
        </div>

        <div>
          <p className="text-sm text-zinc-400">Last Trigger</p>
          <p className="text-2xl font-bold text-emerald-300">{gesture?.last_trigger || "None"}</p>
        </div>
      </div>
    </section>
  );
}