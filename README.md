# lvlBase ⚡ – Educational Gaming Platform

> Transform studying into an epic adventure. Earn XP, rank up, join guilds, and battle classmates!

## 🚀 Quick Start

1. Open `index.html` in a browser (or serve via HTTP)
2. Click "Get Started Free" to create a demo account
3. Use email: `admin@lvlbase.com`, password: `admin123` for admin panel

## 📁 Project Structure

```
lvlBase/
├── index.html          # Landing/marketing page
├── login.html          # Login + 3-step onboarding
├── dashboard.html      # Student dashboard
├── subjects.html       # Subject selection
├── learn.html          # Chapter learning page
├── quiz.html           # Quiz engine
├── battles.html        # Battle arena
├── leaderboard.html    # Rankings
├── ai-assistant.html   # Sage AI tutor
├── goals.html          # Goal tracking
├── parent-dashboard.html # Parent monitoring
├── settings.html       # User settings
├── admin/
│   └── index.html      # Admin control panel
├── css/
│   ├── main.css        # Global styles + variables
│   ├── dashboard.css   # Dashboard + sidebar styles
│   ├── quiz.css        # Quiz interface styles
│   ├── battle.css      # Battle arena styles
│   └── admin.css       # Admin panel styles
└── js/
    ├── firebase-config.js  # Firebase setup (configure before use)
    ├── auth.js             # Authentication (demo mode / Firebase)
    ├── gamification.js     # XP, Ranks, Guilds, Achievements
    ├── quiz.js             # Quiz engine + question bank
    ├── ai-assistant.js     # Sage AI tutor responses
    ├── battles.js          # Battle state machine
    ├── leaderboard.js      # Leaderboard data
    ├── goals.js            # Goal management
    ├── subjects.js         # Subject/chapter content
    ├── dashboard.js        # Dashboard data rendering
    └── admin.js            # Admin utilities
```

## 🎨 Design System

| Variable | Value | Use |
|----------|-------|-----|
| `--primary` | #6C63FF | Main purple |
| `--secondary` | #FF6B6B | Coral/red accents |
| `--accent` | #FFD700 | Gold (XP, achievements) |
| `--success` | #00D1B2 | Teal (correct, progress) |
| `--dark-bg` | #0A0A1A | Page background |
| `--card-bg` | #1A1A2E | Card background |

## 🏆 Ranking System

| Rank | XP Required | Color |
|------|-------------|-------|
| E-Rank | 0 | Grey |
| D-Rank | 500 | Green |
| C-Rank | 1,500 | Blue |
| B-Rank | 3,500 | Purple |
| A-Rank | 7,000 | Gold |
| S-Rank | 15,000 | Red |
| SS-Rank | 30,000 | Gold ⭐ |

## 🏰 Guild Bonuses

| Guild | Bonus |
|-------|-------|
| 🌙 Shadow Guild | +15% Math XP |
| 💧 Azure Order | +15% Science XP |
| 🔥 Inferno Legion | +20% Battle XP |
| ⚡ Titan Brotherhood | +15% English XP |
| ✨ Zenith Circle | +10% All XP |

## 🔧 Firebase Setup

1. Create project at [firebase.google.com](https://firebase.google.com)
2. Enable **Authentication** (Email/Password + Google)
3. Enable **Firestore Database**
4. Copy config to `js/firebase-config.js`
5. Set `DEMO_MODE = false` in `js/auth.js`

## 📱 Features

- ✅ **Quiz Engine** – 45+ questions (Math, Science, English)
- ✅ **Battle Arena** – AI opponents with health bars
- ✅ **Sage AI Tutor** – 24/7 study assistant
- ✅ **Live Leaderboard** – Individual, Guild, National
- ✅ **Goal Tracking** – Set and track learning goals
- ✅ **Parent Dashboard** – Monitor child's progress
- ✅ **Admin Panel** – Full control center
- ✅ **Dark/Light Mode** – Theme toggle
- ✅ **Responsive Design** – Mobile-first
- ✅ **XP & Streak System** – Gamified motivation
- ✅ **Achievement Badges** – 20+ unlockable badges
- ✅ **Demo Mode** – Works without Firebase

## 🛠 Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES Modules)
- **Backend:** Firebase (Auth + Firestore) or localStorage demo mode
- **Fonts:** Google Fonts (Poppins)
- **Icons:** Unicode emoji (no dependencies!)
- **No frameworks, no build tools** – runs directly in browser

## 📝 Admin Access

- URL: `/admin/index.html`
- Email: `admin@lvlbase.com`
- Password: `admin123`

---

*Built with ❤️ for Indian students – Made in India 🇮🇳*
