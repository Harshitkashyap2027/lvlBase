<div align="center">

# ⚡ lvlBase — Gamified School Learning Platform

### 🎓 Student · 👨‍🏫 Teacher · 👨‍👩‍👧 Parent · 🏫 School Admin · 👑 Super Admin

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com)
[![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?style=for-the-badge)](https://web.dev/progressive-web-apps/)

**A fully-gamified school platform — XP, ranks, guilds, battles, quizzes, AI tutor, and a role-based portal.  
Pure HTML · CSS · JavaScript. No framework, no build step required.**

</div>

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Quick Setup (No Server)](#quick-setup-no-server)
4. [Firebase Setup](#firebase-setup)
5. [Demo Login Credentials](#demo-login-credentials)
6. [Role-Based Portal](#role-based-portal)
7. [Complete File Structure](#complete-file-structure)
8. [Features by Role](#features-by-role)
9. [Firestore Security Rules](#firestore-security-rules)
10. [Realtime Database Rules](#realtime-database-rules)
11. [Admin Access](#admin-access)
12. [School Registration and Verification](#school-registration-and-verification)
13. [PWA / Install as App](#pwa--install-as-app)
14. [Deployment](#deployment)
15. [Customisation Guide](#customisation-guide)
16. [Known Issues and Fixes Applied](#known-issues-and-fixes-applied)

---

## Overview

**lvlBase** is a Progressive Web App (PWA) built entirely with plain HTML, CSS and JavaScript. It uses Firebase for authentication and real-time data persistence, and falls back to `localStorage` for demo/offline use. No build step, no framework, no server required.

The platform serves **five distinct roles** — Student, Teacher, Parent, School Admin, and Super Admin — each with their own protected dashboard, navigation, and data access.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript (ES Modules) |
| UI & Animation | Google Fonts (Poppins), CSS particles, CSS Grid/Flexbox |
| Database | Firebase Firestore (primary) + `localStorage` (demo/offline fallback) |
| Auth | Firebase Authentication (Email/Password + Google) |
| Push Notifications | Firebase Cloud Messaging (FCM) |
| Storage | Firebase Storage |
| Realtime (presence) | Firebase Realtime Database |
| PWA | Service Worker (`sw.js`) + Web App Manifest (`manifest.json`) |
| Hosting | Any static host — GitHub Pages, Netlify, Vercel, Firebase Hosting |

---

## Quick Setup (No Server)

You can run lvlBase **without Firebase** for demo or testing. All data is saved to `localStorage`.

### Step 1 — Clone

```bash
git clone https://github.com/Harshitkashyap2027/lvlBase.git
cd lvlBase
```

### Step 2 — Serve locally

**Option A — VS Code Live Server:**

```
Install "Live Server" extension → right-click index.html → Open with Live Server
```

**Option B — Python built-in server:**

```bash
python3 -m http.server 8080
# Then open http://localhost:8080
```

**Option C — Node.js `serve`:**

```bash
npx serve .
```

> ⚠️ You **must** use a local server (not `file://`) because the app uses ES Modules (`type="module"`).

### Step 3 — Open the app

| Page | URL (local) |
|---|---|
| Landing page | `http://localhost:8080/index.html` |
| Student login | `http://localhost:8080/login.html` |
| All-roles portal | `http://localhost:8080/portal-login.html` |
| Super Admin login | `http://localhost:8080/admin/login.html` |

### Step 4 — Register a test account

1. Go to `signup.html` → fill in name, email, password → **Sign Up**
2. You are automatically logged in as a **student**
3. Redirected to `dashboard.html`

For other roles, use `portal-login.html` and select the role, or register a school at `school-signup.html`.

---

## Firebase Setup

For real data persistence, multi-device support, and push notifications, connect a Firebase project.

### Step 1 — Create a Firebase project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **Add project** → name it `lvlBase` → **Create project**

### Step 2 — Enable Authentication

1. **Authentication → Get started**
2. Enable **Email/Password** provider
3. *(Optional)* Enable **Google** provider for one-tap sign-in

### Step 3 — Enable Firestore

1. **Firestore Database → Create database**
2. Choose **production mode** (apply security rules from the section below)
3. Region: `asia-south1` (India) or nearest to your users

### Step 4 — Enable Realtime Database *(optional, for presence/online status)*

1. **Realtime Database → Create database**
2. Same region as Firestore
3. Apply rules from the Realtime Database Rules section below

### Step 5 — Register your web app

1. **Project settings (gear icon) → Your apps → Web** (`</>`)
2. Register app with nickname `lvlBase Web`
3. Copy the `firebaseConfig` object shown

### Step 6 — Update `js/firebase-config.js`

Open `js/firebase-config.js` and replace the credentials:

```javascript
const firebaseConfig = {
  apiKey:            "YOUR_API_KEY",
  authDomain:        "YOUR_PROJECT_ID.firebaseapp.com",
  databaseURL:       "https://YOUR_PROJECT_ID-default-rtdb.REGION.firebasedatabase.app",
  projectId:         "YOUR_PROJECT_ID",
  storageBucket:     "YOUR_PROJECT_ID.firebasestorage.app",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId:             "YOUR_APP_ID",
  measurementId:     "G-XXXXXXXXXX"   // optional
};

// Set to true once you have added real credentials
export const FIREBASE_LIVE = true;

// FCM push notifications VAPID key (optional)
// Get from: Firebase Console → Project settings → Cloud Messaging → Web Push certificates
export const FCM_VAPID_KEY = "YOUR_VAPID_KEY";
```

Also update the same credentials in `admin/shared.js` (lines 8-16) for the legacy admin panel.

> **Security:** Never commit real API keys to a public repository.  
> Restrict your API key in [Google Cloud Console → Credentials](https://console.cloud.google.com/apis/credentials) to your domain only.

### Step 7 — Deploy Firestore Security Rules

Go to **Firebase Console → Firestore Database → Rules** and paste the rules from the section below.

---

## Demo Login Credentials

When `FIREBASE_LIVE = false` (localStorage demo mode), any email + password combination works — the account is auto-created on first login.

### Super Admin (admin panel)

| Field | Value |
|---|---|
| URL | `admin/login.html` |
| Email | `admin@lvlbase.com` |
| Password | `admin123` |

> Change the default password immediately after deployment via **Platform Controls → Admin Credentials**.

### School Admin (after school is registered and verified)

| Field | Value |
|---|---|
| URL | `portal-login.html` → select School Admin |
| Email | The email used during `school-signup.html` |
| Password | Set during school registration |

### Student / Teacher / Parent (demo)

| Field | Value |
|---|---|
| URL | `login.html` or `portal-login.html` |
| Email | Any email (e.g. `student@test.com`) |
| Password | Any 6+ character string |
| Role | Defaults to `student` |

To test a different role in demo mode, open DevTools → Console and run:

```javascript
var u = JSON.parse(localStorage.getItem('lvlbase_current_user'));
u.role = 'teacher';   // or 'parent', 'school_admin', 'admin'
localStorage.setItem('lvlbase_current_user', JSON.stringify(u));
location.reload();
```

---

## Role-Based Portal

lvlBase has **5 roles**, each with a protected dashboard. Accessing the wrong dashboard shows an "Access Denied" screen and redirects automatically.

| Role | Primary Dashboard | Login Page | Guard |
|---|---|---|---|
| 🎓 Student | `dashboard.html` | `login.html` | `role === 'student'` |
| 👨‍🏫 Teacher | `teacher-dashboard.html` | `portal-login.html` | `role === 'teacher'` |
| 👨‍👩‍👧 Parent | `parent-dashboard.html` | `portal-login.html` | `role === 'parent'` |
| 🏫 School Admin | `school-dashboard.html` | `login.html` | `role === 'school_admin'` |
| 👑 Super Admin | `admin/index.html` | `admin/login.html` | `role === 'admin'` |

### How role guards work

Every protected page runs a synchronous IIFE before the DOM loads:

```javascript
(function() {
  var u = JSON.parse(localStorage.getItem('lvlbase_current_user') || 'null');
  if (!u) { window.location.replace('../../login.html'); throw ''; }
  if (u.role !== 'student') { /* show access-denied UI and redirect */ throw 'ACCESS_DENIED'; }
})();
```

The `lvlbase_current_user` object in localStorage must have a `role` field.

---

## Complete File Structure

```
lvlBase/
|
+-- index.html                          # Main landing page (start here)
+-- login.html                          # Student / school-admin login
+-- signup.html                         # Student self-registration
+-- portal-login.html                   # Multi-role login portal
+-- school-signup.html                  # School registration form
+-- dashboard.html                      # Student dashboard (original/root)
+-- teacher-dashboard.html              # Teacher dashboard (root)
+-- parent-dashboard.html               # Parent dashboard (root)
+-- school-dashboard.html               # School admin dashboard (root)
+-- ai-assistant.html                   # AI Tutor (Sage)
+-- quiz.html                           # Quiz engine
+-- battles.html                        # 1v1 Battle arena
+-- subjects.html                       # Subject list & chapters
+-- learn.html                          # Learning content viewer
+-- leaderboard.html                    # Global leaderboard
+-- guild-wars.html                     # Guild vs guild battles
+-- goals.html                          # Daily/weekly goals
+-- certificate.html                    # Certificates earned
+-- competition.html                    # World competition
+-- homework-scanner.html               # Camera homework helper
+-- science-lab.html                    # Interactive science lab
+-- settings.html                       # Account settings
+-- parent-analytics.html               # Parent analytics (root)
+-- parent-complaints.html              # Parent complaints (root)
+-- teacher-tasks.html                  # Teacher task manager (root)
+-- teacher-tests.html                  # Teacher test manager (root)
|
+-- auth/                               # Authentication pages
|   +-- portal-login.html               # Multi-role portal login
|   +-- signup-student.html             # Student sign-up (structured)
|   +-- signup-teacher.html             # Teacher sign-up
|   +-- school-onboarding.html          # School onboarding wizard
|   +-- invite-claim.html               # Claim an invite link
|   +-- magic-link.html                 # Magic-link login
|   +-- sso-gateway.html                # SSO gateway
|   +-- 2fa-setup.html                  # Two-factor auth setup
|   +-- biometric-auth.html             # Biometric auth page
|   +-- forgot-password.html            # Password reset request
|   +-- reset-password.html             # Password reset form
|   +-- blocked.html                    # Account blocked screen
|   +-- session-expired.html            # Session expired screen
|
+-- app/                                # Structured role-based dashboards
|   |
|   +-- student/                        # Student portal
|   |   +-- dashboard.html              # [*] Student main dashboard
|   |   +-- quest-map.html              # Chapter quest map
|   |   +-- profile.html                # Student profile
|   |   +-- backpack.html               # Inventory / backpack
|   |   +-- analytics.html              # Personal analytics
|   |   +-- support-desk.html           # Support ticket desk
|   |   +-- focus-mode.html             # Distraction-free focus mode
|   |   +-- arena/
|   |   |   +-- matchmaking.html        # Battle matchmaking lobby
|   |   |   +-- battle-stage.html       # Live battle stage
|   |   |   +-- tournaments.html        # Tournament listings
|   |   |   +-- leaderboard.html        # Arena leaderboard
|   |   +-- guilds/
|   |   |   +-- guild-dashboard.html    # Guild home
|   |   |   +-- guild-wars.html         # Guild-vs-guild wars
|   |   |   +-- xp-shop.html            # XP reward shop
|   |   |   +-- loot-boxes.html         # Loot box rewards
|   |   +-- ai/
|   |   |   +-- sage-chat.html          # AI Sage chat
|   |   |   +-- smart-flashcards.html   # AI-generated flashcards
|   |   |   +-- weak-analysis.html      # Weak topic analyser
|   |   |   +-- mock-interview.html     # Mock interview simulator
|   |   |   +-- notes.html              # AI notes
|   |   +-- workspace/
|   |       +-- web-studio.html         # In-browser HTML/CSS/JS editor
|   |       +-- python-lab.html         # Python practice lab
|   |       +-- flutter-lab.html        # Flutter/Dart lab
|   |       +-- code-review.html        # AI code review
|   |
|   +-- teacher/                        # Teacher portal
|   |   +-- dashboard.html              # [*] Teacher main dashboard
|   |   +-- communications.html         # Messaging & announcements
|   |   +-- calendar.html               # Teaching calendar
|   |   +-- classes/
|   |   |   +-- rosters.html            # Class rosters
|   |   |   +-- seating-chart.html      # Seating chart
|   |   |   +-- attendance.html         # Attendance tracker
|   |   |   +-- behavior-tracker.html   # Behaviour log
|   |   +-- assessments/
|   |   |   +-- assignments.html        # Assignment manager
|   |   |   +-- rubric-builder.html     # Rubric builder
|   |   |   +-- quiz-builder.html       # Quiz builder
|   |   |   +-- question-bank.html      # Question bank
|   |   |   +-- gradebook.html          # Grade book
|   |   |   +-- ai-grader.html          # AI auto-grader
|   |   +-- proctoring/
|   |   |   +-- live-monitor.html       # Live exam monitor
|   |   |   +-- cheat-reports.html      # Cheat / flag reports
|   |   |   +-- audio-analysis.html     # Audio analysis
|   |   +-- collaboration/
|   |       +-- lesson-marketplace.html # Shared lesson marketplace
|   |       +-- staff-lounge.html       # Staff discussion lounge
|   |
|   +-- school-admin/                   # School admin portal
|   |   +-- dashboard.html              # [*] School admin main dashboard
|   |   +-- broadcast.html              # School-wide broadcast
|   |   +-- calendar.html               # School calendar
|   |   +-- analytics/
|   |   |   +-- performance.html        # School performance
|   |   |   +-- teacher-metrics.html    # Teacher metrics
|   |   |   +-- reports.html            # Downloadable reports
|   |   +-- users/
|   |   |   +-- approvals.html          # Pending user approvals
|   |   |   +-- students.html           # Student roster
|   |   |   +-- teachers.html           # Teacher roster
|   |   |   +-- parents.html            # Parent roster
|   |   |   +-- alumni.html             # Alumni directory
|   |   +-- operations/
|   |   |   +-- hall-pass.html          # Digital hall pass
|   |   |   +-- emergency.html          # Emergency management
|   |   |   +-- assets.html             # School asset tracker
|   |   +-- security/
|   |       +-- sso-config.html         # SSO configuration
|   |       +-- firewall.html           # IP firewall
|   |       +-- audit-logs.html         # Security audit logs
|   |       +-- data-export.html        # GDPR data export
|   |
|   +-- parent/                         # Parent portal
|   |   +-- dashboard.html              # [*] Parent main dashboard
|   |   +-- child-report.html           # Child progress report
|   |   +-- attendance.html             # Child attendance view
|   |   +-- teacher-connect.html        # Message teacher
|   |   +-- pt-meeting.html             # PT meeting scheduler
|   |   +-- screen-time.html            # Screen time controls
|   |   +-- rewards.html                # Child rewards view
|   |   +-- payments.html               # Fee / payment portal
|   |
|   +-- super-admin/                    # Super admin portal
|       +-- dashboard.html              # [*] Super admin main dashboard
|       +-- finance.html                # Platform finance overview
|       +-- global-events.html          # Global XP multiplier events
|       +-- mail.html                   # Bulk mail center
|       +-- tenants/
|       |   +-- requests.html           # New school requests
|       |   +-- active.html             # Active school tenants
|       |   +-- feature-flags.html      # Per-tenant feature flags
|       +-- infrastructure/
|       |   +-- server.html             # Server health monitor
|       |   +-- ai-usage.html           # AI API usage and cost
|       |   +-- db-health.html          # Database health
|       |   +-- backup.html             # Backup management
|       +-- security/
|       |   +-- threats.html            # Active threat monitor
|       |   +-- ddos.html               # DDoS protection
|       |   +-- logs.html               # Security logs
|       +-- content/
|           +-- question-bank.html      # Platform-wide question bank
|           +-- roadmaps.html           # Learning roadmap editor
|           +-- achievements.html       # Achievement / badge editor
|
+-- admin/                              # Legacy super admin panel (bento UI)
|   +-- index.html                      # [*] Admin dashboard
|   +-- login.html                      # Admin login
|   +-- users.html                      # User management
|   +-- user-approvals.html             # Approve pending users
|   +-- schools.html                    # School management
|   +-- analytics.html                  # Platform analytics charts
|   +-- reports.html                    # Reports
|   +-- content.html                    # Content management
|   +-- events.html                     # XP events
|   +-- announcements.html              # Announcements
|   +-- badges-admin.html               # Badge editor
|   +-- leaderboard-admin.html          # Leaderboard admin
|   +-- platform.html                   # Platform controls / feature flags
|   +-- audit.html                      # Audit log
|   +-- teachers.html                   # Teacher list
|   +-- parents.html                    # Parent list
|   +-- shared.js                       # Shared sidebar + session logic
|
+-- public/                             # Marketing and legal pages
|   +-- index.html                      # Public marketing landing
|   +-- pricing.html                    # Pricing plans
|   +-- features.html                   # Feature highlights
|   +-- for-schools.html                # For schools page
|   +-- for-teachers.html               # For teachers page
|   +-- for-parents.html                # For parents page
|   +-- case-studies.html               # Case studies
|   +-- webinars.html                   # Webinars
|   +-- roi-calculator.html             # ROI calculator
|   +-- press.html                      # Press and media
|   +-- faq.html                        # FAQ
|   +-- contact.html                    # Contact form
|   +-- system-status.html              # System status
|   +-- verify-certificate.html         # Certificate verification
|   +-- 404.html                        # 404 error page
|   +-- offline.html                    # Offline fallback page
|   +-- maintenance.html                # Maintenance mode page
|   +-- legal/
|       +-- privacy-policy.html
|       +-- terms-of-service.html
|       +-- compliance.html
|       +-- security-whitepaper.html
|
+-- css/                                # Root-level stylesheets (root pages)
|   +-- main.css                        # Global base styles
|   +-- dashboard.css                   # Student dashboard styles
|   +-- quiz.css                        # Quiz engine styles
|   +-- battle.css                      # Battle arena styles
|   +-- admin.css                       # Admin panel styles
|   +-- admin-bento.css                 # Bento-grid admin design
|
+-- core/                               # Shared design system (app/ pages)
|   +-- css/
|   |   +-- base.css                    # Universal base styles
|   |   +-- data.css                    # Tables, charts, data UI
|   |   +-- bento-grid.css              # Bento-grid layout system
|   |   +-- gamification.css            # XP bars, ranks, badges
|   |   +-- themes/                     # Seasonal colour themes
|   +-- js/
|       +-- core/                       # Core utilities
|       +-- features/                   # Feature modules
|       +-- firebase/                   # Firebase helpers
|
+-- js/                                 # JavaScript modules
|   +-- firebase-config.js              # [EDIT THIS] Firebase credentials
|   +-- firebase-bridge.js              # Firebase <-> localStorage bridge
|   +-- auth.js                         # Sign in / sign up / sign out
|   +-- rbac.js                         # Role-based access control
|   +-- quiz.js                         # Quiz engine logic
|   +-- battles.js                      # Battle arena logic
|   +-- dashboard.js                    # Dashboard data loading
|   +-- gamification.js                 # XP, ranks, achievements
|   +-- leaderboard.js                  # Leaderboard fetch and render
|   +-- goals.js                        # Daily goals logic
|   +-- guild-wars.js                   # Guild war logic
|   +-- subjects.js                     # Subject and content loader
|   +-- personalized-quiz.js            # AI-personalised quiz
|   +-- ai-assistant.js                 # AI tutor (Sage)
|   +-- voice-ai.js                     # Voice input for AI
|   +-- popup.js                        # Toast and modal system
|   +-- admin.js                        # Admin panel logic
|
+-- icons/                              # PWA app icons (192px, 512px)
+-- assets/                             # Images and media assets
+-- pwa/                                # Additional PWA assets
+-- config/
|   +-- firebase.json                   # Firebase Hosting config
|   +-- firestore.rules                 # Firestore security rules
|   +-- storage.rules                   # Firebase Storage rules
|   +-- vercel.json                     # Vercel deployment config
|   +-- package.json                    # Node.js project metadata
|   +-- .env.example                    # Environment variables template
+-- manifest.json                       # PWA Web App Manifest
+-- sw.js                               # Service worker (offline caching)
+-- firestore.rules                     # Firestore rules (root copy)
```

> **[*]** = Primary entry-point dashboard for that role.

---

## Features by Role

### 🎓 Student

| Feature | Description |
|---|---|
| XP System | Earn XP completing quizzes, battles, goals; progress through E → D → C → B → A → S → SS ranks |
| Quiz Engine | Timed multiple-choice quizzes per subject; AI-personalised difficulty |
| Battle Arena | 1v1 real-time knowledge battles; matchmaking, live stage, tournaments |
| Guild System | Join one of 5 guilds (Shadow, Azure, Inferno, Titan, Zenith); guild wars, XP shop, loot boxes |
| Leaderboard | Global real-time ranking sorted by total XP |
| Daily Goals and Streaks | Daily/weekly goal tracking; streak counter with XP multiplier |
| AI Tutor (Sage) | Chat-based AI tutor; smart flashcards; weak-topic analysis; mock interviews |
| Workspace | In-browser Web Studio, Python Lab, Flutter Lab, AI Code Review |
| Quest Map | Chapter-by-chapter quest progression with day-locking |
| Focus Mode | Distraction-free study mode with timer |
| Certificates | Earn downloadable certificates with unique QR code for verification |
| PWA / Offline | Install as a native-like app; core features work offline |

### 👨‍🏫 Teacher

| Feature | Description |
|---|---|
| Dashboard | Active students, quiz completion rate, average score, pending tasks |
| Class Management | Rosters, seating charts, attendance tracker, behaviour log |
| Assessment Tools | Quiz builder, assignment manager, rubric builder, AI auto-grader, gradebook |
| Question Bank | Create/edit/delete questions per subject and difficulty level |
| Proctoring | Live exam monitor, cheat flag reports, audio analysis |
| Collaboration | Lesson marketplace, staff discussion lounge |
| Calendar | Teaching calendar with events and deadlines |

### 👨‍👩‍👧 Parent

| Feature | Description |
|---|---|
| Dashboard | Child's XP, rank, streak, and quiz scores at a glance |
| Progress Report | Detailed subject-by-subject progress breakdown |
| Attendance | View child's daily attendance record |
| Teacher Connect | Direct messaging with the child's teachers |
| PT Meeting Scheduler | Book parent-teacher meetings online |
| Screen Time Controls | Set daily platform usage limits |
| Rewards View | See child's earned badges and achievements |
| Payments | Fee and subscription payment portal |

### 🏫 School Admin

| Feature | Description |
|---|---|
| Dashboard | School-wide stats: total students, pass rate, active teachers |
| User Management | Approve/reject students, teachers, parents; manage alumni |
| Broadcast | Send school-wide announcements to all users |
| Analytics | School performance charts, teacher metrics, downloadable reports |
| Operations | Digital hall pass, emergency management, school asset tracker |
| Security | SSO config, IP firewall, GDPR data export, security audit logs |
| Calendar | School events and schedule |

### 👑 Super Admin

| Feature | Description |
|---|---|
| Platform Dashboard | Live: total schools, students, API usage, revenue |
| School Tenants | Review requests, manage active schools, set per-school feature flags |
| Finance | Subscription revenue, invoices, payouts overview |
| Global Events | Create platform-wide XP multiplier events |
| Infrastructure | Server health, AI cost tracking, database health, backup management |
| Security | Threat monitor, DDoS protection, security log viewer |
| Content | Platform question bank, learning roadmaps, achievement/badge editor |
| Mail Center | Bulk email to any user segment |
| Legacy Admin Panel | `admin/` — bento-grid UI with full audit log and admin credential management |

---

## Firestore Security Rules

Go to **Firebase Console → Firestore Database → Rules** and paste:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    function isSignedIn()    { return request.auth != null; }
    function isOwner(uid)    { return isSignedIn() && request.auth.uid == uid; }
    function myRole()        { return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role; }
    function mySchool()      { return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.schoolId; }
    function isAdmin()       { return isSignedIn() && myRole() == 'admin'; }
    function isSchoolAdmin() { return isSignedIn() && myRole() == 'school_admin'; }
    function isTeacher()     { return isSignedIn() && myRole() == 'teacher'; }
    function isParent()      { return isSignedIn() && myRole() == 'parent'; }
    function sameSchool(sid) { return isSignedIn() && mySchool() == sid; }

    // Super admin: unrestricted access (must be first)
    match /{document=**} { allow read, write: if isAdmin(); }

    // Users collection
    match /users/{userId} {
      allow read, write: if isOwner(userId);
      allow read: if (isTeacher() || isSchoolAdmin()) &&
        get(/databases/$(database)/documents/users/$(userId)).data.schoolId == mySchool();
      allow read: if isParent() &&
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.childUid == userId;
      allow update: if isSchoolAdmin() &&
        get(/databases/$(database)/documents/users/$(userId)).data.schoolId == mySchool() &&
        request.resource.data.diff(resource.data).affectedKeys().hasOnly(['status','updatedAt']);
    }

    // Schools
    match /schools/{schoolId} {
      allow read: if isSignedIn();
      allow create, delete: if isAdmin();
      allow update: if isSchoolAdmin() && sameSchool(schoolId) &&
        !request.resource.data.diff(resource.data).affectedKeys().hasAny(['status','verifiedAt']);
    }

    match /guild_events/{eventId} {
      allow read: if isSignedIn();
      allow create: if isSignedIn();
      allow update, delete: if isAdmin();
    }

    match /questions/{questionId} {
      allow read: if isSignedIn();
      allow write: if isAdmin() || isTeacher();
    }

    match /leaderboard/{entryId} {
      allow read: if isSignedIn();
      allow write: if isSignedIn() && resource.data.uid == request.auth.uid;
    }

    match /announcements/{id} {
      allow read: if isSignedIn();
      allow write: if isAdmin();
    }

    match /events/{id} {
      allow read: if isSignedIn();
      allow write: if isAdmin();
    }

    match /notifications/{id} {
      allow read: if isSignedIn() && (
        resource.data.userId == request.auth.uid ||
        (isSchoolAdmin() && resource.data.schoolId == mySchool())
      );
      allow create: if isAdmin() || isSchoolAdmin();
      allow update: if isSignedIn() && resource.data.userId == request.auth.uid &&
        request.resource.data.diff(resource.data).affectedKeys().hasOnly(['read']);
      allow delete: if isAdmin();
    }

    match /audit_log/{logId} {
      allow read: if isAdmin();
      allow create: if isAdmin();
      allow update, delete: if false;
    }
  }
}
```

### Firestore Collections Reference

| Collection | Stored Data |
|---|---|
| `users/{uid}` | Profile, role, schoolId, XP, guild, grade, progress |
| `schools/{id}` | School name, address, admin email, status |
| `guild_events/{id}` | Guild battle events and scores |
| `questions/{id}` | Quiz question bank (subject, grade, difficulty) |
| `leaderboard/{id}` | XP ranking entries |
| `announcements/{id}` | Platform-wide announcements |
| `events/{id}` | XP multiplier events |
| `notifications/{id}` | Per-user notifications |
| `audit_log/{id}` | Admin action history (append-only) |

---

## Realtime Database Rules

Go to **Firebase Console → Realtime Database → Rules** and paste:

```json
{
  "rules": {
    ".read":  false,
    ".write": false,
    "users": {
      "$uid": {
        ".read":  "auth != null && (auth.uid == $uid || root.child('users').child(auth.uid).child('role').val() == 'admin')",
        ".write": "auth != null && (auth.uid == $uid || root.child('users').child(auth.uid).child('role').val() == 'admin')"
      }
    },
    "schools": {
      ".read": "auth != null",
      "$schoolId": {
        ".write": "auth != null && (root.child('users').child(auth.uid).child('role').val() == 'admin' || (root.child('users').child(auth.uid).child('role').val() == 'school_admin' && root.child('users').child(auth.uid).child('schoolId').val() == $schoolId))"
      }
    },
    "guild_events": { ".read": "auth != null", ".write": "auth != null" },
    "leaderboard":  { ".read": "auth != null", ".write": "auth != null" },
    "questions": {
      ".read": "auth != null",
      ".write": "auth != null && (root.child('users').child(auth.uid).child('role').val() == 'admin' || root.child('users').child(auth.uid).child('role').val() == 'teacher')"
    },
    "announcements": {
      ".read": "auth != null",
      ".write": "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'"
    },
    "events": {
      ".read": "auth != null",
      ".write": "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'"
    },
    "notifications": {
      "$uid": {
        ".read":  "auth != null && auth.uid == $uid",
        ".write": "auth != null && (auth.uid == $uid || root.child('users').child(auth.uid).child('role').val() == 'admin' || root.child('users').child(auth.uid).child('role').val() == 'school_admin')"
      }
    },
    "audit_log": {
      ".read":  "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'",
      ".write": "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'"
    }
  }
}
```

---

## Admin Access

### Super Admin Panel (Legacy Bento UI)

URL: `admin/index.html`  
Login page: `admin/login.html`

Default credentials:

```
Email:    admin@lvlbase.com
Password: admin123
```

> **Change the default password immediately** after deployment via Platform Controls → Admin Credentials in the admin panel.

### Admin Panel Features

| Section | What it does |
|---|---|
| Dashboard | Live platform stats: users, schools, quiz activity, guild distribution |
| User Management | Search, ban/unban, boost XP for any user |
| User Approvals | Approve/reject pending student, teacher, and parent accounts |
| School Management | Verify, reject, or suspend school registrations |
| Analytics | Subject popularity, school performance, activity charts |
| Content | Add, edit, delete quiz questions by subject and grade |
| Events | Create global XP multiplier events (e.g. "Double XP Weekend") |
| Announcements | Push messages to all users or specific roles |
| Badges Admin | Create and assign achievement badges |
| Leaderboard Admin | Manually adjust leaderboard entries |
| Platform Controls | Feature flags, maintenance mode, data export |
| Audit Log | Full timestamped history of every admin action |

---

## School Registration and Verification

### Step 1 — School registers

1. Go to `school-signup.html`
2. Fill in: school name, principal, address, city, state, pincode, phone, email, website
3. Create a school admin account (email + password)
4. Submit → status becomes **Pending Verification**

### Step 2 — Super admin verifies

1. Login to `admin/index.html`
2. Go to **School Management**
3. Click **Verify** next to the pending school

### Step 3 — School admin activates

1. Go to `portal-login.html` → select **School Admin**
2. Enter registered email and password
3. Redirected to `school-dashboard.html`
4. Start adding teachers and students via **Users → Approvals**

---

## PWA / Install as App

lvlBase is a full PWA. Users on Chrome, Edge, and Safari will see an "Install App" prompt.

- **Android / Chrome:** Browser menu → "Add to Home Screen" → Install
- **iOS / Safari:** Share button → "Add to Home Screen"
- **Desktop Chrome/Edge:** Click the install icon in the address bar

The manifest is at `manifest.json` and service worker at `sw.js` (both at root). The app caches key assets and works offline for core features.

---

## Deployment

### GitHub Pages (free)

1. Push to GitHub
2. **Settings → Pages → Source**: `main` branch, `/ (root)` folder
3. Live URL: `https://yourusername.github.io/lvlBase/`

### Netlify (free tier, custom domain)

1. Connect GitHub repo at [netlify.com](https://netlify.com)
2. Build command: *(leave empty)*
3. Publish directory: `/` (root)
4. Click **Deploy**

### Firebase Hosting (recommended)

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
# Publish directory: .  (root)
# Configure as single-page app: No
# Overwrite index.html: No
firebase deploy
```

### Vercel

The repo includes `config/vercel.json`. Deploy with:

```bash
npm install -g vercel
vercel --prod
```

---

## Customisation Guide

### Change the platform name

```bash
# Linux / macOS
grep -rl "lvlBase" . --include="*.html" | xargs sed -i 's/lvlBase/YourSchoolName/g'
```

### Change the primary colour theme

Edit `css/main.css` (root pages) and `core/css/base.css` (app/ pages):

```css
:root {
  --primary:   #6C63FF;   /* Main purple — change this */
  --secondary: #FF6B6B;   /* Coral accent */
  --accent:    #FFD700;   /* Gold (XP colour) */
  --success:   #00D1B2;   /* Teal success colour */
}
```

### Add quiz questions via the Admin Panel

1. Login to `admin/index.html`
2. Go to **Content → Question Bank**
3. Click **Add Question** and fill in subject, grade, difficulty, question, options, correct answer

### Add quiz questions via Firestore

Add a document to the `questions` collection:

```json
{
  "subject": "Math",
  "grade": "10",
  "difficulty": "medium",
  "question": "What is 2 + 2?",
  "options": ["3", "4", "5", "6"],
  "answer": "4",
  "createdBy": "admin"
}
```

### Enable maintenance mode

Admin Panel → **Platform Controls** → toggle **Maintenance Mode**. Non-admin users will be redirected to `public/maintenance.html`.

### Add a new school manually

1. Admin Panel → **School Management → Add School**
2. Or let the school self-register via `school-signup.html` and verify from the admin panel

---

## Known Issues and Fixes Applied

The following issues were found during the page audit and have been fixed:

### Fixed — Broken login redirects in app/ dashboards

**Problem:** Role guard code in `app/student/dashboard.html`, `app/teacher/dashboard.html`, `app/school-admin/dashboard.html`, `app/parent/dashboard.html`, and `app/super-admin/dashboard.html` redirected to `login.html` as a bare relative path. From `app/<role>/`, this resolved to `app/<role>/login.html` which does not exist.

**Fix:** All redirects updated to use correct relative paths (e.g. `../../login.html` for 2-level-deep pages, `../../admin/login.html` for super-admin).

### Fixed — Broken navigation links in app/student/dashboard.html

**Problem:** The student dashboard sidebar linked to `quiz.html`, `battles.html`, `subjects.html`, `leaderboard.html`, etc. as bare filenames. From `app/student/`, these resolved to `app/student/quiz.html` instead of the root-level `quiz.html`.

**Fix:** All sidebar and navbar links updated to use `../../filename.html` prefix.

### Fixed — Broken navigation in app/student sub-pages

**Problem:** Same bare-filename link issue in `app/student/arena/`, `app/student/ai/`, `app/student/guilds/`, `app/student/workspace/`, and `app/teacher/assessments/`.

**Fix:** Updated all links to use `../../../filename.html` (3 levels up to root).

### Fixed — Wrong role-redirect maps in app/ dashboards

**Problem:** When an unauthorised user hit a role-protected dashboard, the "Go to My Dashboard" button used bare filenames like `dashboard.html` which were broken from subdirectories.

**Fix:** All role-redirect maps updated with correct relative-path prefixes.

### Fixed — Secondary logout redirect in school-admin dashboard

**Problem:** The logout confirmation handler in `app/school-admin/dashboard.html` used `window.location.href = 'login.html'` which was broken.

**Fix:** Updated to `../../login.html`.

### Remaining notes

- **Root pages vs app/ pages:** The repo has two parallel sets of pages. The original root-level pages (`dashboard.html`, `quiz.html`, `battles.html`, etc.) are the **primary fully-functional pages** and are the ones linked from the student sidebar. The `app/*/` pages are enhanced versions with extended layout and features that link back to root-level pages for quiz and battle functionality.
- **Firebase credentials:** `js/firebase-config.js` and `admin/shared.js` contain Firebase credentials for the live `lvlbase` project. If you fork this repo, replace these with your own project credentials.

---

<div align="center">

Built with ❤️ for schools · Pure HTML · CSS · JavaScript

**⚡ lvlBase — Level Up Your Learning**

</div>
