// Firebase Configuration
// Replace the placeholder values below with your own Firebase project credentials.
// Find them in: Firebase Console → Project settings → Your apps → SDK setup and configuration
//
// For push notifications (FCM), also set your VAPID key below.
// Get it from: Firebase Console → Project settings → Cloud Messaging → Web Push certificates

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, GoogleAuthProvider,
         signInWithEmailAndPassword, createUserWithEmailAndPassword,
         signOut as firebaseSignOut }
  from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, doc, getDoc, setDoc, updateDoc, onSnapshot, collection, query,
         orderBy, limit, where, getDocs, serverTimestamp }
  from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getMessaging, getToken, onMessage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

// ─── Firebase project credentials ─────────────────────────────────────────────
const firebaseConfig = {
  apiKey: "AIzaSyAO6FNdpr87WPGjXEdfEs5bjB_4T2ZpzZg",
  authDomain: "lvlbase.firebaseapp.com",
  projectId: "lvlbase",
  storageBucket: "lvlbase.firebasestorage.app",
  messagingSenderId: "493311771136",
  appId: "1:493311771136:web:35428db96267a1f55c4ee5",
  measurementId: "G-5GRYW6F3M8"
};

// Your VAPID (Web Push) public key — from Firebase Console → Cloud Messaging
export const FCM_VAPID_KEY = "YOUR_VAPID_KEY";

// Firebase is now live with real credentials.
export const FIREBASE_LIVE = true;

// ─── Initialise ───────────────────────────────────────────────────────────────
let app, auth, db, googleProvider, messaging, storage;

if (FIREBASE_LIVE) {
  app           = initializeApp(firebaseConfig);
  auth          = getAuth(app);
  db            = getFirestore(app);
  googleProvider = new GoogleAuthProvider();
  storage       = getStorage(app);
  try { messaging = getMessaging(app); } catch (_) { /* browser without push support */ }
}

// ─── Firestore helpers (no-ops in demo mode) ──────────────────────────────────

/** Save / merge a user profile document to Firestore. */
export async function syncProfileToFirestore(profile) {
  if (!FIREBASE_LIVE || !db) return;
  try {
    await setDoc(doc(db, 'users', profile.uid), { ...profile, updatedAt: serverTimestamp() }, { merge: true });
  } catch (e) { console.warn('Firestore write failed:', e.message); }
}

/** Read a user profile from Firestore; returns null on failure. */
export async function fetchProfileFromFirestore(uid) {
  if (!FIREBASE_LIVE || !db) return null;
  try {
    const snap = await getDoc(doc(db, 'users', uid));
    return snap.exists() ? snap.data() : null;
  } catch (e) { console.warn('Firestore read failed:', e.message); return null; }
}

/** Subscribe to live profile updates; returns an unsubscribe function. */
export function watchProfile(uid, callback) {
  if (!FIREBASE_LIVE || !db) return () => {};
  return onSnapshot(doc(db, 'users', uid), (snap) => {
    if (snap.exists()) callback(snap.data());
  });
}

/** Fetch top-N leaderboard entries in real-time. */
export function watchLeaderboard(n = 10, callback) {
  if (!FIREBASE_LIVE || !db) return () => {};
  const q = query(collection(db, 'users'), orderBy('totalXP', 'desc'), limit(n));
  return onSnapshot(q, (snap) => {
    callback(snap.docs.map(d => d.data()));
  });
}

/** Post a guild-war event to Firestore. */
export async function postGuildEvent(event) {
  if (!FIREBASE_LIVE || !db) return;
  try {
    await setDoc(doc(collection(db, 'guild_events')), { ...event, ts: serverTimestamp() });
  } catch (e) { console.warn('Guild event write failed:', e.message); }
}

// ─── FCM helpers ─────────────────────────────────────────────────────────────

/**
 * Request notification permission and return the FCM token.
 * Stores the token in localStorage for convenience.
 */
export async function requestNotificationPermission() {
  if (!FIREBASE_LIVE || !messaging) return null;
  try {
    const permission = await Notification.requestPermission();
    if (permission !== 'granted') return null;
    const token = await getToken(messaging, { vapidKey: FCM_VAPID_KEY });
    if (token) localStorage.setItem('lvlbase_fcm_token', token);
    return token;
  } catch (e) { console.warn('FCM token error:', e.message); return null; }
}

/**
 * Register a foreground message handler.
 * callback(payload) is called when a push arrives while the tab is open.
 */
export function onForegroundMessage(callback) {
  if (!FIREBASE_LIVE || !messaging) return () => {};
  return onMessage(messaging, callback);
}

export { app, auth, db, googleProvider, messaging, storage,
         doc, getDoc, setDoc, updateDoc, onSnapshot, collection, query, orderBy, limit, serverTimestamp,
         where, getDocs, signInWithEmailAndPassword, createUserWithEmailAndPassword, firebaseSignOut };
