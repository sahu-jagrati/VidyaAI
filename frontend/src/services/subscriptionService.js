import api from "../utils/api";

export const createSubscription = (planType) =>
  api.post("/subscriptions/create", { plan_type: planType });

export const verifySubscription = (payload) =>
  api.post("/subscriptions/verify", payload);

export const getMySubscription = () => api.get("/subscriptions/me");

export const cancelSubscription = (cancelAtPeriodEnd = true) =>
  api.post("/subscriptions/cancel", { cancel_at_period_end: cancelAtPeriodEnd });

export const changePlan = (newPlanType) =>
  api.post("/subscriptions/change-plan", { new_plan_type: newPlanType });
