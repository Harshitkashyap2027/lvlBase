import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

BASE_STYLES = '''* { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
    :root { --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B; --accent: #FFD700; --success: #00D1B2; --warning: #FF9F43; --danger: #FF4444; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px; --shadow: 0 4px 20px rgba(0,0,0,0.3); --transition: all 0.3s ease; }
    .navbar { position: fixed; top: 0; left: 0; right: 0; height: 65px; background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; }
    .navbar-brand { font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .navbar-nav { display: flex; gap: 0.5rem; }
    .nav-link { padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }
    .nav-link:hover, .nav-link.active { color: var(--text-light); background: rgba(108,99,255,0.15); }
    .navbar-actions { display: flex; align-items: center; gap: 1rem; }
    .badge { padding: 0.3rem 0.75rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; }
    .badge-primary { background: rgba(108,99,255,0.2); color: var(--primary); border: 1px solid rgba(108,99,255,0.3); }
    .avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--primary), var(--secondary)); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; cursor: pointer; }
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
    .btn-ghost:hover { background: rgba(255,255,255,0.05); color: var(--text-light); }
    .form-group { margin-bottom: 1.25rem; }
    .form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
    .form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; transition: var(--transition); }
    .form-control:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(108,99,255,0.15); }
    @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
    @media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def page(title, css, nav, body, scripts=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
  <style>{BASE_STYLES}</style>
</head>
<body>
{nav}
<div class="page-wrapper"><div class="container">
{body}
</div></div>
{scripts}
</body>
</html>'''

# === LEGAL PAGES ===
def legal_nav():
    return '''<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="../index.html" class="nav-link">← Back to Site</a>
  </div>
</nav>'''

write_file('public/legal/privacy-policy.html', page('Privacy Policy', '../../core/css/base.css', legal_nav(), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <h1 style="font-size:2rem; font-weight:900; margin-bottom:0.5rem;">Privacy Policy 🔒</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">Last updated: January 1, 2025</p>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">1. Information We Collect</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">We collect information you provide directly (name, email, school), information from usage (XP earned, assignments completed, login times), and device information (browser type, device type) for security purposes. We never collect sensitive personal information beyond what is necessary for educational purposes.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">2. How We Use Your Information</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">We use collected information to provide and improve our services, personalize learning experiences, communicate with users and parents, ensure platform safety, and generate anonymized analytics for research.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">3. Student Data Protection</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">We comply with FERPA (Family Educational Rights and Privacy Act), COPPA (Children\'s Online Privacy Protection Act), and GDPR. We never sell student data. Student data is only shared with their school, teachers, and parents as defined by school agreements.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">4. Data Security</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">All data is encrypted in transit (TLS 1.3) and at rest (AES-256). We use Firebase Security Rules to enforce access controls. Regular security audits are conducted by independent third parties.</p></div>
  <div class="card"><h2 style="font-size:1.2rem; margin-bottom:1rem;">5. Contact</h2><p style="color:var(--text-muted); font-size:0.9rem;">For privacy concerns: <a href="mailto:privacy@lvlbase.io" style="color:var(--primary);">privacy@lvlbase.io</a></p></div>
</div>
'''))

write_file('public/legal/terms-of-service.html', page('Terms of Service', '../../core/css/base.css', legal_nav(), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <h1 style="font-size:2rem; font-weight:900; margin-bottom:0.5rem;">Terms of Service 📋</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">Last updated: January 1, 2025 — By using lvlBase, you agree to these terms.</p>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">1. Acceptance of Terms</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">By accessing or using lvlBase ("the Platform"), you agree to be bound by these Terms of Service. Schools accepting on behalf of minor students warrant they have the authority to do so.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">2. Acceptable Use</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">Users may not: share login credentials, attempt to circumvent proctoring systems, harass other users, upload inappropriate content, reverse engineer the platform, or use the platform for commercial purposes outside of approved school use.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">3. Intellectual Property</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">lvlBase content, including questions, games, and AI responses, is owned by lvlBase Inc. Student-created content remains the property of the student and their school.</p></div>
  <div class="card"><h2 style="font-size:1.2rem; margin-bottom:1rem;">4. Limitation of Liability</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">lvlBase provides the platform "as is." We are not liable for academic outcomes, though we strive for the best learning results. Service availability is subject to our SLA agreements.</p></div>
</div>
'''))

write_file('public/legal/compliance.html', page('Compliance', '../../core/css/base.css', legal_nav(), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <h1 style="font-size:2rem; font-weight:900; margin-bottom:0.5rem;">Compliance & Certifications 🛡️</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">lvlBase is committed to the highest standards of data protection for students.</p>
  <div class="grid-2" style="margin-bottom:2rem;">
    <div class="card" style="text-align:center; padding:2rem; border-color:rgba(0,209,178,0.3);">
      <div style="font-size:3rem; margin-bottom:1rem;">👶</div>
      <h3 style="margin-bottom:0.5rem; color:var(--success);">COPPA Compliant</h3>
      <p style="color:var(--text-muted); font-size:0.85rem;">Children\'s Online Privacy Protection Act. We obtain verifiable parental consent for users under 13 and never collect unnecessary data from children.</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem; border-color:rgba(108,99,255,0.3);">
      <div style="font-size:3rem; margin-bottom:1rem;">🎓</div>
      <h3 style="margin-bottom:0.5rem; color:var(--primary);">FERPA Compliant</h3>
      <p style="color:var(--text-muted); font-size:0.85rem;">Family Educational Rights and Privacy Act. Schools control student data. Parents have rights to access and correct their children\'s educational records.</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem; border-color:rgba(255,215,0,0.3);">
      <div style="font-size:3rem; margin-bottom:1rem;">🇪🇺</div>
      <h3 style="margin-bottom:0.5rem; color:var(--accent);">GDPR Compliant</h3>
      <p style="color:var(--text-muted); font-size:0.85rem;">General Data Protection Regulation. EU users have full rights to data portability, erasure, and transparency in data processing.</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem; border-color:rgba(255,107,107,0.3);">
      <div style="font-size:3rem; margin-bottom:1rem;">🔒</div>
      <h3 style="margin-bottom:0.5rem; color:var(--secondary);">SOC 2 Type II</h3>
      <p style="color:var(--text-muted); font-size:0.85rem;">Annual independent audits of our security, availability, and confidentiality controls. Audit reports available upon request.</p>
    </div>
  </div>
</div>
'''))

write_file('public/legal/security-whitepaper.html', page('Security Whitepaper', '../../core/css/base.css', legal_nav(), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <h1 style="font-size:2rem; font-weight:900; margin-bottom:0.5rem;">Security Whitepaper 🔐</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">Technical overview of lvlBase security architecture</p>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">🏗️ Infrastructure Security</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">lvlBase runs on Google Firebase infrastructure with multi-region data replication. All services use Google Cloud\'s built-in DDoS protection, WAF, and network segmentation. Infrastructure access is restricted by IP allowlist and requires hardware MFA.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">🔑 Authentication</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">Firebase Authentication handles identity. Supported methods: Email/Password, Google OAuth, Microsoft OAuth, SSO (SAML 2.0). JWT tokens expire after 1 hour. Refresh tokens can be revoked instantly by admins.</p></div>
  <div class="card" style="margin-bottom:1.5rem;"><h2 style="font-size:1.2rem; margin-bottom:1rem;">📊 Data Encryption</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">All data in transit uses TLS 1.3. Firestore data is encrypted at rest with AES-256 keys managed by Google Cloud KMS. Sensitive fields (financial data, contact info) use additional application-level encryption.</p></div>
  <div class="card"><h2 style="font-size:1.2rem; margin-bottom:1rem;">🚨 Incident Response</h2><p style="color:var(--text-muted); font-size:0.9rem; line-height:1.7;">We maintain a 24/7 security monitoring team. In case of a breach, we notify affected schools within 72 hours as required by GDPR. Our RTO is 4 hours and RPO is 1 hour.</p></div>
</div>
'''))

# === ERROR / UTILITY PAGES ===
write_file('public/404.html', page('404 Not Found', '../core/css/base.css', '', '''
<div style="min-height:100vh; display:flex; align-items:center; justify-content:center; text-align:center; padding:2rem;">
  <div>
    <div style="font-size:8rem; margin-bottom:1rem; animation:slideUp 0.6s ease;">👾</div>
    <h1 style="font-size:6rem; font-weight:900; background:linear-gradient(135deg,var(--primary),var(--secondary)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1; margin-bottom:1rem;">404</h1>
    <h2 style="font-size:1.5rem; font-weight:700; margin-bottom:0.75rem;">Quest Not Found!</h2>
    <p style="color:var(--text-muted); font-size:1rem; max-width:400px; margin:0 auto 2rem;">This dungeon level doesn\'t exist. The page you\'re looking for has been moved, deleted, or never existed.</p>
    <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
      <a href="index.html" class="btn btn-primary">🏠 Return to Base</a>
      <a href="javascript:history.back()" class="btn btn-ghost">← Go Back</a>
    </div>
  </div>
</div>
<style>:root { --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --transition: all 0.3s ease; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }
.btn-ghost { background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }
@keyframes slideUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }</style>
'''))

write_file('public/offline.html', page('Offline', '../core/css/base.css', '', '''
<div style="min-height:100vh; display:flex; align-items:center; justify-content:center; text-align:center; padding:2rem;">
  <div>
    <div style="font-size:6rem; margin-bottom:1rem;">📡</div>
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.75rem;">You\'re Offline</h1>
    <p style="color:var(--text-muted); font-size:1rem; max-width:400px; margin:0 auto 2rem;">Your internet connection seems to be down. Don\'t worry — some content is available offline!</p>
    <button onclick="location.reload()" class="btn btn-primary">🔄 Try Again</button>
  </div>
</div>
<style>:root { --primary: #6C63FF; --primary-dark: #5A52E8; --dark-bg: #0A0A1A; --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --transition: all 0.3s ease; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }</style>
'''))

write_file('public/maintenance.html', page('Maintenance', '../core/css/base.css', '', '''
<div style="min-height:100vh; display:flex; align-items:center; justify-content:center; text-align:center; padding:2rem;">
  <div>
    <div style="font-size:6rem; margin-bottom:1rem;">⚙️</div>
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.75rem;">Leveling Up lvlBase</h1>
    <p style="color:var(--text-muted); font-size:1rem; max-width:450px; margin:0 auto 2rem;">We\'re deploying new features and improvements. We\'ll be back soon — usually within 30 minutes!</p>
    <div style="background:var(--card-bg); border:1px solid var(--border-color); border-radius:var(--radius-xl); padding:1.5rem; max-width:300px; margin:0 auto 2rem;">
      <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:0.5rem;">Estimated completion</div>
      <div style="font-size:1.5rem; font-weight:700;" id="countdown">30:00</div>
    </div>
    <a href="system-status.html" style="color:var(--primary); font-size:0.9rem;">Check system status →</a>
  </div>
</div>
<style>:root { --primary: #6C63FF; --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }</style>
'''))

print("Legal and utility pages created")
