import { useNavigate } from "react-router-dom";

export default function SubscriptionFailed() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-linear-to-b from-red-50 to-white px-4 text-center">
      <div className="w-20 h-20 rounded-full bg-red-100 flex items-center justify-center mb-6">
        <svg className="w-10 h-10 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6 18L18 6M6 6l12 12" />
        </svg>
      </div>

      <h1 className="text-2xl font-bold text-gray-900 mb-2">Payment not completed</h1>
      <p className="text-gray-500 mb-8 max-w-sm">
        Your subscription was not activated. No amount has been deducted. You can try again anytime.
      </p>

      <div className="flex flex-col sm:flex-row gap-3">
        <button
          onClick={() => navigate("/pricing")}
          className="bg-teal-700 text-white px-6 py-3 rounded-xl font-semibold hover:bg-teal-800 transition"
        >
          Try Again
        </button>
        <button
          onClick={() => navigate("/home")}
          className="border border-gray-200 text-gray-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-50 transition"
        >
          Back to Home
        </button>
      </div>
    </div>
  );
}
