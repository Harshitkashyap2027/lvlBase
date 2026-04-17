<div align="center">

# ⚡ lvlBase — Gamified Learning Platform

### School · Teacher · Parent · Student · Admin

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com)

**A fully-gamified school learning platform with XP, ranks, guilds, battles, quizzes, and a role-based portal.**

</div>

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Role-Based Portal](#role-based-portal)
3. [Quick Setup (No Server)](#quick-setup-no-server)
4. [Firebase Setup](#firebase-setup)
5. [Admin Access](#admin-access)
6. [School Registration & Verification](#school-registration--verification)
7. [File Structure](#file-structure)
8. [Features by Role](#features-by-role)
9. [Deployment](#deployment)

---

## Overview

lvlBase is a **Progressive Web App (PWA)** built with plain HTML, CSS and JavaScript using Firebase for authentication and data persistence. It runs entirely in the browser — no backend server required.

**Tech stack:**
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Database: Firebase Firestore (real-time) + localStorage (fallback/offline)
- Auth: Firebase Authentication
- Hosting: Any static host (GitHub Pages, Netlify, Vercel, Firebase Hosting)

---

## Role-Based Portal

The platform has **5 distinct roles**, each with their own dashboard:

| Role | Dashboard | Login via |
|------|-----------|-----------|
| 🎓 Student | `dashboard.html` | `login.html` or `portal-login.html` |
| 👨‍🏫 Teacher | `teacher-dashboard.html` | `portal-login.html` |
| 👨‍👩‍👧 Parent | `parent-dashboard.html` | `portal-login.html` |
| 🏫 School Admin | `school-dashboard.html` | `login.html` or `portal-login.html` |
| 👑 Super Admin | `admin/index.html` | Separate admin login |

**Important:** Each dashboard guards its own route — logging in as a school admin will always redirect to `school-dashboard.html`, never to the student dashboard.

---

## Quick Setup (No Server)

You can run lvlBase **without Firebase** for demo/testing using localStorage only.

### Step 1 — Clone or download

```bash
git clone https://github.com/Harshitkashyap2027/lvlBase.git
cd lvlBase
```

### Step 2 — Open in browser

Simply open `index.html` in any modern browser (Chrome, Firefox, Edge, Safari).

> **Tip:** Use VS Code's Live Server extension (`Alt+L, Alt+O`) or Python's built-in server:
> ```bash
> python3 -m http.server 8080
> # Then open http://localhost:8080
> ```

### Step 3 — Register & login

1. Open `index.html` → click **Get Started**
2. Register as a student at `signup.html`
3. Register your school at `school-signup.html`
4. Login at `login.html` (students) or `portal-login.html` (all roles)

---

## Firebase Setup

For real data persistence and multi-device support, connect Firebase.

### Step 1 — Create a Firebase project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **Add project** → name it `lvlBase`
3. Disable Google Analytics (optional) → **Create project**

### Step 2 — Enable Authentication

1. In Firebase Console → **Authentication** → **Get started**
2. Enable **Email/Password** provider

### Step 3 — Enable Firestore

1. **Firestore Database** → **Create database**
2. Start in **test mode** (you can add security rules later)
3. Choose a region close to your users (e.g. `asia-south1` for India)

### Step 4 — Register your web app

1. Project settings (gear icon) → **Your apps** → **Web** (`</>`)
2. Register app with nickname `lvlBase Web`
3. Copy the `firebaseConfig` object

### Step 5 — Update `firebase-config.js`

Edit `js/firebase-config.js` and replace with your config:

```javascript
// js/firebase-config.js
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.firebasestorage.app",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Push Notifications VAPID key (optional)
const VAPID_KEY = "YOUR_VAPID_KEY";
```

> **Never commit real API keys to a public repo.** For production, use environment variables or Firebase App Check.

### Step 6 — Firestore Security Rules (recommended)

In Firebase Console → Firestore → **Rules**, add:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can read/write their own profile
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    // School admins can read their school
    match /schools/{schoolId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && 
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'school_admin';
    }
    // Super admin has full access
    match /{document=**} {
      allow read, write: if request.auth != null && 
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }
  }
}
```

---

## Admin Access

The Super Admin panel is at `admin/index.html`.

### Default credentials

```
Email:    admin@lvlbase.com
Password: admin123
```

> **Change these immediately** after first login via **Platform Controls → Admin Credentials**.

### Admin features

- 📊 **Dashboard** — Real stats from localStorage/Firebase (no demo data)
- 📈 **Analytics** — Subject popularity, guild distribution, school performance
- 🏫 **School Management** — Verify/reject school registrations
- ⏳ **User Approvals** — Approve/reject student, teacher, parent accounts
- 👥 **User Management** — Boost XP, ban/unban users
- 📚 **Content** — Add quiz questions to the question bank
- 🎉 **Events** — Create global XP multiplier events
- 📢 **Announcements** — Send messages to specific roles
- ⚙️ **Platform Controls** — Feature flags, data export, credential management
- 🛡️ **Audit Log** — Complete history of all admin actions

---

## School Registration & Verification

### For schools

1. Go to `school-signup.html`
2. Fill in school details (name, principal, location, contact)
3. Create admin account with email & password
4. Submit — status will be **Pending Verification**

### For super admin (to verify)

1. Login to `admin/index.html`
2. Go to **School Management**
3. Click **Verify** next to the school
4. The school admin can now fully use their dashboard

### For school admin after verification

1. Go to `portal-login.html` or `login.html`
2. Select **School Admin** role
3. Enter registered email & password
4. Redirected to `school-dashboard.html`

---

## File Structure

```
lvlBase/
├── index.html                 # Landing page
├── login.html                 # Student/school login
├── signup.html                # Student registration
├── portal-login.html          # Multi-role login portal
├── school-signup.html         # School registration
├── dashboard.html             # Student dashboard
├── teacher-dashboard.html     # Teacher dashboard
├── parent-dashboard.html      # Parent dashboard
├── school-dashboard.html      # School admin dashboard
├── admin/
│   └── index.html             # Super admin panel (iPhone bento design)
├── css/
│   ├── main.css               # Global styles
│   ├── dashboard.css          # Student dashboard
│   ├── admin-bento.css        # Super admin bento styles
│   └── ...
├── js/
│   ├── firebase-config.js     # Firebase configuration
│   ├── firebase-bridge.js     # Firebase abstraction layer
│   ├── auth.js                # Authentication logic
│   ├── popup.js               # Toast/modal system
│   └── ...
├── manifest.json              # PWA manifest
└── sw.js                      # Service worker (offline support)
```

---

## Features by Role

### 🎓 Student
- XP system with E → SS rank progression
- Quiz engine (timed, multiple choice)
- Battle Arena (1v1 knowledge battles)
- Guild system (Shadow, Azure, Inferno, Titan, Zenith)
- Global leaderboard
- Daily goals & streak tracking
- AI Tutor (Sage)
- Progress reports

### 👨‍🏫 Teacher
- Class management
- Assign quizzes to students
- View student progress & grades
- Cheat monitoring reports
- Attendance tracking

### 👨‍👩‍👧 Parent
- Monitor child's performance
- View XP, quiz scores, streaks
- Daily/weekly progress reports
- Alerts for low performance

### 🏫 School Admin
- Manage students, teachers, parents
- Approve/reject pending users
- View school-wide statistics
- Cheat report management
- School settings & profile

### 👑 Super Admin
- Full platform control
- School verification
- Global XP multiplier
- Feature flags (maintenance mode, battle arena, AI tutor)
- Content management (question bank)
- Platform-wide announcements
- Data export (JSON)
- Audit log of all admin actions
- Admin password management

---

## Deployment

### GitHub Pages (free)

1. Push to GitHub
2. Go to repository **Settings → Pages**
3. Source: `main` branch, `/ (root)` folder
4. Your site: `https://yourusername.github.io/lvlBase/`

### Netlify (free tier)

1. Connect GitHub repo to [Netlify](https://netlify.com)
2. Build command: *(leave empty)*
3. Publish directory: `/` (root)
4. Deploy — Netlify gives you a live URL instantly

### Firebase Hosting (recommended with Firebase)

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
# Public directory: . (root)
# Single-page app: No
# Auto builds: No
firebase deploy
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| School admin sees student dashboard | Clear localStorage (`localStorage.clear()`) and login again via `portal-login.html` |
| School dashboard shows no data | Register school at `school-signup.html` first, then get verified by admin |
| Admin panel shows wrong data | Admin panel shows only real data — register users/schools to see stats |
| Firebase errors in console | Check `js/firebase-config.js` has correct config; check Firestore rules |
| PWA not installing | Must be served over HTTPS; localhost works for testing |

---

## Security Notes

- Never store plaintext passwords in localStorage (passwords are removed before saving school data)
- Change default admin credentials immediately after setup
- Use Firestore Security Rules in production
- Enable Firebase App Check to prevent abuse
- The `adminPassword` field is stripped from school objects before saving

---

<div align="center">

**Built with ❤️ for students who want to level up their learning.**

*lvlBase — Where Study Meets Legend* ⚡

</div>
