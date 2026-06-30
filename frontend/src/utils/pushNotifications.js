import api from './api';

function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
  const raw = window.atob(base64);
  return Uint8Array.from([...raw].map(c => c.charCodeAt(0)));
}

export async function registerSW() {
  if (!('serviceWorker' in navigator)) return null;
  try {
    const reg = await navigator.serviceWorker.register('/sw.js');
    await navigator.serviceWorker.ready;
    return reg;
  } catch (e) {
    console.error('[push] SW registration failed:', e);
    return null;
  }
}

export async function requestPermission() {
  if (!('Notification' in window)) return 'unsupported';
  if (Notification.permission === 'granted') return 'granted';
  const result = await Notification.requestPermission();
  return result;
}

export async function subscribeToPush(reminderTime = null) {
  const reg = await registerSW();
  if (!reg) throw new Error('Service Worker not available');

  const perm = await requestPermission();
  if (perm !== 'granted') throw new Error('Notification permission denied');

  // Get VAPID public key from backend
  const { data } = await api.get('/notifications/vapid-key');
  const applicationServerKey = urlBase64ToUint8Array(data.public_key);

  const subscription = await reg.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey,
  });

  const { endpoint, keys } = subscription.toJSON();

  await api.post('/notifications/subscribe', {
    endpoint,
    p256dh:        keys.p256dh,
    auth:          keys.auth,
    reminder_time: reminderTime,
  });

  return subscription;
}

export async function unsubscribeFromPush() {
  const reg = await navigator.serviceWorker?.getRegistration('/sw.js');
  if (!reg) return;
  const sub = await reg.pushManager.getSubscription();
  if (!sub) return;
  const endpoint = sub.endpoint;
  await sub.unsubscribe();
  await api.delete(`/notifications/unsubscribe?endpoint=${encodeURIComponent(endpoint)}`);
}

export async function setReminder(reminderTime) {
  await api.put('/notifications/reminder', { reminder_time: reminderTime });
}

export async function getMySubscription() {
  try {
    const { data } = await api.get('/notifications/my-subscription');
    return data;
  } catch {
    return { subscribed: false, reminder_time: null };
  }
}
