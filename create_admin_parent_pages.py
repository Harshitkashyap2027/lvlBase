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
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def admin_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Admin</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 🏫</div>
  <div class="navbar-nav">
    <a href="dashboard.html" class="nav-link">🏠 Home</a>
    <a href="analytics/performance.html" class="nav-link">📊 Analytics</a>
    <a href="users/students.html" class="nav-link">👥 Users</a>
    <a href="operations/hall-pass.html" class="nav-link">🔑 Operations</a>
    <a href="security/audit-logs.html" class="nav-link">🔒 Security</a>
  </div>
  <div class="navbar-actions"><div class="avatar" style="background:linear-gradient(135deg,var(--accent),var(--warning));">A</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

def admin_sub_page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Admin</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 🏫</div>
  <div class="navbar-nav">
    <a href="../dashboard.html" class="nav-link">🏠 Home</a>
    <a href="../analytics/performance.html" class="nav-link">📊 Analytics</a>
    <a href="../users/students.html" class="nav-link">👥 Users</a>
    <a href="../operations/hall-pass.html" class="nav-link">🔑 Ops</a>
    <a href="../security/audit-logs.html" class="nav-link">🔒 Security</a>
  </div>
  <div class="navbar-actions"><div class="avatar" style="background:linear-gradient(135deg,var(--accent),var(--warning));">A</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
</body>
</html>'''

# School Admin pages
write_file('app/school-admin/broadcast.html', admin_page('Broadcast', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📢 Broadcast Center</h1><p class="page-subtitle">Send announcements to the whole school</p></div></div></div>
<div class="grid-2">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">✉️ New Announcement</h3>
    <div class="form-group"><label class="form-label">Send To</label><select class="form-control"><option>All Students</option><option>All Teachers</option><option>All Parents</option><option>Everyone</option><option>Grade 10</option></select></div>
    <div class="form-group"><label class="form-label">Priority</label><select class="form-control"><option>Normal</option><option>Important</option><option>🚨 Urgent</option></select></div>
    <div class="form-group"><label class="form-label">Subject</label><input class="form-control" type="text" placeholder="Announcement title"></div>
    <div class="form-group"><label class="form-label">Message</label><textarea class="form-control" rows="5" style="height:120px;resize:vertical;" placeholder="Write your announcement..."></textarea></div>
    <div style="display:flex;gap:0.75rem;"><button class="btn btn-primary">📤 Send Now</button><button class="btn btn-ghost">📅 Schedule</button><button class="btn btn-ghost">👁️ Preview</button></div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📋 Recent Announcements</h3>
    <div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem;"><div style="font-weight:600;font-size:0.9rem;">Term 2 Exam Schedule Released</div><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;">All</span></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">Yesterday · Opened by 847/1200</div>
      </div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem;"><div style="font-weight:600;font-size:0.9rem;">School Closure — Weather Advisory</div><span style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;">Urgent</span></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">3 days ago · Opened by 1,198/1200</div>
      </div>
      <div style="padding:0.75rem;">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem;"><div style="font-weight:600;font-size:0.9rem;">XP Bonus Week — All Classes!</div><span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;">Students</span></div>
        <div style="font-size:0.8rem;color:var(--text-muted);">1 week ago · Opened by 923/1200</div>
      </div>
    </div>
  </div>
</div>
'''))

write_file('app/school-admin/calendar.html', admin_page('School Calendar', '''
<div class="page-header"><h1 class="page-title">📅 School Calendar</h1><p class="page-subtitle">Manage all school events and schedules</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Events This Month</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">18</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Exams Scheduled</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">6</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">PT Meetings</div><div style="font-size:2rem;font-weight:900;color:var(--success);">45</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Holidays</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">2</div></div>
</div>
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;"><h3 style="font-size:1rem;">January 2025</h3><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost" style="padding:0.4rem 1rem;">◀ Prev</button><button class="btn btn-ghost" style="padding:0.4rem 1rem;">Next ▶</button><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.85rem;">+ Add Event</button></div></div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center;">
    <div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Sun</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Mon</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Tue</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Wed</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Thu</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Fri</div><div style="font-size:0.8rem;color:var(--text-muted);padding:0.5rem;font-weight:600;">Sat</div>
    <div style="padding:0.5rem;"></div><div style="padding:0.5rem;"></div><div style="padding:0.5rem;"></div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">1</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">2</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">3</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">4</div>
    <div style="padding:0.5rem;border-radius:8px;cursor:pointer;">5</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">6</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">7</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">8</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">9</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">10</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">11</div>
    <div style="padding:0.5rem;border-radius:8px;cursor:pointer;">12</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;background:rgba(108,99,255,0.2);color:var(--primary);">13</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">14</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;background:linear-gradient(135deg,var(--primary),var(--primary-dark));color:white;font-weight:700;">15</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">16</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;background:rgba(255,68,68,0.2);color:var(--danger);">17</div><div style="padding:0.5rem;border-radius:8px;cursor:pointer;">18</div>
  </div>
</div>
'''))

# Analytics pages
write_file('app/school-admin/analytics/performance.html', admin_sub_page('Performance Analytics', '''
<div class="page-header"><h1 class="page-title">📊 Performance Analytics</h1><p class="page-subtitle">School-wide academic performance overview</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">School Avg</div><div style="font-size:2rem;font-weight:900;color:var(--success);">B+</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Pass Rate</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">94.2%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">At-Risk Students</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">23</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total XP Earned</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">4.2M</div></div>
</div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">📈 Monthly Performance Trend</h3>
    <div style="display:flex;align-items:flex-end;gap:0.75rem;height:150px;padding:0 0.5rem;">
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="flex:1;display:flex;align-items:flex-end;width:100%;"><div style="background:rgba(108,99,255,0.4);border-radius:4px 4px 0 0;width:100%;height:60%;"></div></div><div style="font-size:0.7rem;color:var(--text-muted);">Sep</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="flex:1;display:flex;align-items:flex-end;width:100%;"><div style="background:rgba(108,99,255,0.5);border-radius:4px 4px 0 0;width:100%;height:70%;"></div></div><div style="font-size:0.7rem;color:var(--text-muted);">Oct</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="flex:1;display:flex;align-items:flex-end;width:100%;"><div style="background:rgba(108,99,255,0.6);border-radius:4px 4px 0 0;width:100%;height:75%;"></div></div><div style="font-size:0.7rem;color:var(--text-muted);">Nov</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="flex:1;display:flex;align-items:flex-end;width:100%;"><div style="background:rgba(108,99,255,0.7);border-radius:4px 4px 0 0;width:100%;height:80%;"></div></div><div style="font-size:0.7rem;color:var(--text-muted);">Dec</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="flex:1;display:flex;align-items:flex-end;width:100%;"><div style="background:var(--primary);border-radius:4px 4px 0 0;width:100%;height:92%;"></div></div><div style="font-size:0.7rem;color:var(--text-muted);">Jan</div></div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1.5rem;font-size:1rem;">🎯 Grade Distribution</h3>
    <div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:24px;font-size:0.85rem;font-weight:700;color:var(--success);">A</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--success);border-radius:20px;width:28%;height:100%;"></div></div><div style="font-size:0.85rem;color:var(--text-muted);width:40px;text-align:right;">28%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:24px;font-size:0.85rem;font-weight:700;color:var(--primary);">B</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--primary);border-radius:20px;width:42%;height:100%;"></div></div><div style="font-size:0.85rem;color:var(--text-muted);width:40px;text-align:right;">42%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;"><div style="width:24px;font-size:0.85rem;font-weight:700;color:var(--warning);">C</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--warning);border-radius:20px;width:22%;height:100%;"></div></div><div style="font-size:0.85rem;color:var(--text-muted);width:40px;text-align:right;">22%</div></div>
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:24px;font-size:0.85rem;font-weight:700;color:var(--danger);">D/F</div><div style="flex:1;background:rgba(255,255,255,0.1);border-radius:20px;height:8px;"><div style="background:var(--danger);border-radius:20px;width:8%;height:100%;"></div></div><div style="font-size:0.85rem;color:var(--text-muted);width:40px;text-align:right;">8%</div></div>
    </div>
  </div>
</div>
'''))

write_file('app/school-admin/analytics/teacher-metrics.html', admin_sub_page('Teacher Metrics', '''
<div class="page-header"><h1 class="page-title">👨‍🏫 Teacher Metrics</h1><p class="page-subtitle">Measure teacher effectiveness and student outcomes</p></div>
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;"><h3 style="font-size:1rem;">Teacher Performance Rankings</h3><select style="padding:0.5rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>This Semester</option><option>Last Semester</option></select></div>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;padding:1rem;border-bottom:1px solid var(--border-color);">
      <div style="color:var(--accent);font-weight:700;font-size:1.2rem;width:30px;">1</div>
      <div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;">R</div>
      <div style="flex:1;"><div style="font-weight:700;margin-bottom:0.25rem;">Ms. Rodriguez</div><div style="font-size:0.8rem;color:var(--text-muted);">Mathematics · 3 classes</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--success);">94.2%</div><div style="font-size:0.75rem;color:var(--text-muted);">Student pass rate</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--accent);">4.9★</div><div style="font-size:0.75rem;color:var(--text-muted);">Student rating</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--primary);">+47%</div><div style="font-size:0.75rem;color:var(--text-muted);">Engagement</div></div>
    </div>
    <div style="display:flex;align-items:center;gap:1rem;padding:1rem;border-bottom:1px solid var(--border-color);">
      <div style="color:var(--text-muted);font-weight:700;font-size:1.2rem;width:30px;">2</div>
      <div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;">P</div>
      <div style="flex:1;"><div style="font-weight:700;margin-bottom:0.25rem;">Mr. Patel</div><div style="font-size:0.8rem;color:var(--text-muted);">Science · 2 classes</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--success);">91.8%</div><div style="font-size:0.75rem;color:var(--text-muted);">Student pass rate</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--accent);">4.7★</div><div style="font-size:0.75rem;color:var(--text-muted);">Student rating</div></div>
      <div style="text-align:center;"><div style="font-weight:700;color:var(--primary);">+39%</div><div style="font-size:0.75rem;color:var(--text-muted);">Engagement</div></div>
    </div>
  </div>
</div>
'''))

write_file('app/school-admin/analytics/reports.html', admin_sub_page('Reports', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📑 Reports</h1><p class="page-subtitle">Generate and download school reports</p></div><button class="btn btn-primary">+ Custom Report</button></div></div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="cursor:pointer;">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">📊</div>
    <h3 style="margin-bottom:0.5rem;">Academic Report</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">School-wide grades, pass rates, and performance trends</p>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Generate PDF 📥</button>
  </div>
  <div class="card" style="cursor:pointer;">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">👥</div>
    <h3 style="margin-bottom:0.5rem;">Attendance Report</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Monthly attendance rates per class and student</p>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Generate PDF 📥</button>
  </div>
  <div class="card" style="cursor:pointer;">
    <div style="font-size:2.5rem;margin-bottom:0.75rem;">🔒</div>
    <h3 style="margin-bottom:0.5rem;">Compliance Report</h3>
    <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">FERPA/COPPA compliance status and data summary</p>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Generate PDF 📥</button>
  </div>
</div>
'''))

# Users pages
for page_info in [
    ('users/approvals.html', 'User Approvals', '''
<div class="page-header"><h1 class="page-title">✅ User Approvals</h1><p class="page-subtitle">Review and approve new account requests</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Pending</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">14</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Approved Today</div><div style="font-size:2rem;font-weight:900;color:var(--success);">8</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Rejected</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Users</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">1,247</div></div>
</div>
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">Pending Approvals</h3><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.8rem;">Approve All ✓</button></div>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;border-bottom:1px solid var(--border-color);">
      <div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;">J</div>
      <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">Jordan Smith</div><div style="font-size:0.8rem;color:var(--text-muted);">Student · Grade 10 · Requested 2h ago</div></div>
      <div style="display:flex;gap:0.5rem;">
        <button class="btn btn-primary" style="padding:0.3rem 0.75rem;font-size:0.8rem;background:rgba(0,209,178,0.2);color:var(--success);">✓ Approve</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;color:var(--danger);">✗ Reject</button>
      </div>
    </div>
  </div>
</div>
'''),
    ('users/students.html', 'Student Management', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🎓 Student Management</h1><p class="page-subtitle">1,047 total students enrolled</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">📥 Import CSV</button><button class="btn btn-primary">+ Add Student</button></div></div></div>
<div class="card">
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
    <input type="search" placeholder="Search students..." style="flex:1;min-width:200px;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;">
    <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Grades</option><option>Grade 9</option><option>Grade 10</option><option>Grade 11</option><option>Grade 12</option></select>
  </div>
  <table style="width:100%;border-collapse:collapse;">
    <thead><tr style="border-bottom:1px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Student</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Grade</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Rank</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Status</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Actions</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">A</div><div><div style="font-weight:600;font-size:0.9rem;">Alex Johnson</div><div style="font-size:0.75rem;color:var(--text-muted);">alex@school.edu</div></div></div></td><td style="padding:0.75rem;">Grade 10</td><td style="padding:0.75rem;"><span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;font-weight:700;">A</span></td><td style="padding:0.75rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;">Active</span></td><td style="padding:0.75rem;"><div style="display:flex;gap:0.5rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">View</button><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">Edit</button></div></td></tr>
    </tbody>
  </table>
</div>
'''),
    ('users/teachers.html', 'Teacher Management', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">👨‍🏫 Teacher Management</h1><p class="page-subtitle">42 teachers · 8 departments</p></div><button class="btn btn-primary">+ Invite Teacher</button></div></div>
<div class="grid-3">
  <div class="card" style="cursor:pointer;"><div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;"><div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;">R</div><div><div style="font-weight:700;">Ms. Rodriguez</div><div style="font-size:0.85rem;color:var(--text-muted);">Mathematics Dept.</div></div></div><div style="display:flex;justify-content:space-between;font-size:0.85rem;color:var(--text-muted);margin-bottom:0.75rem;"><span>3 classes · 84 students</span><span style="color:var(--accent);">⭐ Top Teacher</span></div><div style="display:flex;gap:0.5rem;"><button class="btn btn-primary" style="flex:1;font-size:0.8rem;padding:0.4rem;">View Profile</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem;">Message</button></div></div>
  <div class="card" style="cursor:pointer;"><div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;"><div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;">P</div><div><div style="font-weight:700;">Mr. Patel</div><div style="font-size:0.85rem;color:var(--text-muted);">Science Dept.</div></div></div><div style="display:flex;justify-content:space-between;font-size:0.85rem;color:var(--text-muted);margin-bottom:0.75rem;"><span>2 classes · 56 students</span></div><div style="display:flex;gap:0.5rem;"><button class="btn btn-primary" style="flex:1;font-size:0.8rem;padding:0.4rem;">View Profile</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem;">Message</button></div></div>
</div>
'''),
    ('users/parents.html', 'Parent Management', '''
<div class="page-header"><h1 class="page-title">👨‍👩‍👧 Parent Management</h1><p class="page-subtitle">847 parent accounts</p></div>
<div class="card">
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;"><input type="search" placeholder="Search parents..." style="flex:1;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><button class="btn btn-primary" style="font-size:0.85rem;">📨 Bulk Email</button></div>
  <table style="width:100%;border-collapse:collapse;">
    <thead><tr style="border-bottom:1px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Parent</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Child</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Last Login</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Actions</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;font-size:0.9rem;">Mr. & Mrs. Johnson</td><td style="padding:0.75rem;font-size:0.9rem;">Alex Johnson</td><td style="padding:0.75rem;font-size:0.9rem;color:var(--text-muted);">Today 9:30 AM</td><td style="padding:0.75rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">View</button></td></tr>
      <tr><td style="padding:0.75rem;font-weight:600;font-size:0.9rem;">Mrs. Turner</td><td style="padding:0.75rem;font-size:0.9rem;">Marcus Turner</td><td style="padding:0.75rem;font-size:0.9rem;color:var(--text-muted);">Yesterday</td><td style="padding:0.75rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">View</button></td></tr>
    </tbody>
  </table>
</div>
'''),
    ('users/alumni.html', 'Alumni Management', '''
<div class="page-header"><h1 class="page-title">�� Alumni Management</h1><p class="page-subtitle">Track and connect with graduates</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Alumni</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">2,847</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Graduated 2024</div><div style="font-size:2rem;font-weight:900;color:var(--success);">312</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">With Certificates</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">284</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">College Enrolled</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">268</div></div>
</div>
'''),
]:
    write_file(f'app/school-admin/{page_info[0]}', admin_sub_page(page_info[1], page_info[2]))

# Operations pages
write_file('app/school-admin/operations/hall-pass.html', admin_sub_page('Digital Hall Pass', '''
<div class="page-header"><h1 class="page-title">🔑 Digital Hall Pass</h1><p class="page-subtitle">Track student movement in real-time</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Active Passes</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">8</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Issued Today</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">47</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Avg Duration</div><div style="font-size:2rem;font-weight:900;color:var(--success);">8 min</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Flagged (Long)</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">1</div></div>
</div>
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">Active Hall Passes</h3><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.8rem;">+ Issue Pass</button></div>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;border-bottom:1px solid var(--border-color);background:rgba(255,68,68,0.05);border-radius:var(--radius);margin-bottom:0.5rem;">
      <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--danger),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">M</div>
      <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">Marcus Turner</div><div style="font-size:0.8rem;color:var(--text-muted);">Restroom · Grade 10A · Issued 14:23</div></div>
      <div style="font-size:0.9rem;font-weight:700;color:var(--danger);">23 min ⚠️</div>
      <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">Recall</button>
    </div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;">
      <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">S</div>
      <div style="flex:1;"><div style="font-weight:600;font-size:0.9rem;">Sarah Mitchell</div><div style="font-size:0.8rem;color:var(--text-muted);">Nurse · Grade 11A · Issued 14:31</div></div>
      <div style="font-size:0.9rem;font-weight:700;color:var(--success);">4 min ✓</div>
      <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">Recall</button>
    </div>
  </div>
</div>
'''))

write_file('app/school-admin/operations/emergency.html', admin_sub_page('Emergency Protocols', '''
<div class="page-header"><h1 class="page-title">🚨 Emergency Protocols</h1><p class="page-subtitle">Manage school safety and emergency procedures</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card" style="border-color:rgba(255,68,68,0.3);">
    <h3 style="color:var(--danger);margin-bottom:1.5rem;font-size:1rem;">🚨 Emergency Actions</h3>
    <div style="display:flex;flex-direction:column;gap:0.75rem;">
      <button class="btn" style="background:rgba(255,68,68,0.15);color:var(--danger);border:1px solid rgba(255,68,68,0.3);justify-content:center;font-size:1rem;">🔒 LOCKDOWN</button>
      <button class="btn" style="background:rgba(255,159,67,0.15);color:var(--warning);border:1px solid rgba(255,159,67,0.3);justify-content:center;">🔥 Fire Evacuation</button>
      <button class="btn btn-ghost" style="justify-content:center;">🌊 Shelter in Place</button>
      <button class="btn btn-ghost" style="justify-content:center;">📢 Mass Notification</button>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📋 Drill Schedule</h3>
    <div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">🔥 Fire Drill</div><div style="font-size:0.8rem;color:var(--text-muted);">Jan 22, 10:00 AM · Notified all staff</div></div>
      <div style="padding:0.75rem;"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">🔒 Lockdown Drill</div><div style="font-size:0.8rem;color:var(--text-muted);">Feb 5, 2:00 PM · Scheduled</div></div>
    </div>
  </div>
</div>
'''))

write_file('app/school-admin/operations/assets.html', admin_sub_page('Asset Management', '''
<div class="page-header"><h1 class="page-title">🖥️ Asset Management</h1><p class="page-subtitle">Track school devices and equipment</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Devices</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">847</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">In Use</div><div style="font-size:2rem;font-weight:900;color:var(--success);">634</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Needs Repair</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">12</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Available</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">201</div></div>
</div>
<div class="card">
  <table style="width:100%;border-collapse:collapse;">
    <thead><tr style="border-bottom:1px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Device</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Quantity</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Status</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;">Chromebooks</td><td style="padding:0.75rem;">450</td><td style="padding:0.75rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.75rem;border-radius:10px;font-size:0.8rem;">Good</span></td></tr>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;">iPads</td><td style="padding:0.75rem;">200</td><td style="padding:0.75rem;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.75rem;border-radius:10px;font-size:0.8rem;">Good</span></td></tr>
      <tr><td style="padding:0.75rem;font-weight:600;">Projectors</td><td style="padding:0.75rem;">24</td><td style="padding:0.75rem;"><span style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.2rem 0.75rem;border-radius:10px;font-size:0.8rem;">3 Repair</span></td></tr>
    </tbody>
  </table>
</div>
'''))

# Security pages
for page_info in [
    ('security/sso-config.html', 'SSO Configuration', '''
<div class="page-header"><h1 class="page-title">🔑 SSO Configuration</h1><p class="page-subtitle">Configure Single Sign-On providers for your school</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card" style="border-color:rgba(0,209,178,0.3);">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><div style="font-size:1.5rem;">🔵</div><div><h3 style="font-size:1rem;">Google Workspace</h3><div style="font-size:0.85rem;color:var(--success);">✓ Connected</div></div></div><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.85rem;">Configure</button></div>
    <p style="color:var(--text-muted);font-size:0.85rem;">Domain: @riverside-academy.edu · 1,247 accounts synced</p>
  </div>
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><div style="font-size:1.5rem;">🟦</div><div><h3 style="font-size:1rem;">Microsoft 365</h3><div style="font-size:0.85rem;color:var(--text-muted);">Not connected</div></div></div><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.85rem;">Connect</button></div>
    <p style="color:var(--text-muted);font-size:0.85rem;">Sync with Azure AD for seamless login</p>
  </div>
</div>
'''),
    ('security/firewall.html', 'Network Firewall', '''
<div class="page-header"><h1 class="page-title">🛡️ Network Firewall Settings</h1><p class="page-subtitle">Content filtering and network access control</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">�� Blocked Categories</h3>
    <div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Social Media (non-educational)</span><span style="color:var(--danger);">Blocked</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Adult Content</span><span style="color:var(--danger);">Blocked</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>Gaming (during class)</span><span style="color:var(--warning);">Limited</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;font-size:0.9rem;"><span>Educational Resources</span><span style="color:var(--success);">Allowed</span></div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">⏰ Access Schedule</h3>
    <div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>School Hours (8AM-4PM)</span><span style="color:var(--warning);">Filtered</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid var(--border-color);font-size:0.9rem;"><span>After School (4PM-10PM)</span><span style="color:var(--success);">Relaxed</span></div>
      <div style="display:flex;justify-content:space-between;padding:0.5rem 0;font-size:0.9rem;"><span>Exam Mode</span><span style="color:var(--danger);">Strict</span></div>
    </div>
  </div>
</div>
'''),
    ('security/audit-logs.html', 'Audit Logs', '''
<div class="page-header"><h1 class="page-title">📋 Audit Logs</h1><p class="page-subtitle">Track all admin actions and system events</p></div>
<div class="card">
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
    <input type="search" placeholder="Search logs..." style="flex:1;min-width:200px;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;">
    <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Events</option><option>Login</option><option>Data Export</option><option>User Changes</option></select>
    <button class="btn btn-ghost" style="padding:0.6rem 1rem;font-size:0.85rem;">📥 Export CSV</button>
  </div>
  <div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.85rem;"><div style="color:var(--text-muted);width:140px;flex-shrink:0;">Jan 15, 2:34 PM</div><div style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;flex-shrink:0;">USER_CREATE</div><div style="flex:1;padding:0 1rem;">Admin created student account for Alex Johnson</div><div style="color:var(--text-muted);">admin@school.edu</div></div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;border-bottom:1px solid var(--border-color);font-size:0.85rem;"><div style="color:var(--text-muted);width:140px;flex-shrink:0;">Jan 15, 1:22 PM</div><div style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;flex-shrink:0;">DATA_EXPORT</div><div style="flex:1;padding:0 1rem;">Exported student attendance report Q1 2025</div><div style="color:var(--text-muted);">admin@school.edu</div></div>
    <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;font-size:0.85rem;"><div style="color:var(--text-muted);width:140px;flex-shrink:0;">Jan 15, 9:00 AM</div><div style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.15rem 0.5rem;border-radius:8px;font-size:0.75rem;flex-shrink:0;">LOGIN</div><div style="flex:1;padding:0 1rem;">Admin logged in from 192.168.1.45</div><div style="color:var(--text-muted);">admin@school.edu</div></div>
  </div>
</div>
'''),
    ('security/data-export.html', 'Data Export', '''
<div class="page-header"><h1 class="page-title">📤 Data Export</h1><p class="page-subtitle">Export school data in compliance with FERPA/GDPR</p></div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.75rem;">🎓</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Student Records</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">All student academic records, grades, and attendance</p><button class="btn btn-primary" style="width:100%;font-size:0.85rem;">Export CSV 📥</button></div>
  <div class="card" style="cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.75rem;">📊</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Analytics Data</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Performance metrics and engagement analytics</p><button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Export CSV 📥</button></div>
  <div class="card" style="cursor:pointer;"><div style="font-size:2.5rem;margin-bottom:0.75rem;">📋</div><h3 style="margin-bottom:0.5rem;font-size:1rem;">Audit Logs</h3><p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">System access and admin action logs</p><button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">Export CSV 📥</button></div>
</div>
<div class="card"><p style="color:var(--text-muted);font-size:0.85rem;">⚠️ Data exports are logged for compliance. Exports include only data you are authorized to access under FERPA guidelines.</p></div>
'''),
]:
    write_file(f'app/school-admin/{page_info[0]}', admin_sub_page(page_info[1], page_info[2]))

print("School admin pages created")
