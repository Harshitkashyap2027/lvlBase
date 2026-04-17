// firebase-bridge.js
// Exposes Firebase auth + Firestore helpers to window.fb so non-module
// inline scripts in HTML pages can use them without ES module syntax.

import {
  auth, db, FIREBASE_LIVE,
  signInWithEmailAndPassword, createUserWithEmailAndPassword, firebaseSignOut,
  doc, setDoc, getDoc, collection, query, where, getDocs, serverTimestamp
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

  /** Save (merge) a school document to Firestore. */
  async saveSchool(school) {
    if (!FIREBASE_LIVE || !db) return;
    await setDoc(doc(db, 'schools', school.id), { ...school, updatedAt: serverTimestamp() }, { merge: true });
  },

  /** Find a school by adminEmail in Firestore. Returns school data or null. */
  async getSchoolByAdminEmail(email) {
    if (!FIREBASE_LIVE || !db) return null;
    try {
      const q = query(collection(db, 'schools'), where('adminEmail', '==', email.toLowerCase()));
      const snap = await getDocs(q);
      if (snap.empty) return null;
      return snap.docs[0].data();
    } catch (e) { console.warn('Firestore getSchoolByAdminEmail failed:', e.message); return null; }
  },

  /** Save (merge) a user profile document to Firestore under users/{uid}. */
  async saveUser(uid, userData) {
    if (!FIREBASE_LIVE || !db) return;
    await setDoc(doc(db, 'users', uid), { ...userData, updatedAt: serverTimestamp() }, { merge: true });
  },

  /** Get a user profile from Firestore. Returns data or null. */
  async getUser(uid) {
    if (!FIREBASE_LIVE || !db) return null;
    try {
      const snap = await getDoc(doc(db, 'users', uid));
      return snap.exists() ? snap.data() : null;
    } catch (e) { console.warn('Firestore getUser failed:', e.message); return null; }
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
  }
};

// Notify inline scripts that the Firebase bridge is ready.
window.dispatchEvent(new CustomEvent('fb:ready'));
