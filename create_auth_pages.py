import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

STYLES = ''':root { --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B; --accent: #FFD700; --success: #00D1B2; --danger: #FF4444; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px; --shadow-heavy: 0 8px 40px rgba(0,0,0,0.5); --transition: all 0.3s ease; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
.auth-wrapper { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(ellipse at 30% 40%, rgba(108,99,255,0.15) 0%, transparent 60%), radial-gradient(ellipse at 70% 70%, rgba(255,107,107,0.1) 0%, transparent 60%), var(--dark-bg); padding: 2rem; }
.auth-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2.5rem; width: 100%; max-width: 480px; box-shadow: var(--shadow-heavy); animation: slideUp 0.5s ease; }
.auth-logo { text-align: center; font-size: 2rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.25rem; }
.auth-subtitle { text-align: center; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem; }
.form-group { margin-bottom: 1.25rem; }
.form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
.form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; transition: var(--transition); }
.form-control:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(108,99,255,0.15); }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; justify-content: center; width: 100%; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; margin-top: 0.5rem; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(108,99,255,0.4); }
.auth-footer { text-align: center; margin-top: 1.5rem; font-size: 0.9rem; color: var(--text-muted); }
.auth-footer a { color: var(--primary); font-weight: 600; text-decoration: none; }
.auth-divider { display: flex; align-items: center; gap: 1rem; margin: 1.5rem 0; color: var(--text-muted); font-size: 0.85rem; }
.auth-divider::before, .auth-divider::after { content: ""; flex: 1; height: 1px; background: var(--border-color); }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }'''

def auth_page(title, card_content, scripts=''):
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
  <div class="auth-card">
    <div class="auth-logo">lvlBase ⚡</div>
{card_content}
  </div>
</div>
{scripts}
</body>
</html>'''

# auth/signup-teacher.html
write_file('auth/signup-teacher.html', auth_page('Teacher Sign Up', '''
    <div class="auth-subtitle">Join as an Educator 👨‍🏫</div>
    <div class="form-group"><label class="form-label">Full Name</label><input class="form-control" type="text" placeholder="Dr. Jane Smith"></div>
    <div class="form-group"><label class="form-label">School Email</label><input class="form-control" type="email" placeholder="jane@school.edu"></div>
    <div class="form-group"><label class="form-label">School Name</label><input class="form-control" type="text" placeholder="Riverside Academy"></div>
    <div class="form-group"><label class="form-label">Subject(s) You Teach</label><input class="form-control" type="text" placeholder="Math, Science..."></div>
    <div class="form-group"><label class="form-label">Password</label><input class="form-control" type="password" placeholder="Min 8 characters"></div>
    <button class="btn btn-primary">Create Teacher Account →</button>
    <div class="auth-divider">or</div>
    <button class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light);">🔗 Sign up with Google</button>
    <div class="auth-footer">Already have an account? <a href="portal-login.html">Login →</a></div>
    <div class="auth-footer" style="margin-top:0.5rem;"><a href="school-onboarding.html">Register your school instead</a></div>
'''))

# auth/invite-claim.html
write_file('auth/invite-claim.html', auth_page('Claim Your Invite', '''
    <div class="auth-subtitle">You\'ve been invited to join! 🎉</div>
    <div style="background:rgba(108,99,255,0.1); border:1px solid rgba(108,99,255,0.3); border-radius:var(--radius); padding:1rem; margin-bottom:1.5rem; text-align:center;">
      <div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.25rem;">Invited by</div>
      <div style="font-weight:700;">Riverside Academy</div>
      <div style="font-size:0.85rem; color:var(--text-muted);">as Student</div>
    </div>
    <div class="form-group"><label class="form-label">Your Name</label><input class="form-control" type="text" placeholder="Your full name"></div>
    <div class="form-group"><label class="form-label">Create Password</label><input class="form-control" type="password" placeholder="Min 8 characters"></div>
    <div class="form-group"><label class="form-label">Confirm Password</label><input class="form-control" type="password" placeholder="Repeat password"></div>
    <button class="btn btn-primary">Claim My Account 🚀</button>
    <div class="auth-footer">Wrong invite? <a href="portal-login.html">Go to Login</a></div>
'''))

# auth/magic-link.html
write_file('auth/magic-link.html', auth_page('Magic Link Login', '''
    <div class="auth-subtitle">Login without a password ✨</div>
    <div class="form-group"><label class="form-label">Email Address</label><input class="form-control" type="email" placeholder="your@email.com"></div>
    <button class="btn btn-primary">Send Magic Link ✉️</button>
    <div style="text-align:center; margin-top:1.5rem; padding:1rem; background:rgba(0,209,178,0.1); border-radius:var(--radius); display:none;" id="success-msg">
      <div style="font-size:2rem; margin-bottom:0.5rem;">📧</div>
      <p style="color:var(--success); font-weight:600;">Magic link sent!</p>
      <p style="color:var(--text-muted); font-size:0.85rem; margin-top:0.25rem;">Check your inbox and click the link to log in.</p>
    </div>
    <div class="auth-footer">Remember your password? <a href="portal-login.html">Login →</a></div>
'''))

# auth/sso-gateway.html
write_file('auth/sso-gateway.html', auth_page('SSO Login', '''
    <div class="auth-subtitle">Single Sign-On Gateway 🔑</div>
    <div class="form-group"><label class="form-label">School Domain or Email</label><input class="form-control" type="text" placeholder="school.edu or admin@district.org"></div>
    <button class="btn btn-primary">Continue with SSO →</button>
    <div class="auth-divider">or login directly with</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem;">
      <button class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light); font-size:0.85rem;">🔵 Google</button>
      <button class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light); font-size:0.85rem;">🟦 Microsoft</button>
      <button class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light); font-size:0.85rem;">🟠 Clever</button>
      <button class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light); font-size:0.85rem;">🔷 ClassLink</button>
    </div>
    <div class="auth-footer" style="margin-top:1.5rem;"><a href="portal-login.html">← Back to login</a></div>
'''))

# auth/2fa-setup.html
write_file('auth/2fa-setup.html', auth_page('Two-Factor Authentication', '''
    <div class="auth-subtitle">Secure your account with 2FA 🔒</div>
    <div style="text-align:center; margin-bottom:1.5rem;">
      <div style="width:160px; height:160px; background:rgba(255,255,255,0.05); border:2px dashed var(--border-color); border-radius:var(--radius); margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:0.85rem; color:var(--text-muted);">QR Code Here</div>
      <p style="color:var(--text-muted); font-size:0.8rem; margin-top:0.75rem;">Scan with Google Authenticator or Authy</p>
    </div>
    <div class="form-group"><label class="form-label">Manual Key</label><input class="form-control" type="text" value="JBSW Y3DP EHPK 3PXP" readonly style="text-align:center; font-family:monospace; letter-spacing:0.15em;"></div>
    <div class="form-group"><label class="form-label">Verification Code</label><input class="form-control" type="text" placeholder="000000" maxlength="6" style="text-align:center; font-size:1.5rem; letter-spacing:0.5em;"></div>
    <button class="btn btn-primary">Verify & Enable 2FA ✓</button>
    <div class="auth-footer" style="margin-top:1rem;"><a href="portal-login.html">Skip for now</a></div>
'''))

# auth/biometric-auth.html
write_file('auth/biometric-auth.html', auth_page('Biometric Login', '''
    <div class="auth-subtitle">Use your fingerprint or face to login 👁️</div>
    <div style="text-align:center; padding:2.5rem 0;">
      <div id="bio-icon" style="font-size:5rem; margin-bottom:1rem; cursor:pointer; transition:all 0.3s ease;" onclick="triggerBio()">🔒</div>
      <p id="bio-status" style="color:var(--text-muted); font-size:0.9rem;">Tap the lock to authenticate</p>
    </div>
    <button class="btn btn-primary" onclick="triggerBio()">Use Biometric Login 🔐</button>
    <div class="auth-divider">or</div>
    <a href="portal-login.html" class="btn" style="background:rgba(255,255,255,0.05); border:1px solid var(--border-color); color:var(--text-light);">Login with Password</a>
''', '''
<script>
function triggerBio() {
  const icon = document.getElementById('bio-icon');
  const status = document.getElementById('bio-status');
  icon.textContent = '⏳';
  status.textContent = 'Authenticating...';
  if (window.PublicKeyCredential) {
    navigator.credentials.get({ publicKey: { challenge: new Uint8Array(32), timeout: 60000, rpId: window.location.hostname, allowCredentials: [], userVerification: "required" } })
      .then(() => { icon.textContent = '✅'; status.textContent = 'Authentication successful!'; setTimeout(() => window.location.href = '../app/student/dashboard.html', 1000); })
      .catch(() => { icon.textContent = '❌'; status.textContent = 'Authentication failed. Try again.'; setTimeout(() => { icon.textContent = '🔒'; status.textContent = 'Tap the lock to authenticate'; }, 2000); });
  } else { icon.textContent = '❌'; status.textContent = 'Biometric not supported on this device'; }
}
</script>
'''))

# auth/reset-password.html
write_file('auth/reset-password.html', auth_page('Reset Password', '''
    <div class="auth-subtitle">Create a new password 🔑</div>
    <div class="form-group"><label class="form-label">New Password</label><input class="form-control" type="password" placeholder="Min 8 characters"></div>
    <div class="form-group"><label class="form-label">Confirm Password</label><input class="form-control" type="password" placeholder="Repeat new password"></div>
    <ul style="list-style:none; margin-bottom:1.5rem; font-size:0.8rem; color:var(--text-muted);">
      <li>✓ At least 8 characters</li>
      <li>✓ Contains a number</li>
      <li>✓ Contains a special character</li>
    </ul>
    <button class="btn btn-primary">Reset Password →</button>
    <div class="auth-footer"><a href="portal-login.html">← Back to Login</a></div>
'''))

# auth/forgot-password.html
write_file('auth/forgot-password.html', auth_page('Forgot Password', '''
    <div class="auth-subtitle">We\'ll send you a reset link 📧</div>
    <div class="form-group"><label class="form-label">Email Address</label><input class="form-control" type="email" placeholder="your@email.com"></div>
    <button class="btn btn-primary">Send Reset Link →</button>
    <div class="auth-footer"><a href="portal-login.html">← Back to Login</a></div>
'''))

# auth/blocked.html
write_file('auth/blocked.html', auth_page('Account Blocked', '''
    <div style="text-align:center; padding:1rem 0 2rem;">
      <div style="font-size:4rem; margin-bottom:1rem;">🚫</div>
      <h2 style="margin-bottom:0.75rem;">Account Suspended</h2>
      <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem;">Your account has been temporarily suspended. This may be due to a violation of our terms of service or suspicious activity.</p>
      <div style="background:rgba(255,68,68,0.1); border:1px solid rgba(255,68,68,0.3); border-radius:var(--radius); padding:1rem; margin-bottom:1.5rem; font-size:0.85rem; color:var(--danger);">
        <strong>Reason:</strong> Multiple failed login attempts detected
      </div>
    </div>
    <a href="mailto:support@lvlbase.io" class="btn btn-primary">Contact Support 📧</a>
    <div class="auth-footer" style="margin-top:1rem;"><a href="portal-login.html">← Try Login Again</a></div>
'''))

# auth/session-expired.html
write_file('auth/session-expired.html', auth_page('Session Expired', '''
    <div style="text-align:center; padding:1rem 0 2rem;">
      <div style="font-size:4rem; margin-bottom:1rem;">⏰</div>
      <h2 style="margin-bottom:0.75rem;">Session Expired</h2>
      <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem;">Your session has timed out for security reasons. Please log in again to continue your quest.</p>
      <div style="background:rgba(108,99,255,0.1); border:1px solid var(--border-color); border-radius:var(--radius); padding:1rem; margin-bottom:1.5rem; font-size:0.85rem; color:var(--text-muted);">
        💾 Don\'t worry — your progress was automatically saved!
      </div>
    </div>
    <a href="portal-login.html" class="btn btn-primary">Login Again →</a>
'''))

print("Auth pages created")
