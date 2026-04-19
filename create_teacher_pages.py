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
.btn-success { background: linear-gradient(135deg, var(--success), #00A896); color: white; }
.btn-ghost { background: transparent; color: var(--text-muted); border: 1px solid var(--border-color); }
.btn-ghost:hover { background: rgba(255,255,255,0.05); color: var(--text-light); }
.page-header { margin-bottom: 2rem; }
.page-title { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.25rem; }
.page-subtitle { color: var(--text-muted); font-size: 0.95rem; }
.form-group { margin-bottom: 1.25rem; }
.form-label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
.form-control { width: 100%; padding: 0.75rem 1rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border-color); border-radius: var(--radius); color: var(--text-light); font-family: inherit; font-size: 0.9rem; }
.form-control:focus { outline: none; border-color: var(--primary); }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .navbar-nav { display: none; } }'''

def teacher_page(title, body, scripts=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Teacher</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 🍎</div>
  <div class="navbar-nav">
    <a href="dashboard.html" class="nav-link">🏠 Dashboard</a>
    <a href="classes/rosters.html" class="nav-link">👥 Classes</a>
    <a href="assessments/assignments.html" class="nav-link">📋 Assessments</a>
    <a href="proctoring/live-monitor.html" class="nav-link">👁️ Monitor</a>
    <a href="communications.html" class="nav-link">💬 Messages</a>
  </div>
  <div class="navbar-actions">
    <div class="avatar">T</div>
  </div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
{scripts}
</body>
</html>'''

def teacher_subpage(title, css_depth, body, scripts=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Teacher</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_depth}core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 🍎</div>
  <div class="navbar-nav">
    <a href="{css_depth.replace("core/css/base.css","").rstrip("/")}../dashboard.html" class="nav-link">🏠 Dashboard</a>
    <a href="{css_depth.replace("core/css/base.css","").rstrip("/")}../classes/rosters.html" class="nav-link">👥 Classes</a>
    <a href="{css_depth.replace("core/css/base.css","").rstrip("/")}../assessments/assignments.html" class="nav-link">📋 Assessments</a>
    <a href="{css_depth.replace("core/css/base.css","").rstrip("/")}../proctoring/live-monitor.html" class="nav-link">👁️ Monitor</a>
    <a href="{css_depth.replace("core/css/base.css","").rstrip("/")}../communications.html" class="nav-link">💬 Messages</a>
  </div>
  <div class="navbar-actions"><div class="avatar">T</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
{scripts}
</body>
</html>'''

# app/teacher/communications.html
write_file('app/teacher/communications.html', teacher_page('Communications', '''
<div class="page-header"><h1 class="page-title">💬 Communications Hub</h1><p class="page-subtitle">Messages, announcements, and parent connects</p></div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:2rem;margin-bottom:0.5rem;">📨</div><div style="font-size:1.8rem;font-weight:900;color:var(--primary);">8</div><div style="font-size:0.85rem;color:var(--text-muted);">Unread Messages</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:2rem;margin-bottom:0.5rem;">👨‍👩‍👧</div><div style="font-size:1.8rem;font-weight:900;color:var(--success);">3</div><div style="font-size:0.85rem;color:var(--text-muted);">Parent Requests</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:2rem;margin-bottom:0.5rem;">📢</div><div style="font-size:1.8rem;font-weight:900;color:var(--accent);">1</div><div style="font-size:0.85rem;color:var(--text-muted);">Pending Announcement</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">📨 Recent Messages</h3><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.8rem;">Compose ✉️</button></div>
    <div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);cursor:pointer;border-radius:var(--radius);transition:var(--transition);">
        <div style="display:flex;justify-content:space-between;"><div style="font-weight:600;font-size:0.9rem;">Mrs. Johnson (Parent)</div><div style="font-size:0.8rem;color:var(--text-muted);">2h ago</div></div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-top:0.25rem;">Re: Alex\'s math performance this week</div>
      </div>
      <div style="padding:0.75rem;border-bottom:1px solid var(--border-color);cursor:pointer;">
        <div style="display:flex;justify-content:space-between;"><div style="font-weight:600;font-size:0.9rem;">Principal Chen</div><div style="font-size:0.8rem;color:var(--text-muted);">5h ago</div></div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-top:0.25rem;">Staff meeting moved to Tuesday</div>
      </div>
      <div style="padding:0.75rem;cursor:pointer;">
        <div style="display:flex;justify-content:space-between;"><div style="font-weight:600;font-size:0.9rem;">Student: Marcus T.</div><div style="font-size:0.8rem;color:var(--text-muted);">Yesterday</div></div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-top:0.25rem;">Question about tomorrow\'s quiz</div>
      </div>
    </div>
  </div>
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">📢 Class Announcements</h3><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.8rem;">+ New</button></div>
    <div style="margin-bottom:1rem;padding:1rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);border-left:3px solid var(--primary);">
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">📝 Quiz Tomorrow - Chapter 5</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">Sent to Grade 10B · 2 hours ago</div>
    </div>
    <div style="padding:1rem;background:rgba(255,215,0,0.08);border-radius:var(--radius);border-left:3px solid var(--accent);">
      <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">🏆 XP Bonus Week!</div>
      <div style="font-size:0.8rem;color:var(--text-muted);">All classes · Yesterday</div>
    </div>
  </div>
</div>
'''))

# app/teacher/calendar.html
write_file('app/teacher/calendar.html', teacher_page('Calendar', '''
<div class="page-header"><h1 class="page-title">📅 Teacher Calendar</h1><p class="page-subtitle">Manage your schedule, lessons, and parent meetings</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Lessons Today</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">4</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Exams This Week</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">PT Meetings</div><div style="font-size:2rem;font-weight:900;color:var(--success);">5</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Pending Tasks</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">7</div></div>
</div>
<div class="grid-2">
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;"><h3 style="font-size:1rem;">Today\'s Schedule</h3><span style="font-size:0.85rem;color:var(--text-muted);">Monday, Jan 15</span></div>
    <div>
      <div style="display:flex;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);"><div style="font-size:0.8rem;color:var(--text-muted);width:60px;flex-shrink:0;">8:00 AM</div><div style="background:rgba(108,99,255,0.15);border-left:3px solid var(--primary);border-radius:0 var(--radius) var(--radius) 0;padding:0.5rem 0.75rem;flex:1;"><div style="font-weight:600;font-size:0.9rem;">Grade 10A - Mathematics</div><div style="font-size:0.8rem;color:var(--text-muted);">Room 204 · 45 min</div></div></div>
      <div style="display:flex;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);"><div style="font-size:0.8rem;color:var(--text-muted);width:60px;flex-shrink:0;">9:30 AM</div><div style="background:rgba(0,209,178,0.1);border-left:3px solid var(--success);border-radius:0 var(--radius) var(--radius) 0;padding:0.5rem 0.75rem;flex:1;"><div style="font-weight:600;font-size:0.9rem;">Grade 9B - Mathematics</div><div style="font-size:0.8rem;color:var(--text-muted);">Room 204 · 45 min</div></div></div>
      <div style="display:flex;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);"><div style="font-size:0.8rem;color:var(--text-muted);width:60px;flex-shrink:0;">1:00 PM</div><div style="background:rgba(255,159,67,0.1);border-left:3px solid var(--warning);border-radius:0 var(--radius) var(--radius) 0;padding:0.5rem 0.75rem;flex:1;"><div style="font-weight:600;font-size:0.9rem;">PT Meeting - Johnson Family</div><div style="font-size:0.8rem;color:var(--text-muted);">Conference Room · 30 min</div></div></div>
      <div style="display:flex;gap:1rem;padding:0.75rem 0;"><div style="font-size:0.8rem;color:var(--text-muted);width:60px;flex-shrink:0;">3:00 PM</div><div style="background:rgba(108,99,255,0.15);border-left:3px solid var(--primary);border-radius:0 var(--radius) var(--radius) 0;padding:0.5rem 0.75rem;flex:1;"><div style="font-weight:600;font-size:0.9rem;">Grade 11A - Mathematics</div><div style="font-size:0.8rem;color:var(--text-muted);">Room 204 · 45 min</div></div></div>
    </div>
  </div>
  <div class="card">
    <h3 style="font-size:1rem;margin-bottom:1.5rem;">➕ Add Event</h3>
    <div class="form-group"><label class="form-label">Title</label><input class="form-control" type="text" placeholder="e.g., Chapter 5 Quiz"></div>
    <div class="grid-2">
      <div class="form-group"><label class="form-label">Date</label><input class="form-control" type="date"></div>
      <div class="form-group"><label class="form-label">Time</label><input class="form-control" type="time"></div>
    </div>
    <div class="form-group"><label class="form-label">Type</label><select class="form-control"><option>Lesson</option><option>Exam</option><option>PT Meeting</option><option>Staff Meeting</option></select></div>
    <div class="form-group"><label class="form-label">Class</label><select class="form-control"><option>Grade 10A</option><option>Grade 9B</option><option>Grade 11A</option><option>All Classes</option></select></div>
    <button class="btn btn-primary">Add to Calendar 📅</button>
  </div>
</div>
'''))

# app/teacher/classes/rosters.html
write_file('app/teacher/classes/rosters.html', teacher_subpage('Class Rosters', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">👥 Class Rosters</h1><p class="page-subtitle">Manage your classes and student lists</p></div><button class="btn btn-primary">+ New Class</button></div></div>
<div class="grid-3" style="margin-bottom:2rem;">
  <div class="card" style="cursor:pointer;border-color:var(--primary);">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem;">
      <div><h3 style="font-size:1.1rem;">Grade 10A</h3><p style="color:var(--text-muted);font-size:0.85rem;">Mathematics</p></div>
      <span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;">32 students</span>
    </div>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Avg Grade: A- · Avg XP: 12,400</div>
    <button class="btn btn-primary" style="width:100%;font-size:0.85rem;">View Roster →</button>
  </div>
  <div class="card" style="cursor:pointer;">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem;">
      <div><h3 style="font-size:1.1rem;">Grade 9B</h3><p style="color:var(--text-muted);font-size:0.85rem;">Mathematics</p></div>
      <span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;">28 students</span>
    </div>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Avg Grade: B+ · Avg XP: 9,800</div>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">View Roster →</button>
  </div>
  <div class="card" style="cursor:pointer;">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem;">
      <div><h3 style="font-size:1.1rem;">Grade 11A</h3><p style="color:var(--text-muted);font-size:0.85rem;">Advanced Math</p></div>
      <span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;">24 students</span>
    </div>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem;">Avg Grade: A · Avg XP: 18,200</div>
    <button class="btn btn-ghost" style="width:100%;font-size:0.85rem;">View Roster →</button>
  </div>
</div>
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><h3 style="font-size:1rem;">Grade 10A Students</h3><input type="search" placeholder="Search students..." style="padding:0.5rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;width:250px;"></div>
  <table style="width:100%;border-collapse:collapse;">
    <thead><tr style="border-bottom:1px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;">Student</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;">Rank</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;">XP</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;">Avg Grade</th>
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;">Actions</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">A</div><div><div style="font-weight:600;font-size:0.9rem;">Alex Johnson</div><div style="font-size:0.75rem;color:var(--text-muted);">alex@school.edu</div></div></div></td><td style="padding:0.75rem;"><span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;font-weight:700;">A</span></td><td style="padding:0.75rem;font-weight:600;">14,200</td><td style="padding:0.75rem;color:var(--success);">91%</td><td style="padding:0.75rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">View</button></td></tr>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">M</div><div><div style="font-weight:600;font-size:0.9rem;">Marcus Turner</div><div style="font-size:0.75rem;color:var(--text-muted);">marcus@school.edu</div></div></div></td><td style="padding:0.75rem;"><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.2rem 0.6rem;border-radius:10px;font-size:0.8rem;font-weight:700;">B</span></td><td style="padding:0.75rem;font-weight:600;">9,400</td><td style="padding:0.75rem;color:var(--warning);">78%</td><td style="padding:0.75rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">View</button></td></tr>
    </tbody>
  </table>
</div>
'''))

# app/teacher/classes/seating-chart.html
write_file('app/teacher/classes/seating-chart.html', teacher_subpage('Seating Chart', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🪑 Seating Chart</h1><p class="page-subtitle">Drag & drop to arrange seating</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">🔀 Auto-Arrange</button><button class="btn btn-primary">💾 Save</button></div></div></div>
<div class="card" style="margin-bottom:2rem;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;"><h3 style="font-size:1rem;">Grade 10A · Room 204</h3><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.85rem;">��️ View Mode</button><button class="btn btn-ghost" style="padding:0.4rem 1rem;font-size:0.85rem;">Print 🖨️</button></div></div>
  <div style="border:2px dashed var(--border-color);border-radius:var(--radius);padding:1.5rem;margin-bottom:1rem;text-align:center;background:rgba(108,99,255,0.03);">
    <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:1.5rem;">🖥️ WHITEBOARD / FRONT OF CLASS</div>
    <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:0.75rem;max-width:700px;margin:0 auto;">
      <div style="background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Alex J.</div></div>
      <div style="background:rgba(0,209,178,0.1);border:1px solid rgba(0,209,178,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Sarah M.</div></div>
      <div style="background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Marcus T.</div></div>
      <div style="background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Emily K.</div></div>
      <div style="background:rgba(0,209,178,0.1);border:1px solid rgba(0,209,178,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>James R.</div></div>
      <div style="border:1px dashed var(--border-color);border-radius:8px;padding:0.5rem;text-align:center;font-size:0.75rem;color:var(--text-muted);">Empty</div>
      <div style="background:rgba(255,107,107,0.1);border:1px solid rgba(255,107,107,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Zoe L.</div></div>
      <div style="background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Ryan O.</div></div>
      <div style="border:1px dashed var(--border-color);border-radius:8px;padding:0.5rem;text-align:center;font-size:0.75rem;color:var(--text-muted);">Empty</div>
      <div style="background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Nina P.</div></div>
      <div style="background:rgba(0,209,178,0.1);border:1px solid rgba(0,209,178,0.2);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Tom H.</div></div>
      <div style="background:rgba(108,99,255,0.15);border:1px solid rgba(108,99,255,0.3);border-radius:8px;padding:0.5rem;text-align:center;cursor:grab;font-size:0.75rem;"><div>Lisa W.</div></div>
    </div>
    <div style="font-size:0.9rem;color:var(--text-muted);margin-top:1.5rem;">👨‍🏫 TEACHER\'S DESK</div>
  </div>
</div>
'''))

# app/teacher/classes/attendance.html
write_file('app/teacher/classes/attendance.html', teacher_subpage('Attendance', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📋 Attendance Tracker</h1><p class="page-subtitle">Today: Monday, January 15, 2025</p></div><div style="display:flex;gap:0.75rem;"><select style="padding:0.5rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>Grade 10A</option><option>Grade 9B</option><option>Grade 11A</option></select><button class="btn btn-primary">✓ Mark All Present</button></div></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Present</div><div style="font-size:2rem;font-weight:900;color:var(--success);">28</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Absent</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Late</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Attendance Rate</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">94%</div></div>
</div>
<div class="card">
  <div>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);">
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">A</div><div><div style="font-weight:600;font-size:0.9rem;">Alex Johnson</div></div></div>
      <div style="display:flex;gap:0.5rem;">
        <button class="btn btn-success" style="padding:0.3rem 0.75rem;font-size:0.8rem;">✓ Present</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">Late</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;color:var(--danger);">Absent</button>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:0.75rem;border-bottom:1px solid var(--border-color);">
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">M</div><div><div style="font-weight:600;font-size:0.9rem;">Marcus Turner</div></div></div>
      <div style="display:flex;gap:0.5rem;">
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">✓ Present</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;background:rgba(255,159,67,0.15);color:var(--warning);">Late ▼</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;color:var(--danger);">Absent</button>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:0.75rem;">
      <div style="display:flex;align-items:center;gap:1rem;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--warning));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;">E</div><div><div style="font-weight:600;font-size:0.9rem;">Emily Kim</div></div></div>
      <div style="display:flex;gap:0.5rem;">
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">✓ Present</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;">Late</button>
        <button class="btn btn-ghost" style="padding:0.3rem 0.75rem;font-size:0.8rem;background:rgba(255,68,68,0.15);color:var(--danger);">Absent ▼</button>
      </div>
    </div>
  </div>
</div>
'''))

# app/teacher/classes/behavior-tracker.html
write_file('app/teacher/classes/behavior-tracker.html', teacher_subpage('Behavior Tracker', '../../../', '''
<div class="page-header"><h1 class="page-title">🧭 Behavior Tracker</h1><p class="page-subtitle">Track and manage student behavior with points</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">⭐ Award Points</h3>
    <div class="form-group"><label class="form-label">Student</label><select class="form-control"><option>Select student...</option><option>Alex Johnson</option><option>Marcus Turner</option><option>Emily Kim</option></select></div>
    <div class="grid-2">
      <button class="btn btn-success" style="padding:0.75rem;justify-content:center;"><span>+5</span> Participation</button>
      <button class="btn btn-success" style="padding:0.75rem;justify-content:center;"><span>+10</span> Excellence</button>
      <button class="btn btn-success" style="padding:0.75rem;justify-content:center;"><span>+3</span> On-Time</button>
      <button class="btn btn-success" style="padding:0.75rem;justify-content:center;"><span>+15</span> Helping Others</button>
    </div>
    <div style="margin-top:1rem; border-top:1px solid var(--border-color); padding-top:1rem;">
      <h4 style="font-size:0.9rem;margin-bottom:0.75rem;color:var(--danger);">⚠️ Deduct Points</h4>
      <div class="grid-2">
        <button class="btn btn-ghost" style="padding:0.6rem;font-size:0.85rem;color:var(--danger);border-color:rgba(255,68,68,0.3);">-5 Disruption</button>
        <button class="btn btn-ghost" style="padding:0.6rem;font-size:0.85rem;color:var(--danger);border-color:rgba(255,68,68,0.3);">-10 Misconduct</button>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem; font-size:1rem;">🏆 Behavior Leaderboard</h3>
    <div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);"><div style="color:var(--accent);font-weight:700;width:24px;">1</div><div style="flex:1;font-weight:600;font-size:0.9rem;">Alex Johnson</div><div style="color:var(--success);font-weight:700;">+245 pts</div></div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;border-bottom:1px solid var(--border-color);"><div style="color:var(--text-muted);font-weight:700;width:24px;">2</div><div style="flex:1;font-weight:600;font-size:0.9rem;">Sarah Mitchell</div><div style="color:var(--success);font-weight:700;">+198 pts</div></div>
      <div style="display:flex;align-items:center;gap:1rem;padding:0.75rem 0;"><div style="color:var(--warning);font-weight:700;width:24px;">3</div><div style="flex:1;font-weight:600;font-size:0.9rem;">James Roberts</div><div style="color:var(--success);font-weight:700;">+167 pts</div></div>
    </div>
  </div>
</div>
'''))

print("Teacher pages batch 1 created")
