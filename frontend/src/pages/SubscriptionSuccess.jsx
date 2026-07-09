import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function SubscriptionSuccess() {
  const navigate = useNavigate();
  const { refreshUser } = useAuth();

  useEffect(() => {
    // Refresh user so is_premium is reflected immediately
    if (refreshUser) refreshUser();
  }, [refreshUser]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-linear-to-b from-teal-50 to-white px-4 text-center">
      <div className="w-20 h-20 rounded-full bg-teal-100 flex items-center justify-center mb-6">
        <svg className="w-10 h-10 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" />
        </svg>
      </div>

      <h1 className="text-2xl font-bold text-gray-900 mb-2">You're all set!</h1>
      <p className="text-gray-500 mb-1 max-w-sm">
        Your 7-day free trial has started. You won't be charged until the trial ends.
      </p>
      <p className="text-sm text-gray-400 mb-8">
        Your mandate has been registered — sit back and enjoy premium access.
      </p>

      <div className="flex flex-col sm:flex-row gap-3">
        <button
          onClick={() => navigate("/home")}
          className="bg-teal-700 text-white px-6 py-3 rounded-xl font-semibold hover:bg-teal-800 transition"
        >
          Start Learning
        </button>
        <button
          onClick={() => navigate("/subscription/manage")}
          className="border border-gray-200 text-gray-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-50 transition"
        >
          Manage Subscription
        </button>
      </div>
    </div>
  );
}
