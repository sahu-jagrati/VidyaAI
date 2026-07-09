import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { createSubscription, verifySubscription } from "../services/subscriptionService";

const PLANS = [
  {
    id: "monthly",
    label: "Monthly",
    price: "₹99",
    per: "/month",
    description: "Billed monthly after 7-day free trial",
    features: [
      "All subjects: Quant, Reasoning, English, GK",
      "Unlimited practice questions",
      "Detailed analytics & progress tracking",
      "Daily challenges & leaderboard",
      "Ad-free experience",
    ],
    highlight: false,
  },
  {
    id: "yearly",
    label: "Yearly",
    price: "₹999",
    per: "/year",
    description: "Save ₹189 vs monthly  •  Billed after 7-day free trial",
    features: [
      "Everything in Monthly",
      "Priority support",
      "Early access to new topics",
      "Offline mode (coming soon)",
    ],
    highlight: true,
    badge: "Best Value",
  },
];

export default function Pricing() {
  const { isAuthenticated, user } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(null); // 'monthly' | 'yearly'
  const [error, setError] = useState("");

  const handleSelectPlan = async (planType) => {
    if (!isAuthenticated) {
      navigate("/login", { state: { from: "/pricing" } });
      return;
    }

    setError("");
    setLoading(planType);

    try {
      const res = await createSubscription(planType);
      const { razorpay_subscription_id, razorpay_key_id } = res.data;

      const options = {
        key: razorpay_key_id,
        subscription_id: razorpay_subscription_id,
        name: "VidyaAI",
        description: `${planType === "monthly" ? "Monthly" : "Yearly"} Premium — 7-day free trial`,
        image: "/logo.png",
        prefill: {
          name: user?.name || "",
          email: user?.email || "",
        },
        theme: { color: "#0d9488" },
        handler: async (response) => {
          try {
            await verifySubscription({
              razorpay_payment_id: response.razorpay_payment_id,
              razorpay_subscription_id: response.razorpay_subscription_id,
              razorpay_signature: response.razorpay_signature,
            });
            navigate("/subscription/success");
          } catch {
            navigate("/subscription/failed");
          }
        },
        modal: {
          ondismiss: () => {
            setLoading(null);
            navigate("/subscription/failed");
          },
        },
      };

      const rzp = new window.Razorpay(options);
      rzp.open();
    } catch (err) {
      setError(err?.response?.data?.detail || "Something went wrong. Please try again.");
    } finally {
      setLoading(null);
    }
  };

  return (
    <div className="min-h-screen bg-linear-to-b from-teal-50 to-white">
      {/* Nav */}
      <nav className="flex items-center justify-between px-6 py-4 max-w-5xl mx-auto">
        <button onClick={() => navigate("/")} className="text-teal-700 font-bold text-xl tracking-tight">
          VidyaAI
        </button>
        {isAuthenticated ? (
          <button
            onClick={() => navigate("/home")}
            className="text-sm text-teal-700 hover:underline"
          >
            Back to Home
          </button>
        ) : (
          <button
            onClick={() => navigate("/login")}
            className="text-sm bg-teal-700 text-white px-4 py-2 rounded-lg hover:bg-teal-800 transition"
          >
            Login
          </button>
        )}
      </nav>

      {/* Hero */}
      <div className="text-center py-12 px-4">
        <span className="inline-block bg-teal-100 text-teal-700 text-xs font-semibold px-3 py-1 rounded-full mb-4">
          7-Day Free Trial — No charge today
        </span>
        <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-3">
          Unlock Your Full Potential
        </h1>
        <p className="text-gray-500 max-w-md mx-auto">
          Start your free trial today. Your mandate is registered but you won't be charged until
          the trial ends. Cancel anytime.
        </p>
      </div>

      {/* Plans */}
      <div className="flex flex-col md:flex-row gap-6 max-w-3xl mx-auto px-4 pb-16 justify-center items-stretch">
        {PLANS.map((plan) => (
          <div
            key={plan.id}
            className={`relative flex flex-col rounded-2xl border-2 p-6 shadow-sm flex-1 transition ${
              plan.highlight
                ? "border-teal-600 shadow-teal-100 shadow-lg"
                : "border-gray-200 bg-white"
            }`}
          >
            {plan.badge && (
              <span className="absolute -top-3 left-1/2 -translate-x-1/2 bg-teal-600 text-white text-xs font-bold px-3 py-1 rounded-full">
                {plan.badge}
              </span>
            )}

            <div className="mb-4">
              <p className="text-sm font-semibold text-teal-700 uppercase tracking-wide">{plan.label}</p>
              <div className="flex items-end gap-1 mt-1">
                <span className="text-4xl font-bold text-gray-900">{plan.price}</span>
                <span className="text-gray-400 text-sm pb-1">{plan.per}</span>
              </div>
              <p className="text-xs text-gray-400 mt-1">{plan.description}</p>
            </div>

            <ul className="space-y-2 mb-6 flex-1">
              {plan.features.map((f) => (
                <li key={f} className="flex items-start gap-2 text-sm text-gray-600">
                  <span className="text-teal-500 font-bold mt-0.5">&#10003;</span>
                  {f}
                </li>
              ))}
            </ul>

            <button
              onClick={() => handleSelectPlan(plan.id)}
              disabled={!!loading}
              className={`w-full py-3 rounded-xl font-semibold text-sm transition ${
                plan.highlight
                  ? "bg-teal-700 text-white hover:bg-teal-800"
                  : "bg-gray-900 text-white hover:bg-gray-700"
              } disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              {loading === plan.id ? "Opening checkout..." : "Start Free Trial"}
            </button>
          </div>
        ))}
      </div>

      {error && (
        <p className="text-center text-red-500 text-sm pb-8">{error}</p>
      )}

      {/* Footer note */}
      <div className="text-center text-xs text-gray-400 pb-10">
        Payments secured by Razorpay &bull; UPI AutoPay &bull; Cards &bull; Net Banking
      </div>

    </div>
  );
}
