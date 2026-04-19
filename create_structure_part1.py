import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

def read_file(path):
    full = os.path.join(BASE, path)
    if not os.path.exists(full):
        return None
    with open(full) as f:
        return f.read()

def copy_and_update(src, dst, depth_prefix):
    content = read_file(src)
    if content is None:
        print(f'  SKIP (src not found): {src}')
        return None
    replacements = [
        ('css/main.css', depth_prefix + 'core/css/base.css'),
        ('css/dashboard.css', depth_prefix + 'core/css/data.css'),
        ('css/battle.css', depth_prefix + 'core/css/gamification.css'),
        ('css/quiz.css', depth_prefix + 'core/css/gamification.css'),
        ('css/admin-bento.css', depth_prefix + 'core/css/bento-grid.css'),
        ('css/admin.css', depth_prefix + 'core/css/data.css'),
        ('js/firebase-config.js', depth_prefix + 'core/js/firebase/init.js'),
        ('js/auth.js', depth_prefix + 'core/js/firebase/auth.js'),
        ('js/firebase-bridge.js', depth_prefix + 'core/js/firebase/firestore.js'),
        ('js/rbac.js', depth_prefix + 'core/js/core/security.js'),
        ('js/gamification.js', depth_prefix + 'core/js/features/gamification.js'),
        ('js/dashboard.js', depth_prefix + 'core/js/core/state.js'),
        ('js/popup.js', depth_prefix + 'core/js/core/ui-components.js'),
        ('js/ai-assistant.js', depth_prefix + 'core/js/features/ai-proctor.js'),
        ('"login.html"', '"' + depth_prefix + 'auth/portal-login.html"'),
        ('"signup.html"', '"' + depth_prefix + 'auth/signup-student.html"'),
        ('"dashboard.html"', '"' + depth_prefix + 'app/student/dashboard.html"'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    write_file(dst, content)
    return content

# ===== CORE CSS =====
auth_css = '''/* ===== AUTH PAGES ===== */
.auth-wrapper { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(ellipse at 30% 40%, rgba(108,99,255,0.15) 0%, transparent 60%), radial-gradient(ellipse at 70% 70%, rgba(255,107,107,0.1) 0%, transparent 60%), var(--dark-bg); padding: 2rem; }
.auth-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2.5rem; width: 100%; max-width: 480px; box-shadow: var(--shadow-heavy); animation: slideUp 0.5s ease; }
.auth-logo { text-align: center; font-size: 2rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.25rem; }
.auth-subtitle { text-align: center; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem; }
.auth-divider { display: flex; align-items: center; gap: 1rem; margin: 1.5rem 0; color: var(--text-muted); font-size: 0.85rem; }
.auth-divider::before, .auth-divider::after { content: ""; flex: 1; height: 1px; background: var(--border-color); }
.role-selector { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.75rem; margin-bottom: 1.5rem; }
.role-card { background: rgba(255,255,255,0.03); border: 2px solid var(--border-color); border-radius: var(--radius); padding: 1rem; text-align: center; cursor: pointer; transition: var(--transition); }
.role-card:hover { border-color: var(--primary); background: rgba(108,99,255,0.08); }
.role-card.selected { border-color: var(--primary); background: rgba(108,99,255,0.15); }
.role-card .role-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
.role-card .role-label { font-size: 0.85rem; font-weight: 600; }
.auth-google-btn { width: 100%; padding: 0.75rem; background: rgba(255,255,255,0.06); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: var(--transition); display: flex; align-items: center; justify-content: center; gap: 0.75rem; }
.auth-google-btn:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.2); }
.auth-footer { text-align: center; margin-top: 1.5rem; font-size: 0.9rem; color: var(--text-muted); }
.auth-footer a { color: var(--primary); font-weight: 600; }
.auth-error { background: rgba(255,68,68,0.1); border: 1px solid rgba(255,68,68,0.3); border-radius: var(--radius); padding: 0.75rem 1rem; font-size: 0.85rem; color: var(--danger); margin-bottom: 1rem; display: none; }
.auth-error.show { display: block; animation: slideUp 0.3s ease; }
.input-group { position: relative; }
.input-icon { position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 1rem; }
.input-group .form-control { padding-left: 2.75rem; }
'''
write_file('core/css/auth.css', auth_css)

# Merge battle.css + quiz.css => gamification.css
battle = read_file('css/battle.css') or ''
quiz = read_file('css/quiz.css') or ''
write_file('core/css/gamification.css', battle + '\n\n' + quiz)

# Merge dashboard.css + admin.css => data.css
dash = read_file('css/dashboard.css') or ''
adm = read_file('css/admin.css') or ''
write_file('core/css/data.css', dash + '\n\n' + adm)

# Themes CSS
themes_css = ''':root {
  --primary: #6C63FF;
  --primary-dark: #5A52E8;
  --secondary: #FF6B6B;
  --accent: #FFD700;
  --success: #00D1B2;
  --warning: #FF9F43;
  --danger: #FF4444;
  --info: #54A0FF;
  --dark-bg: #0A0A1A;
  --card-bg: #1A1A2E;
  --card-hover: #1E1E35;
  --border-color: rgba(108,99,255,0.2);
  --text-light: #E8E8FF;
  --text-muted: #8892A4;
  --radius: 12px;
  --radius-xl: 24px;
  --shadow: 0 4px 20px rgba(0,0,0,0.3);
  --shadow-heavy: 0 8px 40px rgba(0,0,0,0.5);
  --transition: all 0.3s ease;
}
[data-theme="light"] {
  --dark-bg: #F0F0FF;
  --card-bg: #FFFFFF;
  --card-hover: #F8F8FF;
  --border-color: rgba(108,99,255,0.15);
  --text-light: #1A1A2E;
  --text-muted: #666888;
  --shadow: 0 4px 20px rgba(0,0,0,0.1);
  --shadow-heavy: 0 8px 40px rgba(0,0,0,0.2);
}
[data-theme="high-contrast"] {
  --dark-bg: #000000;
  --card-bg: #111111;
  --border-color: rgba(255,255,255,0.4);
  --text-light: #FFFFFF;
  --text-muted: #CCCCCC;
}
'''
write_file('core/css/themes/themes.css', themes_css)

print("CSS files created")
