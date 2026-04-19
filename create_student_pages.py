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
.page-header { margin-bottom: 2rem; }
.page-title { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.25rem; }
.page-subtitle { color: var(--text-muted); font-size: 0.95rem; }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def student_page(title, css, body, scripts=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡</div>
  <div class="navbar-nav">
    <a href="{css.replace("core/css/base.css","").rstrip("/")}../dashboard.html" class="nav-link">🏠 Home</a>
    <a href="{css.replace("core/css/base.css","").rstrip("/")}../quest-map.html" class="nav-link">📚 Learn</a>
    <a href="{css.replace("core/css/base.css","").rstrip("/")}../arena/battle-stage.html" class="nav-link">⚔️ Arena</a>
    <a href="{css.replace("core/css/base.css","").rstrip("/")}../guilds/guild-dashboard.html" class="nav-link">🏰 Guild</a>
    <a href="{css.replace("core/css/base.css","").rstrip("/")}../ai/sage-chat.html" class="nav-link">🤖 AI Sage</a>
  </div>
  <div class="navbar-actions">
    <span class="badge badge-primary">⚡ 2,450 XP</span>
    <div class="avatar">K</div>
  </div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
{scripts}
</body>
</html>'''

# app/student/backpack.html
write_file('app/student/backpack.html', student_page('Backpack', '../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">🎒 My Backpack</h1>
  <p class="page-subtitle">Your badges, items, and collectibles</p>
</div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Total Badges</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">23</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Rare Items</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">7</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">XP Boosters</div><div style="font-size:2rem;font-weight:900;color:var(--success);">3</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Power-Ups</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">5</div></div>
</div>
<h2 style="font-size:1.2rem;font-weight:700;margin-bottom:1rem;">🏆 Achievement Badges</h2>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">🌟</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">First Blood</div><div style="font-size:0.75rem;color:var(--text-muted);">Won first battle</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">🔥</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">On Fire</div><div style="font-size:0.75rem;color:var(--text-muted);">10-day streak</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">🧠</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Big Brain</div><div style="font-size:0.75rem;color:var(--text-muted);">100% on a test</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">⚔️</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Arena Warrior</div><div style="font-size:0.75rem;color:var(--text-muted);">50 battles won</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem; opacity:0.4;"><div style="font-size:3rem;margin-bottom:0.75rem;">👑</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Guild Master</div><div style="font-size:0.75rem;color:var(--text-muted);">Locked</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem; opacity:0.4;"><div style="font-size:3rem;margin-bottom:0.75rem;">🌈</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Rainbow Scholar</div><div style="font-size:0.75rem;color:var(--text-muted);">Locked</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">⚡</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Speed Demon</div><div style="font-size:0.75rem;color:var(--text-muted);">Fastest battle</div></div>
  <div class="card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:3rem;margin-bottom:0.75rem;">💎</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Diamond Mind</div><div style="font-size:0.75rem;color:var(--text-muted);">SS Rank achieved</div></div>
</div>
<h2 style="font-size:1.2rem;font-weight:700;margin-bottom:1rem;">⚡ Active Items</h2>
<div class="grid-3">
  <div class="card" style="display:flex;align-items:center;gap:1rem;"><div style="font-size:2.5rem;">🚀</div><div><div style="font-weight:700;margin-bottom:0.25rem;">XP Booster x2</div><div style="font-size:0.85rem;color:var(--text-muted);">Expires in 3 days</div><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.8rem;margin-top:0.5rem;">Activate</button></div></div>
  <div class="card" style="display:flex;align-items:center;gap:1rem;"><div style="font-size:2.5rem;">🛡️</div><div><div style="font-weight:700;margin-bottom:0.25rem;">Battle Shield</div><div style="font-size:0.85rem;color:var(--text-muted);">Prevents 1 loss penalty</div><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.8rem;margin-top:0.5rem;">Use</button></div></div>
  <div class="card" style="display:flex;align-items:center;gap:1rem;"><div style="font-size:2.5rem;">🎯</div><div><div style="font-weight:700;margin-bottom:0.25rem;">Focus Potion</div><div style="font-size:0.85rem;color:var(--text-muted);">+20% accuracy in quizzes</div><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.8rem;margin-top:0.5rem;">Use</button></div></div>
</div>
'''))

# app/student/analytics.html
write_file('app/student/analytics.html', student_page('My Analytics', '../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">📊 My Analytics</h1>
  <p class="page-subtitle">Track your learning journey and XP growth</p>
</div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total XP</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">24,850</div><div style="font-size:0.75rem;color:var(--success);">↑ +340 this week</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Current Rank</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">A</div><div style="font-size:0.75rem;color:var(--text-muted);">Top 12% of school</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Study Streak</div><div style="font-size:2rem;font-weight:900;color:var(--success);">🔥 14</div><div style="font-size:0.75rem;color:var(--text-muted);">days in a row</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Battle Win Rate</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">73%</div><div style="font-size:0.75rem;color:var(--text-muted);">47 of 64 battles</div></div>
</div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1.5rem; font-size:1rem;">📈 XP Progress This Month</h3>
    <div style="display:flex;align-items:flex-end;gap:0.5rem;height:120px;padding:0 0.5rem;">
      <div style="flex:1;background:rgba(108,99,255,0.3);border-radius:4px 4px 0 0;height:40%;position:relative;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.4);border-radius:4px 4px 0 0;height:55%;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.5);border-radius:4px 4px 0 0;height:70%;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.6);border-radius:4px 4px 0 0;height:60%;"></div>
      <div style="flex:1;background:var(--primary);border-radius:4px 4px 0 0;height:90%;"></div>
    </div>
    <div style="display:flex;justify-content:space-between;padding:0.5rem 0.5rem 0;font-size:0.75rem;color:var(--text-muted);">
      <span>Wk1</span><span>Wk2</span><span>Wk3</span><span>Wk4</span><span>This</span>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1.5rem; font-size:1rem;">📚 Subject Performance</h3>
    <div>
      <div style="margin-bottom:1rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>Mathematics</span><span style="color:var(--success);">92%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--success);border-radius:20px;width:92%;height:100%;"></div></div></div>
      <div style="margin-bottom:1rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>Science</span><span style="color:var(--primary);">78%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--primary);border-radius:20px;width:78%;height:100%;"></div></div></div>
      <div style="margin-bottom:1rem;"><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>History</span><span style="color:var(--accent);">85%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--accent);border-radius:20px;width:85%;height:100%;"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:0.4rem;"><span>English</span><span style="color:var(--warning);">65%</span></div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--warning);border-radius:20px;width:65%;height:100%;"></div></div></div>
    </div>
  </div>
</div>
'''))

# app/student/support-desk.html
write_file('app/student/support-desk.html', student_page('Support', '../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">🎧 Support Desk</h1>
  <p class="page-subtitle">Get help from teachers or our support team</p>
</div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.75rem;">📚</div><h3 style="margin-bottom:0.5rem;">Help Center</h3><p style="color:var(--text-muted);font-size:0.85rem;">Browse tutorials and guides</p></div>
  <div class="card" style="text-align:center;cursor:pointer;border-color:rgba(108,99,255,0.4);"><div style="font-size:2.5rem;margin-bottom:0.75rem;">💬</div><h3 style="margin-bottom:0.5rem;">Live Chat</h3><p style="color:var(--text-muted);font-size:0.85rem;">Chat with support now</p></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.75rem;">📧</div><h3 style="margin-bottom:0.5rem;">Email Support</h3><p style="color:var(--text-muted);font-size:0.85rem;">Get a response in 24hrs</p></div>
</div>
<div class="card">
  <h3 style="margin-bottom:1.5rem;">📝 Submit a Ticket</h3>
  <div class="grid-2">
    <div style="margin-bottom:1.25rem;"><label style="display:block;font-size:0.8rem;font-weight:600;color:var(--text-muted);margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Category</label><select style="width:100%;padding:0.75rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;"><option>Technical Issue</option><option>Grading Question</option><option>Account Problem</option><option>Content Report</option></select></div>
    <div style="margin-bottom:1.25rem;"><label style="display:block;font-size:0.8rem;font-weight:600;color:var(--text-muted);margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Priority</label><select style="width:100%;padding:0.75rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;"><option>Low</option><option>Medium</option><option>High</option></select></div>
  </div>
  <div style="margin-bottom:1.25rem;"><label style="display:block;font-size:0.8rem;font-weight:600;color:var(--text-muted);margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Subject</label><input type="text" placeholder="Brief description of your issue" style="width:100%;padding:0.75rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;"></div>
  <div style="margin-bottom:1.5rem;"><label style="display:block;font-size:0.8rem;font-weight:600;color:var(--text-muted);margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Description</label><textarea placeholder="Describe your issue in detail..." style="width:100%;padding:0.75rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;rows:5;height:120px;resize:vertical;"></textarea></div>
  <button class="btn btn-primary">Submit Ticket 📤</button>
</div>
'''))

# app/student/focus-mode.html
write_file('app/student/focus-mode.html', student_page('Focus Mode', '../../core/css/base.css', '''
<div style="max-width:600px; margin:0 auto; text-align:center; padding:3rem 0;">
  <h1 class="page-title" style="margin-bottom:0.5rem;">🎯 Focus Mode</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">Block distractions and study with intention</p>
  <div class="card" style="padding:3rem; margin-bottom:2rem;">
    <div style="font-size:6rem; font-weight:900; background:linear-gradient(135deg,var(--primary),var(--accent)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1; margin-bottom:1rem;" id="timer">25:00</div>
    <div style="display:flex;justify-content:center;gap:0.75rem;margin-bottom:2rem;">
      <button onclick="setTimer(25)" class="btn btn-ghost" style="padding:0.5rem 1rem;font-size:0.85rem;">Pomodoro</button>
      <button onclick="setTimer(50)" class="btn btn-ghost" style="padding:0.5rem 1rem;font-size:0.85rem;">Deep Work</button>
      <button onclick="setTimer(5)" class="btn btn-ghost" style="padding:0.5rem 1rem;font-size:0.85rem;">Break</button>
    </div>
    <div style="display:flex;justify-content:center;gap:1rem;">
      <button id="startBtn" onclick="toggleTimer()" class="btn btn-primary" style="padding:1rem 2.5rem;font-size:1.1rem;">▶ Start</button>
      <button onclick="resetTimer()" class="btn btn-ghost" style="padding:1rem 1.5rem;">↺ Reset</button>
    </div>
  </div>
  <div class="card" style="text-align:left;">
    <h3 style="margin-bottom:1rem; font-size:1rem;">Today\'s Focus Sessions</h3>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <div style="background:rgba(0,209,178,0.2);border-radius:8px;padding:0.4rem 0.75rem;font-size:0.8rem;color:var(--success);">✓ 25 min</div>
      <div style="background:rgba(0,209,178,0.2);border-radius:8px;padding:0.4rem 0.75rem;font-size:0.8rem;color:var(--success);">✓ 25 min</div>
      <div style="background:rgba(108,99,255,0.2);border-radius:8px;padding:0.4rem 0.75rem;font-size:0.8rem;color:var(--primary);">▶ Current</div>
    </div>
    <div style="margin-top:1rem; font-size:0.85rem; color:var(--text-muted);">Total today: 50 minutes · +100 XP earned</div>
  </div>
</div>
''', '''
<script>
let seconds = 25*60, running = false, interval = null;
function fmt(s) { return String(Math.floor(s/60)).padStart(2,'0') + ':' + String(s%60).padStart(2,'0'); }
function setTimer(m) { clearInterval(interval); running = false; seconds = m*60; document.getElementById('timer').textContent = fmt(seconds); document.getElementById('startBtn').textContent = '▶ Start'; }
function toggleTimer() {
  if (running) { clearInterval(interval); running = false; document.getElementById('startBtn').textContent = '▶ Start'; }
  else { running = true; document.getElementById('startBtn').textContent = '⏸ Pause'; interval = setInterval(() => { if (seconds > 0) { seconds--; document.getElementById('timer').textContent = fmt(seconds); } else { clearInterval(interval); running = false; document.getElementById('startBtn').textContent = '▶ Start'; alert('Session complete! +50 XP earned! 🎉'); }}, 1000); }
}
function resetTimer() { clearInterval(interval); running = false; seconds = 25*60; document.getElementById('timer').textContent = fmt(seconds); document.getElementById('startBtn').textContent = '▶ Start'; }
</script>
'''))

# app/student/arena/matchmaking.html
write_file('app/student/arena/matchmaking.html', student_page('Matchmaking', '../../../core/css/base.css', '''
<div style="max-width:700px; margin:0 auto; text-align:center; padding:3rem 0;">
  <h1 class="page-title" style="margin-bottom:0.5rem;">⚔️ Battle Matchmaking</h1>
  <p style="color:var(--text-muted); margin-bottom:3rem;">Find your worthy opponent</p>
  <div class="card" style="margin-bottom:2rem;">
    <h3 style="margin-bottom:1.5rem;">Select Subject & Mode</h3>
    <div class="grid-3" style="margin-bottom:1.5rem;">
      <div onclick="selectSubject(this,'Math')" class="card" style="cursor:pointer;padding:1rem;text-align:center;border:2px solid var(--border-color);">📐 Math</div>
      <div onclick="selectSubject(this,'Science')" class="card" style="cursor:pointer;padding:1rem;text-align:center;border:2px solid var(--border-color);">🧪 Science</div>
      <div onclick="selectSubject(this,'English')" class="card" style="cursor:pointer;padding:1rem;text-align:center;border:2px solid var(--border-color);">📖 English</div>
    </div>
    <div class="grid-2" style="margin-bottom:1.5rem;">
      <div class="card" style="cursor:pointer;padding:1rem;text-align:center;border:2px solid var(--primary);">⚡ Quick Battle<br><small style="color:var(--text-muted);">5 questions</small></div>
      <div class="card" style="cursor:pointer;padding:1rem;text-align:center;">🏆 Ranked<br><small style="color:var(--text-muted);">10 questions</small></div>
    </div>
    <button id="findBtn" onclick="findMatch()" class="btn btn-primary" style="padding:1rem 3rem;font-size:1.1rem;">Find Match ⚔️</button>
  </div>
  <div id="searching" style="display:none;" class="card" style="padding:3rem;">
    <div style="font-size:3rem;margin-bottom:1rem;animation:pulse 1.5s infinite;">🔍</div>
    <h3 style="margin-bottom:0.5rem;">Searching for opponent...</h3>
    <p style="color:var(--text-muted);font-size:0.9rem;" id="search-time">00:03</p>
    <button onclick="cancelSearch()" class="btn btn-ghost" style="margin-top:1.5rem;">Cancel</button>
  </div>
</div>
''', '''
<script>
let searchTime = 0, searchInterval;
function findMatch() { document.getElementById('searching').style.display='block'; document.getElementById('findBtn').disabled=true; searchInterval = setInterval(()=>{ searchTime++; document.getElementById('search-time').textContent=String(Math.floor(searchTime/60)).padStart(2,'0')+':'+String(searchTime%60).padStart(2,'0'); if(searchTime>=8){clearInterval(searchInterval); window.location.href='battle-stage.html';}},1000);}
function cancelSearch() { clearInterval(searchInterval); searchTime=0; document.getElementById('searching').style.display='none'; document.getElementById('findBtn').disabled=false;}
function selectSubject(el,name) { document.querySelectorAll('.grid-3 .card').forEach(c=>c.style.borderColor='var(--border-color)'); el.style.borderColor='var(--primary)'; }
</script>
'''))

# app/student/guilds/guild-dashboard.html
write_file('app/student/guilds/guild-dashboard.html', student_page('Guild Dashboard', '../../../core/css/base.css', '''
<div class="page-header">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;">
    <div>
      <h1 class="page-title">🐺 Shadow Wolves</h1>
      <p class="page-subtitle">Guild Rank #2 · 847 members</p>
    </div>
    <div style="display:flex;gap:0.75rem;">
      <span class="badge" style="background:rgba(108,99,255,0.2);color:var(--primary);border:1px solid rgba(108,99,255,0.3);font-size:0.9rem;padding:0.5rem 1rem;">Guild XP: 124,850</span>
      <button class="btn btn-primary">⚔️ Guild Wars</button>
    </div>
  </div>
</div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Guild Rank</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">#2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Members</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">847</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Wars Won</div><div style="font-size:2rem;font-weight:900;color:var(--success);">23</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">My Contribution</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">3,200</div></div>
</div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">🏆 Top Guild Members</h3>
    <div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);">
        <div style="font-weight:700;color:var(--accent);width:24px;">1</div>
        <div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;">K</div>
        <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">KingSlayer99</div><div style="font-size:0.75rem;color:var(--text-muted);">Rank SS</div></div>
        <div style="font-weight:700;color:var(--primary);">12,400 XP</div>
      </div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);">
        <div style="font-weight:700;color:var(--text-muted);width:24px;">2</div>
        <div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--warning));display:flex;align-items:center;justify-content:center;font-weight:700;">Z</div>
        <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">ZenMaster</div><div style="font-size:0.75rem;color:var(--text-muted);">Rank S</div></div>
        <div style="font-weight:700;color:var(--primary);">9,800 XP</div>
      </div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;">
        <div style="font-weight:700;color:var(--warning);width:24px;">3</div>
        <div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;">A</div>
        <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">AceHunter</div><div style="font-size:0.75rem;color:var(--text-muted);">Rank A</div></div>
        <div style="font-weight:700;color:var(--primary);">7,200 XP</div>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">📅 Guild Events</h3>
    <div>
      <div style="padding:0.75rem;background:rgba(108,99,255,0.1);border-radius:var(--radius);margin-bottom:0.75rem;"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">⚔️ Weekly Guild War</div><div style="font-size:0.8rem;color:var(--text-muted);">vs Azure Dragons · Tomorrow 5PM</div></div>
      <div style="padding:0.75rem;background:rgba(255,215,0,0.08);border-radius:var(--radius);margin-bottom:0.75rem;"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">🏆 XP Bonus Weekend</div><div style="font-size:0.8rem;color:var(--text-muted);">2x XP all weekend!</div></div>
      <div style="padding:0.75rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">📋 Guild Meeting</div><div style="font-size:0.8rem;color:var(--text-muted);">Friday 4PM · Strategy session</div></div>
    </div>
  </div>
</div>
'''))

# app/student/guilds/xp-shop.html
write_file('app/student/guilds/xp-shop.html', student_page('XP Shop', '../../../core/css/base.css', '''
<div class="page-header">
  <div style="display:flex;justify-content:space-between;align-items:center;">
    <div><h1 class="page-title">🛒 XP Shop</h1><p class="page-subtitle">Spend your hard-earned XP on epic items</p></div>
    <div class="badge badge-primary" style="font-size:1rem;padding:0.5rem 1.5rem;">⚡ 2,450 XP available</div>
  </div>
</div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;cursor:pointer;border-color:var(--primary);"><div style="font-size:3rem;margin-bottom:0.75rem;">🚀</div><div style="font-weight:700;margin-bottom:0.25rem;">XP Booster 2x</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">3-day boost</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">500 XP</div><button class="btn btn-primary" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🛡️</div><div style="font-weight:700;margin-bottom:0.25rem;">Battle Shield</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">1 loss protection</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">300 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🎭</div><div style="font-weight:700;margin-bottom:0.25rem;">Custom Avatar Frame</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Galaxy theme</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">800 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🎯</div><div style="font-weight:700;margin-bottom:0.25rem;">Focus Potion</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">+20% accuracy</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">250 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🎵</div><div style="font-weight:700;margin-bottom:0.25rem;">Study Playlist</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Lo-fi beats</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">150 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">👑</div><div style="font-weight:700;margin-bottom:0.25rem;">Legendary Title</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">"The Unstoppable"</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">2,000 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">💣</div><div style="font-weight:700;margin-bottom:0.25rem;">Time Freeze</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">+10s in battle</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">400 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🌟</div><div style="font-weight:700;margin-bottom:0.25rem;">Streak Saver</div><div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Protect your streak</div><div style="color:var(--accent);font-weight:700;margin-bottom:0.75rem;">600 XP</div><button class="btn btn-ghost" style="width:100%;padding:0.5rem;">Buy</button></div>
</div>
'''))

# app/student/guilds/loot-boxes.html
write_file('app/student/guilds/loot-boxes.html', student_page('Loot Boxes', '../../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">📦 Loot Boxes</h1>
  <p class="page-subtitle">Open boxes to get random rare items and XP</p>
</div>
<div class="grid-3" style="margin-bottom:3rem;">
  <div class="card" style="text-align:center;cursor:pointer;" onclick="openBox('common')">
    <div style="font-size:5rem;margin-bottom:1rem;">📦</div>
    <h3 style="margin-bottom:0.5rem;">Common Box</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Basic items & 50-200 XP</p>
    <div style="color:var(--success);font-weight:700;margin-bottom:1rem;">FREE daily</div>
    <button class="btn btn-primary" style="width:100%;">Open 📦</button>
  </div>
  <div class="card" style="text-align:center;cursor:pointer;border-color:var(--primary);" onclick="openBox('rare')">
    <div style="position:relative;display:inline-block;margin-bottom:1rem;">
      <div style="font-size:5rem;">💎</div>
      <div style="position:absolute;top:0;right:-10px;background:var(--primary);color:white;font-size:0.65rem;font-weight:700;padding:0.2rem 0.5rem;border-radius:10px;">RARE</div>
    </div>
    <h3 style="margin-bottom:0.5rem;">Rare Box</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Rare items & 200-1000 XP</p>
    <div style="color:var(--accent);font-weight:700;margin-bottom:1rem;">1,000 XP</div>
    <button class="btn btn-primary" style="width:100%;">Open 💎</button>
  </div>
  <div class="card" style="text-align:center;cursor:pointer;border-color:var(--accent);" onclick="openBox('legendary')">
    <div style="position:relative;display:inline-block;margin-bottom:1rem;">
      <div style="font-size:5rem;">👑</div>
      <div style="position:absolute;top:0;right:-10px;background:var(--accent);color:#000;font-size:0.65rem;font-weight:700;padding:0.2rem 0.5rem;border-radius:10px;">LEGEND</div>
    </div>
    <h3 style="margin-bottom:0.5rem;">Legendary Box</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Epic items & 1000-5000 XP</p>
    <div style="color:var(--accent);font-weight:700;margin-bottom:1rem;">5,000 XP</div>
    <button class="btn btn-primary" style="width:100%;">Open 👑</button>
  </div>
</div>
<div id="reveal" style="display:none;" class="card" style="text-align:center;padding:3rem;">
  <div id="reveal-icon" style="font-size:5rem;margin-bottom:1rem;">🎁</div>
  <h2 id="reveal-title" style="margin-bottom:0.5rem;">Opening...</h2>
  <p id="reveal-desc" style="color:var(--text-muted);"></p>
</div>
''', '''
<script>
const items = {common:["🎯 Focus Potion (+50 XP)","🛡️ Mini Shield (+100 XP)","⚡ XP Chip (+75 XP)"],rare:["🚀 XP Booster 2x (+300 XP)","💣 Time Freeze (+200 XP)","🎭 Rare Avatar Frame (+500 XP)"],legendary:["👑 Legendary Title (+2000 XP)","💎 Diamond Shield (+1500 XP)","🌌 Galaxy Frame (+3000 XP)"]};
function openBox(type) {
  const reveal = document.getElementById("reveal");
  reveal.style.display="block"; reveal.scrollIntoView({behavior:"smooth"});
  document.getElementById("reveal-icon").textContent="⏳";
  document.getElementById("reveal-title").textContent="Opening...";
  document.getElementById("reveal-desc").textContent="";
  setTimeout(()=>{
    const arr=items[type]; const item=arr[Math.floor(Math.random()*arr.length)];
    document.getElementById("reveal-icon").textContent="🎉";
    document.getElementById("reveal-title").textContent="You got: "+item;
    document.getElementById("reveal-desc").textContent="Added to your backpack!";
  },1500);
}
</script>
'''))

# app/student/ai/weak-analysis.html
write_file('app/student/ai/weak-analysis.html', student_page('Weakness Analysis', '../../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">🔍 Weakness Analysis</h1>
  <p class="page-subtitle">AI-powered identification of your learning gaps</p>
</div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card" style="border-color:rgba(255,68,68,0.3);">
    <h3 style="margin-bottom:1rem; color:var(--danger);">⚠️ Areas Needing Attention</h3>
    <div>
      <div style="padding:0.75rem;background:rgba(255,68,68,0.08);border-radius:var(--radius);margin-bottom:0.75rem;display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">Quadratic Equations</div><div style="font-size:0.8rem;color:var(--text-muted);">Math · 8 questions attempted</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--danger);">34%</div></div>
      <div style="padding:0.75rem;background:rgba(255,68,68,0.08);border-radius:var(--radius);margin-bottom:0.75rem;display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">Photosynthesis</div><div style="font-size:0.8rem;color:var(--text-muted);">Science · 12 questions</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--warning);">48%</div></div>
      <div style="padding:0.75rem;background:rgba(255,159,67,0.08);border-radius:var(--radius);display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">Essay Structure</div><div style="font-size:0.8rem;color:var(--text-muted);">English · 5 essays</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--warning);">55%</div></div>
    </div>
  </div>
  <div class="card" style="border-color:rgba(0,209,178,0.3);">
    <h3 style="margin-bottom:1rem; color:var(--success);">💪 Your Strengths</h3>
    <div>
      <div style="padding:0.75rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);margin-bottom:0.75rem;display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">Geometry</div><div style="font-size:0.8rem;color:var(--text-muted);">Math · 45 questions</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--success);">94%</div></div>
      <div style="padding:0.75rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);margin-bottom:0.75rem;display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">World History</div><div style="font-size:0.8rem;color:var(--text-muted);">History · 38 questions</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--success);">91%</div></div>
      <div style="padding:0.75rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">Vocabulary</div><div style="font-size:0.8rem;color:var(--text-muted);">English · 60 questions</div></div><div style="font-size:1.2rem;font-weight:700;color:var(--success);">88%</div></div>
    </div>
  </div>
</div>
<div class="card">
  <h3 style="margin-bottom:1rem;">🤖 AI Recommendations</h3>
  <div class="grid-3">
    <div style="padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);border:1px solid rgba(108,99,255,0.2);">
      <div style="font-size:1.5rem;margin-bottom:0.5rem;">📚</div>
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">Practice Quadratics</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">10 targeted exercises</div>
      <a href="smart-flashcards.html" class="btn btn-primary" style="margin-top:0.75rem;padding:0.4rem 1rem;font-size:0.8rem;">Start →</a>
    </div>
    <div style="padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);border:1px solid rgba(108,99,255,0.2);">
      <div style="font-size:1.5rem;margin-bottom:0.5rem;">🎬</div>
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">Watch Photosynthesis</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">15-min explainer video</div>
      <a href="sage-chat.html" class="btn btn-primary" style="margin-top:0.75rem;padding:0.4rem 1rem;font-size:0.8rem;">Watch →</a>
    </div>
    <div style="padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);border:1px solid rgba(108,99,255,0.2);">
      <div style="font-size:1.5rem;margin-bottom:0.5rem;">✏️</div>
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">Essay Workshop</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">AI-guided writing</div>
      <a href="sage-chat.html" class="btn btn-primary" style="margin-top:0.75rem;padding:0.4rem 1rem;font-size:0.8rem;">Start →</a>
    </div>
  </div>
</div>
'''))

# app/student/ai/mock-interview.html
write_file('app/student/ai/mock-interview.html', student_page('Mock Interview', '../../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">🎙️ Mock Interview</h1>
  <p class="page-subtitle">Practice oral exams and interviews with AI</p>
</div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;cursor:pointer;border-color:var(--primary);">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">📐</div>
    <h3 style="margin-bottom:0.5rem;">Math Defense</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Explain math concepts verbally</p>
    <button class="btn btn-primary" style="width:100%;">Start →</button>
  </div>
  <div class="card" style="text-align:center;cursor:pointer;">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">🔬</div>
    <h3 style="margin-bottom:0.5rem;">Science Oral</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Defend your scientific reasoning</p>
    <button class="btn btn-ghost" style="width:100%;">Start →</button>
  </div>
  <div class="card" style="text-align:center;cursor:pointer;">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">📖</div>
    <h3 style="margin-bottom:0.5rem;">Literature Discussion</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Discuss books and themes</p>
    <button class="btn btn-ghost" style="width:100%;">Start →</button>
  </div>
</div>
<div class="card" id="interview-area" style="min-height:400px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;">
    <h3 style="font-size:1rem;">AI Interviewer</h3>
    <div style="display:flex;gap:0.75rem;">
      <button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.85rem;" id="mic-btn" onclick="toggleMic()">🎙️ Unmute</button>
      <button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.85rem;">📹 Camera</button>
    </div>
  </div>
  <div style="background:rgba(108,99,255,0.08);border-radius:var(--radius);padding:1.5rem;margin-bottom:1.5rem;">
    <div style="font-size:2rem;margin-bottom:0.75rem;">🤖</div>
    <p style="font-size:1rem;line-height:1.6;">Welcome to your Math Mock Interview. I will ask you questions about algebra and you should explain your thinking process clearly. Are you ready to begin? <strong>First question:</strong> Can you explain what the quadratic formula is and when you would use it?</p>
  </div>
  <textarea placeholder="Type your answer here, or use the microphone..." style="width:100%;height:120px;padding:1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;resize:vertical;"></textarea>
  <div style="display:flex;gap:0.75rem;margin-top:1rem;">
    <button class="btn btn-primary">Submit Answer →</button>
    <button class="btn btn-ghost">Skip Question</button>
  </div>
</div>
''', '''<script>
function toggleMic() {
  const btn = document.getElementById("mic-btn");
  btn.textContent = btn.textContent.includes("Unmute") ? "🎙️ Mute" : "🎙️ Unmute";
}
</script>'''))

# app/student/workspace/web-studio.html
write_file('app/student/workspace/web-studio.html', student_page('Web Studio', '../../../core/css/base.css', '''
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;flex-wrap:wrap;gap:1rem;">
  <div><h1 class="page-title">💻 Web Studio</h1><p class="page-subtitle">Build and preview HTML/CSS/JS projects</p></div>
  <div style="display:flex;gap:0.75rem;">
    <button class="btn btn-ghost">📁 New File</button>
    <button class="btn btn-ghost">💾 Save</button>
    <button onclick="runCode()" class="btn btn-primary">▶ Run</button>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;height:calc(100vh - 200px);">
  <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
    <div style="display:flex;border-bottom:1px solid var(--border-color);">
      <button id="tab-html" onclick="switchTab('html')" style="padding:0.75rem 1.5rem;background:rgba(108,99,255,0.15);border:none;color:var(--primary);font-family:inherit;font-size:0.85rem;font-weight:600;cursor:pointer;border-right:1px solid var(--border-color);">HTML</button>
      <button id="tab-css" onclick="switchTab('css')" style="padding:0.75rem 1.5rem;background:transparent;border:none;color:var(--text-muted);font-family:inherit;font-size:0.85rem;cursor:pointer;border-right:1px solid var(--border-color);">CSS</button>
      <button id="tab-js" onclick="switchTab('js')" style="padding:0.75rem 1.5rem;background:transparent;border:none;color:var(--text-muted);font-family:inherit;font-size:0.85rem;cursor:pointer;">JS</button>
    </div>
    <textarea id="editor" style="flex:1;padding:1rem;background:rgba(0,0,0,0.4);border:none;color:#E8E8FF;font-family:monospace;font-size:0.9rem;resize:none;outline:none;line-height:1.6;">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;My Project&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Hello, World!&lt;/h1&gt;
  &lt;p&gt;Start coding here...&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</textarea>
  </div>
  <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
    <div style="padding:0.75rem 1.5rem;border-bottom:1px solid var(--border-color);font-size:0.85rem;color:var(--text-muted);">Preview</div>
    <iframe id="preview" style="flex:1;border:none;background:white;"></iframe>
  </div>
</div>
''', '''
<script>
function runCode() {
  const html = document.getElementById("editor").value;
  const preview = document.getElementById("preview");
  preview.srcdoc = html;
}
function switchTab(tab) {
  document.querySelectorAll("[id^=tab-]").forEach(b => { b.style.background="transparent"; b.style.color="var(--text-muted)"; });
  document.getElementById("tab-"+tab).style.background="rgba(108,99,255,0.15)";
  document.getElementById("tab-"+tab).style.color="var(--primary)";
}
</script>
'''))

# app/student/workspace/flutter-lab.html
write_file('app/student/workspace/flutter-lab.html', student_page('Flutter Lab', '../../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">📱 Flutter Lab</h1>
  <p class="page-subtitle">Learn mobile app development with Flutter & Dart</p>
</div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card"><h3 style="margin-bottom:0.75rem;">📱 Widget Basics</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Learn Text, Container, Row, Column widgets</p><div style="font-size:0.8rem;color:var(--text-muted);">Progress: 8/12 lessons</div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:6px;margin-top:0.5rem;margin-bottom:1rem;"><div style="background:var(--success);border-radius:20px;width:67%;height:100%;"></div></div><button class="btn btn-primary" style="font-size:0.85rem;padding:0.5rem 1rem;">Continue →</button></div>
  <div class="card"><h3 style="margin-bottom:0.75rem;">🎨 Styling & Themes</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Colors, fonts, and custom themes</p><div style="font-size:0.8rem;color:var(--text-muted);">Progress: 3/10 lessons</div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:6px;margin-top:0.5rem;margin-bottom:1rem;"><div style="background:var(--primary);border-radius:20px;width:30%;height:100%;"></div></div><button class="btn btn-ghost" style="font-size:0.85rem;padding:0.5rem 1rem;">Start →</button></div>
  <div class="card"><h3 style="margin-bottom:0.75rem;">🔗 State Management</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">setState, Provider, Riverpod</p><div style="font-size:0.8rem;color:var(--text-muted);">Progress: 0/15 lessons</div><div style="background:rgba(255,255,255,0.1);border-radius:20px;height:6px;margin-top:0.5rem;margin-bottom:1rem;"><div style="background:var(--text-muted);border-radius:20px;width:0%;height:100%;"></div></div><button class="btn btn-ghost" style="font-size:0.85rem;padding:0.5rem 1rem;">Locked 🔒</button></div>
</div>
<div class="card" style="margin-bottom:2rem;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
    <h3 style="font-size:1rem;">🔨 Current Assignment: Build a Todo App</h3>
    <span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;font-weight:700;">Due: 3 days</span>
  </div>
  <div style="background:rgba(0,0,0,0.3);border-radius:var(--radius);padding:1rem;font-family:monospace;font-size:0.85rem;line-height:1.6;color:#C5E1A5;">
    <div style="color:#7986CB;">// lib/main.dart</div>
    <div style="color:#CE93D8;">import <span style="color:#A5D6A7;">"package:flutter/material.dart"</span>;</div>
    <div></div>
    <div style="color:#CE93D8;">void <span style="color:#80DEEA;">main</span>() =&gt; runApp(MyApp());</div>
    <div></div>
    <div style="color:#CE93D8;">class <span style="color:#80DEEA;">MyApp</span> extends StatelessWidget &#123;</div>
    <div style="color:#FFFFFF;padding-left:1.5rem;">  // Your code here...</div>
    <div>&#125;</div>
  </div>
  <div style="display:flex;gap:0.75rem;margin-top:1rem;">
    <button class="btn btn-primary" style="font-size:0.85rem;">📱 Open Editor</button>
    <button class="btn btn-ghost" style="font-size:0.85rem;">📖 View Docs</button>
    <button class="btn btn-ghost" style="font-size:0.85rem;">🤖 Ask AI</button>
  </div>
</div>
'''))

# app/student/workspace/code-review.html
write_file('app/student/workspace/code-review.html', student_page('Code Review', '../../../core/css/base.css', '''
<div class="page-header">
  <h1 class="page-title">🔍 Code Review</h1>
  <p class="page-subtitle">Get AI feedback and peer reviews on your code</p>
</div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">📝 Submit Code for Review</h3>
    <div style="margin-bottom:1rem;"><label style="font-size:0.8rem;font-weight:600;color:var(--text-muted);display:block;margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Language</label><select style="width:100%;padding:0.75rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.9rem;"><option>Python</option><option>JavaScript</option><option>Dart/Flutter</option><option>Java</option></select></div>
    <div style="margin-bottom:1rem;"><label style="font-size:0.8rem;font-weight:600;color:var(--text-muted);display:block;margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:0.05em;">Paste Code</label><textarea style="width:100%;height:200px;padding:1rem;background:rgba(0,0,0,0.4);border:1px solid var(--border-color);border-radius:var(--radius);color:#C5E1A5;font-family:monospace;font-size:0.85rem;resize:vertical;" placeholder="# Paste your Python code here..."></textarea></div>
    <button class="btn btn-primary">🤖 AI Review</button>
    <button class="btn btn-ghost" style="margin-left:0.75rem;">👥 Peer Review</button>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">🤖 AI Feedback</h3>
    <div style="padding:1rem;background:rgba(0,209,178,0.08);border-radius:var(--radius);border-left:3px solid var(--success);margin-bottom:1rem;">
      <div style="font-weight:600;font-size:0.9rem;color:var(--success);margin-bottom:0.4rem;">✓ Good Practices</div>
      <ul style="color:var(--text-muted);font-size:0.85rem;padding-left:1rem;line-height:1.8;"><li>Good variable naming</li><li>Proper indentation</li><li>Comments are helpful</li></ul>
    </div>
    <div style="padding:1rem;background:rgba(255,159,67,0.08);border-radius:var(--radius);border-left:3px solid var(--warning);margin-bottom:1rem;">
      <div style="font-weight:600;font-size:0.9rem;color:var(--warning);margin-bottom:0.4rem;">⚠️ Suggestions</div>
      <ul style="color:var(--text-muted);font-size:0.85rem;padding-left:1rem;line-height:1.8;"><li>Use list comprehension on line 12</li><li>Handle edge case: empty input</li></ul>
    </div>
    <div style="padding:1rem;background:rgba(255,68,68,0.08);border-radius:var(--radius);border-left:3px solid var(--danger);">
      <div style="font-weight:600;font-size:0.9rem;color:var(--danger);margin-bottom:0.4rem;">✗ Issues Found</div>
      <ul style="color:var(--text-muted);font-size:0.85rem;padding-left:1rem;line-height:1.8;"><li>Line 23: Division by zero risk</li></ul>
    </div>
  </div>
</div>
'''))

print("Student pages created")
