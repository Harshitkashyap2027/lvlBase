import os, json

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

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

firebase_json = {
  "hosting": {
    "public": ".",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**", "config/**"],
    "rewrites": [{"source": "**", "destination": "/index.html"}],
    "headers": [{"source": "**/*.@(js|css)", "headers": [{"key": "Cache-Control", "value": "max-age=31536000"}]}]
  }
}
write_file('config/firebase.json', json.dumps(firebase_json, indent=2))

write_file('config/storage.rules', '''rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
    match /schools/{schoolId}/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && 
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.schoolId == schoolId;
    }
    match /public/{allPaths=**} {
      allow read: if true;
      allow write: if request.auth != null && 
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role in ["admin", "super_admin"];
    }
  }
}
''')

vercel_json = {
  "rewrites": [
    {"source": "/app/(.*)", "destination": "/app/$1"},
    {"source": "/auth/(.*)", "destination": "/auth/$1"},
    {"source": "/public/(.*)", "destination": "/public/$1"},
    {"source": "/(.*)", "destination": "/public/index.html"}
  ],
  "headers": [
    {"source": "/(.*)", "headers": [
      {"key": "X-Content-Type-Options", "value": "nosniff"},
      {"key": "X-Frame-Options", "value": "DENY"},
      {"key": "X-XSS-Protection", "value": "1; mode=block"}
    ]}
  ]
}
write_file('config/vercel.json', json.dumps(vercel_json, indent=2))

pkg_json = {
  "name": "lvlbase",
  "version": "2.0.0",
  "description": "lvlBase - Gamified Learning Platform",
  "main": "index.html",
  "scripts": {
    "dev": "npx serve . -p 3000",
    "lint": "npx eslint js/ core/js/",
    "deploy": "firebase deploy"
  },
  "keywords": ["education", "gamification", "learning", "firebase"],
  "author": "lvlBase Team",
  "license": "MIT",
  "devDependencies": {
    "firebase-tools": "^13.0.0"
  }
}
write_file('config/package.json', json.dumps(pkg_json, indent=2))

write_file('config/.gitignore', '''.env
.env.local
node_modules/
.firebase/
dist/
*.log
.DS_Store
Thumbs.db
''')

# PWA Manifests
def pwa_manifest(name, short_name, start_url, bg_color, theme_color, description):
    return json.dumps({
      "name": name,
      "short_name": short_name,
      "description": description,
      "start_url": start_url,
      "display": "standalone",
      "background_color": bg_color,
      "theme_color": theme_color,
      "orientation": "any",
      "icons": [
        {"src": "../assets/icons/icon-72.png", "sizes": "72x72", "type": "image/png"},
        {"src": "../assets/icons/icon-96.png", "sizes": "96x96", "type": "image/png"},
        {"src": "../assets/icons/icon-128.png", "sizes": "128x128", "type": "image/png"},
        {"src": "../assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "../assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}
      ],
      "categories": ["education", "productivity"]
    }, indent=2)

write_file('pwa/manifest-student.json', pwa_manifest(
  "lvlBase Student", "lvlBase", "/app/student/dashboard.html",
  "#0A0A1A", "#6C63FF", "Level up your learning journey"))
write_file('pwa/manifest-teacher.json', pwa_manifest(
  "lvlBase Teacher", "lvlBase Pro", "/app/teacher/dashboard.html",
  "#0A0A1A", "#00D1B2", "Empower your classroom with gamification"))
write_file('pwa/manifest-parent.json', pwa_manifest(
  "lvlBase Parent", "lvlBase", "/app/parent/dashboard.html",
  "#0A0A1A", "#FF6B6B", "Track your child's learning progress"))
write_file('pwa/manifest-admin.json', pwa_manifest(
  "lvlBase Admin", "lvlBase Ctrl", "/app/school-admin/dashboard.html",
  "#0A0A1A", "#FFD700", "School administration dashboard"))

print("Config and PWA files created")
