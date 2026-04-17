// ===== AUTH MODULE =====
// Supports both Firebase Auth and localStorage demo mode.
// When FIREBASE_LIVE (firebase-config.js) is true, profiles are synced to Firestore.

import { syncProfileToFirestore, fetchProfileFromFirestore, FIREBASE_LIVE } from './firebase-config.js';

export const DEMO_MODE = !FIREBASE_LIVE;

// Default new user profile
function createDefaultProfile(uid, email, displayName) {
  return {
    uid, email, displayName: displayName || email.split('@')[0],
    grade: '10', guild: null,
    totalXP: 20, streak: 1,
    lastLogin: new Date().toISOString(),
    quizzesCompleted: 0, battlesWon: 0, battlesPlayed: 0,
    goalsCompleted: 0, perfectScores: 0, lateNightStudy: 0, earlyMorningStudy: 0,
    achievements: [], subjectProgress: { math: 0, science: 0, english: 0 },
    joinedAt: new Date().toISOString(), role: 'student'
  };
}

// Sign in with email/password
export async function signInWithEmail(email, password) {
  if (!email || !password) throw new Error('Email and password required');
  const key = 'lvlbase_user_' + btoa(email).replace(/=/g,'');
  let profile = JSON.parse(localStorage.getItem(key) || 'null');
  if (!profile) {
    // Auto-create on first login (demo)
    const uid = 'demo_' + Date.now();
    profile = createDefaultProfile(uid, email, null);
    localStorage.setItem(key, JSON.stringify(profile));
  }
  profile.lastLogin = new Date().toISOString();
  profile.totalXP = (profile.totalXP || 0) + 20;
  localStorage.setItem(key, JSON.stringify(profile));
  localStorage.setItem('lvlbase_user_profile', JSON.stringify(profile));
  localStorage.setItem('lvlbase_current_user', JSON.stringify({ uid: profile.uid, email, displayName: profile.displayName }));
  return profile;
}

// Sign up with email/password
export async function signUpWithEmail(email, password, displayName) {
  if (!email || !password) throw new Error('Email and password required');
  if (password.length < 6) throw new Error('Password must be at least 6 characters');
  const uid = 'user_' + Date.now();
  const profile = createDefaultProfile(uid, email, displayName);
  const key = 'lvlbase_user_' + btoa(email).replace(/=/g,'');
  localStorage.setItem(key, JSON.stringify(profile));
  localStorage.setItem('lvlbase_user_profile', JSON.stringify(profile));
  localStorage.setItem('lvlbase_current_user', JSON.stringify({ uid, email, displayName: profile.displayName }));
  return profile;
}

// Sign in with Google (demo simulation)
export async function signInWithGoogle() {
  const names = ['Arjun Kumar', 'Priya Sharma', 'Rohan Patel', 'Sneha Iyer', 'Dev Kapoor'];
  const displayName = names[Math.floor(Math.random() * names.length)];
  const email = displayName.toLowerCase().replace(' ', '.') + '@gmail.com';
  const uid = 'google_' + Date.now();
  const profile = createDefaultProfile(uid, email, displayName);
  localStorage.setItem('lvlbase_user_profile', JSON.stringify(profile));
  localStorage.setItem('lvlbase_current_user', JSON.stringify({ uid, email, displayName }));
  return profile;
}

// Sign out
export function signOut() {
  localStorage.removeItem('lvlbase_current_user');
  window.location.href = 'login.html';
}

// Get current user
export function getCurrentUser() {
  return JSON.parse(localStorage.getItem('lvlbase_current_user') || 'null');
}

// Get user profile
export function getUserProfile() {
  return JSON.parse(localStorage.getItem('lvlbase_user_profile') || 'null');
}

// Save user profile (localStorage + optional Firestore sync)
export function saveUserProfile(profile) {
  localStorage.setItem('lvlbase_user_profile', JSON.stringify(profile));
  syncProfileToFirestore(profile).catch(() => {});
}

// Check if authenticated (redirect if not)
export function checkAuth(redirectUrl = 'login.html') {
  const user = getCurrentUser();
  if (!user) { window.location.href = redirectUrl; return null; }
  return user;
}

// Auth state change callback
export function onAuthStateChanged(callback) {
  const user = getCurrentUser();
  callback(user);
}

export default { signInWithEmail, signUpWithEmail, signInWithGoogle, signOut, getCurrentUser, getUserProfile, saveUserProfile, checkAuth, onAuthStateChanged };
