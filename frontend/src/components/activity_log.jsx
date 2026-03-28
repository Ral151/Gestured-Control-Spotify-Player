export default function ActivityLog({ logs }) {
  return (
    <section className="rounded-2xl border border-white/10 bg-white/5 p-6 shadow-lg">
      <h2 className="mb-4 text-xl font-semibold">Activity Log</h2>

      {logs.length === 0 ? (
        <p className="text-zinc-400">No actions yet.</p>
      ) : (
        <div className="space-y-2">
          {logs.map((log) => (
            <div
              key={log.id}
              className="flex items-center justify-between rounded-lg bg-zinc-900 px-4 py-3 text-sm"
            >
              <span>{log.label}</span>
              <span className="text-zinc-400">{log.time}</span>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}