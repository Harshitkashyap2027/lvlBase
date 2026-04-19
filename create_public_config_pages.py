import os, re

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

def read_file(path):
    try:
        with open(os.path.join(BASE, path)) as f:
            return f.read()
    except:
        return None

def copy_with_path_updates(src, dst, css_depth):
    content = read_file(src)
    if not content:
        return False
    replacements = [
        ('css/main.css', f'{css_depth}core/css/base.css'),
        ('css/dashboard.css', f'{css_depth}core/css/data.css'),
        ('css/battle.css', f'{css_depth}core/css/gamification.css'),
        ('css/quiz.css', f'{css_depth}core/css/gamification.css'),
        ('css/admin-bento.css', f'{css_depth}core/css/bento-grid.css'),
        ('css/admin.css', f'{css_depth}core/css/data.css'),
        ('js/firebase-config.js', f'{css_depth}core/js/firebase/init.js'),
        ('js/auth.js', f'{css_depth}core/js/firebase/auth.js'),
        ('js/firebase-bridge.js', f'{css_depth}core/js/firebase/firestore.js'),
        ('js/rbac.js', f'{css_depth}core/js/core/security.js'),
        ('js/gamification.js', f'{css_depth}core/js/features/gamification.js'),
        ('js/dashboard.js', f'{css_depth}core/js/core/state.js'),
        ('js/popup.js', f'{css_depth}core/js/core/ui-components.js'),
        ('js/ai-assistant.js', f'{css_depth}core/js/features/ai-proctor.js'),
        ('"login.html"', '"../../auth/portal-login.html"'),
        ('"signup.html"', '"../../auth/signup-student.html"'),
        ('"dashboard.html"', '"../../app/student/dashboard.html"'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    write_file(dst, content)
    return True

# Copy existing pages
copy_with_path_updates('index.html', 'public/index.html', '../')
copy_with_path_updates('certificate.html', 'public/verify-certificate.html', '../')
copy_with_path_updates('portal-login.html', 'auth/portal-login.html', '../')
copy_with_path_updates('signup.html', 'auth/signup-student.html', '../')
copy_with_path_updates('school-signup.html', 'auth/school-onboarding.html', '../')
copy_with_path_updates('dashboard.html', 'app/student/dashboard.html', '../../')
copy_with_path_updates('learn.html', 'app/student/quest-map.html', '../../')
copy_with_path_updates('settings.html', 'app/student/profile.html', '../../')
copy_with_path_updates('battles.html', 'app/student/arena/battle-stage.html', '../../../')
copy_with_path_updates('competition.html', 'app/student/arena/tournaments.html', '../../../')
copy_with_path_updates('leaderboard.html', 'app/student/arena/leaderboard.html', '../../../')
copy_with_path_updates('guild-wars.html', 'app/student/guilds/guild-wars.html', '../../../')
copy_with_path_updates('ai-assistant.html', 'app/student/ai/sage-chat.html', '../../../')
copy_with_path_updates('quiz.html', 'app/student/ai/smart-flashcards.html', '../../../')
copy_with_path_updates('homework-scanner.html', 'app/student/ai/notes.html', '../../../')
copy_with_path_updates('science-lab.html', 'app/student/workspace/python-lab.html', '../../../')
copy_with_path_updates('teacher-dashboard.html', 'app/teacher/dashboard.html', '../../')
copy_with_path_updates('teacher-tasks.html', 'app/teacher/assessments/assignments.html', '../../../')
copy_with_path_updates('teacher-tests.html', 'app/teacher/assessments/quiz-builder.html', '../../../')
copy_with_path_updates('school-dashboard.html', 'app/school-admin/dashboard.html', '../../')
copy_with_path_updates('parent-dashboard.html', 'app/parent/dashboard.html', '../../')
copy_with_path_updates('parent-analytics.html', 'app/parent/child-report.html', '../../')
copy_with_path_updates('parent-complaints.html', 'app/parent/teacher-connect.html', '../../')

# Admin super dashboard - try admin/index.html
src = read_file('admin/index.html')
if src:
    for old, new in [('css/main.css','../../core/css/base.css'),('js/firebase-config.js','../../core/js/firebase/init.js'),('js/auth.js','../../core/js/firebase/auth.js')]:
        src = src.replace(old, new)
    write_file('app/super-admin/dashboard.html', src)
else:
    copy_with_path_updates('school-dashboard.html', 'app/super-admin/dashboard.html', '../../')
    print("Used school-dashboard as super-admin dashboard fallback")

# CSS themes file
write_file('core/css/themes/themes.css', '''/* Light Theme */
[data-theme="light"] {
  --primary: #6C63FF;
  --primary-dark: #5A52E8;
  --dark-bg: #F5F5FF;
  --card-bg: #FFFFFF;
  --border-color: rgba(108,99,255,0.2);
  --text-light: #1A1A2E;
  --text-muted: #666688;
}
/* Dark Theme (default) */
[data-theme="dark"], :root {
  --primary: #6C63FF;
  --primary-dark: #5A52E8;
  --secondary: #FF6B6B;
  --accent: #FFD700;
  --success: #00D1B2;
  --warning: #FF9F43;
  --danger: #FF4444;
  --dark-bg: #0A0A1A;
  --card-bg: #1A1A2E;
  --border-color: rgba(108,99,255,0.2);
  --text-light: #E8E8FF;
  --text-muted: #8892A4;
  --radius: 12px;
  --radius-xl: 24px;
  --shadow: 0 4px 20px rgba(0,0,0,0.3);
  --shadow-heavy: 0 8px 40px rgba(0,0,0,0.5);
  --transition: all 0.3s ease;
}
/* High Contrast Theme */
[data-theme="high-contrast"] {
  --primary: #00FF88;
  --dark-bg: #000000;
  --card-bg: #111111;
  --text-light: #FFFFFF;
  --text-muted: #AAAAAA;
  --border-color: rgba(0,255,136,0.3);
}
''')

# JS Core files
write_file('core/js/core/router.js', '''// lvlBase SPA Router
const Router = {
  routes: {},
  currentRoute: null,
  
  register(path, handler, roles = []) {
    this.routes[path] = { handler, roles };
  },
  
  navigate(path, pushState = true) {
    const route = this.routes[path] || this.routes['*'];
    if (!route) return console.warn('No route for:', path);
    
    const user = this.getCurrentUser();
    if (route.roles.length > 0 && user && !route.roles.includes(user.role)) {
      return this.navigate('/auth/blocked.html');
    }
    
    if (pushState) history.pushState({ path }, '', path);
    this.currentRoute = path;
    route.handler(path);
  },
  
  getCurrentUser() {
    try { return JSON.parse(localStorage.getItem('lvlbase_user')); }
    catch { return null; }
  },
  
  init() {
    window.addEventListener('popstate', (e) => {
      if (e.state?.path) this.navigate(e.state.path, false);
    });
    this.navigate(window.location.pathname, false);
  }
};

export default Router;
''')

write_file('core/js/features/bento-drag.js', '''// lvlBase Bento Grid Drag & Drop
const BentoDrag = {
  dragItem: null,
  dragSource: null,
  
  init(containerSelector = '.bento-grid') {
    const grids = document.querySelectorAll(containerSelector);
    grids.forEach(grid => this.initGrid(grid));
  },
  
  initGrid(grid) {
    const items = grid.querySelectorAll('.bento-item');
    items.forEach(item => {
      item.setAttribute('draggable', 'true');
      item.addEventListener('dragstart', (e) => this.onDragStart(e));
      item.addEventListener('dragend', (e) => this.onDragEnd(e));
      item.addEventListener('dragover', (e) => this.onDragOver(e));
      item.addEventListener('drop', (e) => this.onDrop(e));
    });
  },
  
  onDragStart(e) {
    this.dragItem = e.target;
    this.dragSource = e.target.parentNode;
    e.target.style.opacity = '0.4';
    e.dataTransfer.effectAllowed = 'move';
  },
  
  onDragEnd(e) {
    e.target.style.opacity = '1';
    document.querySelectorAll('.bento-item').forEach(i => i.classList.remove('drag-over'));
  },
  
  onDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    e.currentTarget.classList.add('drag-over');
  },
  
  onDrop(e) {
    e.preventDefault();
    if (e.currentTarget !== this.dragItem) {
      const parent = e.currentTarget.parentNode;
      const afterEl = this.getDragAfterElement(parent, e.clientY);
      if (!afterEl) parent.appendChild(this.dragItem);
      else parent.insertBefore(this.dragItem, afterEl);
    }
    this.saveLayout();
  },
  
  getDragAfterElement(container, y) {
    const elements = [...container.querySelectorAll('.bento-item:not(.dragging)')];
    return elements.reduce((closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      return (offset < 0 && offset > closest.offset) ? { offset, element: child } : closest;
    }, { offset: Number.NEGATIVE_INFINITY }).element;
  },
  
  saveLayout() {
    const grid = document.querySelector('.bento-grid');
    if (!grid) return;
    const order = [...grid.children].map(el => el.dataset.id || el.className);
    localStorage.setItem('bento-layout', JSON.stringify(order));
  }
};

export default BentoDrag;
''')

write_file('core/js/features/webrtc.js', '''// lvlBase WebRTC Utilities for Battle & Proctoring
const WebRTCManager = {
  peerConnection: null,
  localStream: null,
  remoteStream: null,
  
  config: {
    iceServers: [
      { urls: 'stun:stun.l.google.com:19302' },
      { urls: 'stun:stun1.l.google.com:19302' }
    ]
  },
  
  async getMedia(video = true, audio = true) {
    try {
      this.localStream = await navigator.mediaDevices.getUserMedia({ video, audio });
      return this.localStream;
    } catch (err) {
      console.error('Media access denied:', err);
      throw err;
    }
  },
  
  async createPeerConnection(onIceCandidate, onTrack) {
    this.peerConnection = new RTCPeerConnection(this.config);
    
    this.peerConnection.onicecandidate = (e) => {
      if (e.candidate) onIceCandidate(e.candidate);
    };
    
    this.peerConnection.ontrack = (e) => {
      this.remoteStream = e.streams[0];
      onTrack(this.remoteStream);
    };
    
    if (this.localStream) {
      this.localStream.getTracks().forEach(track => {
        this.peerConnection.addTrack(track, this.localStream);
      });
    }
    
    return this.peerConnection;
  },
  
  async createOffer() {
    const offer = await this.peerConnection.createOffer();
    await this.peerConnection.setLocalDescription(offer);
    return offer;
  },
  
  async createAnswer(offer) {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await this.peerConnection.createAnswer();
    await this.peerConnection.setLocalDescription(answer);
    return answer;
  },
  
  async addAnswer(answer) {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
  },
  
  addIceCandidate(candidate) {
    this.peerConnection?.addIceCandidate(new RTCIceCandidate(candidate));
  },
  
  disconnect() {
    this.localStream?.getTracks().forEach(t => t.stop());
    this.peerConnection?.close();
    this.peerConnection = null;
    this.localStream = null;
    this.remoteStream = null;
  }
};

export default WebRTCManager;
''')

# Config files
write_file('config/.env.example', '''FIREBASE_API_KEY=your_api_key_here
FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
FIREBASE_DATABASE_URL=https://your_project-default-rtdb.region.firebasedatabase.app
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_project.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id
FIREBASE_MEASUREMENT_ID=G-XXXXXXXXXX
FCM_VAPID_KEY=your_vapid_key_here
''')

write_file('config/firebase.json', '''{
  "hosting": {
    "public": "public",
    "rewrites": [
      { "source": "/app/**", "destination": "/app/student/dashboard.html" },
      { "source": "/auth/**", "destination": "/auth/portal-login.html" }
    ],
    "headers": [
      {
        "source": "**/*.@(js|css)",
        "headers": [{ "key": "Cache-Control", "value": "max-age=31536000" }]
      }
    ],
    "cleanUrls": true,
    "trailingSlash": false
  },
  "firestore": {
    "rules": "config/firestore.rules",
    "indexes": "config/firestore.indexes.json"
  },
  "storage": {
    "rules": "config/storage.rules"
  }
}
''')

write_file('config/storage.rules', '''rules_version = \'2\';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
    match /schools/{schoolId}/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && 
        (request.auth.token.role == \'admin\' || 
         request.auth.token.schoolId == schoolId);
    }
    match /public/{allPaths=**} {
      allow read;
      allow write: if request.auth != null && request.auth.token.role == \'super_admin\';
    }
  }
}
''')

write_file('config/vercel.json', '''{
  "rewrites": [
    { "source": "/app/student/:path*", "destination": "/app/student/dashboard.html" },
    { "source": "/auth/:path*", "destination": "/auth/portal-login.html" },
    { "source": "/", "destination": "/public/index.html" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
''')

write_file('config/package.json', '''{
  "name": "lvlbase",
  "version": "2.0.0",
  "description": "The Ultimate Gamified Learning Platform for Schools",
  "scripts": {
    "dev": "npx live-server --port=3000 --host=localhost",
    "build": "node scripts/build.js",
    "lint": "npx eslint core/js/**/*.js",
    "deploy": "firebase deploy"
  },
  "keywords": ["education", "gamification", "learning", "school", "edtech"],
  "license": "MIT",
  "dependencies": {
    "firebase": "^10.7.1"
  },
  "devDependencies": {
    "eslint": "^8.56.0",
    "live-server": "^1.2.2"
  }
}
''')

write_file('config/.gitignore', '''# Dependencies
node_modules/
.npm

# Environment
.env
.env.local
.env.*.local

# Build outputs
dist/
build/

# Firebase
.firebase/
firebase-debug.log
firestore-debug.log

# OS
.DS_Store
Thumbs.db
desktop.ini

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
logs/
*.log
npm-debug.log*

# Testing
coverage/
.nyc_output/

# Misc
*.tmp
*.temp
.cache/
''')

# PWA manifests
write_file('pwa/manifest-student.json', '''{
  "name": "lvlBase Student",
  "short_name": "lvlBase",
  "description": "Your gamified learning adventure",
  "start_url": "/app/student/dashboard.html",
  "scope": "/app/student/",
  "display": "standalone",
  "background_color": "#0A0A1A",
  "theme_color": "#6C63FF",
  "orientation": "portrait-primary",
  "icons": [
    { "src": "/assets/icons/icon-72.png", "sizes": "72x72", "type": "image/png" },
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "shortcuts": [
    { "name": "My Dashboard", "url": "/app/student/dashboard.html", "description": "View your dashboard" },
    { "name": "Battle Arena", "url": "/app/student/arena/battle-stage.html", "description": "Enter the arena" },
    { "name": "AI Sage", "url": "/app/student/ai/sage-chat.html", "description": "Chat with AI" }
  ],
  "categories": ["education", "games"]
}
''')

write_file('pwa/manifest-teacher.json', '''{
  "name": "lvlBase Teacher",
  "short_name": "lvlBase T",
  "description": "Manage your classes and track student progress",
  "start_url": "/app/teacher/dashboard.html",
  "scope": "/app/teacher/",
  "display": "standalone",
  "background_color": "#0A0A1A",
  "theme_color": "#00D1B2",
  "icons": [
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "categories": ["education", "productivity"]
}
''')

write_file('pwa/manifest-parent.json', '''{
  "name": "lvlBase Parent",
  "short_name": "lvlBase P",
  "description": "Monitor your child\'s learning progress",
  "start_url": "/app/parent/dashboard.html",
  "scope": "/app/parent/",
  "display": "standalone",
  "background_color": "#0A0A1A",
  "theme_color": "#FF9F43",
  "icons": [
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "categories": ["education"]
}
''')

write_file('pwa/manifest-admin.json', '''{
  "name": "lvlBase Admin",
  "short_name": "lvlBase A",
  "description": "School administration and analytics",
  "start_url": "/app/school-admin/dashboard.html",
  "scope": "/app/",
  "display": "standalone",
  "background_color": "#0A0A1A",
  "theme_color": "#FFD700",
  "icons": [
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "categories": ["education", "productivity"]
}
''')

print("Config and JS files created")
