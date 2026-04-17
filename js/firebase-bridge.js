// firebase-bridge.js
// Exposes Firebase auth + Firestore/RTDB helpers to window.fb so non-module
// inline scripts in HTML pages can use them without ES module syntax.

import {
  auth, db, rtdb, googleProvider, FIREBASE_LIVE,
  signInWithEmailAndPassword, createUserWithEmailAndPassword, firebaseSignOut, signInWithPopup,
  doc, setDoc, getDoc, collection, query, where, getDocs, serverTimestamp,
  dbRef, dbSet, dbGet
} from './firebase-config.js';

window.fb = {
  live: FIREBASE_LIVE,

  /** Sign in with email + password via Firebase Auth. Returns the user credential. */
  async signIn(email, password) {
    if (!FIREBASE_LIVE || !auth) return null;
    return await signInWithEmailAndPassword(auth, email, password);
  },

  /** Create a Firebase Auth account. Returns the user credential. */
  async signUp(email, password) {
    if (!FIREBASE_LIVE || !auth) return null;
    return await createUserWithEmailAndPassword(auth, email, password);
  },

  /** Sign out the current Firebase Auth user. */
  async signOut() {
    if (!FIREBASE_LIVE || !auth) return;
    await firebaseSignOut(auth);
  },

  /** Save a school document to RTDB (primary) and Firestore (secondary). */
  async saveSchool(school) {
    if (!FIREBASE_LIVE) return;
    // Primary: Realtime Database — permissive default rules allow writes
    if (rtdb) {
      await dbSet(dbRef(rtdb, 'schools/' + school.id), { ...school, updatedAt: Date.now() });
    }
    // Secondary: Firestore (best-effort; silently ignored if rules block it)
    if (db) {
      try {
        await setDoc(doc(db, 'schools', school.id), { ...school, updatedAt: serverTimestamp() }, { merge: true });
      } catch (e) { console.warn('Firestore saveSchool skipped:', e.message); }
    }
  },

  /** Find a school by adminEmail. Checks RTDB first, then Firestore. Returns school data or null. */
  async getSchoolByAdminEmail(email) {
    if (!FIREBASE_LIVE) return null;
    // Try Firestore
    if (db) {
      try {
        const q = query(collection(db, 'schools'), where('adminEmail', '==', email.toLowerCase()));
        const snap = await getDocs(q);
        if (!snap.empty) return snap.docs[0].data();
      } catch (e) { console.warn('Firestore getSchoolByAdminEmail failed:', e.message); }
    }
    return null;
  },

  /** Save a user profile document to RTDB (primary) and Firestore (secondary). */
  async saveUser(uid, userData) {
    if (!FIREBASE_LIVE) return;
    // Primary: Realtime Database
    if (rtdb) {
      await dbSet(dbRef(rtdb, 'users/' + uid), { ...userData, updatedAt: Date.now() });
    }
    // Secondary: Firestore (best-effort)
    if (db) {
      try {
        await setDoc(doc(db, 'users', uid), { ...userData, updatedAt: serverTimestamp() }, { merge: true });
      } catch (e) { console.warn('Firestore saveUser skipped:', e.message); }
    }
  },

  /** Get a user profile. Checks Firestore first, falls back to RTDB. Returns data or null. */
  async getUser(uid) {
    if (!FIREBASE_LIVE) return null;
    if (db) {
      try {
        const snap = await getDoc(doc(db, 'users', uid));
        if (snap.exists()) return snap.data();
      } catch (e) { console.warn('Firestore getUser failed:', e.message); }
    }
    if (rtdb) {
      try {
        const snap = await dbGet(dbRef(rtdb, 'users/' + uid));
        if (snap.exists()) return snap.val();
      } catch (e) { console.warn('RTDB getUser failed:', e.message); }
    }
    return null;
  },

  /** Find a user by email in Firestore. Returns user data or null. */
  async getUserByEmail(email) {
    if (!FIREBASE_LIVE || !db) return null;
    try {
      const q = query(collection(db, 'users'), where('email', '==', email.toLowerCase()));
      const snap = await getDocs(q);
      if (snap.empty) return null;
      return snap.docs[0].data();
    } catch (e) { console.warn('Firestore getUserByEmail failed:', e.message); return null; }
  },

  /** Sign in with Google popup. Returns the user credential. */
  async signInWithGoogle() {
    if (!FIREBASE_LIVE || !auth || !googleProvider) return null;
    return await signInWithPopup(auth, googleProvider);
  },

  /** Fetch all verified schools from Firestore. Returns array or null. */
  async getSchools() {
    if (!FIREBASE_LIVE || !db) return null;
    try {
      const q = query(collection(db, 'schools'), where('status', '==', 'verified'));
      const snap = await getDocs(q);
      return snap.docs.map(d => d.data());
    } catch (e) { console.warn('Firestore getSchools failed:', e.message); return null; }
  }
};

// Notify inline scripts that the Firebase bridge is ready.
window.dispatchEvent(new CustomEvent('fb:ready'));
