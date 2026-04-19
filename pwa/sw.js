// ===== lvlBase Service Worker =====
const CACHE_NAME = 'lvlbase-v2';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/login.html',
  '/signup.html',
  '/dashboard.html',
  '/teacher-dashboard.html',
  '/parent-dashboard.html',
  '/school-dashboard.html',
  '/school-signup.html',
  '/quiz.html',
  '/battles.html',
  '/ai-assistant.html',
  '/homework-scanner.html',
  '/science-lab.html',
  '/competition.html',
  '/certificate.html',
  '/guild-wars.html',
  '/admin/index.html',
  '/css/main.css',
  '/css/dashboard.css',
  '/css/quiz.css',
  '/js/popup.js',
  '/manifest.json'
];

// Install: cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // addAll with individual error handling so one missing asset doesn't fail everything
      return Promise.allSettled(
        STATIC_ASSETS.map(url =>
          cache.add(new Request(url, { cache: 'reload' })).catch(() => {})
        )
      );
    }).catch((err) => {
      console.warn('SW install cache error (non-fatal):', err);
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter(n => n !== CACHE_NAME).map(n => caches.delete(n)))
    )
  );
  self.clients.claim();
});

// Fetch: network-first strategy, fallback to cache
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response && response.status === 200) {
          const cloned = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, cloned));
        }
        return response;
      })
      .catch(() => {
        return caches.match(event.request).then((cached) => {
          if (cached) return cached;
          if (event.request.mode === 'navigate') {
            return caches.match('/index.html');
          }
        });
      })
  );
});

// ─── Push Notifications (Firebase Cloud Messaging) ───────────────────────────
self.addEventListener('push', (event) => {
  let data = { title: 'lvlBase ⚡', body: 'You have a new notification!', icon: '/icons/icon-192.png' };
  try {
    const payload = event.data ? event.data.json() : {};
    const n = payload.notification || payload;
    data = {
      title: n.title || data.title,
      body:  n.body  || data.body,
      icon:  n.icon  || data.icon,
      badge: '/icons/icon-192.png',
      data:  n.data  || {}
    };
  } catch (_) {}

  event.waitUntil(
    self.registration.showNotification(data.title, {
      body:  data.body,
      icon:  data.icon,
      badge: data.badge,
      data:  data.data,
      vibrate: [200, 100, 200]
    })
  );
});

// Handle notification click – open the relevant page
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const url = (event.notification.data && event.notification.data.url) || '/dashboard.html';
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((windowClients) => {
      for (const client of windowClients) {
        if (client.url.includes(self.location.origin) && 'focus' in client) {
          client.focus();
          client.navigate(url);
          return;
        }
      }
      if (clients.openWindow) return clients.openWindow(url);
    })
  );
});
