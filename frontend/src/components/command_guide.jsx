const commands = [
  { gesture: "Palm", action: "Play/Pause" },
  { gesture: "Like", action: "Next Track" },
  { gesture: "Dislike", action: "Previous Track" },
  { gesture: "One", action: "Volume Up" },
  { gesture: "Two", action: "Volume Down" },
  { gesture: "Four", action: "Like Song" },
];

export default function CommandGuide() {
  return (
    <section className="rounded-2xl border col-span-1 border-white/10 bg-white/5 p-6 shadow-lg">
      <h2 className="mb-4 text-xl font-semibold">Gesture Guide</h2>

      <div className="space-y-3">
        {commands.map((item) => (
          <div
            key={item.gesture}
            className="flex items-center justify-between rounded-xl bg-zinc-900 px-4 py-3"
          >
            <span className="font-medium">{item.gesture}</span>
            <span className="text-sm text-zinc-400">{item.action}</span>
          </div>
        ))}
      </div>
    </section>
  );
}