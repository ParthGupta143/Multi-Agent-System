import { useState } from "react";
import axios from "axios";

const API_URL = "https://multi-agent-system-production-245b.up.railway.app";

// Agent status component
const AgentCard = ({ icon, name, status }) => {
  const colors = {
    idle: "bg-gray-800 border-gray-700 text-gray-400",
    working: "bg-yellow-900 border-yellow-600 text-yellow-300",
    done: "bg-green-900 border-green-600 text-green-300",
  };
  return (
    <div className={`border rounded-lg p-3 flex items-center gap-3 transition-all duration-500 ${colors[status]}`}>
      <span className="text-2xl">{icon}</span>
      <div>
        <p className="font-semibold text-sm">{name}</p>
        <p className="text-xs capitalize">{status === "working" ? "⏳ Working..." : status === "done" ? "✅ Complete" : "⏸ Idle"}</p>
      </div>
    </div>
  );
};

export default function App() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [timeTaken, setTimeTaken] = useState(null);
  const [fromMemory, setFromMemory] = useState(false);
  const [agentStatus, setAgentStatus] = useState({
    researcher: "idle",
    writer: "idle",
    reviewer: "idle",
  });

  const simulateAgentProgress = () => {
    // Simulate agent progress visually
    setTimeout(() => setAgentStatus(s => ({ ...s, researcher: "working" })), 500);
    setTimeout(() => setAgentStatus(s => ({ ...s, researcher: "done", writer: "working" })), 4000);
    setTimeout(() => setAgentStatus(s => ({ ...s, writer: "done", reviewer: "working" })), 8000);
    setTimeout(() => setAgentStatus(s => ({ ...s, reviewer: "done" })), 12000);
  };

  const runPipeline = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setResult(null);
    setError(null);
    setFromMemory(false);
    setAgentStatus({ researcher: "idle", writer: "idle", reviewer: "idle" });

    simulateAgentProgress();

    try {
      const start = Date.now();
      const response = await axios.post(`${API_URL}/run-pipeline`, { query });
      const elapsed = ((Date.now() - start) / 1000).toFixed(2);

      setResult(response.data.output);
      setTimeTaken(elapsed);

      // If very fast → came from memory
      if (elapsed < 3) setFromMemory(true);

      setAgentStatus({ researcher: "done", writer: "done", reviewer: "done" });
    } catch (err) {
      setError("Server is waking up... Please wait few seconds and try again! ⏳");
      setAgentStatus({ researcher: "idle", writer: "idle", reviewer: "idle" });
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !loading) runPipeline();
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <div className="max-w-4xl mx-auto">

        {/* Header */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold text-white mb-2">
            🤖 Multi-Agent System
          </h1>
          <p className="text-gray-400 text-lg">
            AI-powered pipeline — Research → Write → Review
          </p>
          <div className="flex justify-center gap-2 mt-3">
            <span className="bg-green-900 text-green-300 text-xs px-3 py-1 rounded-full">
              ● API Connected
            </span>
            <span className="bg-blue-900 text-blue-300 text-xs px-3 py-1 rounded-full">
              ChromaDB Memory Active
            </span>
          </div>
        </div>

        {/* Input Section */}
        <div className="bg-gray-900 rounded-2xl p-6 mb-6 border border-gray-800">
          <label className="block text-gray-400 text-sm mb-2">
            Enter your research query:
          </label>
          <textarea
            className="w-full bg-gray-800 text-white rounded-xl p-4 text-sm resize-none border border-gray-700 focus:outline-none focus:border-blue-500 transition-colors"
            rows={3}
            placeholder="e.g. Explain Artificial Intelligence and its real world applications..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={loading}
          />
          <div className="flex justify-between items-center mt-3">
            <span className="text-gray-600 text-xs">{query.length}/500 characters</span>
            <button
              onClick={runPipeline}
              disabled={loading || !query.trim()}
              className="bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:text-gray-500 text-white font-semibold px-8 py-3 rounded-xl transition-all duration-200"
            >
              {loading ? "⏳ Running..." : "🚀 Run Pipeline"}
            </button>
          </div>
        </div>

        {/* Agent Status */}
        <div className="grid grid-cols-3 gap-4 mb-6">
          <AgentCard icon="🔍" name="Research Agent" status={agentStatus.researcher} />
          <AgentCard icon="✍️" name="Writer Agent" status={agentStatus.writer} />
          <AgentCard icon="🔎" name="Reviewer Agent" status={agentStatus.reviewer} />
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-900 border border-red-700 text-red-300 rounded-xl p-4 mb-6">
            ❌ {error}
          </div>
        )}

        {/* Result */}
        {result && (
          <div className="bg-gray-900 rounded-2xl p-6 border border-gray-800">

            {/* Meta info */}
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-lg font-bold text-white">📊 Final Report</h2>
              <div className="flex gap-2">
                {fromMemory && (
                  <span className="bg-purple-900 text-purple-300 text-xs px-3 py-1 rounded-full">
                    ⚡ From Memory
                  </span>
                )}
                <span className="bg-gray-800 text-gray-400 text-xs px-3 py-1 rounded-full">
                  ⏱ {timeTaken}s
                </span>
              </div>
            </div>

            {/* Report content */}
            <div className="bg-gray-800 rounded-xl p-5 text-sm text-gray-300 leading-relaxed whitespace-pre-wrap max-h-[500px] overflow-y-auto">
              {result}
            </div>

            {/* Copy button */}
            <button
              onClick={() => navigator.clipboard.writeText(result)}
              className="mt-4 text-xs text-gray-500 hover:text-gray-300 transition-colors"
            >
              📋 Copy Report
            </button>
          </div>
        )}

        {/* Footer */}
        <p className="text-center text-gray-700 text-xs mt-8">
          Built with LangChain • Groq • ChromaDB • FastAPI • React
        </p>

      </div>
    </div>
  );
}