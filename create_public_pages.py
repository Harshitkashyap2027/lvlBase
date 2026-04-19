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
body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
.navbar { position: fixed; top: 0; left: 0; right: 0; height: 65px; background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; }
.navbar-brand { font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-decoration: none; }
.navbar-nav { display: flex; gap: 0.5rem; }
.nav-link { padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }
.nav-link:hover { color: var(--text-light); background: rgba(108,99,255,0.15); }
.page-wrapper { padding-top: 65px; min-height: 100vh; }
.container { max-width: 1200px; margin: 0 auto; padding: 4rem 2rem; }
.card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.5rem; transition: var(--transition); }
.card:hover { border-color: rgba(108,99,255,0.4); box-shadow: var(--shadow); }
.grid-2 { display: grid; grid-template-columns: repeat(2,1fr); gap: 1.5rem; }
.grid-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.5rem; }
.grid-4 { display: grid; grid-template-columns: repeat(4,1fr); gap: 1.5rem; }
.btn { padding: 0.75rem 1.5rem; border-radius: var(--radius); font-family: inherit; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(108,99,255,0.4); }
.btn-ghost { background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }
.hero { text-align: center; padding: 6rem 2rem; }
.hero-title { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem; }
.hero-subtitle { font-size: 1.2rem; color: var(--text-muted); max-width: 600px; margin: 0 auto 2.5rem; }
.footer { background: var(--card-bg); border-top: 1px solid var(--border-color); padding: 3rem 2rem; text-align: center; margin-top: 6rem; }
.form-group { margin-bottom: 1.25rem; }
.form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; }
.form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def pub_page(title, body):
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
<nav class="navbar">
  <a href="index.html" class="navbar-brand">lvlBase ⚡</a>
  <div class="navbar-nav">
    <a href="features.html" class="nav-link">Features</a>
    <a href="pricing.html" class="nav-link">Pricing</a>
    <a href="for-schools.html" class="nav-link">Schools</a>
    <a href="case-studies.html" class="nav-link">Case Studies</a>
  </div>
  <div style="display:flex;gap:0.75rem;">
    <a href="../auth/portal-login.html" class="btn btn-ghost" style="padding:0.5rem 1rem;font-size:0.9rem;">Login</a>
    <a href="../auth/school-onboarding.html" class="btn btn-primary" style="padding:0.5rem 1rem;font-size:0.9rem;">Get Started →</a>
  </div>
</nav>
<div class="page-wrapper">
{body}
<div class="footer">
  <p style="color:var(--text-muted);font-size:0.9rem;">© 2025 lvlBase Inc. · <a href="legal/privacy-policy.html" style="color:var(--text-muted);">Privacy</a> · <a href="legal/terms-of-service.html" style="color:var(--text-muted);">Terms</a> · <a href="legal/compliance.html" style="color:var(--text-muted);">Compliance</a></p>
</div>
</div>
</body>
</html>'''

# public/pricing.html
write_file('public/pricing.html', pub_page('Pricing', '''
<div class="hero">
  <h1 class="hero-title">Simple, <span style="background:linear-gradient(135deg,var(--primary),var(--secondary));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Transparent</span> Pricing</h1>
  <p class="hero-subtitle">Start free, scale as you grow. No per-student limits on Enterprise.</p>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-3" style="margin-bottom:4rem;">
    <div class="card" style="text-align:center;padding:2.5rem;">
      <div style="font-size:1.1rem;font-weight:700;margin-bottom:0.5rem;color:var(--text-muted);">FREE</div>
      <div style="font-size:3rem;font-weight:900;margin-bottom:0.25rem;">$0</div>
      <div style="color:var(--text-muted);font-size:0.9rem;margin-bottom:2rem;">per month, forever</div>
      <ul style="list-style:none;text-align:left;margin-bottom:2rem;font-size:0.9rem;line-height:2;">
        <li>✓ Up to 30 students</li>
        <li>✓ 1 teacher account</li>
        <li>✓ Basic gamification</li>
        <li>✓ Standard quizzes</li>
        <li style="color:var(--text-muted);">✗ AI Sage</li>
        <li style="color:var(--text-muted);">✗ Proctoring</li>
      </ul>
      <a href="../auth/school-onboarding.html" class="btn btn-ghost" style="width:100%;justify-content:center;">Get Started Free</a>
    </div>
    <div class="card" style="text-align:center;padding:2.5rem;border-color:var(--primary);position:relative;">
      <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--primary),var(--primary-dark));color:white;padding:0.3rem 1.5rem;border-radius:20px;font-size:0.8rem;font-weight:700;">MOST POPULAR</div>
      <div style="font-size:1.1rem;font-weight:700;margin-bottom:0.5rem;color:var(--primary);">PRO SCHOOL</div>
      <div style="font-size:3rem;font-weight:900;margin-bottom:0.25rem;">$299</div>
      <div style="color:var(--text-muted);font-size:0.9rem;margin-bottom:2rem;">per month per school</div>
      <ul style="list-style:none;text-align:left;margin-bottom:2rem;font-size:0.9rem;line-height:2;">
        <li>✓ Unlimited students</li>
        <li>✓ All teacher features</li>
        <li>✓ AI Sage chat</li>
        <li>✓ Live proctoring</li>
        <li>✓ Guild Wars</li>
        <li>✓ Parent dashboard</li>
        <li>✓ Analytics & reports</li>
      </ul>
      <a href="../auth/school-onboarding.html" class="btn btn-primary" style="width:100%;justify-content:center;">Start Free Trial →</a>
    </div>
    <div class="card" style="text-align:center;padding:2.5rem;">
      <div style="font-size:1.1rem;font-weight:700;margin-bottom:0.5rem;color:var(--accent);">ENTERPRISE</div>
      <div style="font-size:3rem;font-weight:900;margin-bottom:0.25rem;">Custom</div>
      <div style="color:var(--text-muted);font-size:0.9rem;margin-bottom:2rem;">for districts & groups</div>
      <ul style="list-style:none;text-align:left;margin-bottom:2rem;font-size:0.9rem;line-height:2;">
        <li>✓ Everything in Pro</li>
        <li>✓ Multi-school dashboard</li>
        <li>✓ Custom SSO/SAML</li>
        <li>✓ Custom branding</li>
        <li>✓ Dedicated support</li>
        <li>✓ SLA guarantee</li>
        <li>✓ On-premise option</li>
      </ul>
      <a href="contact.html" class="btn btn-ghost" style="width:100%;justify-content:center;">Contact Sales →</a>
    </div>
  </div>
</div>
'''))

# public/features.html
write_file('public/features.html', pub_page('Features', '''
<div class="hero">
  <h1 class="hero-title">Everything Your School <span style="background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Needs</span></h1>
  <p class="hero-subtitle">A complete educational platform with gamification at its core</p>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-3" style="margin-bottom:3rem;">
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">⚔️</div><h3 style="margin-bottom:0.75rem;">Battle Arena</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">Real-time academic battles between students. 1v1, team battles, and tournaments with XP rewards and rankings.</p></div>
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">🤖</div><h3 style="margin-bottom:0.75rem;">AI Sage</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">24/7 AI tutor that explains concepts, generates personalized quizzes, and identifies knowledge gaps.</p></div>
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">🏰</div><h3 style="margin-bottom:0.75rem;">Guild System</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">Students form guilds (Shadow Wolves, Azure Dragons...) and compete in inter-guild academic wars.</p></div>
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">👁️</div><h3 style="margin-bottom:0.75rem;">AI Proctoring</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">Camera-based exam monitoring with tab-switch detection, gaze tracking, and audio analysis.</p></div>
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">📊</div><h3 style="margin-bottom:0.75rem;">Deep Analytics</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">Detailed dashboards for students, teachers, parents, and admins with actionable insights.</p></div>
    <div class="card"><div style="font-size:3rem;margin-bottom:1rem;">💻</div><h3 style="margin-bottom:0.75rem;">Coding Labs</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">Browser-based Python, Web, and Flutter development environments with AI code review.</p></div>
  </div>
</div>
'''))

# public/for-schools.html
write_file('public/for-schools.html', pub_page('For Schools', '''
<div class="hero">
  <h1 class="hero-title">Transform Your <span style="background:linear-gradient(135deg,var(--primary),var(--success));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">School</span></h1>
  <p class="hero-subtitle">lvlBase helps schools increase student engagement by 340% and improve test scores by 28%</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
    <a href="../auth/school-onboarding.html" class="btn btn-primary" style="font-size:1.1rem;padding:1rem 2.5rem;">Start Free Trial →</a>
    <a href="case-studies.html" class="btn btn-ghost" style="font-size:1.1rem;padding:1rem 2.5rem;">See Results</a>
  </div>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-4" style="margin-bottom:4rem;">
    <div class="card" style="text-align:center;"><div style="font-size:2rem;font-weight:900;color:var(--primary);margin-bottom:0.5rem;">340%</div><p style="color:var(--text-muted);font-size:0.85rem;">Avg engagement increase</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:2rem;font-weight:900;color:var(--success);margin-bottom:0.5rem;">28%</div><p style="color:var(--text-muted);font-size:0.85rem;">Test score improvement</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:2rem;font-weight:900;color:var(--accent);margin-bottom:0.5rem;">1,247</div><p style="color:var(--text-muted);font-size:0.85rem;">Schools trust lvlBase</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:2rem;font-weight:900;color:var(--secondary);margin-bottom:0.5rem;">98%</div><p style="color:var(--text-muted);font-size:0.85rem;">School renewal rate</p></div>
  </div>
</div>
'''))

# public/for-teachers.html
write_file('public/for-teachers.html', pub_page('For Teachers', '''
<div class="hero">
  <h1 class="hero-title">Teaching Made <span style="background:linear-gradient(135deg,var(--success),var(--primary));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Magical</span></h1>
  <p class="hero-subtitle">Reduce grading time by 70% with AI. Create engaging quizzes in minutes. Monitor every student in real time.</p>
  <a href="../auth/signup-teacher.html" class="btn btn-primary" style="font-size:1.1rem;padding:1rem 2.5rem;">Join as Teacher →</a>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-3">
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">⚡</div><h3 style="margin-bottom:0.75rem;">AI Quiz Builder</h3><p style="color:var(--text-muted);font-size:0.9rem;">Create a 10-question quiz on any topic in under 60 seconds. AI generates, you approve.</p></div>
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">🤖</div><h3 style="margin-bottom:0.75rem;">AI Grader</h3><p style="color:var(--text-muted);font-size:0.9rem;">Grade essays and open-ended answers with your rubric automatically. Review and approve in seconds.</p></div>
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">👁️</div><h3 style="margin-bottom:0.75rem;">Live Monitoring</h3><p style="color:var(--text-muted);font-size:0.9rem;">See every student in a thumbnail grid during exams. AI flags suspicious activity instantly.</p></div>
  </div>
</div>
'''))

# public/for-parents.html
write_file('public/for-parents.html', pub_page('For Parents', '''
<div class="hero">
  <h1 class="hero-title">Stay Connected to Your <span style="background:linear-gradient(135deg,var(--accent),var(--warning));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Child\'s Journey</span></h1>
  <p class="hero-subtitle">Real-time visibility into your child\'s academic progress, attendance, and gaming habits</p>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-3">
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">📊</div><h3 style="margin-bottom:0.75rem;">Daily Reports</h3><p style="color:var(--text-muted);font-size:0.9rem;">Get daily summaries of what your child learned, their XP gains, and upcoming assignments.</p></div>
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">⏰</div><h3 style="margin-bottom:0.75rem;">Screen Time Controls</h3><p style="color:var(--text-muted);font-size:0.9rem;">Set daily limits, bedtime blocks, and monitor how much time is spent on study vs games.</p></div>
    <div class="card"><div style="font-size:2.5rem;margin-bottom:1rem;">💬</div><h3 style="margin-bottom:0.75rem;">Teacher Connect</h3><p style="color:var(--text-muted);font-size:0.9rem;">Message teachers directly, schedule PT meetings, and track any concerns raised.</p></div>
  </div>
</div>
'''))

# public/case-studies.html
write_file('public/case-studies.html', pub_page('Case Studies', '''
<div class="hero">
  <h1 class="hero-title">Real Schools, <span style="background:linear-gradient(135deg,var(--primary),var(--success));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Real Results</span></h1>
  <p class="hero-subtitle">See how schools around the world transformed learning with lvlBase</p>
</div>
<div class="container" style="padding-top:0;">
  <div class="grid-3" style="margin-bottom:3rem;">
    <div class="card"><div style="font-size:1rem;font-weight:600;color:var(--primary);margin-bottom:0.5rem;">🏫 RIVERSIDE ACADEMY, CA</div><h3 style="margin-bottom:0.75rem;font-size:1.2rem;">From 67% to 94% Pass Rate in One Year</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;margin-bottom:1rem;">After implementing lvlBase, battle-mode learning boosted student engagement dramatically.</p><div style="display:flex;gap:1rem;"><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--success);">+27%</div><div style="font-size:0.75rem;color:var(--text-muted);">Pass rate</div></div><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--primary);">340%</div><div style="font-size:0.75rem;color:var(--text-muted);">Engagement</div></div></div></div>
    <div class="card"><div style="font-size:1rem;font-weight:600;color:var(--success);margin-bottom:0.5rem;">🏫 WESTWOOD PREP, NY</div><h3 style="margin-bottom:0.75rem;font-size:1.2rem;">Teachers Save 8 Hours Per Week</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;margin-bottom:1rem;">AI grading and quiz building freed up precious time for actual teaching.</p><div style="display:flex;gap:1rem;"><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--success);">8h/week</div><div style="font-size:0.75rem;color:var(--text-muted);">Time saved</div></div><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--primary);">4.9★</div><div style="font-size:0.75rem;color:var(--text-muted);">Teacher rating</div></div></div></div>
    <div class="card"><div style="font-size:1rem;font-weight:600;color:var(--accent);margin-bottom:0.5rem;">🏫 LINCOLN HIGH, IL</div><h3 style="margin-bottom:0.75rem;font-size:1.2rem;">Zero Cheating in First Term</h3><p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;margin-bottom:1rem;">AI proctoring eliminated academic dishonesty completely in their first implementation term.</p><div style="display:flex;gap:1rem;"><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--danger);">-100%</div><div style="font-size:0.75rem;color:var(--text-muted);">Cheating</div></div><div style="text-align:center;flex:1;"><div style="font-weight:700;color:var(--success);">+19%</div><div style="font-size:0.75rem;color:var(--text-muted);">Test scores</div></div></div></div>
  </div>
</div>
'''))

# public/faq.html
write_file('public/faq.html', pub_page('FAQ', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">❓ Frequently Asked Questions</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:3rem;">Everything you need to know about lvlBase</p>
  <div style="max-width:800px;margin:0 auto;">
    <details style="border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem 1.5rem;margin-bottom:0.75rem;cursor:pointer;"><summary style="font-weight:600;font-size:1rem;cursor:pointer;">Is lvlBase safe for children? Are you COPPA compliant?</summary><p style="color:var(--text-muted);margin-top:0.75rem;line-height:1.6;font-size:0.9rem;">Yes! lvlBase is fully COPPA compliant. We never share student data with third parties, collect minimal necessary data, and all data is encrypted. Schools sign our Data Processing Agreements (DPAs). See our <a href="legal/compliance.html" style="color:var(--primary);">Compliance page</a> for details.</p></details>
    <details style="border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem 1.5rem;margin-bottom:0.75rem;cursor:pointer;"><summary style="font-weight:600;font-size:1rem;cursor:pointer;">How does the XP and ranking system work?</summary><p style="color:var(--text-muted);margin-top:0.75rem;line-height:1.6;font-size:0.9rem;">Students earn XP through quizzes, battles, homework, and streaks. Rankings go E → D → C → B → A → S → SS. XP is only earned through genuine academic activity — not gaming shortcuts.</p></details>
    <details style="border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem 1.5rem;margin-bottom:0.75rem;cursor:pointer;"><summary style="font-weight:600;font-size:1rem;cursor:pointer;">Can I use lvlBase with my existing LMS (Canvas, Google Classroom)?</summary><p style="color:var(--text-muted);margin-top:0.75rem;line-height:1.6;font-size:0.9rem;">Yes! lvlBase integrates with Google Classroom, Canvas, Clever, and ClassLink via our API. Student rosters and assignments can be synced automatically.</p></details>
    <details style="border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem 1.5rem;margin-bottom:0.75rem;cursor:pointer;"><summary style="font-weight:600;font-size:1rem;cursor:pointer;">What devices does lvlBase support?</summary><p style="color:var(--text-muted);margin-top:0.75rem;line-height:1.6;font-size:0.9rem;">lvlBase works on any modern browser — Chromebooks, iPads, Windows, Mac, and Android tablets. We also have installable PWA apps for offline support.</p></details>
    <details style="border:1px solid var(--border-color);border-radius:var(--radius);padding:1rem 1.5rem;cursor:pointer;"><summary style="font-weight:600;font-size:1rem;cursor:pointer;">How long does school onboarding take?</summary><p style="color:var(--text-muted);margin-top:0.75rem;line-height:1.6;font-size:0.9rem;">Most schools are fully set up within 48 hours. Our onboarding team handles account creation, teacher training (1-2 hours), and student imports. We offer live support throughout.</p></details>
  </div>
</div>
'''))

# public/contact.html
write_file('public/contact.html', pub_page('Contact', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">📬 Get in Touch</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:3rem;">We\'d love to hear from you</p>
  <div class="grid-2" style="max-width:900px;margin:0 auto;">
    <div class="card">
      <h3 style="margin-bottom:1.5rem;">Send us a Message</h3>
      <div class="form-group"><label class="form-label">Your Name</label><input class="form-control" type="text" placeholder="Your full name"></div>
      <div class="form-group"><label class="form-label">Email</label><input class="form-control" type="email" placeholder="you@school.edu"></div>
      <div class="form-group"><label class="form-label">I am a...</label><select class="form-control"><option>School Administrator</option><option>Teacher</option><option>Parent</option><option>Student</option><option>Investor/Press</option></select></div>
      <div class="form-group"><label class="form-label">Message</label><textarea class="form-control" rows="5" style="height:120px;resize:vertical;" placeholder="How can we help?"></textarea></div>
      <button class="btn btn-primary">Send Message 📤</button>
    </div>
    <div>
      <div class="card" style="margin-bottom:1.5rem;"><div style="font-size:2rem;margin-bottom:0.75rem;">💬</div><h3 style="margin-bottom:0.5rem;">Live Chat</h3><p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:1rem;">Available Mon-Fri 9AM-6PM EST</p><button class="btn btn-primary" style="font-size:0.9rem;">Start Chat</button></div>
      <div class="card" style="margin-bottom:1.5rem;"><div style="font-size:2rem;margin-bottom:0.75rem;">📧</div><h3 style="margin-bottom:0.5rem;">Email</h3><p style="color:var(--primary);font-weight:600;">hello@lvlbase.io</p></div>
      <div class="card"><div style="font-size:2rem;margin-bottom:0.75rem;">📞</div><h3 style="margin-bottom:0.5rem;">Sales</h3><p style="color:var(--primary);font-weight:600;">+1 (888) 585-2273</p></div>
    </div>
  </div>
</div>
'''))

# public/system-status.html
write_file('public/system-status.html', pub_page('System Status', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">⚡ System Status</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:1rem;">Real-time status of all lvlBase services</p>
  <div style="text-align:center;margin-bottom:3rem;"><span style="background:rgba(0,209,178,0.15);color:var(--success);padding:0.75rem 2rem;border-radius:20px;font-weight:700;font-size:1.1rem;">✓ All Systems Operational</span></div>
  <div class="card" style="max-width:700px;margin:0 auto;">
    <div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Web Application</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>API Services</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>AI Sage (GPT)</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Realtime Database</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Authentication</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Video/WebRTC</span><span style="color:var(--success);">✓ Operational</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.75rem;"><span>CDN / File Storage</span><span style="color:var(--success);">✓ Operational</span></div>
    </div>
  </div>
</div>
'''))

# public/404.html
write_file('public/404.html', pub_page('404 Not Found', '''
<div style="text-align:center;padding:8rem 2rem;">
  <div style="font-size:8rem;margin-bottom:1rem;">💀</div>
  <h1 style="font-size:4rem;font-weight:900;margin-bottom:0.5rem;">404</h1>
  <p style="font-size:1.5rem;color:var(--text-muted);margin-bottom:2rem;">Quest not found, adventurer!</p>
  <p style="color:var(--text-muted);margin-bottom:2.5rem;max-width:400px;margin-left:auto;margin-right:auto;">The page you\'re looking for has been defeated and sent to the shadow realm. Let\'s get you back to safety.</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
    <a href="index.html" class="btn btn-primary" style="font-size:1rem;padding:1rem 2rem;">← Back to Home</a>
    <a href="../auth/portal-login.html" class="btn btn-ghost" style="font-size:1rem;padding:1rem 2rem;">Login →</a>
  </div>
</div>
'''))

# public/offline.html
write_file('public/offline.html', pub_page('Offline', '''
<div style="text-align:center;padding:8rem 2rem;">
  <div style="font-size:8rem;margin-bottom:1rem;">📡</div>
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">You\'re Offline</h1>
  <p style="color:var(--text-muted);font-size:1.1rem;margin-bottom:1rem;">No internet connection detected</p>
  <p style="color:var(--text-muted);margin-bottom:2.5rem;max-width:400px;margin-left:auto;margin-right:auto;">Don\'t worry — your XP and progress were saved! Connect to the internet to continue your quest.</p>
  <button onclick="window.location.reload()" class="btn btn-primary" style="font-size:1rem;padding:1rem 2rem;">🔄 Try Again</button>
</div>
'''))

# public/maintenance.html
write_file('public/maintenance.html', pub_page('Maintenance', '''
<div style="text-align:center;padding:8rem 2rem;">
  <div style="font-size:8rem;margin-bottom:1rem;">⚙️</div>
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">Level Up in Progress</h1>
  <p style="color:var(--text-muted);font-size:1.1rem;margin-bottom:1rem;">We\'re deploying exciting new features!</p>
  <div style="max-width:400px;margin:0 auto 2.5rem;">
    <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:12px;margin-bottom:0.5rem;overflow:hidden;">
      <div style="background:linear-gradient(135deg,var(--primary),var(--success));border-radius:20px;width:73%;height:100%;animation:loading 2s infinite;"></div>
    </div>
    <p style="color:var(--text-muted);font-size:0.85rem;">73% complete · Back online in ~30 minutes</p>
  </div>
  <a href="system-status.html" class="btn btn-ghost" style="font-size:0.95rem;">Check Status Page</a>
</div>
<style>@keyframes loading { 0% { width: 60%; } 50% { width: 85%; } 100% { width: 73%; } }</style>
'''))

# public/webinars.html
write_file('public/webinars.html', pub_page('Webinars & Events', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">🎓 Webinars & Events</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:3rem;">Learn, grow, and connect with educators worldwide</p>
  <h2 style="font-size:1.3rem;font-weight:700;margin-bottom:1.5rem;">📅 Upcoming</h2>
  <div class="grid-3" style="margin-bottom:3rem;">
    <div class="card"><div style="background:rgba(108,99,255,0.15);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;"><div style="font-weight:700;font-size:1.1rem;">JAN 25</div><div style="font-size:0.85rem;color:var(--text-muted);">2:00 PM EST</div></div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Getting Started with AI Grading</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Save 8 hours a week on grading with AI. Live demo included.</p><button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Register Free</button></div>
    <div class="card"><div style="background:rgba(0,209,178,0.1);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;"><div style="font-weight:700;font-size:1.1rem;">FEB 5</div><div style="font-size:0.85rem;color:var(--text-muted);">3:00 PM EST</div></div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Gamification That Actually Works</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Best practices for using XP and battles to drive real learning.</p><button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Register Free</button></div>
    <div class="card"><div style="background:rgba(255,215,0,0.1);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;"><div style="font-weight:700;font-size:1.1rem;">FEB 15</div><div style="font-size:0.85rem;color:var(--text-muted);">1:00 PM EST</div></div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Admin Analytics Deep Dive</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">How to use school data to make better decisions.</p><button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Register Free</button></div>
  </div>
</div>
'''))

# public/roi-calculator.html
write_file('public/roi-calculator.html', pub_page('ROI Calculator', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">💰 ROI Calculator</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:3rem;">Calculate the value lvlBase brings to your school</p>
  <div class="grid-2" style="max-width:900px;margin:0 auto;">
    <div class="card">
      <h3 style="margin-bottom:1.5rem;font-size:1rem;">Enter Your School Details</h3>
      <div class="form-group"><label class="form-label">Number of Students</label><input class="form-control" type="number" id="students" value="500" oninput="calc()"></div>
      <div class="form-group"><label class="form-label">Number of Teachers</label><input class="form-control" type="number" id="teachers" value="30" oninput="calc()"></div>
      <div class="form-group"><label class="form-label">Avg Teacher Salary ($/year)</label><input class="form-control" type="number" id="salary" value="55000" oninput="calc()"></div>
      <div class="form-group"><label class="form-label">Current Pass Rate (%)</label><input class="form-control" type="number" id="passrate" value="75" oninput="calc()"></div>
    </div>
    <div class="card" id="results">
      <h3 style="margin-bottom:1.5rem;font-size:1rem;">📊 Your Estimated ROI</h3>
      <div style="margin-bottom:1rem;padding:1rem;background:rgba(0,209,178,0.1);border-radius:var(--radius);">
        <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Teacher Time Saved</div>
        <div id="r-time" style="font-size:1.5rem;font-weight:700;color:var(--success);">$24,750/year</div>
      </div>
      <div style="margin-bottom:1rem;padding:1rem;background:rgba(108,99,255,0.1);border-radius:var(--radius);">
        <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Estimated Cost (Pro)</div>
        <div id="r-cost" style="font-size:1.5rem;font-weight:700;color:var(--primary);">$3,588/year</div>
      </div>
      <div style="padding:1rem;background:rgba(255,215,0,0.1);border-radius:var(--radius);border:2px solid rgba(255,215,0,0.3);">
        <div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Net ROI</div>
        <div id="r-roi" style="font-size:2rem;font-weight:900;color:var(--accent);">590%</div>
      </div>
    </div>
  </div>
</div>
<script>
function calc() {
  const t = +document.getElementById("teachers").value || 0;
  const s = +document.getElementById("salary").value || 0;
  const timeSaved = t * (s * 0.15);
  const cost = 299 * 12;
  const roi = Math.round((timeSaved - cost) / cost * 100);
  document.getElementById("r-time").textContent = "$" + timeSaved.toLocaleString() + "/year";
  document.getElementById("r-cost").textContent = "$" + cost.toLocaleString() + "/year";
  document.getElementById("r-roi").textContent = roi + "%";
}
</script>
'''))

# public/press.html
write_file('public/press.html', pub_page('Press & Media', '''
<div class="container">
  <h1 style="font-size:2.5rem;font-weight:900;text-align:center;margin-bottom:0.75rem;">📰 Press & Media</h1>
  <p style="text-align:center;color:var(--text-muted);margin-bottom:3rem;">Latest news, press releases, and media resources</p>
  <div class="grid-3" style="margin-bottom:3rem;">
    <div class="card"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.5rem;">TECHCRUNCH · JAN 10, 2025</div><h3 style="margin-bottom:0.75rem;font-size:1rem;">lvlBase Raises $24M Series B to Gamify Education Globally</h3><a href="#" style="color:var(--primary);font-size:0.85rem;font-weight:600;">Read Article →</a></div>
    <div class="card"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.5rem;">EDWEEK · DEC 5, 2024</div><h3 style="margin-bottom:0.75rem;font-size:1rem;">The Platform That\'s Making Math Students Actually Want to Study</h3><a href="#" style="color:var(--primary);font-size:0.85rem;font-weight:600;">Read Article →</a></div>
    <div class="card"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.5rem;">FORBES · NOV 20, 2024</div><h3 style="margin-bottom:0.75rem;font-size:1rem;">30 Under 30 in Education: lvlBase Founders Named</h3><a href="#" style="color:var(--primary);font-size:0.85rem;font-weight:600;">Read Article →</a></div>
  </div>
  <div class="card" style="max-width:700px;margin:0 auto;text-align:center;padding:3rem;">
    <h3 style="margin-bottom:1rem;">Press Inquiries</h3>
    <p style="color:var(--text-muted);margin-bottom:1.5rem;">For interviews, press kit, or media requests, contact our PR team.</p>
    <a href="mailto:press@lvlbase.io" class="btn btn-primary">press@lvlbase.io</a>
  </div>
</div>
'''))

# Legal pages
def legal_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <a href="../index.html" class="navbar-brand">lvlBase ⚡</a>
  <div class="navbar-nav">
    <a href="../pricing.html" class="nav-link">Pricing</a>
    <a href="../contact.html" class="nav-link">Contact</a>
  </div>
</nav>
<div class="page-wrapper">
{body}
</div>
</body>
</html>'''

write_file('public/legal/privacy-policy.html', legal_page('Privacy Policy', '''
<div class="container" style="max-width:800px;">
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">Privacy Policy</h1>
  <p style="color:var(--text-muted);margin-bottom:3rem;">Last updated: January 15, 2025</p>
  <div style="line-height:1.8;font-size:0.95rem;color:var(--text-muted);">
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">1. Information We Collect</h2>
    <p>We collect information you provide directly (name, email, school information), information generated by using our services (XP, quiz results, attendance), and device/browser information for security purposes.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">2. How We Use Your Information</h2>
    <p>We use collected information to: provide and improve our educational services, personalize learning experiences, communicate with users, and ensure platform security. We never sell student data to third parties.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">3. Data Sharing</h2>
    <p>Student data is only shared with: the school/district associated with the student, teachers and administrators at that school, and service providers who process data on our behalf under strict DPAs.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">4. Student Data (FERPA/COPPA)</h2>
    <p>For users under 13, we comply with COPPA. Schools provide verifiable parental consent. We do not use student data for targeted advertising. Parents can request data deletion at any time.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">5. Contact</h2>
    <p>Privacy questions: privacy@lvlbase.io · +1 (888) 585-2273</p>
  </div>
</div>
'''))

write_file('public/legal/terms-of-service.html', legal_page('Terms of Service', '''
<div class="container" style="max-width:800px;">
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">Terms of Service</h1>
  <p style="color:var(--text-muted);margin-bottom:3rem;">Last updated: January 15, 2025</p>
  <div style="line-height:1.8;font-size:0.95rem;color:var(--text-muted);">
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">1. Acceptance of Terms</h2>
    <p>By accessing lvlBase, you agree to these terms. Schools accept on behalf of their students and staff. Users under 13 require parental/school consent.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">2. Acceptable Use</h2>
    <p>You agree not to: share accounts, use AI to cheat on assessments, harass other users, attempt to hack or disrupt the platform, or use the service for any illegal activity.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">3. Academic Integrity</h2>
    <p>The XP and ranking system is designed to reward genuine learning. Any attempt to manipulate scores, use bots, or cheat on exams will result in account suspension.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">4. Subscription & Payments</h2>
    <p>Subscriptions renew automatically. Cancellation takes effect at the end of the billing period. Refunds are available within 30 days for annual plans if no significant data has been created.</p>
  </div>
</div>
'''))

write_file('public/legal/compliance.html', legal_page('Compliance', '''
<div class="container" style="max-width:800px;">
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">🔒 Compliance & Certifications</h1>
  <p style="color:var(--text-muted);margin-bottom:3rem;">lvlBase takes student safety and data privacy seriously</p>
  <div class="grid-2" style="margin-bottom:3rem;">
    <div class="card" style="text-align:center;"><div style="font-size:3rem;margin-bottom:0.75rem;">🇺🇸</div><h3 style="margin-bottom:0.5rem;">FERPA Compliant</h3><p style="color:var(--text-muted);font-size:0.85rem;">Full compliance with Family Educational Rights and Privacy Act</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:3rem;margin-bottom:0.75rem;">👶</div><h3 style="margin-bottom:0.5rem;">COPPA Compliant</h3><p style="color:var(--text-muted);font-size:0.85rem;">Compliant for users under 13 with school-based consent</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:3rem;margin-bottom:0.75rem;">🇪🇺</div><h3 style="margin-bottom:0.5rem;">GDPR Compliant</h3><p style="color:var(--text-muted);font-size:0.85rem;">Full EU data protection regulation compliance with DPAs</p></div>
    <div class="card" style="text-align:center;"><div style="font-size:3rem;margin-bottom:0.75rem;">🔐</div><h3 style="margin-bottom:0.5rem;">SOC 2 Type II</h3><p style="color:var(--text-muted);font-size:0.85rem;">Annual security audits by independent third parties</p></div>
  </div>
</div>
'''))

write_file('public/legal/security-whitepaper.html', legal_page('Security Whitepaper', '''
<div class="container" style="max-width:800px;">
  <h1 style="font-size:2.5rem;font-weight:900;margin-bottom:0.75rem;">🔐 Security Whitepaper</h1>
  <p style="color:var(--text-muted);margin-bottom:3rem;">Technical overview of lvlBase security architecture</p>
  <div style="line-height:1.8;font-size:0.95rem;color:var(--text-muted);">
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">Infrastructure</h2>
    <p>lvlBase runs on Google Cloud Platform and Firebase. All data is encrypted at rest (AES-256) and in transit (TLS 1.3). We use Google Cloud Armor for DDoS protection and Cloudflare as CDN.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">Authentication</h2>
    <p>We support Google OAuth, Microsoft SSO, Clever, and ClassLink. All sessions use JWT tokens with 24-hour expiration. 2FA is available and recommended for admin accounts.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">Data Access Controls</h2>
    <p>Role-based access control (RBAC) ensures students can only see their own data. Teachers see their class only. Admins see their school only. Super admins access all data under strict audit logging.</p>
    <h2 style="color:var(--text-light);margin:2rem 0 0.75rem;">Incident Response</h2>
    <p>We maintain a 24/7 security operations team. In case of a breach, affected customers are notified within 72 hours per GDPR requirements.</p>
  </div>
</div>
'''))

print("Public pages created")
