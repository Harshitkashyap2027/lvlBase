import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

# ===== BASE TEMPLATE =====
def base_page(title, css_path, body, extra_head='', extra_scripts=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_path}">
  {extra_head}
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }}
    :root {{
      --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B;
      --accent: #FFD700; --success: #00D1B2; --warning: #FF9F43; --danger: #FF4444;
      --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --card-hover: #1E1E35;
      --border-color: rgba(108,99,255,0.2); --text-light: #E8E8FF; --text-muted: #8892A4;
      --radius: 12px; --radius-xl: 24px;
      --shadow: 0 4px 20px rgba(0,0,0,0.3); --shadow-heavy: 0 8px 40px rgba(0,0,0,0.5);
      --transition: all 0.3s ease;
    }}
    .navbar {{ position: fixed; top: 0; left: 0; right: 0; height: 65px; background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; }}
    .navbar-brand {{ font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
    .navbar-nav {{ display: flex; gap: 0.5rem; }}
    .nav-link {{ padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }}
    .nav-link:hover, .nav-link.active {{ color: var(--text-light); background: rgba(108,99,255,0.15); }}
    .navbar-actions {{ display: flex; align-items: center; gap: 1rem; }}
    .badge {{ padding: 0.3rem 0.75rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; }}
    .badge-primary {{ background: rgba(108,99,255,0.2); color: var(--primary); border: 1px solid rgba(108,99,255,0.3); }}
    .badge-success {{ background: rgba(0,209,178,0.2); color: var(--success); border: 1px solid rgba(0,209,178,0.3); }}
    .badge-warning {{ background: rgba(255,159,67,0.2); color: var(--warning); border: 1px solid rgba(255,159,67,0.3); }}
    .avatar {{ width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--primary), var(--secondary)); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; cursor: pointer; }}
    .page-wrapper {{ padding-top: 65px; min-height: 100vh; }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 2rem; }}
    .page-header {{ margin-bottom: 2rem; }}
    .page-title {{ font-size: 1.8rem; font-weight: 800; margin-bottom: 0.25rem; }}
    .page-subtitle {{ color: var(--text-muted); font-size: 0.95rem; }}
    .card {{ background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.5rem; transition: var(--transition); }}
    .card:hover {{ border-color: rgba(108,99,255,0.4); box-shadow: var(--shadow); }}
    .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
    .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; }}
    .btn {{ padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; }}
    .btn-primary {{ background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }}
    .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 25px rgba(108,99,255,0.4); }}
    .btn-secondary {{ background: rgba(255,107,107,0.15); color: var(--secondary); border: 1px solid rgba(255,107,107,0.3); }}
    .btn-secondary:hover {{ background: rgba(255,107,107,0.25); }}
    .btn-ghost {{ background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }}
    .btn-ghost:hover {{ background: rgba(255,255,255,0.05); color: var(--text-light); }}
    .stat-card {{ text-align: center; }}
    .stat-value {{ font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
    .stat-label {{ color: var(--text-muted); font-size: 0.85rem; margin-top: 0.25rem; }}
    .form-group {{ margin-bottom: 1.25rem; }}
    .form-label {{ display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }}
    .form-control {{ width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; transition: var(--transition); }}
    .form-control:focus {{ outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(108,99,255,0.15); }}
    .rank-badge {{ display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; }}
    .rank-e {{ background: rgba(138,138,138,0.2); color: #8A8A8A; }}
    .rank-d {{ background: rgba(100,200,100,0.2); color: #64C864; }}
    .rank-c {{ background: rgba(100,149,237,0.2); color: #6495ED; }}
    .rank-b {{ background: rgba(147,112,219,0.2); color: #9370DB; }}
    .rank-a {{ background: rgba(255,215,0,0.2); color: #FFD700; }}
    .rank-s {{ background: rgba(255,107,107,0.2); color: #FF6B6B; }}
    .rank-ss {{ background: linear-gradient(135deg, rgba(108,99,255,0.3), rgba(255,107,107,0.3)); color: var(--primary); border: 1px solid var(--primary); }}
    @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.6; }} }}
    @media (max-width: 768px) {{ .grid-2, .grid-3, .grid-4 {{ grid-template-columns: 1fr; }} .navbar-nav {{ display: none; }} }}
  </style>
</head>
<body>
{body}
{extra_scripts}
</body>
</html>'''

# ===== PUBLIC PAGES =====

# public/pricing.html
write_file('public/pricing.html', base_page('Pricing', '../core/css/base.css', '''
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="index.html" class="nav-link">Home</a>
    <a href="features.html" class="nav-link">Features</a>
    <a href="pricing.html" class="nav-link active">Pricing</a>
    <a href="for-schools.html" class="nav-link">For Schools</a>
    <a href="faq.html" class="nav-link">FAQ</a>
  </div>
  <div class="navbar-actions">
    <a href="../auth/portal-login.html" class="btn btn-primary">Login →</a>
  </div>
</nav>
<div class="page-wrapper">
  <div class="container">
    <div class="page-header" style="text-align:center; padding: 3rem 0 2rem;">
      <div style="display:inline-block; background: rgba(108,99,255,0.15); border: 1px solid rgba(108,99,255,0.3); border-radius: 20px; padding: 0.4rem 1rem; font-size: 0.85rem; color: var(--primary); margin-bottom: 1rem;">💰 Transparent Pricing</div>
      <h1 class="page-title" style="font-size: 3rem;">Level Up Your School</h1>
      <p class="page-subtitle" style="font-size: 1.1rem; max-width: 500px; margin: 0.5rem auto 0;">Choose the plan that powers your institution's gamified learning journey</p>
    </div>
    <div class="grid-3" style="max-width: 1100px; margin: 0 auto 4rem;">
      <!-- Free -->
      <div class="card" style="border-radius: var(--radius-xl);">
        <div style="text-align:center; padding: 1rem 0 1.5rem;">
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌱</div>
          <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 0.25rem;">Free</h3>
          <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.5rem;">Get started today</p>
          <div style="font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, var(--success), #00A896); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">$0</div>
          <div style="color: var(--text-muted); font-size: 0.85rem;">forever</div>
        </div>
        <ul style="list-style: none; margin-bottom: 2rem;">
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Up to 30 students</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> 3 subjects</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Basic XP system</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> AI Sage (50 msgs/mo)</li>
          <li style="padding: 0.6rem 0; font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--text-muted);">✗</span> <span style="color: var(--text-muted);">Guild Wars</span></li>
        </ul>
        <a href="../auth/school-onboarding.html" class="btn btn-ghost" style="width: 100%; justify-content: center;">Start Free →</a>
      </div>
      <!-- Pro -->
      <div class="card" style="border-radius: var(--radius-xl); border-color: var(--primary); box-shadow: 0 0 40px rgba(108,99,255,0.2); position: relative; transform: scale(1.03);">
        <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; padding: 0.3rem 1.5rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">⭐ MOST POPULAR</div>
        <div style="text-align:center; padding: 1rem 0 1.5rem;">
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🏫</div>
          <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 0.25rem;">Pro School</h3>
          <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.5rem;">For growing schools</p>
          <div style="font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">$299</div>
          <div style="color: var(--text-muted); font-size: 0.85rem;">per month / per school</div>
        </div>
        <ul style="list-style: none; margin-bottom: 2rem;">
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Unlimited students</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> All subjects</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Full gamification suite</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> AI Sage unlimited</li>
          <li style="padding: 0.6rem 0; font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Guild Wars & Arena</li>
        </ul>
        <a href="../auth/school-onboarding.html" class="btn btn-primary" style="width: 100%; justify-content: center;">Start 14-Day Trial →</a>
      </div>
      <!-- Enterprise -->
      <div class="card" style="border-radius: var(--radius-xl);">
        <div style="text-align:center; padding: 1rem 0 1.5rem;">
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🏢</div>
          <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 0.25rem;">Enterprise</h3>
          <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.5rem;">District-wide deployment</p>
          <div style="font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, var(--accent), #FF9F43); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Custom</div>
          <div style="color: var(--text-muted); font-size: 0.85rem;">contact us</div>
        </div>
        <ul style="list-style: none; margin-bottom: 2rem;">
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Multi-school management</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> SSO / LDAP integration</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> Dedicated AI models</li>
          <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> On-premise deployment</li>
          <li style="padding: 0.6rem 0; font-size: 0.9rem; display: flex; gap: 0.75rem; align-items: center;"><span style="color: var(--success);">✓</span> SLA & Priority support</li>
        </ul>
        <a href="contact.html" class="btn btn-secondary" style="width: 100%; justify-content: center;">Contact Sales →</a>
      </div>
    </div>
    <!-- FAQ -->
    <div style="max-width: 700px; margin: 0 auto 4rem;">
      <h2 style="text-align:center; margin-bottom: 2rem; font-size: 1.8rem; font-weight: 800;">Frequently Asked Questions</h2>
      <div class="card" style="margin-bottom: 1rem; padding: 1.25rem 1.5rem;">
        <h4 style="margin-bottom: 0.5rem;">Is there a free trial for Pro?</h4>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Yes! Every Pro School plan includes a 14-day free trial with full access to all features. No credit card required.</p>
      </div>
      <div class="card" style="margin-bottom: 1rem; padding: 1.25rem 1.5rem;">
        <h4 style="margin-bottom: 0.5rem;">Can students use lvlBase on mobile?</h4>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Absolutely! lvlBase is a Progressive Web App (PWA) that works on any device — phone, tablet, or desktop.</p>
      </div>
      <div class="card" style="padding: 1.25rem 1.5rem;">
        <h4 style="margin-bottom: 0.5rem;">Is lvlBase COPPA and GDPR compliant?</h4>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Yes. lvlBase is fully COPPA and GDPR compliant. See our <a href="legal/compliance.html" style="color: var(--primary);">compliance page</a> for details.</p>
      </div>
    </div>
  </div>
</div>
'''))

# public/features.html
write_file('public/features.html', base_page('Features', '../core/css/base.css', '''
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="index.html" class="nav-link">Home</a>
    <a href="features.html" class="nav-link active">Features</a>
    <a href="pricing.html" class="nav-link">Pricing</a>
    <a href="for-schools.html" class="nav-link">For Schools</a>
  </div>
  <div class="navbar-actions">
    <a href="../auth/portal-login.html" class="btn btn-primary">Login →</a>
  </div>
</nav>
<div class="page-wrapper">
  <div class="container">
    <div class="page-header" style="text-align:center; padding: 3rem 0 2rem;">
      <h1 class="page-title" style="font-size: 3rem;">Everything You Need to Gamify Education</h1>
      <p class="page-subtitle" style="font-size: 1.1rem; max-width: 600px; margin: 0.5rem auto 0;">From AI-powered tutoring to epic guild wars — lvlBase transforms ordinary classrooms into legendary academies.</p>
    </div>
    <div class="grid-3" style="margin-bottom: 3rem;">
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">⚔️</div><h3 style="margin-bottom: 0.5rem;">Battle Arena</h3><p style="color:var(--text-muted); font-size:0.9rem;">Real-time 1v1 and team quiz battles with live matchmaking, spectator mode, and tournament brackets.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">🏰</div><h3 style="margin-bottom: 0.5rem;">Guild System</h3><p style="color:var(--text-muted); font-size:0.9rem;">Form guilds like Shadow Wolves, Azure Dragons, and compete in weekly Guild Wars for school dominance.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">🤖</div><h3 style="margin-bottom: 0.5rem;">AI Sage</h3><p style="color:var(--text-muted); font-size:0.9rem;">Personal AI tutor powered by GPT-4 that adapts to each student's learning style and identifies weaknesses.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">📊</div><h3 style="margin-bottom: 0.5rem;">Smart Analytics</h3><p style="color:var(--text-muted); font-size:0.9rem;">Deep insights for teachers, parents, and admins with predictive analytics and intervention alerts.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">🎯</div><h3 style="margin-bottom: 0.5rem;">XP & Ranks</h3><p style="color:var(--text-muted); font-size:0.9rem;">Seven-tier rank system (E → SS) with XP rewards, achievement badges, and seasonal leaderboards.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">💻</div><h3 style="margin-bottom: 0.5rem;">Code Labs</h3><p style="color:var(--text-muted); font-size:0.9rem;">In-browser Python, JavaScript, and Flutter labs with AI code review and real project deployment.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">🔒</div><h3 style="margin-bottom: 0.5rem;">AI Proctoring</h3><p style="color:var(--text-muted); font-size:0.9rem;">Camera-based cheat detection, audio analysis, and tab-switch monitoring for fair assessments.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">👨‍👩‍👧</div><h3 style="margin-bottom: 0.5rem;">Parent Portal</h3><p style="color:var(--text-muted); font-size:0.9rem;">Real-time progress tracking, teacher messaging, screen time controls, and reward systems for parents.</p></div>
      <div class="card"><div style="font-size: 2.5rem; margin-bottom: 1rem;">🏆</div><h3 style="margin-bottom: 0.5rem;">Certificates</h3><p style="color:var(--text-muted); font-size:0.9rem;">Blockchain-verified certificates for course completion, tournament wins, and skill mastery.</p></div>
    </div>
  </div>
</div>
'''))

# public/for-schools.html
write_file('public/for-schools.html', base_page('For Schools', '../core/css/base.css', '''
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="index.html" class="nav-link">Home</a>
    <a href="features.html" class="nav-link">Features</a>
    <a href="pricing.html" class="nav-link">Pricing</a>
    <a href="for-schools.html" class="nav-link active">For Schools</a>
  </div>
  <div class="navbar-actions">
    <a href="../auth/school-onboarding.html" class="btn btn-primary">Apply Now →</a>
  </div>
</nav>
<div class="page-wrapper">
  <div class="container">
    <div style="text-align:center; padding: 4rem 0 3rem;">
      <h1 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem;">Transform Your School into an Epic Academy 🏫</h1>
      <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto 2rem;">lvlBase gives school administrators complete control while making learning the most exciting part of every student\'s day.</p>
      <a href="../auth/school-onboarding.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2.5rem;">Get Your School Started →</a>
    </div>
    <div class="grid-4" style="margin-bottom: 3rem;">
      <div class="card stat-card"><div class="stat-value">47%</div><div class="stat-label">avg. engagement increase</div></div>
      <div class="card stat-card"><div class="stat-value">2.3x</div><div class="stat-label">homework completion rate</div></div>
      <div class="card stat-card"><div class="stat-value">89%</div><div class="stat-label">student satisfaction</div></div>
      <div class="card stat-card"><div class="stat-value">30%</div><div class="stat-label">reduction in disciplinary issues</div></div>
    </div>
    <h2 style="text-align:center; font-size: 2rem; font-weight: 800; margin-bottom: 2rem;">Admin Superpowers 💪</h2>
    <div class="grid-3" style="margin-bottom: 3rem;">
      <div class="card"><h3 style="margin-bottom: 0.75rem;">👥 User Management</h3><p style="color:var(--text-muted); font-size:0.9rem;">Bulk import students and teachers, manage roles, and control access with granular permissions.</p></div>
      <div class="card"><h3 style="margin-bottom: 0.75rem;">📢 Broadcast Center</h3><p style="color:var(--text-muted); font-size:0.9rem;">Send announcements, schedule events, and communicate with the entire school community instantly.</p></div>
      <div class="card"><h3 style="margin-bottom: 0.75rem;">📈 Analytics Dashboard</h3><p style="color:var(--text-muted); font-size:0.9rem;">School-wide performance metrics, teacher effectiveness scores, and early intervention alerts.</p></div>
      <div class="card"><h3 style="margin-bottom: 0.75rem;">🔐 SSO Integration</h3><p style="color:var(--text-muted); font-size:0.9rem;">Connect with Google Workspace, Microsoft 365, Clever, and ClassLink for seamless login.</p></div>
      <div class="card"><h3 style="margin-bottom: 0.75rem;">🚨 Emergency Protocols</h3><p style="color:var(--text-muted); font-size:0.9rem;">Digital lockdown procedures, emergency notifications, and hall pass digital management.</p></div>
      <div class="card"><h3 style="margin-bottom: 0.75rem;">📊 Compliance Reports</h3><p style="color:var(--text-muted); font-size:0.9rem;">Automated FERPA, COPPA, and state-specific compliance reports with one-click data exports.</p></div>
    </div>
  </div>
</div>
'''))

print("Public pages batch 1 created")
