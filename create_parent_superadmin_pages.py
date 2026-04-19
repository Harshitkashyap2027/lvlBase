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
.nav-link:hover { color: var(--text-light); background: rgba(108,99,255,0.15); }
.navbar-actions { display: flex; align-items: center; gap: 1rem; }
.avatar { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; }
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
.form-group { margin-bottom: 1.25rem; }
.form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
.form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def parent_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Parent</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 👨‍👩‍👧</div>
  <div class="navbar-nav">
    <a href="dashboard.html" class="nav-link">🏠 Home</a>
    <a href="child-report.html" class="nav-link">📊 Reports</a>
    <a href="teacher-connect.html" class="nav-link">💬 Teachers</a>
    <a href="screen-time.html" class="nav-link">⏰ Screen Time</a>
    <a href="payments.html" class="nav-link">💳 Payments</a>
  </div>
  <div class="navbar-actions"><div class="avatar" style="background:linear-gradient(135deg,var(--warning),var(--accent));">P</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

# Parent pages
write_file('app/parent/attendance.html', parent_page('Attendance', '''
<div class="page-header"><h1 class="page-title">📅 Child Attendance</h1><p class="page-subtitle">Alex Johnson · Grade 10A</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Attendance Rate</div><div style="font-size:2rem;font-weight:900;color:var(--success);">97.3%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Days Present</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">71</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Days Absent</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Times Late</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">1</div></div>
</div>
<div class="card">
  <h3 style="margin-bottom:1rem;font-size:1rem;">📋 Recent Attendance Records</h3>
  <div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Monday, Jan 15</span><span style="color:var(--success);font-weight:600;">✓ Present</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Friday, Jan 12</span><span style="color:var(--success);font-weight:600;">✓ Present</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);"><span>Thursday, Jan 11</span><span style="color:var(--success);font-weight:600;">✓ Present</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;"><span>Jan 5</span><span style="color:var(--danger);font-weight:600;">✗ Absent (sick)</span></div>
  </div>
</div>
'''))

write_file('app/parent/pt-meeting.html', parent_page('PT Meeting Scheduler', '''
<div class="page-header"><h1 class="page-title">📅 Parent-Teacher Meetings</h1><p class="page-subtitle">Schedule meetings with your child\'s teachers</p></div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">Schedule a Meeting</h3>
    <div class="form-group"><label class="form-label">Select Teacher</label><select class="form-control"><option>Ms. Rodriguez (Math)</option><option>Mr. Patel (Science)</option><option>Mrs. Chen (English)</option></select></div>
    <div class="form-group"><label class="form-label">Meeting Type</label><select class="form-control"><option>In-Person</option><option>Video Call</option><option>Phone Call</option></select></div>
    <div class="grid-2">
      <div class="form-group"><label class="form-label">Date</label><input class="form-control" type="date"></div>
      <div class="form-group"><label class="form-label">Time</label><select class="form-control"><option>8:00 AM</option><option>8:30 AM</option><option>3:30 PM</option><option>4:00 PM</option></select></div>
    </div>
    <div class="form-group"><label class="form-label">Topic (Optional)</label><textarea class="form-control" rows="3" style="height:80px;resize:none;" placeholder="What do you want to discuss?"></textarea></div>
    <button class="btn btn-primary">Schedule Meeting 📅</button>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">📋 Upcoming Meetings</h3>
    <div style="padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);margin-bottom:0.75rem;border-left:3px solid var(--primary);">
      <div style="font-weight:600;margin-bottom:0.25rem;">Ms. Rodriguez · Math</div>
      <div style="font-size:0.85rem;color:var(--text-muted);">Jan 20 · 3:30 PM · In-Person</div>
      <div style="display:flex;gap:0.5rem;margin-top:0.75rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">Reschedule</button><button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;color:var(--danger);">Cancel</button></div>
    </div>
    <h3 style="font-size:1rem;margin-bottom:1rem;margin-top:1.5rem;">📅 Available Teacher Slots</h3>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.5rem;">
      <div style="padding:0.5rem;text-align:center;background:rgba(0,209,178,0.1);border-radius:8px;cursor:pointer;font-size:0.8rem;border:1px solid rgba(0,209,178,0.2);">Mon 3:30</div>
      <div style="padding:0.5rem;text-align:center;background:rgba(0,209,178,0.1);border-radius:8px;cursor:pointer;font-size:0.8rem;border:1px solid rgba(0,209,178,0.2);">Tue 4:00</div>
      <div style="padding:0.5rem;text-align:center;background:rgba(108,99,255,0.15);border-radius:8px;cursor:pointer;font-size:0.8rem;border:1px solid rgba(108,99,255,0.3);">Thu 8:00</div>
    </div>
  </div>
</div>
'''))

write_file('app/parent/screen-time.html', parent_page('Screen Time Controls', '''
<div class="page-header"><h1 class="page-title">⏰ Screen Time Controls</h1><p class="page-subtitle">Manage Alex\'s daily usage of lvlBase</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Today</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">2h 34m</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Daily Limit</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">4h 0m</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">This Week</div><div style="font-size:2rem;font-weight:900;color:var(--success);">14h 20m</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Study vs Play</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">80/20</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">⚙️ Daily Limits</h3>
    <div class="form-group"><label class="form-label">Weekday Limit (hours)</label><input class="form-control" type="range" min="1" max="8" value="4"></div>
    <div class="form-group"><label class="form-label">Weekend Limit (hours)</label><input class="form-control" type="range" min="1" max="8" value="6"></div>
    <h3 style="margin-bottom:1rem;font-size:1rem;margin-top:1rem;">⛔ Blocked Hours</h3>
    <div class="grid-2">
      <div class="form-group"><label class="form-label">Block From</label><input class="form-control" type="time" value="22:00"></div>
      <div class="form-group"><label class="form-label">Block Until</label><input class="form-control" type="time" value="07:00"></div>
    </div>
    <button class="btn btn-primary">Save Settings 💾</button>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📊 Time Breakdown This Week</h3>
    <div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:100px;font-size:0.85rem;">Studying</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--success);border-radius:20px;width:75%;height:100%;"></div></div><div style="font-size:0.85rem;width:50px;text-align:right;">75%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:100px;font-size:0.85rem;">Battles</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--primary);border-radius:20px;width:15%;height:100%;"></div></div><div style="font-size:0.85rem;width:50px;text-align:right;">15%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:100px;font-size:0.85rem;">Social/Guild</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--warning);border-radius:20px;width:10%;height:100%;"></div></div><div style="font-size:0.85rem;width:50px;text-align:right;">10%</div></div>
    </div>
  </div>
</div>
'''))

write_file('app/parent/rewards.html', parent_page('Rewards & Allowance', '''
<div class="page-header"><h1 class="page-title">🎁 Rewards & Allowance</h1><p class="page-subtitle">Set up real-world rewards for Alex\'s achievements</p></div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">➕ Create a Reward</h3>
    <div class="form-group"><label class="form-label">Reward Name</label><input class="form-control" type="text" placeholder="e.g., Extra game time, Pizza night"></div>
    <div class="form-group"><label class="form-label">Trigger</label><select class="form-control"><option>Reach Rank A</option><option>Complete 10 quests</option><option>Win 5 battles</option><option>100% attendance week</option><option>Custom XP goal</option></select></div>
    <div class="form-group"><label class="form-label">XP Goal (if custom)</label><input class="form-control" type="number" placeholder="e.g., 5000"></div>
    <button class="btn btn-primary">Create Reward 🎁</button>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">🏆 Active Rewards</h3>
    <div>
      <div style="padding:0.75rem;border:1px solid rgba(0,209,178,0.3);border-radius:var(--radius);margin-bottom:0.75rem;background:rgba(0,209,178,0.05);">
        <div style="font-weight:600;margin-bottom:0.25rem;">🍕 Pizza Night</div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:0.5rem;">Trigger: Reach Rank A</div>
        <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;margin-bottom:0.4rem;"><div style="background:var(--success);border-radius:20px;width:85%;height:100%;"></div></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">Almost there! Alex is Rank B+ now</div>
      </div>
      <div style="padding:0.75rem;border:1px solid rgba(108,99,255,0.3);border-radius:var(--radius);background:rgba(108,99,255,0.05);">
        <div style="font-weight:600;margin-bottom:0.25rem;">🎮 Extra Gaming Friday</div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:0.5rem;">Trigger: 100% attendance week</div>
        <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;margin-bottom:0.4rem;"><div style="background:var(--primary);border-radius:20px;width:60%;height:100%;"></div></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">3/5 days complete</div>
      </div>
    </div>
  </div>
</div>
'''))

write_file('app/parent/payments.html', parent_page('Payments & Billing', '''
<div class="page-header"><h1 class="page-title">💳 Payments & Billing</h1><p class="page-subtitle">Manage your subscription and school payments</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card" style="border-color:var(--primary);">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem;"><div><h3 style="font-size:1rem;">Current Plan</h3><div style="font-size:0.85rem;color:var(--text-muted);">Family Pro</div></div><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;">Active</span></div>
    <div style="font-size:1.5rem;font-weight:900;color:var(--primary);margin-bottom:0.5rem;">$9.99/mo</div>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Next billing: Feb 1, 2025</div>
    <button class="btn btn-ghost" style="font-size:0.85rem;">Manage Plan</button>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">🎒 School Fee Payments</h3>
    <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);display:flex;justify-content:space-between;"><div><div style="font-weight:600;font-size:0.9rem;">Lab Fee Q1</div><div style="font-size:0.8rem;color:var(--text-muted);">Due Jan 30</div></div><div style="text-align:right;"><div style="font-weight:700;color:var(--warning);">$45.00</div><button class="btn btn-primary" style="padding:0.3rem 0.75rem;font-size:0.8rem;margin-top:0.4rem;">Pay</button></div></div>
    <div style="padding:0.75rem;display:flex;justify-content:space-between;"><div><div style="font-weight:600;font-size:0.9rem;">Field Trip — Science Museum</div><div style="font-size:0.8rem;color:var(--text-muted);">Due Feb 10</div></div><div style="text-align:right;"><div style="font-weight:700;color:var(--warning);">$25.00</div><button class="btn btn-primary" style="padding:0.3rem 0.75rem;font-size:0.8rem;margin-top:0.4rem;">Pay</button></div></div>
  </div>
</div>
<div class="card">
  <h3 style="font-size:1rem;margin-bottom:1rem;">📋 Payment History</h3>
  <div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>lvlBase Family Pro — January</span><span style="color:var(--text-muted);">Jan 1, 2025</span><span style="color:var(--success);">$9.99 ✓</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>XP Booster Pack (x3)</span><span style="color:var(--text-muted);">Dec 20, 2024</span><span style="color:var(--success);">$4.99 ✓</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;font-size:0.9rem;"><span>lvlBase Family Pro — December</span><span style="color:var(--text-muted);">Dec 1, 2024</span><span style="color:var(--success);">$9.99 ✓</span></div>
  </div>
</div>
'''))

# Super Admin pages
def super_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Super Admin</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡ SA</div>
  <div class="navbar-nav">
    <a href="dashboard.html" class="nav-link">🏠 Home</a>
    <a href="tenants/active.html" class="nav-link">🏫 Schools</a>
    <a href="infrastructure/server.html" class="nav-link">🖥️ Infra</a>
    <a href="security/threats.html" class="nav-link">🔒 Security</a>
    <a href="content/question-bank.html" class="nav-link">📚 Content</a>
  </div>
  <div class="navbar-actions"><div class="avatar" style="background:linear-gradient(135deg,var(--danger),var(--secondary));">SA</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

def super_sub(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Super Admin</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase ⚡ SA</div>
  <div class="navbar-nav">
    <a href="../dashboard.html" class="nav-link">🏠 Home</a>
    <a href="../tenants/active.html" class="nav-link">🏫 Schools</a>
    <a href="../infrastructure/server.html" class="nav-link">��️ Infra</a>
    <a href="../security/threats.html" class="nav-link">🔒 Security</a>
    <a href="../content/question-bank.html" class="nav-link">📚 Content</a>
  </div>
  <div class="navbar-actions"><div class="avatar" style="background:linear-gradient(135deg,var(--danger),var(--secondary));">SA</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

write_file('app/super-admin/finance.html', super_page('Platform Finance', '''
<div class="page-header"><h1 class="page-title">💰 Platform Finance</h1><p class="page-subtitle">Revenue, subscriptions, and financial metrics</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">MRR</div><div style="font-size:2rem;font-weight:900;color:var(--success);">$847K</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">ARR</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">$10.2M</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Active Schools</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">1,247</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Churn Rate</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">1.2%</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">📊 Revenue by Plan</h3>
    <div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:100px;font-size:0.85rem;">Enterprise</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--success);border-radius:20px;width:55%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:50px;">55%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:100px;font-size:0.85rem;">Pro School</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--primary);border-radius:20px;width:35%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:50px;">35%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:100px;font-size:0.85rem;">Family Pro</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--accent);border-radius:20px;width:10%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:50px;">10%</div></div>
    </div>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">📈 MRR Growth</h3>
    <div style="display:flex;align-items:flex-end;gap:0.75rem;height:120px;">
      <div style="flex:1;background:rgba(108,99,255,0.3);border-radius:4px 4px 0 0;height:45%;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.4);border-radius:4px 4px 0 0;height:55%;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.5);border-radius:4px 4px 0 0;height:65%;"></div>
      <div style="flex:1;background:rgba(108,99,255,0.6);border-radius:4px 4px 0 0;height:75%;"></div>
      <div style="flex:1;background:var(--primary);border-radius:4px 4px 0 0;height:90%;"></div>
    </div>
    <div style="display:flex;justify-content:space-between;font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem;"><span>Sep</span><span>Oct</span><span>Nov</span><span>Dec</span><span>Jan</span></div>
  </div>
</div>
'''))

write_file('app/super-admin/global-events.html', super_page('Global Events', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🌍 Global Events</h1><p class="page-subtitle">Platform-wide competitions and events for all schools</p></div><button class="btn btn-primary">+ Create Global Event</button></div></div>
<div class="grid-3">
  <div class="card" style="border-color:rgba(255,215,0,0.4);">
    <div style="display:flex;gap:0.5rem;margin-bottom:1rem;"><span style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">LIVE</span></div>
    <div style="font-size:2rem;margin-bottom:0.75rem;">🏆</div>
    <h3 style="margin-bottom:0.5rem;">World Math Championship</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">47,284 students competing globally across 312 schools</p>
    <div class="grid-2" style="gap:0.5rem;margin-bottom:1rem;">
      <div style="text-align:center;background:rgba(108,99,255,0.1);border-radius:var(--radius);padding:0.5rem;"><div style="font-weight:700;font-size:1rem;">312</div><div style="font-size:0.7rem;color:var(--text-muted);">Schools</div></div>
      <div style="text-align:center;background:rgba(108,99,255,0.1);border-radius:var(--radius);padding:0.5rem;"><div style="font-weight:700;font-size:1rem;">47.2K</div><div style="font-size:0.7rem;color:var(--text-muted);">Participants</div></div>
    </div>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Monitor Event →</button>
  </div>
  <div class="card">
    <div style="display:flex;gap:0.5rem;margin-bottom:1rem;"><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">UPCOMING</span></div>
    <div style="font-size:2rem;margin-bottom:0.75rem;">📖</div>
    <h3 style="margin-bottom:0.5rem;">Global Science Quiz Bowl</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Starts Feb 1 · Sign-up open for all Pro Schools</p>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Edit Event</button>
  </div>
  <div class="card">
    <div style="display:flex;gap:0.5rem;margin-bottom:1rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;font-weight:700;">DRAFT</span></div>
    <div style="font-size:2rem;margin-bottom:0.75rem;">🎯</div>
    <h3 style="margin-bottom:0.5rem;">Spring Coding Challenge</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Python & Web dev tracks · March 2025</p>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Publish →</button>
  </div>
</div>
'''))

write_file('app/super-admin/mail.html', super_page('Mass Email', '''
<div class="page-header"><h1 class="page-title">📧 Mass Email</h1><p class="page-subtitle">Send platform-wide emails to schools and users</p></div>
<div class="grid-2">
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1.5rem;">✉️ Compose Email</h3>
    <div class="form-group"><label class="form-label">Send To</label><select class="form-control"><option>All School Admins (1,247)</option><option>All Teachers (12,400)</option><option>Pro School Tier</option><option>Enterprise Tier</option></select></div>
    <div class="form-group"><label class="form-label">Subject</label><input class="form-control" type="text" placeholder="Email subject line"></div>
    <div class="form-group"><label class="form-label">Template</label><select class="form-control"><option>Custom</option><option>Feature Update</option><option>Maintenance Notice</option><option>New Release</option></select></div>
    <div class="form-group"><label class="form-label">Message</label><textarea class="form-control" rows="8" style="height:150px;resize:vertical;" placeholder="Email body..."></textarea></div>
    <div style="display:flex;gap:0.75rem;"><button class="btn btn-primary">📤 Send Email</button><button class="btn btn-ghost">👁️ Preview</button><button class="btn btn-ghost">📅 Schedule</button></div>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1rem;">📋 Recent Campaigns</h3>
    <div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">v2.5 Feature Update</div><div style="font-size:0.8rem;color:var(--text-muted);">Sent Jan 10 · 1,247 recipients · 89% open rate</div></div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">Scheduled Maintenance Notice</div><div style="font-size:0.8rem;color:var(--text-muted);">Sent Dec 28 · All users · 94% open rate</div></div>
      <div style="padding:0.75rem;"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">Happy New Year from lvlBase!</div><div style="font-size:0.8rem;color:var(--text-muted);">Sent Jan 1 · All users · 71% open rate</div></div>
    </div>
  </div>
</div>
'''))

# Tenants pages
for page_info in [
    ('tenants/requests.html', 'School Requests', '''
<div class="page-header"><h1 class="page-title">📋 School Onboarding Requests</h1><p class="page-subtitle">Review and approve new school applications</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Pending</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">23</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Approved Today</div><div style="font-size:2rem;font-weight:900;color:var(--success);">5</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">This Month</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">47</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Schools</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">1,247</div></div>
</div>
<div class="card">
  <div style="padding:1rem;border:1px solid rgba(255,215,0,0.3);border-radius:var(--radius);background:rgba(255,215,0,0.05);margin-bottom:0.75rem;">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;">
      <div><h3 style="font-size:1rem;margin-bottom:0.25rem;">Lincoln High School — Chicago, IL</h3><div style="font-size:0.85rem;color:var(--text-muted);">Plan: Pro School · 1,200 students · Contact: admin@lincoln.edu</div></div>
      <div style="display:flex;gap:0.5rem;"><button class="btn btn-primary" style="font-size:0.85rem;padding:0.4rem 1rem;background:rgba(0,209,178,0.2);color:var(--success);">✓ Approve</button><button class="btn btn-ghost" style="font-size:0.85rem;padding:0.4rem 1rem;">View Details</button><button class="btn btn-ghost" style="font-size:0.85rem;padding:0.4rem 1rem;color:var(--danger);">✗ Reject</button></div>
    </div>
  </div>
</div>
'''),
    ('tenants/active.html', 'Active Schools', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏫 Active Schools</h1><p class="page-subtitle">1,247 schools on the platform</p></div><input type="search" placeholder="Search schools..." style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;width:250px;"></div></div>
<div class="card">
  <table style="width:100%;border-collapse:collapse;">
    <thead><tr style="border-bottom:1px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">School</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Plan</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Students</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Status</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;">Riverside Academy, CA</td><td style="padding:0.75rem;"><span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;">Enterprise</span></td><td style="padding:0.75rem;">1,200</td><td style="padding:0.75rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;">Active</span></td></tr>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;">Westwood Prep, NY</td><td style="padding:0.75rem;"><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;">Pro School</span></td><td style="padding:0.75rem;">800</td><td style="padding:0.75rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;">Active</span></td></tr>
    </tbody>
  </table>
</div>
'''),
    ('tenants/feature-flags.html', 'Feature Flags', '''
<div class="page-header"><h1 class="page-title">🚩 Feature Flags</h1><p class="page-subtitle">Enable/disable features per school or globally</p></div>
<div class="card">
  <div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:1rem;border-bottom:1px solid var(--border-color);">
      <div><div style="font-weight:600;font-size:0.95rem;">🤖 AI Proctoring</div><div style="font-size:0.85rem;color:var(--text-muted);">Facial recognition and gaze tracking during exams</div></div>
      <div style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.3rem 1rem;border-radius:20px;font-size:0.85rem;font-weight:700;cursor:pointer;">ON</div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:1rem;border-bottom:1px solid var(--border-color);">
      <div><div style="font-weight:600;font-size:0.95rem;">🎮 Guild Wars</div><div style="font-size:0.85rem;color:var(--text-muted);">Cross-school competitive guild battles</div></div>
      <div style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.3rem 1rem;border-radius:20px;font-size:0.85rem;font-weight:700;cursor:pointer;">ON</div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:1rem;border-bottom:1px solid var(--border-color);">
      <div><div style="font-weight:600;font-size:0.95rem;">🔬 Flutter Lab</div><div style="font-size:0.85rem;color:var(--text-muted);">Mobile development workspace (Beta)</div></div>
      <div style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.3rem 1rem;border-radius:20px;font-size:0.85rem;font-weight:700;cursor:pointer;">BETA</div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:1rem;">
      <div><div style="font-weight:600;font-size:0.95rem;">🧬 Biometric Login</div><div style="font-size:0.85rem;color:var(--text-muted);">WebAuthn fingerprint/face login</div></div>
      <div style="background:rgba(255,255,255,0.1);color:var(--text-muted);padding:0.3rem 1rem;border-radius:20px;font-size:0.85rem;font-weight:700;cursor:pointer;">OFF</div>
    </div>
  </div>
</div>
'''),
]:
    write_file(f'app/super-admin/{page_info[0]}', super_sub(page_info[1], page_info[2]))

# Infrastructure pages
for page_info in [
    ('infrastructure/server.html', 'Server Dashboard', '''
<div class="page-header"><h1 class="page-title">🖥️ Server Dashboard</h1><p class="page-subtitle">Real-time infrastructure monitoring</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;border-color:rgba(0,209,178,0.3);"><div style="font-size:0.8rem;color:var(--text-muted);">API Health</div><div style="font-size:1.5rem;font-weight:900;color:var(--success);">✓ Healthy</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">CPU Usage</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">34%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Memory</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">67%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Active Users</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">48,234</div></div>
</div>
<div class="grid-3">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Firestore Reads/s</div><div style="font-size:1.5rem;font-weight:900;color:var(--success);">8,472</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">API Requests/min</div><div style="font-size:1.5rem;font-weight:900;color:var(--primary);">24,891</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Avg Response Time</div><div style="font-size:1.5rem;font-weight:900;color:var(--success);">84ms</div></div>
</div>
'''),
    ('infrastructure/ai-usage.html', 'AI Usage & Costs', '''
<div class="page-header"><h1 class="page-title">🤖 AI Usage & Costs</h1><p class="page-subtitle">Monitor AI API consumption and spending</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">This Month Cost</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">$24,847</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">API Calls Today</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">1.2M</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Avg Cost/Student</div><div style="font-size:2rem;font-weight:900;color:var(--success);">$0.08</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Budget Remaining</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">$15K</div></div>
</div>
<div class="card">
  <h3 style="font-size:1rem;margin-bottom:1rem;">💰 Cost by Feature</h3>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:140px;font-size:0.85rem;">AI Sage Chat</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--primary);border-radius:20px;width:45%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:60px;">$11,181</div></div>
    <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:140px;font-size:0.85rem;">AI Grader</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--success);border-radius:20px;width:30%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:60px;">$7,454</div></div>
    <div style="display:flex;align-items:center;gap:1rem;"><div style="width:140px;font-size:0.85rem;">AI Proctoring</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:10px;"><div style="background:var(--warning);border-radius:20px;width:25%;height:100%;"></div></div><div style="font-size:0.85rem;text-align:right;width:60px;">$6,212</div></div>
  </div>
</div>
'''),
    ('infrastructure/db-health.html', 'Database Health', '''
<div class="page-header"><h1 class="page-title">🔥 Database Health</h1><p class="page-subtitle">Firebase Firestore monitoring and performance</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;border-color:rgba(0,209,178,0.3);"><div style="font-size:0.8rem;color:var(--text-muted);">Status</div><div style="font-size:1.5rem;font-weight:900;color:var(--success);">✓ Healthy</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Documents</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">847M</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Storage Used</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">2.4 TB</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Daily Reads</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">412M</div></div>
</div>
'''),
    ('infrastructure/backup.html', 'Backup Management', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">💾 Backup Management</h1><p class="page-subtitle">Automated backups and disaster recovery</p></div><button class="btn btn-primary">🔄 Manual Backup Now</button></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Last Backup</div><div style="font-size:1.2rem;font-weight:700;color:var(--success);">2h ago</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">RTO</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">4h</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">RPO</div><div style="font-size:2rem;font-weight:900;color:var(--success);">1h</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Backup Size</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">2.4 TB</div></div>
</div>
<div class="card">
  <h3 style="font-size:1rem;margin-bottom:1rem;">📋 Recent Backups</h3>
  <div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Full Backup</span><span style="color:var(--text-muted);">Jan 15, 12:00 AM</span><span style="color:var(--success);">✓ Success · 2.38 TB</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Incremental</span><span style="color:var(--text-muted);">Jan 14, 6:00 PM</span><span style="color:var(--success);">✓ Success · 124 GB</span></div>
    <div style="display:flex;justify-content:space-between;padding:0.75rem;font-size:0.9rem;"><span>Incremental</span><span style="color:var(--text-muted);">Jan 14, 12:00 PM</span><span style="color:var(--success);">✓ Success · 89 GB</span></div>
  </div>
</div>
'''),
]:
    write_file(f'app/super-admin/{page_info[0]}', super_sub(page_info[1], page_info[2]))

# Security pages
for page_info in [
    ('security/threats.html', 'Threat Detection', '''
<div class="page-header"><h1 class="page-title">🚨 Threat Detection</h1><p class="page-subtitle">Real-time security monitoring and threat intelligence</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;border-color:rgba(0,209,178,0.3);"><div style="font-size:0.8rem;color:var(--text-muted);">Threat Level</div><div style="font-size:1.5rem;font-weight:700;color:var(--success);">LOW</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Blocked Today</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">1,247</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Active Incidents</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">0</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Failed Logins</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">234</div></div>
</div>
<div class="card">
  <h3 style="font-size:1rem;margin-bottom:1rem;">🔒 Recent Threat Events</h3>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.85rem;">
      <div style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;flex-shrink:0;">WARN</div>
      <div style="flex:1;">Brute force attempt blocked — 52 failed logins from 203.45.67.89</div>
      <div style="color:var(--text-muted);flex-shrink:0;">14:23</div>
    </div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;font-size:0.85rem;">
      <div style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;flex-shrink:0;">INFO</div>
      <div style="flex:1;">Suspicious login pattern detected and blocked for user account</div>
      <div style="color:var(--text-muted);flex-shrink:0;">09:15</div>
    </div>
  </div>
</div>
'''),
    ('security/ddos.html', 'DDoS Protection', '''
<div class="page-header"><h1 class="page-title">🛡️ DDoS Protection</h1><p class="page-subtitle">Cloudflare + Google Cloud Armor integration</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;border-color:rgba(0,209,178,0.3);"><div style="font-size:0.8rem;color:var(--text-muted);">Protection Status</div><div style="font-size:1.2rem;font-weight:700;color:var(--success);">✓ Active</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Requests/s</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">12,847</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Blocked Today</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">4.2K</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Challenge Rate</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">0.3%</div></div>
</div>
'''),
    ('security/logs.html', 'Security Logs', '''
<div class="page-header"><h1 class="page-title">📋 Security Logs</h1><p class="page-subtitle">Complete audit trail of all security events</p></div>
<div class="card">
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
    <input type="search" placeholder="Search security logs..." style="flex:1;min-width:200px;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;">
    <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Severity</option><option>Critical</option><option>High</option><option>Medium</option><option>Low</option></select>
    <button class="btn btn-ghost" style="padding:0.6rem 1rem;font-size:0.85rem;">📥 Export</button>
  </div>
  <div style="font-family:monospace;font-size:0.8rem;line-height:2;color:var(--text-muted);">
    <div><span style="color:var(--text-muted);">[2025-01-15 14:23:47]</span> <span style="color:var(--warning);">WARN</span> Brute force: 52 failed attempts from 203.45.67.89 — blocked</div>
    <div><span style="color:var(--text-muted);">[2025-01-15 12:00:00]</span> <span style="color:var(--success);">INFO</span> Automated backup completed successfully — 2.38 TB</div>
    <div><span style="color:var(--text-muted);">[2025-01-15 09:15:33]</span> <span style="color:var(--warning);">WARN</span> Anomalous login pattern detected — account temporarily locked</div>
    <div><span style="color:var(--text-muted);">[2025-01-15 08:00:12]</span> <span style="color:var(--success);">INFO</span> All systems health check passed</div>
  </div>
</div>
'''),
]:
    write_file(f'app/super-admin/{page_info[0]}', super_sub(page_info[1], page_info[2]))

# Content pages
for page_info in [
    ('content/question-bank.html', 'Global Question Bank', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏦 Global Question Bank</h1><p class="page-subtitle">Master question repository for all schools</p></div><button class="btn btn-primary">+ Add Questions</button></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Questions</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">2.4M</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">AI Generated</div><div style="font-size:2rem;font-weight:900;color:var(--success);">840K</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Subjects</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">28</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Grade Levels</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">10</div></div>
</div>
'''),
    ('content/roadmaps.html', 'Learning Roadmaps', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🗺️ Learning Roadmaps</h1><p class="page-subtitle">Curriculum pathways for all subjects and grades</p></div><button class="btn btn-primary">+ Create Roadmap</button></div></div>
<div class="grid-3">
  <div class="card"><div style="font-size:2rem;margin-bottom:0.75rem;">📐</div><h3 style="margin-bottom:0.5rem;">Mathematics</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Grades 3-12 · 10 levels · 240 topics</p><div style="font-size:0.8rem;color:var(--text-muted);">Last updated: Jan 10, 2025</div><div style="display:flex;gap:0.5rem;margin-top:1rem;"><button class="btn btn-primary" style="flex:1;font-size:0.8rem;padding:0.4rem;">Edit</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem;">Preview</button></div></div>
  <div class="card"><div style="font-size:2rem;margin-bottom:0.75rem;">🔬</div><h3 style="margin-bottom:0.5rem;">Science</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Grades 3-12 · 10 levels · 180 topics</p><div style="font-size:0.8rem;color:var(--text-muted);">Last updated: Jan 8, 2025</div><div style="display:flex;gap:0.5rem;margin-top:1rem;"><button class="btn btn-primary" style="flex:1;font-size:0.8rem;padding:0.4rem;">Edit</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem;">Preview</button></div></div>
  <div class="card"><div style="font-size:2rem;margin-bottom:0.75rem;">💻</div><h3 style="margin-bottom:0.5rem;">Computer Science</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Grades 6-12 · 7 levels · 120 topics</p><div style="font-size:0.8rem;color:var(--text-muted);">Last updated: Jan 12, 2025</div><div style="display:flex;gap:0.5rem;margin-top:1rem;"><button class="btn btn-primary" style="flex:1;font-size:0.8rem;padding:0.4rem;">Edit</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem;">Preview</button></div></div>
</div>
'''),
    ('content/achievements.html', 'Achievements Management', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏆 Achievements Manager</h1><p class="page-subtitle">Configure platform-wide badges and achievements</p></div><button class="btn btn-primary">+ Create Achievement</button></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Achievements</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">247</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Earned Today</div><div style="font-size:2rem;font-weight:900;color:var(--success);">8,472</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Rarest Badge</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">💎</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Most Earned</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">🔥</div></div>
</div>
<div class="grid-4">
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🌟</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">First Blood</div><div style="font-size:0.75rem;color:var(--text-muted);">Earned: 124K times</div></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">🔥</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">On Fire</div><div style="font-size:0.75rem;color:var(--text-muted);">Earned: 89K times</div></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">💎</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Diamond Mind</div><div style="font-size:0.75rem;color:var(--text-muted);">Earned: 47 times</div></div>
  <div class="card" style="text-align:center;cursor:pointer;"><div style="font-size:3rem;margin-bottom:0.75rem;">👑</div><div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem;">Guild Master</div><div style="font-size:0.75rem;color:var(--text-muted);">Earned: 1,247 times</div></div>
</div>
'''),
]:
    write_file(f'app/super-admin/{page_info[0]}', super_sub(page_info[1], page_info[2]))

print("Parent and super admin pages created")
