import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

BASE_STYLES = '''
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: "Poppins", sans-serif; background: var(--dark-bg); color: var(--text-light); }
    :root {
      --primary: #6C63FF; --primary-dark: #5A52E8; --secondary: #FF6B6B;
      --accent: #FFD700; --success: #00D1B2; --warning: #FF9F43; --danger: #FF4444;
      --dark-bg: #0A0A1A; --card-bg: #1A1A2E; --border-color: rgba(108,99,255,0.2);
      --text-light: #E8E8FF; --text-muted: #8892A4; --radius: 12px; --radius-xl: 24px;
      --shadow: 0 4px 20px rgba(0,0,0,0.3); --transition: all 0.3s ease;
    }
    .navbar { position: fixed; top: 0; left: 0; right: 0; height: 65px; background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; }
    .navbar-brand { font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .navbar-nav { display: flex; gap: 0.5rem; }
    .nav-link { padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }
    .nav-link:hover, .nav-link.active { color: var(--text-light); background: rgba(108,99,255,0.15); }
    .navbar-actions { display: flex; align-items: center; gap: 1rem; }
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
    .stat-value { font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .stat-label { color: var(--text-muted); font-size: 0.85rem; margin-top: 0.25rem; }
    @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }
'''

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

def pub_nav(active=''):
    return f'''<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="index.html" class="nav-link{"  active" if active=="home" else ""}">Home</a>
    <a href="features.html" class="nav-link{"  active" if active=="features" else ""}">Features</a>
    <a href="pricing.html" class="nav-link{"  active" if active=="pricing" else ""}">Pricing</a>
    <a href="for-schools.html" class="nav-link{"  active" if active=="schools" else ""}">For Schools</a>
    <a href="faq.html" class="nav-link{"  active" if active=="faq" else ""}">FAQ</a>
  </div>
  <div class="navbar-actions">
    <a href="../auth/portal-login.html" class="btn btn-primary">Login →</a>
  </div>
</nav>'''

# public/for-teachers.html
write_file('public/for-teachers.html', page('For Teachers', '../core/css/base.css', pub_nav(''), '''
<div style="text-align:center; padding: 4rem 0 3rem;">
  <h1 style="font-size:3rem; font-weight:900; margin-bottom:1rem;">Supercharge Your Teaching 👨‍🏫</h1>
  <p style="color:var(--text-muted); font-size:1.1rem; max-width:600px; margin:0 auto 2rem;">lvlBase gives teachers powerful tools to engage students, automate grading, and track every learner's journey.</p>
  <a href="../auth/signup-teacher.html" class="btn btn-primary" style="font-size:1.1rem; padding:1rem 2.5rem;">Join as Teacher →</a>
</div>
<div class="grid-3" style="margin-bottom:3rem;">
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">🤖</div><h3 style="margin-bottom:0.5rem;">AI Grader</h3><p style="color:var(--text-muted); font-size:0.9rem;">Grade essays, code submissions, and open-ended answers automatically with AI and custom rubrics.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">📋</div><h3 style="margin-bottom:0.5rem;">Question Bank</h3><p style="color:var(--text-muted); font-size:0.9rem;">Access thousands of curriculum-aligned questions or create your own and share with colleagues.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">👁️</div><h3 style="margin-bottom:0.5rem;">Live Monitor</h3><p style="color:var(--text-muted); font-size:0.9rem;">Watch student screens in real-time during exams with AI-powered cheat detection alerts.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">📊</div><h3 style="margin-bottom:0.5rem;">Gradebook</h3><p style="color:var(--text-muted); font-size:0.9rem;">Automatic grade calculations, weighted assignments, and integration with school SIS systems.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">🎮</div><h3 style="margin-bottom:0.5rem;">Quest Builder</h3><p style="color:var(--text-muted); font-size:0.9rem;">Turn any lesson into a gamified quest with XP rewards, badges, and progressive difficulty levels.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">💬</div><h3 style="margin-bottom:0.5rem;">Parent Connect</h3><p style="color:var(--text-muted); font-size:0.9rem;">Direct messaging with parents, schedule PT meetings, and auto-send progress reports.</p></div>
</div>
'''))

# public/for-parents.html
write_file('public/for-parents.html', page('For Parents', '../core/css/base.css', pub_nav(''), '''
<div style="text-align:center; padding: 4rem 0 3rem;">
  <h1 style="font-size:3rem; font-weight:900; margin-bottom:1rem;">Stay Connected to Your Child's Journey 👨‍👩‍👧</h1>
  <p style="color:var(--text-muted); font-size:1.1rem; max-width:600px; margin:0 auto 2rem;">Get real-time insights into your child's academic performance, screen time, and social interactions.</p>
  <a href="../auth/portal-login.html" class="btn btn-primary" style="font-size:1.1rem; padding:1rem 2.5rem;">Parent Login →</a>
</div>
<div class="grid-3" style="margin-bottom:3rem;">
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">📈</div><h3 style="margin-bottom:0.5rem;">Progress Reports</h3><p style="color:var(--text-muted); font-size:0.9rem;">Weekly AI-generated reports showing XP earned, subjects mastered, and areas needing attention.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">⏰</div><h3 style="margin-bottom:0.5rem;">Screen Time Controls</h3><p style="color:var(--text-muted); font-size:0.9rem;">Set daily usage limits, block non-study hours, and get alerts when limits approach.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">💬</div><h3 style="margin-bottom:0.5rem;">Teacher Messages</h3><p style="color:var(--text-muted); font-size:0.9rem;">Direct communication with teachers and schedule parent-teacher meetings from the app.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">🎁</div><h3 style="margin-bottom:0.5rem;">Reward System</h3><p style="color:var(--text-muted); font-size:0.9rem;">Set up allowance-linked rewards for academic achievements — motivate through real incentives.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">📅</div><h3 style="margin-bottom:0.5rem;">Attendance Tracker</h3><p style="color:var(--text-muted); font-size:0.9rem;">Real-time attendance notifications and monthly attendance analytics for your child.</p></div>
  <div class="card"><div style="font-size:2rem; margin-bottom:0.75rem;">💳</div><h3 style="margin-bottom:0.5rem;">Payments</h3><p style="color:var(--text-muted); font-size:0.9rem;">Pay school fees, buy XP boosters, and manage your subscription all in one place.</p></div>
</div>
'''))

# public/case-studies.html
write_file('public/case-studies.html', page('Case Studies', '../core/css/base.css', pub_nav(''), '''
<div style="padding: 3rem 0 2rem;">
  <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">Success Stories 🏆</h1>
  <p style="color:var(--text-muted); font-size:1rem; margin-bottom:3rem;">Real schools, real results. See how lvlBase transformed these institutions.</p>
  <div class="grid-2" style="margin-bottom:3rem;">
    <div class="card">
      <div style="background:linear-gradient(135deg,rgba(108,99,255,0.2),rgba(255,107,107,0.1)); border-radius:var(--radius); padding:1.5rem; margin-bottom:1.5rem; text-align:center;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🏫</div>
        <h3 style="font-size:1.2rem;">Riverside Academy, CA</h3>
        <p style="color:var(--text-muted); font-size:0.85rem;">1,200 students · Grades 6-12</p>
      </div>
      <div class="grid-3" style="margin-bottom:1rem; gap:1rem;">
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--success);">+63%</div><div style="font-size:0.75rem; color:var(--text-muted);">engagement</div></div>
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--accent);">2.8x</div><div style="font-size:0.75rem; color:var(--text-muted);">homework rate</div></div>
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--primary);">A-</div><div style="font-size:0.75rem; color:var(--text-muted);">avg grade up</div></div>
      </div>
      <p style="color:var(--text-muted); font-size:0.9rem; font-style:italic;">"lvlBase completely changed how our students perceive homework. It stopped being a chore and became something they looked forward to." — Principal Martinez</p>
    </div>
    <div class="card">
      <div style="background:linear-gradient(135deg,rgba(0,209,178,0.15),rgba(108,99,255,0.1)); border-radius:var(--radius); padding:1.5rem; margin-bottom:1.5rem; text-align:center;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🏫</div>
        <h3 style="font-size:1.2rem;">Westwood Prep, NY</h3>
        <p style="color:var(--text-muted); font-size:0.85rem;">800 students · Grades 9-12</p>
      </div>
      <div class="grid-3" style="margin-bottom:1rem; gap:1rem;">
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--success);">+41%</div><div style="font-size:0.75rem; color:var(--text-muted);">test scores</div></div>
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--accent);">95%</div><div style="font-size:0.75rem; color:var(--text-muted);">satisfaction</div></div>
        <div style="text-align:center;"><div style="font-size:1.5rem; font-weight:900; color:var(--primary);">-45%</div><div style="font-size:0.75rem; color:var(--text-muted);">dropout risk</div></div>
      </div>
      <p style="color:var(--text-muted); font-size:0.9rem; font-style:italic;">"The AI Sage identified that 23% of our students had gaps in algebra foundations — we intervened and saw dramatic improvements within 6 weeks." — Head of Academics</p>
    </div>
  </div>
</div>
'''))

# public/webinars.html
write_file('public/webinars.html', page('Webinars', '../core/css/base.css', pub_nav(''), '''
<div style="padding: 3rem 0 2rem;">
  <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">Webinars & Events 📅</h1>
  <p style="color:var(--text-muted); font-size:1rem; margin-bottom:3rem;">Learn from educators, admins, and edtech experts. All webinars are free for lvlBase users.</p>
  <h2 style="font-size:1.3rem; font-weight:700; margin-bottom:1.5rem; color:var(--primary);">🔴 Upcoming Live Events</h2>
  <div class="grid-3" style="margin-bottom:3rem;">
    <div class="card">
      <div style="background:rgba(255,68,68,0.15); color:var(--danger); padding:0.3rem 0.75rem; border-radius:20px; font-size:0.75rem; font-weight:700; display:inline-block; margin-bottom:1rem;">LIVE · Jan 20</div>
      <h3 style="margin-bottom:0.5rem; font-size:1rem;">Gamifying Math: From Dread to Delight</h3>
      <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:1rem;">Learn how to turn algebra problems into epic quests that students actually want to complete.</p>
      <p style="color:var(--text-muted); font-size:0.8rem; margin-bottom:1rem;">🕐 2:00 PM EST · ⏱ 60 min</p>
      <a href="#" class="btn btn-primary" style="font-size:0.85rem; padding:0.5rem 1rem;">Register Free →</a>
    </div>
    <div class="card">
      <div style="background:rgba(255,159,67,0.15); color:var(--warning); padding:0.3rem 0.75rem; border-radius:20px; font-size:0.75rem; font-weight:700; display:inline-block; margin-bottom:1rem;">UPCOMING · Jan 27</div>
      <h3 style="margin-bottom:0.5rem; font-size:1rem;">AI Proctoring: Ethics & Effectiveness</h3>
      <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:1rem;">A deep dive into responsible AI use for exam monitoring and how to communicate it to parents.</p>
      <p style="color:var(--text-muted); font-size:0.8rem; margin-bottom:1rem;">🕐 3:00 PM EST · ⏱ 45 min</p>
      <a href="#" class="btn btn-primary" style="font-size:0.85rem; padding:0.5rem 1rem;">Register Free →</a>
    </div>
    <div class="card">
      <div style="background:rgba(108,99,255,0.15); color:var(--primary); padding:0.3rem 0.75rem; border-radius:20px; font-size:0.75rem; font-weight:700; display:inline-block; margin-bottom:1rem;">UPCOMING · Feb 3</div>
      <h3 style="margin-bottom:0.5rem; font-size:1rem;">Guild Wars: Building School Community</h3>
      <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:1rem;">How to leverage the guild system to reduce bullying and build positive peer relationships.</p>
      <p style="color:var(--text-muted); font-size:0.8rem; margin-bottom:1rem;">🕐 1:00 PM EST · ⏱ 60 min</p>
      <a href="#" class="btn btn-primary" style="font-size:0.85rem; padding:0.5rem 1rem;">Register Free →</a>
    </div>
  </div>
</div>
'''))

# public/roi-calculator.html
write_file('public/roi-calculator.html', page('ROI Calculator', '../core/css/base.css', pub_nav(''), '''
<div style="padding: 3rem 0 2rem; max-width:800px; margin:0 auto;">
  <div style="text-align:center; margin-bottom:3rem;">
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">ROI Calculator 💰</h1>
    <p style="color:var(--text-muted); font-size:1rem;">See how much time and money lvlBase can save your school</p>
  </div>
  <div class="card" style="margin-bottom:2rem;">
    <h3 style="margin-bottom:1.5rem; font-size:1.2rem;">📊 Your School Details</h3>
    <div class="grid-2">
      <div class="form-group">
        <label class="form-label">Number of Students</label>
        <input type="number" class="form-control" id="students" value="500" min="1">
      </div>
      <div class="form-group">
        <label class="form-label">Number of Teachers</label>
        <input type="number" class="form-control" id="teachers" value="30" min="1">
      </div>
      <div class="form-group">
        <label class="form-label">Avg Teacher Hourly Rate ($)</label>
        <input type="number" class="form-control" id="rate" value="35" min="1">
      </div>
      <div class="form-group">
        <label class="form-label">Hours/Week on Manual Grading</label>
        <input type="number" class="form-control" id="grading" value="8" min="0">
      </div>
    </div>
    <button onclick="calcROI()" class="btn btn-primary" style="margin-top:0.5rem;">Calculate Savings →</button>
  </div>
  <div class="card" id="results" style="display:none;">
    <h3 style="margin-bottom:1.5rem; font-size:1.2rem;">💡 Your Estimated Annual Savings</h3>
    <div class="grid-3">
      <div style="text-align:center; padding:1rem; background:rgba(0,209,178,0.1); border-radius:var(--radius);">
        <div style="font-size:2rem; font-weight:900; color:var(--success);" id="grading-saved">$0</div>
        <div style="font-size:0.85rem; color:var(--text-muted);">Grading time saved</div>
      </div>
      <div style="text-align:center; padding:1rem; background:rgba(108,99,255,0.1); border-radius:var(--radius);">
        <div style="font-size:2rem; font-weight:900; color:var(--primary);" id="engagement-value">$0</div>
        <div style="font-size:0.85rem; color:var(--text-muted);">Engagement value</div>
      </div>
      <div style="text-align:center; padding:1rem; background:rgba(255,215,0,0.1); border-radius:var(--radius);">
        <div style="font-size:2rem; font-weight:900; color:var(--accent);" id="total-roi">$0</div>
        <div style="font-size:0.85rem; color:var(--text-muted);">Total annual ROI</div>
      </div>
    </div>
  </div>
</div>
''', '''
<script>
function calcROI() {
  const s = parseInt(document.getElementById('students').value)||0;
  const t = parseInt(document.getElementById('teachers').value)||0;
  const r = parseInt(document.getElementById('rate').value)||0;
  const g = parseInt(document.getElementById('grading').value)||0;
  const gradingSaved = t * g * 0.7 * r * 40;
  const engagementVal = s * 50;
  const total = gradingSaved + engagementVal;
  const fmt = n => '$' + n.toLocaleString();
  document.getElementById('grading-saved').textContent = fmt(Math.round(gradingSaved));
  document.getElementById('engagement-value').textContent = fmt(Math.round(engagementVal));
  document.getElementById('total-roi').textContent = fmt(Math.round(total));
  document.getElementById('results').style.display = 'block';
}
</script>
'''))

# public/press.html
write_file('public/press.html', page('Press', '../core/css/base.css', pub_nav(''), '''
<div style="padding: 3rem 0 2rem;">
  <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">Press & Media 📰</h1>
  <p style="color:var(--text-muted); font-size:1rem; margin-bottom:3rem;">For press inquiries, contact <a href="mailto:press@lvlbase.io" style="color:var(--primary);">press@lvlbase.io</a></p>
  <h2 style="font-size:1.3rem; font-weight:700; margin-bottom:1.5rem;">🗞️ In the News</h2>
  <div style="margin-bottom:3rem;">
    <div class="card" style="margin-bottom:1rem; padding:1.25rem 1.5rem; display:flex; align-items:center; gap:1.5rem;">
      <div style="width:80px; height:40px; background:rgba(255,255,255,0.1); border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.8rem; flex-shrink:0;">TechCrunch</div>
      <div><h4 style="margin-bottom:0.25rem; font-size:1rem;">"lvlBase is turning classrooms into RPGs — and students love it"</h4><p style="color:var(--text-muted); font-size:0.85rem;">January 2025 · 5 min read</p></div>
    </div>
    <div class="card" style="margin-bottom:1rem; padding:1.25rem 1.5rem; display:flex; align-items:center; gap:1.5rem;">
      <div style="width:80px; height:40px; background:rgba(255,255,255,0.1); border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.8rem; flex-shrink:0;">EdWeek</div>
      <div><h4 style="margin-bottom:0.25rem; font-size:1rem;">Can Gamification Fix the Engagement Crisis in K-12 Education?</h4><p style="color:var(--text-muted); font-size:0.85rem;">December 2024 · 8 min read</p></div>
    </div>
    <div class="card" style="padding:1.25rem 1.5rem; display:flex; align-items:center; gap:1.5rem;">
      <div style="width:80px; height:40px; background:rgba(255,255,255,0.1); border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.8rem; flex-shrink:0;">Forbes</div>
      <div><h4 style="margin-bottom:0.25rem; font-size:1rem;">30 EdTech Startups to Watch in 2025</h4><p style="color:var(--text-muted); font-size:0.85rem;">November 2024 · 3 min read</p></div>
    </div>
  </div>
</div>
'''))

# public/faq.html
write_file('public/faq.html', page('FAQ', '../core/css/base.css', pub_nav('faq'), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <div style="text-align:center; margin-bottom:3rem;">
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">Frequently Asked Questions ❓</h1>
    <p style="color:var(--text-muted);">Everything you need to know about lvlBase</p>
  </div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem; cursor:pointer;">What grade levels does lvlBase support?</h4><p style="color:var(--text-muted); font-size:0.9rem;">lvlBase supports grades 3-12 (ages 8-18), with age-appropriate content and difficulty scaling.</p></div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem;">How does the XP and ranking system work?</h4><p style="color:var(--text-muted); font-size:0.9rem;">Students earn XP by completing assignments, winning battles, and achieving goals. Ranks progress E → D → C → B → A → S → SS, resetting each semester.</p></div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem;">Is student data safe?</h4><p style="color:var(--text-muted); font-size:0.9rem;">Yes. All data is encrypted at rest and in transit. We are FERPA, COPPA, and GDPR compliant. We never sell student data.</p></div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem;">Can I use lvlBase with my existing LMS?</h4><p style="color:var(--text-muted); font-size:0.9rem;">lvlBase integrates with Google Classroom, Canvas, Schoology, and other major LMS platforms via our API.</p></div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem;">What devices are supported?</h4><p style="color:var(--text-muted); font-size:0.9rem;">Any device with a modern browser — Chromebooks, iPads, Android tablets, Windows PCs, and phones.</p></div>
  <div style="margin-bottom:0.75rem;" class="card"><h4 style="margin-bottom:0.5rem;">How does AI proctoring work?</h4><p style="color:var(--text-muted); font-size:0.9rem;">It uses the device camera and audio to detect suspicious behavior. All processing is on-device for privacy. No video is stored.</p></div>
  <div class="card"><h4 style="margin-bottom:0.5rem;">Do students need to create accounts?</h4><p style="color:var(--text-muted); font-size:0.9rem;">Students can be provisioned by their school admin or teacher. They can log in with Google, Microsoft, or a school email.</p></div>
</div>
'''))

# public/contact.html
write_file('public/contact.html', page('Contact', '../core/css/base.css', pub_nav(''), '''
<div style="padding:3rem 0 2rem; max-width:700px; margin:0 auto;">
  <div style="text-align:center; margin-bottom:3rem;">
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">Contact Us 📬</h1>
    <p style="color:var(--text-muted);">We typically respond within 24 hours</p>
  </div>
  <div class="grid-2" style="margin-bottom:3rem;">
    <div class="card" style="text-align:center; padding:2rem;">
      <div style="font-size:2.5rem; margin-bottom:1rem;">📧</div>
      <h3 style="margin-bottom:0.5rem;">Email</h3>
      <a href="mailto:hello@lvlbase.io" style="color:var(--primary); font-size:0.9rem;">hello@lvlbase.io</a>
    </div>
    <div class="card" style="text-align:center; padding:2rem;">
      <div style="font-size:2.5rem; margin-bottom:1rem;">💬</div>
      <h3 style="margin-bottom:0.5rem;">Live Chat</h3>
      <p style="color:var(--text-muted); font-size:0.9rem;">Available Mon-Fri 9am-6pm EST</p>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1.5rem;">Send a Message</h3>
    <div class="grid-2">
      <div class="form-group"><label class="form-label">Name</label><input class="form-control" type="text" placeholder="Your name"></div>
      <div class="form-group"><label class="form-label">Email</label><input class="form-control" type="email" placeholder="your@email.com"></div>
    </div>
    <div class="form-group"><label class="form-label">Subject</label>
      <select class="form-control"><option>General Inquiry</option><option>Sales / Pricing</option><option>Technical Support</option><option>Partnership</option><option>Press</option></select>
    </div>
    <div class="form-group"><label class="form-label">Message</label><textarea class="form-control" rows="5" placeholder="Tell us how we can help..."></textarea></div>
    <button class="btn btn-primary">Send Message 📤</button>
  </div>
</div>
'''))

# public/system-status.html
write_file('public/system-status.html', page('System Status', '../core/css/base.css', pub_nav(''), '''
<div style="padding:3rem 0 2rem; max-width:800px; margin:0 auto;">
  <div style="text-align:center; margin-bottom:3rem;">
    <div style="display:inline-flex; align-items:center; gap:0.75rem; background:rgba(0,209,178,0.15); border:1px solid rgba(0,209,178,0.3); border-radius:20px; padding:0.5rem 1.5rem; margin-bottom:1.5rem;">
      <div style="width:10px; height:10px; border-radius:50%; background:var(--success); animation:pulse 2s infinite;"></div>
      <span style="color:var(--success); font-weight:700;">All Systems Operational</span>
    </div>
    <h1 style="font-size:2.5rem; font-weight:900; margin-bottom:0.5rem;">System Status</h1>
    <p style="color:var(--text-muted);">Last updated: Just now</p>
  </div>
  <div class="card" style="margin-bottom:1rem;">
    <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem 0; border-bottom:1px solid var(--border-color);">
      <div><strong>🌐 Web App</strong><p style="color:var(--text-muted); font-size:0.85rem;">Main student/teacher interface</p></div>
      <span style="background:rgba(0,209,178,0.2); color:var(--success); padding:0.3rem 1rem; border-radius:20px; font-size:0.8rem; font-weight:700;">Operational</span>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem 0; border-bottom:1px solid var(--border-color);">
      <div><strong>🔥 Firebase / Database</strong><p style="color:var(--text-muted); font-size:0.85rem;">Realtime data & authentication</p></div>
      <span style="background:rgba(0,209,178,0.2); color:var(--success); padding:0.3rem 1rem; border-radius:20px; font-size:0.8rem; font-weight:700;">Operational</span>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem 0; border-bottom:1px solid var(--border-color);">
      <div><strong>🤖 AI Services</strong><p style="color:var(--text-muted); font-size:0.85rem;">AI Sage, grader, proctoring</p></div>
      <span style="background:rgba(0,209,178,0.2); color:var(--success); padding:0.3rem 1rem; border-radius:20px; font-size:0.8rem; font-weight:700;">Operational</span>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem 0;">
      <div><strong>📧 Email / Notifications</strong><p style="color:var(--text-muted); font-size:0.85rem;">Email alerts and push notifications</p></div>
      <span style="background:rgba(0,209,178,0.2); color:var(--success); padding:0.3rem 1rem; border-radius:20px; font-size:0.8rem; font-weight:700;">Operational</span>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;">📋 Incident History (30 days)</h3>
    <p style="color:var(--text-muted); font-size:0.9rem; text-align:center; padding:2rem;">✅ No incidents in the last 30 days</p>
  </div>
</div>
'''))

print("Public pages batch 2 done")
