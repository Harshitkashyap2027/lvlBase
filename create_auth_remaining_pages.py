import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

STYLES = ''':root { --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B; --accent: #FFD700; --success: #00D1B2; --warning: #FF9F43; --danger: #FF4444; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px; --shadow: 0 4px 20px rgba(0,0,0,0.3); --transition: all 0.3s ease; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); min-height: 100vh; }
.auth-wrapper { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(ellipse at 30% 40%, rgba(108,99,255,0.15) 0%, transparent 60%), radial-gradient(ellipse at 70% 70%, rgba(255,107,107,0.1) 0%, transparent 60%), var(--dark-bg); padding: 2rem; }
.auth-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2.5rem; width: 100%; max-width: 480px; box-shadow: 0 8px 40px rgba(0,0,0,0.5); animation: slideUp 0.5s ease; }
.auth-logo { text-align: center; font-size: 2rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.25rem; }
.auth-subtitle { text-align: center; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem; }
.form-group { margin-bottom: 1.25rem; }
.form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
.form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; }
.form-control:focus { outline: none; border-color: var(--primary); }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(108,99,255,0.4); }
.btn-ghost { background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }
.auth-footer { text-align: center; margin-top: 1.5rem; font-size: 0.9rem; color: var(--text-muted); }
.auth-footer a { color: var(--primary); font-weight: 600; }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }'''

def auth_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<div class="auth-wrapper">
{body}
</div>
</body>
</html>'''

write_file('auth/signup-teacher.html', auth_page('Teacher Signup', '''
<div class="auth-card">
  <div class="auth-logo">lvlBase ⚡</div>
  <p class="auth-subtitle">Join as a Teacher 🍎</p>
  <div class="form-group"><label class="form-label">Full Name</label><input class="form-control" type="text" placeholder="Your full name"></div>
  <div class="form-group"><label class="form-label">School Email</label><input class="form-control" type="email" placeholder="you@school.edu"></div>
  <div class="form-group"><label class="form-label">Subject(s)</label><input class="form-control" type="text" placeholder="e.g., Mathematics, Science"></div>
  <div class="form-group"><label class="form-label">School Name</label><input class="form-control" type="text" placeholder="Riverside Academy"></div>
  <div class="form-group"><label class="form-label">Password</label><input class="form-control" type="password" placeholder="Create a strong password"></div>
  <button class="btn btn-primary" style="margin-top:0.5rem;">Create Teacher Account 🚀</button>
  <div style="text-align:center;margin:1.5rem 0;color:var(--text-muted);">— or —</div>
  <button class="btn btn-ghost">🔵 Sign up with Google Workspace</button>
  <div class="auth-footer">Already have an account? <a href="portal-login.html">Sign in →</a></div>
</div>
'''))

write_file('auth/invite-claim.html', auth_page('Claim Invite', '''
<div class="auth-card">
  <div class="auth-logo">lvlBase ⚡</div>
  <p class="auth-subtitle">You\'ve been invited to join! 🎉</p>
  <div style="background:rgba(0,209,178,0.1);border:1px solid rgba(0,209,178,0.3);border-radius:var(--radius);padding:1rem;margin-bottom:1.5rem;text-align:center;">
    <div style="font-weight:700;color:var(--success);">Riverside Academy</div>
    <div style="font-size:0.85rem;color:var(--text-muted);">invited you as Student · Grade 10A</div>
  </div>
  <div class="form-group"><label class="form-label">Your Name</label><input class="form-control" type="text" placeholder="Your full name"></div>
  <div class="form-group"><label class="form-label">Create Password</label><input class="form-control" type="password" placeholder="At least 8 characters"></div>
  <button class="btn btn-primary">Claim Invite & Enter ⚡</button>
  <div class="auth-footer">Wrong invite? <a href="portal-login.html">Login instead</a></div>
</div>
'''))

write_file('auth/magic-link.html', auth_page('Magic Link', '''
<div class="auth-card">
  <div style="text-align:center;font-size:4rem;margin-bottom:1rem;">✨</div>
  <div class="auth-logo">Magic Link Login</div>
  <p class="auth-subtitle">We\'ll email you a one-click login link — no password needed!</p>
  <div class="form-group"><label class="form-label">Your Email</label><input class="form-control" type="email" placeholder="you@school.edu"></div>
  <button class="btn btn-primary">Send Magic Link ✉️</button>
  <div style="margin-top:1.5rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);padding:1rem;text-align:center;display:none;" id="sent-msg">
    <div style="font-size:1.5rem;margin-bottom:0.5rem;">📬</div>
    <div style="font-weight:600;margin-bottom:0.25rem;">Check your inbox!</div>
    <div style="font-size:0.85rem;color:var(--text-muted);">Link expires in 15 minutes</div>
  </div>
  <div class="auth-footer"><a href="portal-login.html">← Back to Login</a></div>
</div>
'''))

write_file('auth/sso-gateway.html', auth_page('SSO Gateway', '''
<div class="auth-card">
  <div class="auth-logo">lvlBase ⚡</div>
  <p class="auth-subtitle">Single Sign-On Gateway</p>
  <div class="form-group"><label class="form-label">School Domain or Email</label><input class="form-control" type="text" placeholder="school.edu or your email"></div>
  <button class="btn btn-primary" style="margin-bottom:1rem;">Continue with SSO →</button>
  <div style="border-top:1px solid var(--border-color);padding-top:1.5rem;">
    <p style="color:var(--text-muted);font-size:0.85rem;text-align:center;margin-bottom:1rem;">Or sign in with:</p>
    <button class="btn btn-ghost" style="margin-bottom:0.75rem;">🔵 Google Workspace</button>
    <button class="btn btn-ghost">🟦 Microsoft 365</button>
  </div>
  <div class="auth-footer"><a href="portal-login.html">← Regular Login</a></div>
</div>
'''))

write_file('auth/2fa-setup.html', auth_page('2FA Setup', '''
<div class="auth-card">
  <div style="text-align:center;font-size:3rem;margin-bottom:0.75rem;">🔐</div>
  <div class="auth-logo">Two-Factor Authentication</div>
  <p class="auth-subtitle">Add an extra layer of security to your account</p>
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;">
    <div style="flex:1;background:rgba(108,99,255,0.15);border:2px solid var(--primary);border-radius:var(--radius);padding:1rem;text-align:center;cursor:pointer;"><div style="font-size:1.5rem;margin-bottom:0.5rem;">📱</div><div style="font-size:0.85rem;font-weight:600;">Authenticator App</div><div style="font-size:0.75rem;color:var(--text-muted);">Recommended</div></div>
    <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem;text-align:center;cursor:pointer;"><div style="font-size:1.5rem;margin-bottom:0.5rem;">📧</div><div style="font-size:0.85rem;font-weight:600;">Email Code</div><div style="font-size:0.75rem;color:var(--text-muted);">Less secure</div></div>
  </div>
  <div style="background:rgba(255,255,255,0.04);border-radius:var(--radius);padding:1.5rem;text-align:center;margin-bottom:1.5rem;">
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:0.75rem;">Scan with your authenticator app:</div>
    <div style="width:120px;height:120px;background:white;border-radius:8px;margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:0.7rem;color:#333;">QR Code Here</div>
    <div style="margin-top:0.75rem;font-size:0.75rem;color:var(--text-muted);">Or enter code: LVLB-2FA5-XKCD</div>
  </div>
  <div class="form-group"><label class="form-label">Enter 6-Digit Code to Verify</label><input class="form-control" type="text" placeholder="000000" style="letter-spacing:0.5em;text-align:center;font-size:1.2rem;"></div>
  <button class="btn btn-primary">Enable 2FA 🔐</button>
</div>
'''))

write_file('auth/biometric-auth.html', auth_page('Biometric Auth', '''
<div class="auth-card">
  <div style="text-align:center;font-size:4rem;margin-bottom:0.75rem;">🔏</div>
  <div class="auth-logo">Biometric Login</div>
  <p class="auth-subtitle">Use your fingerprint or face to sign in instantly</p>
  <div style="text-align:center;padding:2rem 0;">
    <div style="width:100px;height:100px;border-radius:50%;background:rgba(108,99,255,0.2);border:2px solid var(--primary);display:inline-flex;align-items:center;justify-content:center;font-size:3rem;cursor:pointer;transition:var(--transition);margin-bottom:1rem;animation:pulse 2s infinite;">👆</div>
    <p style="color:var(--text-muted);font-size:0.9rem;">Touch the sensor or look at your camera</p>
  </div>
  <div class="auth-footer"><a href="portal-login.html">← Use password instead</a></div>
</div>
<style>@keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(108,99,255,0.4); } 50% { box-shadow: 0 0 0 20px rgba(108,99,255,0); } }</style>
'''))

write_file('auth/reset-password.html', auth_page('Reset Password', '''
<div class="auth-card">
  <div class="auth-logo">lvlBase ⚡</div>
  <p class="auth-subtitle">Create a New Password 🔑</p>
  <div class="form-group"><label class="form-label">New Password</label><input class="form-control" type="password" placeholder="At least 8 characters"></div>
  <div class="form-group"><label class="form-label">Confirm New Password</label><input class="form-control" type="password" placeholder="Repeat your password"></div>
  <div style="background:rgba(255,255,255,0.04);border-radius:var(--radius);padding:0.75rem;margin-bottom:1.25rem;font-size:0.8rem;color:var(--text-muted);">
    <div id="p1">• At least 8 characters</div>
    <div id="p2">• Contains a number</div>
    <div id="p3">• Contains an uppercase letter</div>
  </div>
  <button class="btn btn-primary">Update Password 🔐</button>
  <div class="auth-footer"><a href="portal-login.html">← Back to Login</a></div>
</div>
'''))

write_file('auth/forgot-password.html', auth_page('Forgot Password', '''
<div class="auth-card">
  <div style="text-align:center;font-size:3rem;margin-bottom:0.75rem;">🤔</div>
  <div class="auth-logo">Forgot Password?</div>
  <p class="auth-subtitle">No worries! Enter your email and we\'ll send a reset link.</p>
  <div class="form-group"><label class="form-label">Your Email</label><input class="form-control" type="email" placeholder="you@school.edu"></div>
  <button class="btn btn-primary">Send Reset Link 📧</button>
  <div class="auth-footer"><a href="portal-login.html">← Back to Login</a></div>
</div>
'''))

write_file('auth/blocked.html', auth_page('Account Blocked', '''
<div class="auth-card">
  <div style="text-align:center;font-size:4rem;margin-bottom:0.75rem;">🚫</div>
  <div class="auth-logo" style="background:linear-gradient(135deg,var(--danger),var(--secondary));">Account Blocked</div>
  <div style="background:rgba(255,68,68,0.1);border:1px solid rgba(255,68,68,0.3);border-radius:var(--radius);padding:1rem;margin:1.5rem 0;text-align:center;">
    <p style="color:var(--danger);font-weight:600;margin-bottom:0.25rem;">Access Suspended</p>
    <p style="color:var(--text-muted);font-size:0.85rem;">Your account has been temporarily blocked due to a policy violation or suspicious activity.</p>
  </div>
  <div class="form-group"><label class="form-label">Reason</label><textarea class="form-control" rows="3" style="height:80px;resize:none;" placeholder="Explain your situation to an admin..."></textarea></div>
  <button class="btn btn-primary" style="background:linear-gradient(135deg,var(--warning),var(--accent));color:#000;">Appeal Suspension</button>
  <div class="auth-footer"><a href="portal-login.html">← Login Page</a></div>
</div>
'''))

write_file('auth/session-expired.html', auth_page('Session Expired', '''
<div class="auth-card">
  <div style="text-align:center;font-size:4rem;margin-bottom:0.75rem;">⏰</div>
  <div class="auth-logo">Session Expired</div>
  <p class="auth-subtitle">Your session has timed out for security reasons</p>
  <div style="background:rgba(255,159,67,0.1);border:1px solid rgba(255,159,67,0.3);border-radius:var(--radius);padding:1rem;margin:1.5rem 0;text-align:center;font-size:0.85rem;color:var(--text-muted);">
    Don\'t worry — your progress was auto-saved! You\'ll be right back where you left off.
  </div>
  <a href="portal-login.html" class="btn btn-primary">🔑 Login Again</a>
  <div class="auth-footer" style="margin-top:1rem;">Need help? <a href="../public/contact.html">Contact Support</a></div>
</div>
'''))

print("Auth pages created")

# Remaining student pages
STUDENT_STYLES = ''':root { --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B; --accent: #FFD700; --success: #00D1B2; --warning: #FF9F43; --danger: #FF4444; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px; --shadow: 0 4px 20px rgba(0,0,0,0.3); --transition: all 0.3s ease; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
.navbar { position: fixed; top: 0; left: 0; right: 0; height: 65px; background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; }
.navbar-brand { font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.navbar-nav { display: flex; gap: 0.5rem; }
.nav-link { padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }
.nav-link:hover, .nav-link.active { color: var(--text-light); background: rgba(108,99,255,0.15); }
.navbar-actions { display: flex; align-items: center; gap: 1rem; }
.badge { padding: 0.3rem 0.75rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; background: rgba(108,99,255,0.2); color: var(--primary); }
.avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--success), #00A896); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; cursor: pointer; }
.page-wrapper { padding-top: 65px; min-height: 100vh; }
.container { max-width: 1280px; margin: 0 auto; padding: 2rem; }
.card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.5rem; transition: var(--transition); }
.card:hover { border-color: rgba(108,99,255,0.4); box-shadow: var(--shadow); }
.grid-2 { display: grid; grid-template-columns: repeat(2,1fr); gap: 1.5rem; }
.grid-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.5rem; }
.grid-4 { display: grid; grid-template-columns: repeat(4,1fr); gap: 1.5rem; }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(108,99,255,0.4); }
.btn-ghost { background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }
.page-title { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.25rem; }
.page-subtitle { color: var(--text-muted); font-size: 0.95rem; }
.page-header { margin-bottom: 2rem; }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def student_page(title, body, depth='../../'):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{depth}core/css/base.css">
  <style>{STUDENT_STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="{depth}app/student/dashboard.html" class="nav-link">🏠 Home</a>
    <a href="{depth}app/student/quest-map.html" class="nav-link">📚 Learn</a>
    <a href="{depth}app/student/arena/battle-stage.html" class="nav-link">⚔️ Arena</a>
    <a href="{depth}app/student/guilds/guild-dashboard.html" class="nav-link">🏰 Guild</a>
    <a href="{depth}app/student/ai/sage-chat.html" class="nav-link">🤖 AI Sage</a>
  </div>
  <div class="navbar-actions">
    <span class="badge">⚡ 12,450 XP</span>
    <div class="avatar">A</div>
  </div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

write_file('app/student/backpack.html', student_page('Backpack', '''
<div class="page-header"><h1 class="page-title">🎒 My Backpack</h1><p class="page-subtitle">Your collected items, badges, and power-ups</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Badges</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">47</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Power-Ups</div><div style="font-size:2rem;font-weight:900;color:var(--success);">12</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">XP Boosters</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">3</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Guild Coins</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">240</div></div>
</div>
<div class="card" style="margin-bottom:2rem;">
  <h3 style="margin-bottom:1.5rem;font-size:1rem;">🏆 Recent Badges</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:1rem;">
    <div style="text-align:center;padding:1rem;background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.3);border-radius:var(--radius);cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.5rem;">🌟</div><div style="font-size:0.75rem;font-weight:600;">First Victory</div></div>
    <div style="text-align:center;padding:1rem;background:rgba(255,107,107,0.1);border:1px solid rgba(255,107,107,0.3);border-radius:var(--radius);cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.5rem;">🔥</div><div style="font-size:0.75rem;font-weight:600;">7-Day Streak</div></div>
    <div style="text-align:center;padding:1rem;background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:var(--radius);cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.5rem;">⚔️</div><div style="font-size:0.75rem;font-weight:600;">Battle Master</div></div>
    <div style="text-align:center;padding:1rem;background:rgba(0,209,178,0.1);border:1px solid rgba(0,209,178,0.3);border-radius:var(--radius);cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.5rem;">🎯</div><div style="font-size:0.75rem;font-weight:600;">Perfect Score</div></div>
    <div style="text-align:center;padding:1rem;background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.3);border-radius:var(--radius);cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.5rem;">👑</div><div style="font-size:0.75rem;font-weight:600;">Rank S</div></div>
    <div style="text-align:center;padding:1rem;background:rgba(255,255,255,0.04);border:1px dashed var(--border-color);border-radius:var(--radius);"><div style="font-size:2.5rem;margin-bottom:0.5rem;opacity:0.3;">🔒</div><div style="font-size:0.75rem;font-weight:600;color:var(--text-muted);">Locked</div></div>
  </div>
</div>
'''))

write_file('app/student/analytics.html', student_page('My Analytics', '''
<div class="page-header"><h1 class="page-title">📊 My Analytics</h1><p class="page-subtitle">Track your learning journey and XP growth</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total XP</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">12,450</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Current Rank</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">A</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Battles Won</div><div style="font-size:2rem;font-weight:900;color:var(--success);">48</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Study Streak</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">🔥 7</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">📈 XP Over Time (Last 7 Days)</h3>
    <div style="display:flex;align-items:flex-end;gap:0.5rem;height:120px;">
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.4);border-radius:4px 4px 0 0;width:100%;height:40%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Mon</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.5);border-radius:4px 4px 0 0;width:100%;height:65%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Tue</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.6);border-radius:4px 4px 0 0;width:100%;height:50%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Wed</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.7);border-radius:4px 4px 0 0;width:100%;height:80%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Thu</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.6);border-radius:4px 4px 0 0;width:100%;height:55%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Fri</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:rgba(108,99,255,0.8);border-radius:4px 4px 0 0;width:100%;height:90%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Sat</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.4rem;"><div style="background:var(--primary);border-radius:4px 4px 0 0;width:100%;height:100%;"></div><div style="font-size:0.65rem;color:var(--text-muted);">Sun</div></div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">🎯 Strength by Subject</h3>
    <div>
      <div style="margin-bottom:0.75rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>Mathematics</span><span style="color:var(--success);">92%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--success);border-radius:20px;width:92%;height:100%;"></div></div></div>
      <div style="margin-bottom:0.75rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>Science</span><span style="color:var(--primary);">78%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--primary);border-radius:20px;width:78%;height:100%;"></div></div></div>
      <div style="margin-bottom:0.75rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>English</span><span style="color:var(--warning);">65%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--warning);border-radius:20px;width:65%;height:100%;"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>History</span><span style="color:var(--success);">88%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--success);border-radius:20px;width:88%;height:100%;"></div></div></div>
    </div>
  </div>
</div>
'''))

write_file('app/student/support-desk.html', student_page('Support', '''
<div class="page-header"><h1 class="page-title">🎧 Support Desk</h1><p class="page-subtitle">Get help with any lvlBase issue</p></div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="cursor:pointer;text-align:center;padding:2rem;"><div style="font-size:3rem;margin-bottom:1rem;">💬</div><h3 style="margin-bottom:0.5rem;">Live Chat</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Chat with our support team</p><button class="btn btn-primary" style="font-size:0.85rem;">Start Chat</button></div>
  <div class="card" style="cursor:pointer;text-align:center;padding:2rem;"><div style="font-size:3rem;margin-bottom:1rem;">📧</div><h3 style="margin-bottom:0.5rem;">Submit Ticket</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Get a response within 24h</p><button class="btn btn-ghost" style="font-size:0.85rem;">New Ticket</button></div>
  <div class="card" style="cursor:pointer;text-align:center;padding:2rem;"><div style="font-size:3rem;margin-bottom:1rem;">📚</div><h3 style="margin-bottom:0.5rem;">Help Center</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Browse tutorials and guides</p><button class="btn btn-ghost" style="font-size:0.85rem;">Browse FAQs</button></div>
</div>
'''))

write_file('app/student/focus-mode.html', student_page('Focus Mode', '''
<div style="text-align:center;padding:3rem 0;">
  <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.1em;">Focus Session</div>
  <div id="timer" style="font-size:8rem;font-weight:900;line-height:1;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:1rem;">25:00</div>
  <div style="font-size:1rem;color:var(--text-muted);margin-bottom:3rem;">Pomodoro Mode 🍅</div>
  <div style="display:flex;justify-content:center;gap:1rem;margin-bottom:3rem;">
    <button id="startBtn" onclick="toggleTimer()" class="btn btn-primary" style="font-size:1.1rem;padding:1rem 3rem;">▶ Start Focus</button>
    <button onclick="resetTimer()" class="btn btn-ghost" style="font-size:1.1rem;padding:1rem 2rem;">↺ Reset</button>
  </div>
  <div class="grid-3" style="max-width:600px;margin:0 auto 2rem;">
    <div style="background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:var(--radius);padding:1rem;text-align:center;cursor:pointer;" onclick="setMode(25,'🍅 Pomodoro')"><div style="font-weight:700;margin-bottom:0.25rem;">25 min</div><div style="font-size:0.8rem;color:var(--text-muted);">🍅 Pomodoro</div></div>
    <div style="background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem;text-align:center;cursor:pointer;" onclick="setMode(5,'☕ Short Break')"><div style="font-weight:700;margin-bottom:0.25rem;">5 min</div><div style="font-size:0.8rem;color:var(--text-muted);">☕ Short Break</div></div>
    <div style="background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem;text-align:center;cursor:pointer;" onclick="setMode(15,'🌿 Long Break')"><div style="font-weight:700;margin-bottom:0.25rem;">15 min</div><div style="font-size:0.8rem;color:var(--text-muted);">🌿 Long Break</div></div>
  </div>
</div>
<script>
let mins = 25, secs = 0, running = false, interval;
function setMode(m, label) { clearInterval(interval); running = false; mins = m; secs = 0; document.getElementById('timer').textContent = String(m).padStart(2,'0')+':00'; document.getElementById('startBtn').textContent = '▶ Start Focus'; }
function toggleTimer() {
  if (running) { clearInterval(interval); running = false; document.getElementById('startBtn').textContent = '▶ Resume'; }
  else { running = true; document.getElementById('startBtn').textContent = '⏸ Pause'; interval = setInterval(() => { if (secs === 0) { if (mins === 0) { clearInterval(interval); running = false; document.getElementById('startBtn').textContent = '▶ Start'; return; } mins--; secs = 59; } else secs--; document.getElementById('timer').textContent = String(mins).padStart(2,'0')+':'+String(secs).padStart(2,'0'); }, 1000); }
}
function resetTimer() { clearInterval(interval); running = false; mins = 25; secs = 0; document.getElementById('timer').textContent = '25:00'; document.getElementById('startBtn').textContent = '▶ Start Focus'; }
</script>
'''))

# Arena matchmaking
write_file('app/student/arena/matchmaking.html', student_page('Matchmaking', '''
<div style="text-align:center;padding:3rem 0;">
  <div class="page-header"><h1 class="page-title">⚔️ Battle Matchmaking</h1><p class="page-subtitle">Find your opponent and enter the arena</p></div>
  <div class="grid-2" style="max-width:800px;margin:0 auto 2rem;text-align:left;">
    <div class="card">
      <h3 style="margin-bottom:1rem;font-size:1rem;">⚙️ Battle Settings</h3>
      <div style="margin-bottom:1rem;"><label style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;display:block;margin-bottom:0.4rem;">Mode</label><select style="width:100%;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>1v1 Classic</option><option>1v1 Speed Run</option><option>Guild Team Battle</option></select></div>
      <div style="margin-bottom:1rem;"><label style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;display:block;margin-bottom:0.4rem;">Subject</label><select style="width:100%;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>Mathematics</option><option>Science</option><option>English</option><option>Mixed</option></select></div>
      <div style="margin-bottom:1rem;"><label style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;display:block;margin-bottom:0.4rem;">Difficulty</label><select style="width:100%;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>Matched (recommended)</option><option>Easy</option><option>Hard</option></select></div>
      <button class="btn btn-primary" style="width:100%;">⚔️ Find Battle</button>
    </div>
    <div class="card">
      <h3 style="margin-bottom:1rem;font-size:1rem;">🏆 Online Now (8 players)</h3>
      <div>
        <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;border-bottom:1px solid var(--border-color);"><div style="width:10px;height:10px;border-radius:50%;background:var(--success);flex-shrink:0;"></div><div style="flex:1;font-size:0.9rem;">Marcus T.</div><div style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">B+</div><button class="btn btn-ghost" style="padding:0.25rem 0.6rem;font-size:0.75rem;">Challenge</button></div>
        <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;border-bottom:1px solid var(--border-color);"><div style="width:10px;height:10px;border-radius:50%;background:var(--success);flex-shrink:0;"></div><div style="flex:1;font-size:0.9rem;">Sarah M.</div><div style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">A-</div><button class="btn btn-ghost" style="padding:0.25rem 0.6rem;font-size:0.75rem;">Challenge</button></div>
        <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;"><div style="width:10px;height:10px;border-radius:50%;background:var(--success);flex-shrink:0;"></div><div style="flex:1;font-size:0.9rem;">James R.</div><div style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">C</div><button class="btn btn-ghost" style="padding:0.25rem 0.6rem;font-size:0.75rem;">Challenge</button></div>
      </div>
    </div>
  </div>
</div>
''', '../../../'))

# Guild dashboard
write_file('app/student/guilds/guild-dashboard.html', student_page('Guild Dashboard', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏰 Shadow Wolves</h1><p class="page-subtitle">Rank #2 Guild · 847,200 Guild XP</p></div><div style="display:flex;gap:0.75rem;"><a href="guild-wars.html" class="btn btn-primary">⚔️ Guild Wars</a><a href="xp-shop.html" class="btn btn-ghost">🛍️ XP Shop</a></div></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Members</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">24</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Guild Rank</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">#2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Wars Won</div><div style="font-size:2rem;font-weight:900;color:var(--success);">18</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Your Contribution</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">12,450</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">🐺 Top Members</h3>
    <div>
      <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;border-bottom:1px solid var(--border-color);"><div style="color:var(--accent);font-weight:700;width:20px;">1</div><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">A</div><div style="flex:1;font-size:0.9rem;font-weight:600;">Alex Johnson <span style="color:var(--text-muted);font-weight:400;font-size:0.8rem;">(You)</span></div><div style="font-size:0.85rem;font-weight:700;color:var(--accent);">12,450</div></div>
      <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;border-bottom:1px solid var(--border-color);"><div style="color:var(--text-muted);font-weight:700;width:20px;">2</div><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">S</div><div style="flex:1;font-size:0.9rem;font-weight:600;">Sarah M.</div><div style="font-size:0.85rem;font-weight:700;color:var(--primary);">11,200</div></div>
      <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;"><div style="color:var(--warning);font-weight:700;width:20px;">3</div><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--warning),var(--accent));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">J</div><div style="flex:1;font-size:0.9rem;font-weight:600;">James R.</div><div style="font-size:0.85rem;font-weight:700;color:var(--success);">9,840</div></div>
    </div>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">🎯 Weekly Guild Quest</h3>
    <div style="padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);margin-bottom:1rem;border-left:3px solid var(--primary);">
      <div style="font-weight:600;margin-bottom:0.25rem;">Defeat Azure Dragons in 3 wars</div>
      <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">2/3 complete · Ends in 3 days</div>
      <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:linear-gradient(135deg,var(--primary),var(--success));border-radius:20px;width:66%;height:100%;"></div></div>
    </div>
    <div style="background:rgba(255,215,0,0.08);border-radius:var(--radius);padding:0.75rem;border-left:3px solid var(--accent);">
      <div style="font-size:0.85rem;font-weight:600;">Reward: 5,000 Guild XP + Rare Loot Box 🎁</div>
    </div>
  </div>
</div>
''', '../../../'))

# XP Shop
write_file('app/student/guilds/xp-shop.html', student_page('XP Shop', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🛍️ XP Shop</h1><p class="page-subtitle">Spend your Guild Coins on power-ups and cosmetics</p></div><div style="background:rgba(255,215,0,0.15);border:1px solid rgba(255,215,0,0.3);border-radius:20px;padding:0.5rem 1.25rem;font-weight:700;color:var(--accent);">💰 240 Guild Coins</div></div></div>
<div class="grid-4">
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">⚡</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">XP Booster</h3><p style="color:var(--text-muted);font-size:0.8rem;margin-bottom:1rem;">2x XP for 1 hour</p><div style="font-weight:700;color:var(--accent);margin-bottom:0.75rem;">50 💰</div><button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🛡️</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Battle Shield</h3><p style="color:var(--text-muted);font-size:0.8rem;margin-bottom:1rem;">Protect XP on loss</p><div style="font-weight:700;color:var(--accent);margin-bottom:0.75rem;">80 💰</div><button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🎯</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Hint Token</h3><p style="color:var(--text-muted);font-size:0.8rem;margin-bottom:1rem;">5 hints in battles</p><div style="font-weight:700;color:var(--accent);margin-bottom:0.75rem;">30 💰</div><button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🎨</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Avatar Frame</h3><p style="color:var(--text-muted);font-size:0.8rem;margin-bottom:1rem;">Legendary wolf frame</p><div style="font-weight:700;color:var(--accent);margin-bottom:0.75rem;">120 💰</div><button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Buy</button></div>
</div>
''', '../../../'))

# Loot boxes
write_file('app/student/guilds/loot-boxes.html', student_page('Loot Boxes', '''
<div class="page-header"><h1 class="page-title">🎁 Loot Boxes</h1><p class="page-subtitle">Open boxes to win rare items and XP boosts</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="border-color:rgba(255,215,0,0.4);text-align:center;cursor:pointer;padding:2rem;">
    <div style="font-size:4rem;margin-bottom:0.75rem;animation:bounce 2s infinite;">📦</div>
    <div style="font-weight:700;color:var(--accent);font-size:1.1rem;margin-bottom:0.5rem;">Common</div>
    <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:1rem;">XP · Items · Hints</div>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Open (Free)</button>
  </div>
  <div class="card" style="border-color:rgba(108,99,255,0.4);text-align:center;cursor:pointer;padding:2rem;">
    <div style="font-size:4rem;margin-bottom:0.75rem;">💼</div>
    <div style="font-weight:700;color:var(--primary);font-size:1.1rem;margin-bottom:0.5rem;">Rare</div>
    <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:1rem;">+XP Booster · Frames</div>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Open (50 💰)</button>
  </div>
  <div class="card" style="border-color:rgba(0,209,178,0.4);text-align:center;cursor:pointer;padding:2rem;">
    <div style="font-size:4rem;margin-bottom:0.75rem;">💎</div>
    <div style="font-weight:700;color:var(--success);font-size:1.1rem;margin-bottom:0.5rem;">Epic</div>
    <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:1rem;">Rare badges · Titles</div>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Open (150 💰)</button>
  </div>
  <div class="card" style="border-color:rgba(255,107,107,0.4);text-align:center;cursor:pointer;padding:2rem;">
    <div style="font-size:4rem;margin-bottom:0.75rem;">👑</div>
    <div style="font-weight:700;color:var(--secondary);font-size:1.1rem;margin-bottom:0.5rem;">Legendary</div>
    <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:1rem;">Exclusive cosmetics</div>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Open (500 💰)</button>
  </div>
</div>
<style>@keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }</style>
''', '../../../'))

# AI weak analysis
write_file('app/student/ai/weak-analysis.html', student_page('Weakness Analysis', '''
<div class="page-header"><h1 class="page-title">🔍 Weakness Analysis</h1><p class="page-subtitle">AI identifies your knowledge gaps so you can focus where it matters</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Weak Areas</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">3</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Improving</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">5</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Strong</div><div style="font-size:2rem;font-weight:900;color:var(--success);">12</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">AI Accuracy</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">94%</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">🔴 Areas to Improve</h3>
    <div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;"><div style="font-weight:600;font-size:0.9rem;">Trigonometry</div><div style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;">52% accuracy</div></div>
        <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:6px;margin-bottom:0.4rem;"><div style="background:var(--danger);border-radius:20px;width:52%;height:100%;"></div></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">Struggling with: Sin/Cos identities, Unit circle</div>
        <button class="btn btn-primary" style="padding:0.35rem 0.75rem;font-size:0.8rem;margin-top:0.5rem;">Study Now →</button>
      </div>
      <div style="padding:0.75rem;">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;"><div style="font-weight:600;font-size:0.9rem;">Organic Chemistry</div><div style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;">61% accuracy</div></div>
        <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:6px;margin-bottom:0.4rem;"><div style="background:var(--warning);border-radius:20px;width:61%;height:100%;"></div></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">Struggling with: Reaction mechanisms</div>
        <button class="btn btn-primary" style="padding:0.35rem 0.75rem;font-size:0.8rem;margin-top:0.5rem;">Study Now →</button>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">🟢 Your Strengths</h3>
    <div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Algebra</span><span style="color:var(--success);">92% ✓</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Geometry</span><span style="color:var(--success);">88% ✓</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;font-size:0.9rem;"><span>Statistics</span><span style="color:var(--success);">85% ✓</span></div>
    </div>
  </div>
</div>
''', '../../../'))

# Mock interview
write_file('app/student/ai/mock-interview.html', student_page('Mock Interview', '''
<div class="page-header"><h1 class="page-title">🎙️ Mock Interview</h1><p class="page-subtitle">Practice oral presentations and interview skills with AI</p></div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">Select Interview Type</h3>
    <div style="display:flex;flex-direction:column;gap:0.75rem;margin-bottom:1.5rem;">
      <div style="background:rgba(108,99,255,0.15);border:2px solid var(--primary);border-radius:var(--radius);padding:0.75rem;cursor:pointer;"><div style="font-weight:600;font-size:0.9rem;">📚 Subject Knowledge Test</div><div style="font-size:0.8rem;color:var(--text-muted);">AI asks questions about your subject</div></div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);padding:0.75rem;cursor:pointer;"><div style="font-weight:600;font-size:0.9rem;">💼 College Admissions</div><div style="font-size:0.8rem;color:var(--text-muted);">Practice college interview questions</div></div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);padding:0.75rem;cursor:pointer;"><div style="font-weight:600;font-size:0.9rem;">🗣️ Presentation Practice</div><div style="font-size:0.8rem;color:var(--text-muted);">Present on any topic with feedback</div></div>
    </div>
    <button class="btn btn-primary" style="width:100%;">Start Interview 🎙️</button>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📊 Last Session Results</h3>
    <div style="padding:1rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);margin-bottom:0.75rem;border-left:3px solid var(--success);">
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.5rem;">Subject Knowledge — Mathematics</div>
      <div class="grid-2" style="gap:0.5rem;">
        <div style="text-align:center;background:rgba(255,255,255,0.04);border-radius:8px;padding:0.5rem;"><div style="font-weight:700;color:var(--success);">85%</div><div style="font-size:0.7rem;color:var(--text-muted);">Accuracy</div></div>
        <div style="text-align:center;background:rgba(255,255,255,0.04);border-radius:8px;padding:0.5rem;"><div style="font-weight:700;color:var(--primary);">A-</div><div style="font-size:0.7rem;color:var(--text-muted);">Confidence</div></div>
      </div>
    </div>
    <div style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;padding:0.75rem;background:rgba(255,255,255,0.04);border-radius:var(--radius);">
      <strong style="color:var(--text-light);">AI Feedback:</strong> Strong conceptual understanding. Work on explaining your reasoning more clearly step-by-step.
    </div>
  </div>
</div>
''', '../../../'))

# Web studio
write_file('app/student/workspace/web-studio.html', student_page('Web Studio', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🌐 Web Studio</h1><p class="page-subtitle">Build websites with HTML, CSS, and JavaScript</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">💾 Save</button><button class="btn btn-primary">▶ Run</button></div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;height:500px;">
  <div style="background:rgba(0,0,0,0.5);border:1px solid var(--border-color);border-radius:var(--radius);display:flex;flex-direction:column;">
    <div style="display:flex;border-bottom:1px solid var(--border-color);">
      <button style="padding:0.5rem 1rem;background:rgba(108,99,255,0.2);color:var(--primary);border:none;font-family:inherit;font-size:0.8rem;cursor:pointer;border-right:1px solid var(--border-color);">HTML</button>
      <button style="padding:0.5rem 1rem;background:transparent;color:var(--text-muted);border:none;font-family:inherit;font-size:0.8rem;cursor:pointer;border-right:1px solid var(--border-color);">CSS</button>
      <button style="padding:0.5rem 1rem;background:transparent;color:var(--text-muted);border:none;font-family:inherit;font-size:0.8rem;cursor:pointer;">JS</button>
    </div>
    <textarea style="flex:1;background:transparent;border:none;padding:1rem;color:#A8D8FF;font-family:monospace;font-size:0.85rem;resize:none;line-height:1.6;" spellcheck="false"><!DOCTYPE html>
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;My First Page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Hello, World! 🌍&lt;/h1&gt;
  &lt;p&gt;Welcome to Web Studio!&lt;/p&gt;
  &lt;button onclick="greet()"&gt;Click me!&lt;/button&gt;
&lt;/body&gt;
&lt;/html&gt;</textarea>
  </div>
  <div style="background:white;border-radius:var(--radius);display:flex;align-items:center;justify-content:center;border:1px solid var(--border-color);">
    <div style="text-align:center;color:#333;padding:2rem;">
      <h1 style="font-size:2rem;margin-bottom:0.5rem;">Hello, World! 🌍</h1>
      <p>Welcome to Web Studio!</p>
      <button style="margin-top:1rem;padding:0.5rem 1rem;background:#6C63FF;color:white;border:none;border-radius:8px;cursor:pointer;">Click me!</button>
    </div>
  </div>
</div>
''', '../../../'))

# Flutter lab
write_file('app/student/workspace/flutter-lab.html', student_page('Flutter Lab', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📱 Flutter Lab</h1><p class="page-subtitle">Build mobile apps with Dart & Flutter — Beta</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">💾 Save</button><button class="btn btn-primary">▶ Run</button></div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;height:500px;">
  <div style="background:rgba(0,0,0,0.5);border:1px solid var(--border-color);border-radius:var(--radius);overflow:hidden;">
    <div style="padding:0.5rem 1rem;border-bottom:1px solid var(--border-color);font-size:0.8rem;color:var(--text-muted);">main.dart</div>
    <pre style="padding:1rem;color:#A8D8FF;font-family:monospace;font-size:0.8rem;line-height:1.7;margin:0;overflow:auto;height:calc(100% - 40px);">import \'package:flutter/material.dart\';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: \'lvlBase App\',
      home: Scaffold(
        appBar: AppBar(
          title: Text(\'Hello Flutter! 📱\'),
          backgroundColor: Color(0xFF6C63FF),
        ),
        body: Center(
          child: Column(children: [
            Text(\'Welcome to Flutter Lab!\',
              style: TextStyle(fontSize: 24)),
            ElevatedButton(
              child: Text(\'Level Up! ⚡\'),
              onPressed: () {},
            ),
          ]),
        ),
      ),
    );
  }
}</pre>
  </div>
  <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border-color);border-radius:var(--radius);display:flex;align-items:center;justify-content:center;">
    <div style="width:200px;height:380px;background:#1A1A2E;border-radius:20px;border:2px solid rgba(108,99,255,0.4);overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.5);">
      <div style="background:var(--primary);padding:0.5rem 0.75rem;font-size:0.75rem;font-weight:700;">Hello Flutter! 📱</div>
      <div style="display:flex;align-items:center;justify-content:center;height:80%;flex-direction:column;gap:1rem;padding:1rem;">
        <p style="font-size:0.75rem;text-align:center;color:var(--text-light);">Welcome to Flutter Lab!</p>
        <button style="background:var(--primary);color:white;border:none;border-radius:8px;padding:0.4rem 1rem;font-size:0.75rem;cursor:pointer;">Level Up! ⚡</button>
      </div>
    </div>
  </div>
</div>
''', '../../../'))

# Code review
write_file('app/student/workspace/code-review.html', student_page('Code Review', '''
<div class="page-header"><h1 class="page-title">🔍 AI Code Review</h1><p class="page-subtitle">Get instant feedback on your code quality and style</p></div>
<div class="grid-2">
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">📝 Your Code</h3><div style="display:flex;gap:0.5rem;"><select style="padding:0.4rem 0.75rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.8rem;"><option>Python</option><option>JavaScript</option><option>Dart</option></select><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.8rem;">Review 🤖</button></div></div>
    <textarea style="width:100%;height:300px;background:rgba(0,0,0,0.3);border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem;color:#A8D8FF;font-family:monospace;font-size:0.85rem;resize:none;line-height:1.7;">def find_max(lst):
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(find_max(numbers))</textarea>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">🤖 AI Review Results</h3>
    <div style="padding:0.75rem;background:rgba(0,209,178,0.1);border-radius:var(--radius);margin-bottom:0.75rem;border-left:3px solid var(--success);">
      <div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;color:var(--success);">✓ Logic is correct</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">The algorithm correctly finds the maximum value</div>
    </div>
    <div style="padding:0.75rem;background:rgba(255,159,67,0.1);border-radius:var(--radius);margin-bottom:0.75rem;border-left:3px solid var(--warning);">
      <div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;color:var(--warning);">💡 Suggestion: Use built-in max()</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">Python has a built-in max() function. Consider: return max(lst)</div>
    </div>
    <div style="padding:0.75rem;background:rgba(108,99,255,0.1);border-radius:var(--radius);border-left:3px solid var(--primary);">
      <div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;color:var(--primary);">💡 Pythonic Style</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">Use "for item in lst" instead of index-based loop</div>
    </div>
    <div style="display:flex;gap:1rem;margin-top:1.5rem;"><div style="text-align:center;flex:1;background:rgba(0,209,178,0.1);border-radius:var(--radius);padding:0.75rem;"><div style="font-weight:700;color:var(--success);">B+</div><div style="font-size:0.7rem;color:var(--text-muted);">Overall</div></div><div style="text-align:center;flex:1;background:rgba(108,99,255,0.1);border-radius:var(--radius);padding:0.75rem;"><div style="font-weight:700;color:var(--primary);">A</div><div style="font-size:0.7rem;color:var(--text-muted);">Correctness</div></div><div style="text-align:center;flex:1;background:rgba(255,159,67,0.1);border-radius:var(--radius);padding:0.75rem;"><div style="font-weight:700;color:var(--warning);">C+</div><div style="font-size:0.7rem;color:var(--text-muted);">Style</div></div></div>
  </div>
</div>
''', '../../../'))

print("Auth and remaining student pages created")
