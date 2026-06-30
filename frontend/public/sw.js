self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(clients.claim()));

self.addEventListener('push', event => {
  const data = event.data?.json() || {};
  const title = data.title || 'VidyaAi';
  const body  = data.body  || 'Time to practice!';
  const url   = data.url   || '/home';

  event.waitUntil(
    self.registration.showNotification(title, {
      body,
      icon:             '/vite.svg',
      badge:            '/vite.svg',
      data:             { url },
      vibrate:          [200, 100, 200],
      requireInteraction: false,
    })
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then(list => {
      const url = event.notification.data.url;
      for (const client of list) {
        if (client.url.includes(url) && 'focus' in client) return client.focus();
      }
      return clients.openWindow(url);
    })
  );
});
