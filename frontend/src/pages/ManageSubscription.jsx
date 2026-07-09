import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  getMySubscription,
  cancelSubscription,
} from "../services/subscriptionService";

const STATUS_LABEL = {
  created: { text: "Pending activation", color: "text-yellow-600 bg-yellow-50" },
  authenticated: { text: "Trial active", color: "text-teal-700 bg-teal-50" },
  active: { text: "Active", color: "text-green-700 bg-green-50" },
  halted: { text: "Payment failed", color: "text-red-600 bg-red-50" },
  cancelled: { text: "Cancelled", color: "text-gray-500 bg-gray-100" },
  completed: { text: "Completed", color: "text-gray-500 bg-gray-100" },
  pending: { text: "Pending", color: "text-yellow-600 bg-yellow-50" },
};

function fmt(dateStr) {
  if (!dateStr) return "—";
  return new Date(dateStr).toLocaleDateString("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

export default function ManageSubscription() {
  const navigate = useNavigate();
  const { user } = useAuth();

  const [sub, setSub] = useState(null);
  const [loading, setLoading] = useState(true);
  const [cancelling, setCancelling] = useState(false);
  const [error, setError] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

  useEffect(() => {
    getMySubscription()
      .then((r) => setSub(r.data))
      .catch(() => setSub(null))
      .finally(() => setLoading(false));
  }, []);

  const handleCancel = async (immediate) => {
    if (!window.confirm(immediate ? "Cancel subscription immediately?" : "Cancel at end of billing period?"))
      return;

    setCancelling(true);
    setError("");
    try {
      const r = await cancelSubscription(!immediate);
      setSuccessMsg(r.data.message);
      setSub((prev) => ({ ...prev, status: immediate ? "cancelled" : prev.status, cancel_at_period_end: !immediate }));
    } catch (e) {
      setError(e?.response?.data?.detail || "Failed to cancel subscription.");
    } finally {
      setCancelling(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-teal-600 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const statusInfo = sub ? (STATUS_LABEL[sub.status] || { text: sub.status, color: "text-gray-500 bg-gray-100" }) : null;

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white border-b px-6 py-4">
        <div className="max-w-2xl mx-auto flex items-center justify-between">
          <button onClick={() => navigate(-1)} className="text-gray-500 hover:text-gray-800 text-sm">
            &larr; Back
          </button>
          <span className="font-semibold text-gray-800">Manage Subscription</span>
          <span />
        </div>
      </nav>

      <div className="max-w-2xl mx-auto px-4 py-8">
        {successMsg && (
          <div className="bg-green-50 border border-green-200 text-green-700 rounded-xl px-4 py-3 mb-6 text-sm">
            {successMsg}
          </div>
        )}
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-600 rounded-xl px-4 py-3 mb-6 text-sm">
            {error}
          </div>
        )}

        {!sub ? (
          <div className="bg-white rounded-2xl border border-gray-200 p-8 text-center">
            <p className="text-gray-500 mb-4">You don't have an active subscription.</p>
            <button
              onClick={() => navigate("/pricing")}
              className="bg-teal-700 text-white px-6 py-3 rounded-xl font-semibold hover:bg-teal-800 transition"
            >
              View Plans
            </button>
          </div>
        ) : (
          <div className="bg-white rounded-2xl border border-gray-200 divide-y divide-gray-100">
            {/* Header */}
            <div className="p-6 flex items-center justify-between">
              <div>
                <p className="font-semibold text-gray-900 text-lg capitalize">
                  {sub.plan_type} Plan
                </p>
                <p className="text-gray-400 text-sm">
                  {sub.plan_type === "monthly" ? "₹99/month" : "₹999/year"}
                </p>
              </div>
              <span className={`text-xs font-semibold px-3 py-1 rounded-full ${statusInfo.color}`}>
                {statusInfo.text}
              </span>
            </div>

            {/* Details */}
            <div className="p-6 grid grid-cols-2 gap-4">
              <div>
                <p className="text-xs text-gray-400 uppercase tracking-wide">Trial Start</p>
                <p className="text-gray-800 text-sm font-medium mt-1">{fmt(sub.trial_start_date)}</p>
              </div>
              <div>
                <p className="text-xs text-gray-400 uppercase tracking-wide">Trial End</p>
                <p className="text-gray-800 text-sm font-medium mt-1">{fmt(sub.trial_end_date)}</p>
              </div>
              <div>
                <p className="text-xs text-gray-400 uppercase tracking-wide">Next Billing</p>
                <p className="text-gray-800 text-sm font-medium mt-1">{fmt(sub.next_billing_date)}</p>
              </div>
              <div>
                <p className="text-xs text-gray-400 uppercase tracking-wide">AutoPay</p>
                <p className="text-gray-800 text-sm font-medium mt-1">
                  {sub.autopay_enabled ? "Enabled" : "Not yet active"}
                </p>
              </div>
              {sub.cancel_at_period_end && (
                <div className="col-span-2">
                  <p className="text-xs text-orange-500 font-medium">
                    Cancellation scheduled at end of billing period
                  </p>
                </div>
              )}
            </div>

            {/* Actions */}
            {["authenticated", "active", "created"].includes(sub.status) && !sub.cancel_at_period_end && (
              <div className="p-6 flex flex-col sm:flex-row gap-3">
                <button
                  onClick={() => navigate("/pricing")}
                  className="flex-1 border border-teal-600 text-teal-700 py-2.5 rounded-xl text-sm font-semibold hover:bg-teal-50 transition"
                >
                  Change Plan
                </button>
                <button
                  onClick={() => handleCancel(false)}
                  disabled={cancelling}
                  className="flex-1 border border-gray-200 text-gray-600 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 transition disabled:opacity-50"
                >
                  Cancel at Period End
                </button>
                <button
                  onClick={() => handleCancel(true)}
                  disabled={cancelling}
                  className="flex-1 border border-red-200 text-red-600 py-2.5 rounded-xl text-sm font-semibold hover:bg-red-50 transition disabled:opacity-50"
                >
                  Cancel Immediately
                </button>
              </div>
            )}
          </div>
        )}

        <p className="text-center text-xs text-gray-400 mt-8">
          Questions? Contact us at support@vidyaai.in
        </p>
      </div>
    </div>
  );
}
