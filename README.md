<div align="center">

# ⚡ lvlBase — Where Learning Meets Legends

### *The World's Most Gamified Educational Platform for School Students*

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com)

**Transform every study session into an epic adventure. Earn XP, rank up, join guilds, battle opponents, and become the ultimate scholar.**

[🚀 Live Demo](#) • [📖 Documentation](#-quick-start) • [⚙️ Firebase Setup](#-firebase-setup) • [🛡️ Admin Panel](#-admin-access)

---

> *"We don't just teach students. We level them up."*

</div>

---

## 🌟 Why lvlBase?

> Most educational platforms are **boring**. Students open them once and never come back.

**lvlBase is different.** We've engineered a learning system that is *psychologically addictive* — not through dark patterns, but through the same mechanics that make great video games impossible to put down:

- 🎮 **Ranked progression** — Rise from E-Rank to legendary SS-Rank
- ⚔️ **Battle system** — Challenge AI and real opponents in knowledge battles
- 🏰 **Guild wars** — Compete as a team, not just as an individual
- 🔥 **Streaks & bonuses** — Daily rewards that compound over time
- 🤖 **AI-powered tutoring** — 24/7 personalized study assistant
- 📊 **Smart analytics** — Know exactly where you're weak before exams

---

## ✨ Feature Overview

### 📚 Core Learning System

| Feature | Description |
|---------|-------------|
| Subject Learning | Math 📐, Science 🔬, English 📖 — chapter-by-chapter |
| Smart Notes | Simple language explanations, not boring theory |
| Video Support | Optional video embed per topic |
| Offline Mode | Download notes, study without internet |
| Progress Tracking | Chapter-wise completion with visual progress bars |

### 🎮 Gamification Engine

| Feature | Description |
|---------|-------------|
| XP System | Earn experience points for every action |
| 8 Rank Tiers | E → D → C → B → A → S → SS → National |
| Streak System | Daily login streaks with XP multipliers |
| Achievement Badges | 20+ unlockable badges (First Quiz, Week Warrior, etc.) |
| Power Score | Composite score of accuracy + speed + consistency |
| Level Evolution | Beginner → Intermediate → Pro → Master → Legend |

### ⚔️ Battle Arena

| Mode | Description |
|------|-------------|
| Solo Battle | Quiz-based fight against AI opponent (health bars!) |
| Quick Duel | 1v1 random match — async or real-time |
| Guild Battle | Team vs team, contributions add up |
| Daily Challenge | AI-generated test based on your weak topics |
| Study Battle | Full knowledge showdown with power-ups |

### 🏰 Guild System

Five elite guilds — each with unique personality, XP bonuses, and battle matchups:

| Guild | Theme | Color | Bonus |
|-------|-------|-------|-------|
| 🌙 Shadow Guild | Stealth + Intelligence | Purple/Black | +15% Math XP |
| 💧 Azure Order | Logic + Calm Focus | Blue | +15% Science XP |
| 🔥 Inferno Legion | Aggression + Speed | Red/Orange | +20% Battle XP |
| ⚡ Titan Brotherhood | Consistency + Power | Green | +15% English XP |
| ✨ Zenith Circle | Elite + All-Round | Gold | +10% All XP |

> Guilds have cooldown-based switching (30-day lockout). No same-guild matchups in battles.

### 🏆 Ranking System

Progress through 8 ranks — each unlocking new features, UI themes, and bragging rights:

| Rank | XP Required | Color | Unlock |
|------|-------------|-------|--------|
| ⚫ E-Rank | 0 | Gray | Starter quizzes |
| 🟢 D-Rank | 500 | Green | Guild access |
| 🔵 C-Rank | 1,500 | Blue | Battle mode |
| 🟣 B-Rank | 3,500 | Purple | Ranked duels |
| 🟡 A-Rank | 7,000 | Gold | Guild wars |
| 🔴 S-Rank | 15,000 | Red | AI advanced mode |
| ⭐ SS-Rank | 30,000 | Gold+Glow | Exclusive SS UI |
| 🌟 National | 50,000 | Rainbow | Hall of Fame |

### 🤖 AI Study Assistant — "Sage"

- 💬 Chat interface similar to modern AI assistants
- 📝 Ask any doubt in any subject
- 🧒 "Explain like I'm 10" mode for complex topics
- 📚 Homework help with step-by-step solutions
- 📅 "What should I study next?" recommendations
- 🎙️ Voice input support (Web Speech API)
- 📸 Image-based question solving (camera input)
- 🧠 Memory of previous conversations per session

### 📊 Admin Dashboard

Enterprise-grade admin control panel with:

- 📈 **AI Insights** — "Student engagement dropped 18% this week"
- 🕹️ **Gamification Controller** — XP multipliers, Double XP events
- ⚔️ **Guild Balance System** — Auto-detect imbalance, correct bonuses
- 🚨 **Cheat Detection** — Pattern analysis, suspicious score flagging
- 📅 **Event Creator** — Launch Math Marathons, Weekend Battles
- 🌍 **Real-Time Analytics** — Engagement heatmaps, performance trends
- 👤 **User Management** — Ban, boost, promote, reset progress
- 📋 **Audit Timeline** — Every admin action logged with timestamp
- 🔐 **Security Dashboard** — IP tracking, geo-blocking, device history

### 👨‍👩‍👧 Parent Dashboard

- 📊 Child's full performance overview
- 📉 Weak subject detection with improvement suggestions
- 📅 Study activity calendar
- 🏆 Achievement celebration feed
- 📋 Weekly/monthly performance reports
- ⏱️ Time-on-platform analytics

---

## 🚀 Quick Start

### Option 1 — Open Directly (No Setup)

```bash
# Just open in browser — works in demo mode immediately!
open index.html
```

> **Demo Mode** uses `localStorage` for all data — no Firebase needed.

### Option 2 — Local HTTP Server

```bash
# Python (recommended)
python3 -m http.server 3000

# Node.js
npx serve .

# Then open: http://localhost:3000
```

### Option 3 — Deploy to Hosting

Deploy to any static host:
- [Firebase Hosting](https://firebase.google.com/docs/hosting) (recommended — same project)
- [Vercel](https://vercel.com) — drag & drop
- [Netlify](https://netlify.com) — free tier
- [GitHub Pages](https://pages.github.com) — free with repo

---

## 📁 Project Structure

```
lvlBase/
├── 📄 index.html              # Landing page (hero, guilds, ranks, CTA)
├── 📄 login.html              # 3-step onboarding (auth → profile → guild)
├── 📄 dashboard.html          # Student command center
├── 📄 subjects.html           # Subject selection hub
├── 📄 learn.html              # Chapter learning with notes
├── 📄 quiz.html               # Quiz engine (MCQ, timer, score)
├── 📄 battles.html            # Battle arena (Solo/Duel/Guild)
├── 📄 leaderboard.html        # Live rankings (Individual/Guild/National)
├── 📄 ai-assistant.html       # Sage — AI study assistant
├── 📄 goals.html              # Goal setting and progress tracking
├── 📄 parent-dashboard.html   # Parent monitoring portal
├── 📄 settings.html           # Profile, theme, preferences
│
├── 📁 admin/
│   └── 📄 index.html          # Full admin control panel
│
├── 📁 css/
│   ├── 🎨 main.css            # Design system, components, animations
│   ├── 🎨 dashboard.css       # Dashboard layout + sidebar
│   ├── 🎨 quiz.css            # Quiz interface + result screens
│   ├── 🎨 battle.css          # Battle arena + health bars
│   └── 🎨 admin.css           # Admin panel + charts
│
└── 📁 js/
    ├── ⚙️ firebase-config.js  # Firebase initialization (configure me!)
    ├── ⚙️ auth.js             # Authentication (demo + Firebase modes)
    ├── ⚙️ gamification.js     # XP engine, ranks, achievements, guilds
    ├── ⚙️ quiz.js             # Quiz data (45+ questions), timer, scoring
    ├── ⚙️ ai-assistant.js     # Sage AI response engine
    ├── ⚙️ battles.js          # Battle state machine + AI opponent
    ├── ⚙️ leaderboard.js      # Leaderboard fetching + rendering
    ├── ⚙️ goals.js            # Goal CRUD + progress tracking
    ├── ⚙️ subjects.js         # Curriculum content (chapters, topics)
    ├── ⚙️ dashboard.js        # Dashboard data binding
    └── ⚙️ admin.js            # Admin utilities + analytics
```

---

## 🔧 Firebase Setup

### Step 1 — Create Firebase Project

1. Go to [firebase.google.com](https://firebase.google.com) → **Add Project**
2. Name it `lvlbase` (or anything you like)
3. Enable **Google Analytics** (optional but recommended)

### Step 2 — Enable Services

```
Authentication → Sign-in method → Enable:
  ✅ Email/Password
  ✅ Google

Firestore Database → Create database → Production mode

Storage (optional) → For profile pictures
```

### Step 3 — Configure Your App

```javascript
// js/firebase-config.js — Replace with YOUR config
const firebaseConfig = {
  apiKey: "AIzaSy...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123",
  measurementId: "G-XXXXXXXX"
};
```

### Step 4 — Firestore Security Rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    // Leaderboard is publicly readable
    match /leaderboard/{document=**} {
      allow read: if true;
      allow write: if request.auth != null;
    }
    // Admin-only collections
    match /admin/{document=**} {
      allow read, write: if request.auth != null && 
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }
  }
}
```

### Step 5 — Enable Live Mode

```javascript
// In js/auth.js, change:
const DEMO_MODE = false;  // Switch from demo to Firebase
```

---

## 🎨 Design System

### Color Palette

| Token | Value | Purpose |
|-------|-------|---------|
| `--primary` | `#6C63FF` | Purple — primary actions, links |
| `--secondary` | `#FF6B6B` | Coral — highlights, danger |
| `--accent` | `#FFD700` | Gold — XP, achievements, rank |
| `--success` | `#00D1B2` | Teal — correct answers, progress |
| `--dark-bg` | `#0A0A1A` | Deep navy — page background |
| `--card-bg` | `#1A1A2E` | Dark card surfaces |
| `--text-light` | `#E8E8FF` | Primary text on dark |
| `--text-muted` | `#8892A4` | Secondary text, labels |

### Typography

- **Font:** Poppins (Google Fonts)
- **Weights used:** 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 800 (extrabold), 900 (black)
- **Scale:** 0.75rem → 0.85rem → 0.9rem → 1rem → 1.1rem → 1.3rem → 1.5rem → 2rem → 2.5rem → 3rem → 4rem

### Components

- Glassmorphism cards with `backdrop-filter: blur()`
- CSS-only animations (`fadeIn`, `slideUp`, `float`, `pulse`, `glow`, `bounce`)
- Custom scrollbar (6px, purple)
- Responsive grid system (1/2/3/4/5 columns)
- Mobile hamburger menu
- Toast notification system
- Modal dialogs
- XP progress bars with glow effects
- Rank badges with color-coded gradients
- Guild cards with thematic gradients

---

## 🧠 AI Integration

### Built-in (No API Key Needed)

Sage comes with a built-in knowledge base covering:
- Mathematics (Algebra, Geometry, Trigonometry, Calculus basics)
- Science (Physics, Chemistry, Biology)
- English (Grammar, Vocabulary, Comprehension)

### Gemini AI Integration (Optional)

```javascript
// In js/ai-assistant.js — add your Gemini API key for real AI responses
const GEMINI_API_KEY = "your-key-here";
const GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent";
```

---

## 📱 Pages Reference

| Page | URL | Auth Required | Description |
|------|-----|---------------|-------------|
| Homepage | `/index.html` | No | Marketing + features showcase |
| Login/Signup | `/login.html` | No | 3-step onboarding |
| Dashboard | `/dashboard.html` | Yes | Student command center |
| Subjects | `/subjects.html` | Yes | Subject selection |
| Learn | `/learn.html?subject=math` | Yes | Chapter content |
| Quiz | `/quiz.html` | Yes | Quiz engine |
| Battles | `/battles.html` | Yes | Battle arena |
| Leaderboard | `/leaderboard.html` | No | Global rankings |
| AI Assistant | `/ai-assistant.html` | Yes | Sage AI chat |
| Goals | `/goals.html` | Yes | Goal tracking |
| Parent Portal | `/parent-dashboard.html` | No | Parent view |
| Settings | `/settings.html` | Yes | User preferences |
| Admin | `/admin/index.html` | Admin only | Control panel |

---

## 🛡️ Admin Access

| Detail | Value |
|--------|-------|
| URL | `/admin/index.html` |
| Email | `admin@lvlbase.com` |
| Password | `admin123` |

> ⚠️ **Change the admin password before deploying to production!**

### Admin Panels

1. **📊 Overview** — Platform stats, active users, daily metrics
2. **👥 User Management** — Search, ban, boost, promote users
3. **📚 Content Manager** — Add subjects, chapters, quiz questions
4. **🎮 Gamification HQ** — XP rates, double XP events, badge triggers
5. **🏰 Guild Control** — Guild stats, imbalance detection, auto-balance
6. **📅 Event Creator** — Launch platform-wide challenges and tournaments
7. **🤖 AI Insights** — Automated platform health analysis
8. **📈 Analytics** — Performance charts, engagement heatmaps
9. **🚨 Security** — IP tracking, suspicious activity, cheat detection
10. **📋 Audit Log** — Full history of all admin actions

---

## 🔐 Security Considerations

### Implemented

- ✅ Auth state checks on all protected pages
- ✅ Admin route protection (password + role check)
- ✅ Input sanitization (XSS prevention)
- ✅ Firebase security rules (Firestore)
- ✅ Demo mode isolation (localStorage scoped)
- ✅ Suspicious activity detection flags

### Before Production

- 🔲 Replace demo admin password with strong credentials
- 🔲 Enable Firebase App Check (prevent API abuse)
- 🔲 Set proper Firestore security rules
- 🔲 Enable Firebase Authentication email verification
- 🔲 Configure Content Security Policy headers
- 🔲 Set up rate limiting on Firebase Functions (if using)
- 🔲 Enable Google reCAPTCHA on signup

---

## 🌐 Deployment Guide

### Firebase Hosting (Recommended)

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login and init
firebase login
firebase init hosting

# Deploy
firebase deploy --only hosting
```

### Netlify

1. Push code to GitHub
2. Connect repo in Netlify dashboard
3. Build command: *(leave empty)*
4. Publish directory: `.` (root)
5. Click Deploy

### Vercel

```bash
npm install -g vercel
vercel --prod
```

---

## 📊 Database Schema (Firestore)

```
/users/{uid}
  ├── uid: string
  ├── email: string
  ├── displayName: string
  ├── grade: string (6-12)
  ├── guild: string (shadow/azure/inferno/titan/zenith)
  ├── totalXP: number
  ├── streak: number
  ├── lastLogin: timestamp
  ├── quizzesCompleted: number
  ├── battlesWon: number
  ├── battlesPlayed: number
  ├── achievements: array
  ├── subjectProgress: { math, science, english }
  ├── role: string (student/admin/parent)
  └── joinedAt: timestamp

/leaderboard/individual/{uid}
  ├── displayName: string
  ├── totalXP: number
  ├── rank: string
  ├── guild: string
  └── updatedAt: timestamp

/guilds/{guildId}
  ├── name: string
  ├── totalXP: number
  ├── memberCount: number
  └── weeklyXP: number

/quizResults/{id}
  ├── userId: string
  ├── subject: string
  ├── score: number
  ├── xpEarned: number
  └── completedAt: timestamp

/battles/{id}
  ├── player1: string
  ├── player2: string
  ├── winner: string
  └── completedAt: timestamp

/goals/{id}
  ├── userId: string
  ├── title: string
  ├── current: number
  ├── target: number
  ├── completed: boolean
  └── deadline: timestamp
```

---

## 🗺️ Roadmap

### v1.0 — Current ✅
- [x] Full gamification system
- [x] 5 guilds with bonuses
- [x] Battle arena (Solo + Duel + Guild)
- [x] AI study assistant
- [x] Admin dashboard
- [x] Parent portal
- [x] Dark/light theme
- [x] 45+ quiz questions

### v1.1 — Coming Soon 🚧
- [ ] Real Firebase integration (live data sync)
- [ ] Push notifications (FCM)
- [ ] Voice-based AI tutor (Web Speech API full integration)
- [ ] Homework scanner (camera → AI solve)
- [ ] Teacher mode (upload notes, create classes)
- [ ] Offline mode with Service Worker

### v2.0 — Future Vision 🌟
- [ ] Mobile apps (PWA → React Native)
- [ ] Live guild wars (WebSocket real-time)
- [ ] AI-generated personalized quizzes
- [ ] Virtual science lab simulations
- [ ] International competition mode
- [ ] Certificate generation & sharing
- [ ] School/institution licensing

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | HTML5 + CSS3 | Structure & styling |
| Logic | Vanilla JavaScript (ES Modules) | All interactivity |
| Backend | Firebase Auth + Firestore | Auth, database |
| AI | Built-in KB + Gemini API (optional) | Study assistant |
| Fonts | Google Fonts (Poppins) | Typography |
| Icons | Unicode Emoji | Zero-dependency icons |
| Hosting | Firebase Hosting / Netlify | Deployment |
| Analytics | Firebase Analytics | Usage tracking |

> **Zero external JS frameworks.** No React, no Vue, no Angular — pure vanilla performance.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Areas

- 📝 Add more quiz questions (any subject/grade)
- 🌐 Translations (Hindi, Tamil, Telugu, etc.)
- 🎨 New UI themes and guild skins
- 🤖 Improve AI response quality
- 🐛 Bug fixes and performance improvements
- 📖 Documentation improvements

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 About

**lvlBase** was built with the mission of making education feel as compelling as your favorite game. We believe every student has the potential to reach SS-Rank — they just need the right system.

> *"The students who think they hate studying don't hate learning. They hate boring."*

---

<div align="center">

**⭐ If lvlBase helped you or your students, please give it a star!**

Made with ❤️ for students everywhere 🌍

[🚀 Get Started](#-quick-start) • [📧 Contact](mailto:support@lvlbase.com) • [🐛 Report Bug](../../issues) • [💡 Request Feature](../../issues)

</div>
