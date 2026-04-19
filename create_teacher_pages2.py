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
.nav-link { padding: 0.5rem 1rem; border-radius: var(--radius); color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: var(--transition); }
.nav-link:hover { color: var(--text-light); background: rgba(108,99,255,0.15); }
.navbar-nav { display: flex; gap: 0.5rem; }
.navbar-actions { display: flex; align-items: center; gap: 1rem; }
.avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--success), #00A896); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; }
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

def tpage(title, css_prefix, body, scripts=''):
    nav_base = css_prefix
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | lvlBase Teacher</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_prefix}core/css/base.css">
  <style>{STYLES}</style>
</head>
<body>
<nav class="navbar">
  <div class="navbar-brand">lvlBase 🍎</div>
  <div class="navbar-nav">
    <a href="{nav_base}app/teacher/dashboard.html" class="nav-link">🏠 Home</a>
    <a href="{nav_base}app/teacher/classes/rosters.html" class="nav-link">👥 Classes</a>
    <a href="{nav_base}app/teacher/assessments/assignments.html" class="nav-link">📋 Assess</a>
    <a href="{nav_base}app/teacher/proctoring/live-monitor.html" class="nav-link">👁️ Monitor</a>
  </div>
  <div class="navbar-actions"><div class="avatar">T</div></div>
</nav>
<div class="page-wrapper"><div class="container">
{body}
</div></div>
{scripts}
</body>
</html>'''

# Assessment pages
write_file('app/teacher/assessments/rubric-builder.html', tpage('Rubric Builder', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📏 Rubric Builder</h1><p class="page-subtitle">Create detailed grading rubrics for any assignment</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">📋 Templates</button><button class="btn btn-primary">💾 Save Rubric</button></div></div></div>
<div class="card" style="margin-bottom:2rem;">
  <h3 style="margin-bottom:1.5rem; font-size:1rem;">Rubric Details</h3>
  <div class="grid-2">
    <div class="form-group"><label class="form-label">Assignment Title</label><input class="form-control" type="text" placeholder="e.g., Chapter 5 Essay"></div>
    <div class="form-group"><label class="form-label">Total Points</label><input class="form-control" type="number" value="100"></div>
  </div>
</div>
<div class="card" style="margin-bottom:1.5rem;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;"><h3 style="font-size:1rem;">Criteria</h3><button class="btn btn-primary" style="padding:0.4rem 1rem;font-size:0.85rem;">+ Add Criterion</button></div>
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;min-width:700px;">
      <thead><tr style="border-bottom:2px solid var(--border-color);">
        <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;width:25%;">Criterion</th>
        <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--success);text-transform:uppercase;">Excellent (4)</th>
        <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--primary);text-transform:uppercase;">Good (3)</th>
        <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--warning);text-transform:uppercase;">Fair (2)</th>
        <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--danger);text-transform:uppercase;">Poor (1)</th>
      </tr></thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border-color);">
          <td style="padding:0.75rem;"><input class="form-control" value="Content Accuracy" style="font-size:0.85rem;"></td>
          <td style="padding:0.75rem;"><textarea style="width:100%;padding:0.5rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:8px;color:var(--text-light);font-family:inherit;font-size:0.8rem;resize:none;height:60px;">All facts accurate and well-supported</textarea></td>
          <td style="padding:0.75rem;"><textarea style="width:100%;padding:0.5rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:8px;color:var(--text-light);font-family:inherit;font-size:0.8rem;resize:none;height:60px;">Most facts accurate</textarea></td>
          <td style="padding:0.75rem;"><textarea style="width:100%;padding:0.5rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:8px;color:var(--text-light);font-family:inherit;font-size:0.8rem;resize:none;height:60px;">Some inaccuracies</textarea></td>
          <td style="padding:0.75rem;"><textarea style="width:100%;padding:0.5rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:8px;color:var(--text-light);font-family:inherit;font-size:0.8rem;resize:none;height:60px;">Many inaccuracies</textarea></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
'''))

# app/teacher/assessments/question-bank.html
write_file('app/teacher/assessments/question-bank.html', tpage('Question Bank', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏦 Question Bank</h1><p class="page-subtitle">Create, browse, and reuse questions</p></div><button class="btn btn-primary">+ New Question</button></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">My Questions</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">347</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Shared Questions</div><div style="font-size:2rem;font-weight:900;color:var(--success);">2,840</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">AI Generated</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">128</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Used in Tests</div><div style="font-size:2rem;font-weight:900;color:var(--secondary);">89</div></div>
</div>
<div class="card">
  <div style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
    <input type="search" placeholder="Search questions..." style="flex:1;min-width:200px;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;">
    <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Subjects</option><option>Mathematics</option><option>Science</option><option>English</option></select>
    <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Types</option><option>Multiple Choice</option><option>True/False</option><option>Short Answer</option></select>
    <button class="btn btn-ghost" style="padding:0.6rem 1rem;font-size:0.85rem;">🤖 Generate with AI</button>
  </div>
  <div>
    <div style="padding:1rem;border:1px solid var(--border-color);border-radius:var(--radius);margin-bottom:0.75rem;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.75rem;">
        <div style="flex:1;"><div style="display:flex;gap:0.5rem;margin-bottom:0.5rem;"><span style="background:rgba(108,99,255,0.2);color:var(--primary);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;">MCQ</span><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;">Grade 10</span><span style="background:rgba(255,215,0,0.2);color:var(--accent);padding:0.2rem 0.5rem;border-radius:8px;font-size:0.75rem;">Math</span></div><p style="font-weight:600;font-size:0.9rem;">What is the discriminant of the quadratic equation 2x² + 5x - 3 = 0?</p></div>
        <div style="display:flex;gap:0.5rem;margin-left:1rem;"><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">✏️</button><button class="btn btn-ghost" style="padding:0.3rem 0.6rem;font-size:0.8rem;">+ Add to Test</button></div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;"><div style="padding:0.4rem 0.75rem;background:rgba(0,209,178,0.15);border-radius:8px;font-size:0.85rem;border:1px solid rgba(0,209,178,0.3);">A. 49 ✓</div><div style="padding:0.4rem 0.75rem;background:rgba(255,255,255,0.04);border-radius:8px;font-size:0.85rem;border:1px solid var(--border-color);">B. 25</div><div style="padding:0.4rem 0.75rem;background:rgba(255,255,255,0.04);border-radius:8px;font-size:0.85rem;border:1px solid var(--border-color);">C. -19</div><div style="padding:0.4rem 0.75rem;background:rgba(255,255,255,0.04);border-radius:8px;font-size:0.85rem;border:1px solid var(--border-color);">D. 1</div></div>
    </div>
  </div>
</div>
'''))

# app/teacher/assessments/gradebook.html
write_file('app/teacher/assessments/gradebook.html', tpage('Gradebook', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">📊 Gradebook</h1><p class="page-subtitle">Grade 10A · Mathematics</p></div><div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost">📥 Export</button><button class="btn btn-primary">+ Add Grade</button></div></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Class Average</div><div style="font-size:2rem;font-weight:900;color:var(--success);">83.4%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Highest</div><div style="font-size:2rem;font-weight:900;color:var(--accent);">98%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Lowest</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">52%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">At Risk</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">3</div></div>
</div>
<div class="card" style="overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;min-width:800px;">
    <thead><tr style="border-bottom:2px solid var(--border-color);">
      <th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Student</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Quiz 1</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Quiz 2</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Midterm</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Assignment</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Final</th>
      <th style="padding:0.75rem;text-align:center;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">Grade</th>
    </tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;font-size:0.9rem;">Alex Johnson</td><td style="padding:0.75rem;text-align:center;color:var(--success);">95</td><td style="padding:0.75rem;text-align:center;color:var(--success);">88</td><td style="padding:0.75nm;padding:0.75rem;text-align:center;color:var(--success);">92</td><td style="padding:0.75rem;text-align:center;color:var(--success);">97</td><td style="padding:0.75rem;text-align:center;color:var(--success);">—</td><td style="padding:0.75rem;text-align:center;"><span style="background:rgba(0,209,178,0.2);color:var(--success);padding:0.25rem 0.75rem;border-radius:10px;font-weight:700;">A</span></td></tr>
      <tr style="border-bottom:1px solid var(--border-color);"><td style="padding:0.75rem;font-weight:600;font-size:0.9rem;">Marcus Turner</td><td style="padding:0.75rem;text-align:center;color:var(--warning);">72</td><td style="padding:0.75rem;text-align:center;color:var(--warning);">68</td><td style="padding:0.75rem;text-align:center;color:var(--warning);">75</td><td style="padding:0.75rem;text-align:center;color:var(--warning);">80</td><td style="padding:0.75rem;text-align:center;color:var(--success);">—</td><td style="padding:0.75rem;text-align:center;"><span style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.25rem 0.75rem;border-radius:10px;font-weight:700;">C+</span></td></tr>
      <tr><td style="padding:0.75rem;font-weight:600;font-size:0.9rem;">Emily Kim</td><td style="padding:0.75rem;text-align:center;color:var(--danger);">55</td><td style="padding:0.75rem;text-align:center;color:var(--danger);">52</td><td style="padding:0.75rem;text-align:center;color:var(--danger);">58</td><td style="padding:0.75rem;text-align:center;color:var(--warning);">65</td><td style="padding:0.75rem;text-align:center;">—</td><td style="padding:0.75rem;text-align:center;"><span style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.25rem 0.75rem;border-radius:10px;font-weight:700;">D+</span></td></tr>
    </tbody>
  </table>
</div>
'''))

# app/teacher/assessments/ai-grader.html
write_file('app/teacher/assessments/ai-grader.html', tpage('AI Grader', '../../../', '''
<div class="page-header"><h1 class="page-title">🤖 AI Grader</h1><p class="page-subtitle">Let AI grade essays and open-ended answers with your rubric</p></div>
<div class="grid-2" style="margin-bottom:2rem;">
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📋 Grading Settings</h3>
    <div class="form-group"><label class="form-label">Assignment</label><select class="form-control"><option>Chapter 5 Essay - Grade 10A</option><option>Science Lab Report</option></select></div>
    <div class="form-group"><label class="form-label">Rubric</label><select class="form-control"><option>Essay Rubric (4 criteria)</option><option>Lab Report Rubric</option></select></div>
    <div class="form-group"><label class="form-label">Strictness Level</label><select class="form-control"><option>Standard</option><option>Strict</option><option>Lenient</option></select></div>
    <div style="display:flex;gap:0.75rem;"><button class="btn btn-primary">🤖 Grade All (32)</button><button class="btn btn-ghost">Preview</button></div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:1rem;font-size:1rem;">📊 Grading Status</h3>
    <div style="background:rgba(255,255,255,0.04);border-radius:var(--radius);padding:1.5rem;text-align:center;margin-bottom:1rem;">
      <div style="font-size:3rem;font-weight:900;color:var(--primary);margin-bottom:0.25rem;">28/32</div>
      <div style="color:var(--text-muted);font-size:0.9rem;">submissions graded</div>
    </div>
    <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:10px;margin-bottom:0.75rem;"><div style="background:linear-gradient(135deg,var(--primary),var(--success));border-radius:20px;width:87.5%;height:100%;"></div></div>
    <div style="display:flex;justify-content:space-between;font-size:0.85rem;"><span style="color:var(--success);">✓ 28 graded</span><span style="color:var(--warning);">⏳ 4 pending</span></div>
  </div>
</div>
<div class="card">
  <h3 style="margin-bottom:1rem;font-size:1rem;">🔍 AI Graded Sample</h3>
  <div style="background:rgba(255,255,255,0.04);border-radius:var(--radius);padding:1rem;margin-bottom:1rem;font-size:0.9rem;line-height:1.7;color:var(--text-muted);font-style:italic;">"The French Revolution was a period of radical political transformation in France. The causes were many including economic inequality, the influence of Enlightenment ideas, and the weakness of King Louis XVI. The storming of the Bastille on July 14, 1789 marked the beginning of the revolution..."</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-bottom:1rem;">
    <div style="text-align:center;padding:0.75rem;background:rgba(0,209,178,0.1);border-radius:var(--radius);"><div style="font-weight:700;color:var(--success);">3.5/4</div><div style="font-size:0.75rem;color:var(--text-muted);">Content</div></div>
    <div style="text-align:center;padding:0.75rem;background:rgba(108,99,255,0.1);border-radius:var(--radius);"><div style="font-weight:700;color:var(--primary);">4/4</div><div style="font-size:0.75rem;color:var(--text-muted);">Structure</div></div>
    <div style="text-align:center;padding:0.75rem;background:rgba(255,215,0,0.1);border-radius:var(--radius);"><div style="font-weight:700;color:var(--accent);">3/4</div><div style="font-size:0.75rem;color:var(--text-muted);">Analysis</div></div>
    <div style="text-align:center;padding:0.75rem;background:rgba(0,209,178,0.1);border-radius:var(--radius);"><div style="font-weight:700;color:var(--success);">87%</div><div style="font-size:0.75rem;color:var(--text-muted);">Overall</div></div>
  </div>
  <div style="display:flex;gap:0.75rem;"><button class="btn btn-primary" style="font-size:0.85rem;">✓ Accept Grade</button><button class="btn btn-ghost" style="font-size:0.85rem;">✏️ Override</button></div>
</div>
'''))

# app/teacher/proctoring/live-monitor.html
write_file('app/teacher/proctoring/live-monitor.html', tpage('Live Monitor', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">👁️ Live Exam Monitor</h1><p class="page-subtitle">Chapter 5 Quiz · Grade 10A · 28 active</p></div><div style="display:flex;gap:0.75rem;align-items:center;"><div style="background:rgba(255,68,68,0.15);border:1px solid rgba(255,68,68,0.3);padding:0.4rem 1rem;border-radius:20px;display:flex;align-items:center;gap:0.5rem;font-size:0.85rem;color:var(--danger);"><div style="width:8px;height:8px;border-radius:50%;background:var(--danger);animation:pulse 1s infinite;"></div>LIVE</div><button class="btn btn-ghost">⏹ End Exam</button></div></div></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Active Students</div><div style="font-size:2rem;font-weight:900;color:var(--success);">28</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">🚨 Alerts</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">2</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Avg Progress</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">64%</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Time Left</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">18:42</div></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:1rem;margin-bottom:2rem;">
  <div style="background:var(--card-bg);border:2px solid rgba(255,68,68,0.5);border-radius:var(--radius);padding:0.75rem;position:relative;">
    <div style="position:absolute;top:-8px;right:-8px;background:var(--danger);color:white;font-size:0.65rem;padding:0.2rem 0.4rem;border-radius:8px;font-weight:700;">ALERT</div>
    <div style="background:rgba(255,68,68,0.1);border-radius:8px;height:80px;display:flex;align-items:center;justify-content:center;margin-bottom:0.5rem;font-size:2rem;">��</div>
    <div style="font-size:0.8rem;font-weight:600;">Marcus T.</div>
    <div style="font-size:0.7rem;color:var(--danger);">Tab switch detected</div>
  </div>
  <div style="background:var(--card-bg);border:1px solid rgba(0,209,178,0.3);border-radius:var(--radius);padding:0.75rem;">
    <div style="background:rgba(0,209,178,0.08);border-radius:8px;height:80px;display:flex;align-items:center;justify-content:center;margin-bottom:0.5rem;font-size:2rem;">😊</div>
    <div style="font-size:0.8rem;font-weight:600;">Alex J.</div>
    <div style="font-size:0.7rem;color:var(--success);">Question 7/10</div>
  </div>
  <div style="background:var(--card-bg);border:1px solid rgba(0,209,178,0.3);border-radius:var(--radius);padding:0.75rem;">
    <div style="background:rgba(108,99,255,0.08);border-radius:8px;height:80px;display:flex;align-items:center;justify-content:center;margin-bottom:0.5rem;font-size:2rem;">🤔</div>
    <div style="font-size:0.8rem;font-weight:600;">Emily K.</div>
    <div style="font-size:0.7rem;color:var(--text-muted);">Question 5/10</div>
  </div>
  <div style="background:var(--card-bg);border:2px solid rgba(255,68,68,0.5);border-radius:var(--radius);padding:0.75rem;position:relative;">
    <div style="position:absolute;top:-8px;right:-8px;background:var(--warning);color:#000;font-size:0.65rem;padding:0.2rem 0.4rem;border-radius:8px;font-weight:700;">WARN</div>
    <div style="background:rgba(255,159,67,0.1);border-radius:8px;height:80px;display:flex;align-items:center;justify-content:center;margin-bottom:0.5rem;font-size:2rem;">😬</div>
    <div style="font-size:0.8rem;font-weight:600;">Sarah M.</div>
    <div style="font-size:0.7rem;color:var(--warning);">Eye gaze off screen</div>
  </div>
</div>
'''))

# app/teacher/proctoring/cheat-reports.html
write_file('app/teacher/proctoring/cheat-reports.html', tpage('Cheat Reports', '../../../', '''
<div class="page-header"><h1 class="page-title">🚨 Cheat Detection Reports</h1><p class="page-subtitle">Review AI-flagged suspicious activity</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Total Alerts</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">12</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Confirmed</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">3</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Dismissed</div><div style="font-size:2rem;font-weight:900;color:var(--success);">7</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Pending Review</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">2</div></div>
</div>
<div class="card">
  <div>
    <div style="padding:1rem;border:1px solid rgba(255,68,68,0.3);border-radius:var(--radius);margin-bottom:0.75rem;background:rgba(255,68,68,0.05);">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.75rem;"><div><div style="font-weight:700;font-size:0.95rem;">Marcus Turner — Chapter 5 Quiz</div><div style="font-size:0.8rem;color:var(--danger);">🚨 High Confidence (87%) · Jan 15, 2:34 PM</div></div><span style="background:rgba(255,68,68,0.2);color:var(--danger);padding:0.25rem 0.75rem;border-radius:10px;font-size:0.8rem;">Pending</span></div>
      <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:0.75rem;"><strong>Flags:</strong> Tab switched 3 times, phone detected in camera view, audio spike at 2:31 PM</div>
      <div style="display:flex;gap:0.75rem;"><button class="btn btn-primary" style="font-size:0.8rem;padding:0.4rem 1rem;background:rgba(255,68,68,0.3);color:var(--danger);border:1px solid rgba(255,68,68,0.4);">Mark as Cheating</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem 1rem;">Dismiss</button><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem 1rem;">View Evidence</button></div>
    </div>
    <div style="padding:1rem;border:1px solid rgba(255,159,67,0.3);border-radius:var(--radius);background:rgba(255,159,67,0.05);">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.75rem;"><div><div style="font-weight:700;font-size:0.95rem;">Sarah Mitchell — Chapter 5 Quiz</div><div style="font-size:0.8rem;color:var(--warning);">⚠️ Medium Confidence (45%) · Jan 15, 2:41 PM</div></div><span style="background:rgba(255,159,67,0.2);color:var(--warning);padding:0.25rem 0.75rem;border-radius:10px;font-size:0.8rem;">Pending</span></div>
      <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:0.75rem;"><strong>Flags:</strong> Eye gaze off-screen for 15+ seconds twice</div>
      <div style="display:flex;gap:0.75rem;"><button class="btn btn-ghost" style="font-size:0.8rem;padding:0.4rem 1rem;color:var(--danger);">Mark as Cheating</button><button class="btn btn-primary" style="font-size:0.8rem;padding:0.4rem 1rem;">Dismiss as False Positive</button></div>
    </div>
  </div>
</div>
'''))

# app/teacher/proctoring/audio-analysis.html
write_file('app/teacher/proctoring/audio-analysis.html', tpage('Audio Analysis', '../../../', '''
<div class="page-header"><h1 class="page-title">🎵 Audio Analysis</h1><p class="page-subtitle">Real-time audio monitoring during assessments</p></div>
<div class="grid-4" style="margin-bottom:2rem;">
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Monitored Students</div><div style="font-size:2rem;font-weight:900;color:var(--primary);">28</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Audio Anomalies</div><div style="font-size:2rem;font-weight:900;color:var(--warning);">4</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Avg Noise Level</div><div style="font-size:2rem;font-weight:900;color:var(--success);">Low</div></div>
  <div class="card" style="text-align:center;"><div style="font-size:0.8rem;color:var(--text-muted);">Recording Status</div><div style="font-size:2rem;font-weight:900;color:var(--danger);">🔴</div></div>
</div>
<div class="card" style="margin-bottom:2rem;">
  <h3 style="margin-bottom:1.5rem;font-size:1rem;">🎵 Audio Timeline — Marcus Turner</h3>
  <div style="background:rgba(0,0,0,0.3);border-radius:var(--radius);padding:1rem;margin-bottom:1rem;position:relative;overflow:hidden;height:80px;display:flex;align-items:flex-end;gap:2px;">
    <div style="width:4px;height:20%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:15%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:25%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:10%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:80%;background:rgba(255,68,68,0.8);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:90%;background:rgba(255,68,68,0.8);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:75%;background:rgba(255,68,68,0.7);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:20%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="width:4px;height:15%;background:rgba(108,99,255,0.4);border-radius:2px;flex-shrink:0;"></div>
    <div style="position:absolute;top:5px;left:30%;font-size:0.75rem;background:rgba(255,68,68,0.2);color:var(--danger);padding:0.2rem 0.5rem;border-radius:8px;">Spike: 14:31</div>
  </div>
  <div style="font-size:0.85rem;color:var(--text-muted);">⚠️ Unusual audio spike detected at 2:31 PM — possible verbal communication. Confidence: 72%</div>
</div>
'''))

# app/teacher/collaboration/lesson-marketplace.html
write_file('app/teacher/collaboration/lesson-marketplace.html', tpage('Lesson Marketplace', '../../../', '''
<div class="page-header"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;"><div><h1 class="page-title">🏪 Lesson Marketplace</h1><p class="page-subtitle">Share and discover lessons from educators worldwide</p></div><button class="btn btn-primary">📤 Share a Lesson</button></div></div>
<div style="display:flex;gap:1rem;margin-bottom:2rem;flex-wrap:wrap;">
  <input type="search" placeholder="Search lessons, topics..." style="flex:1;min-width:200px;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;">
  <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Subjects</option><option>Mathematics</option><option>Science</option></select>
  <select style="padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><option>All Grades</option><option>Grade 9</option><option>Grade 10</option></select>
</div>
<div class="grid-3">
  <div class="card"><div style="background:rgba(108,99,255,0.1);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;font-size:2rem;">📐</div><h3 style="margin-bottom:0.25rem;font-size:1rem;">Quadratic Equations — Visual Approach</h3><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">By Ms. Rodriguez · Grade 10 · Math</div><div style="display:flex;justify-content:space-between;align-items:center;"><div style="font-size:0.85rem;color:var(--accent);">⭐ 4.9 (128 reviews)</div><div style="font-size:0.8rem;color:var(--text-muted);">1.2k downloads</div></div><button class="btn btn-primary" style="width:100%;margin-top:1rem;font-size:0.85rem;">Download Free →</button></div>
  <div class="card"><div style="background:rgba(0,209,178,0.1);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;font-size:2rem;">🧪</div><h3 style="margin-bottom:0.25rem;font-size:1rem;">Photosynthesis Lab Activity</h3><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">By Mr. Patel · Grade 9 · Science</div><div style="display:flex;justify-content:space-between;align-items:center;"><div style="font-size:0.85rem;color:var(--accent);">⭐ 4.7 (89 reviews)</div><div style="font-size:0.8rem;color:var(--text-muted);">874 downloads</div></div><button class="btn btn-primary" style="width:100%;margin-top:1rem;font-size:0.85rem;">Download Free →</button></div>
  <div class="card"><div style="background:rgba(255,215,0,0.1);border-radius:var(--radius);padding:1rem;text-align:center;margin-bottom:1rem;font-size:2rem;">📖</div><h3 style="margin-bottom:0.25rem;font-size:1rem;">Shakespeare — Modern Day Context</h3><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">By Mrs. Chen · Grade 11 · English</div><div style="display:flex;justify-content:space-between;align-items:center;"><div style="font-size:0.85rem;color:var(--accent);">⭐ 4.8 (203 reviews)</div><div style="font-size:0.8rem;color:var(--text-muted);">2.1k downloads</div></div><button class="btn btn-primary" style="width:100%;margin-top:1rem;font-size:0.85rem;">Download Free →</button></div>
</div>
'''))

# app/teacher/collaboration/staff-lounge.html
write_file('app/teacher/collaboration/staff-lounge.html', tpage('Staff Lounge', '../../../', '''
<div class="page-header"><h1 class="page-title">☕ Staff Lounge</h1><p class="page-subtitle">Connect, share ideas, and collaborate with colleagues</p></div>
<div class="grid-2">
  <div class="card" style="height:500px;display:flex;flex-direction:column;">
    <h3 style="font-size:1rem;margin-bottom:1rem;">💬 Staff Chat</h3>
    <div style="flex:1;overflow-y:auto;padding-bottom:1rem;">
      <div style="margin-bottom:1rem;"><div style="display:flex;gap:0.75rem;align-items:flex-start;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--success),#00A896);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;flex-shrink:0;">R</div><div><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Ms. Rodriguez · 10:30 AM</div><div style="background:rgba(255,255,255,0.06);border-radius:0 var(--radius) var(--radius) var(--radius);padding:0.75rem;font-size:0.9rem;">Has anyone tried the new AI quiz generator? The questions are surprisingly good!</div></div></div></div>
      <div style="margin-bottom:1rem;display:flex;justify-content:flex-end;"><div style="max-width:70%;"><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;text-align:right;">You · 10:35 AM</div><div style="background:rgba(108,99,255,0.2);border-radius:var(--radius) 0 var(--radius) var(--radius);padding:0.75rem;font-size:0.9rem;">Yes! Used it for Grade 10A yesterday. Saved me an hour!</div></div></div>
      <div style="margin-bottom:1rem;"><div style="display:flex;gap:0.75rem;align-items:flex-start;"><div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.8rem;flex-shrink:0;">P</div><div><div style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.25rem;">Mr. Patel · 10:38 AM</div><div style="background:rgba(255,255,255,0.06);border-radius:0 var(--radius) var(--radius) var(--radius);padding:0.75rem;font-size:0.9rem;">Staff meeting moved to 3PM today. FYI everyone.</div></div></div></div>
    </div>
    <div style="display:flex;gap:0.75rem;border-top:1px solid var(--border-color);padding-top:1rem;"><input type="text" placeholder="Type a message..." style="flex:1;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;"><button class="btn btn-primary" style="padding:0.6rem 1rem;">Send</button></div>
  </div>
  <div>
    <div class="card" style="margin-bottom:1.5rem;">
      <h3 style="font-size:1rem;margin-bottom:1rem;">📋 Staff Bulletin Board</h3>
      <div style="padding:0.75rem;background:rgba(108,99,255,0.08);border-radius:var(--radius);margin-bottom:0.75rem;border-left:3px solid var(--primary);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">📅 Professional Development Day</div><div style="font-size:0.8rem;color:var(--text-muted);">February 7 — All day. Focus on AI integration in teaching.</div></div>
      <div style="padding:0.75rem;background:rgba(255,215,0,0.08);border-radius:var(--radius);border-left:3px solid var(--accent);"><div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">🎉 Teacher of the Month</div><div style="font-size:0.8rem;color:var(--text-muted);">Congratulations Ms. Rodriguez! Highest student engagement rate.</div></div>
    </div>
    <div class="card">
      <h3 style="font-size:1rem;margin-bottom:1rem;">💡 Idea Box</h3>
      <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Suggest improvements for lvlBase or school policies</p>
      <textarea placeholder="Share your idea..." style="width:100%;height:80px;padding:0.75rem;background:rgba(255,255,255,0.04);border:1px solid var(--border-color);border-radius:var(--radius);color:var(--text-light);font-family:inherit;font-size:0.85rem;resize:none;"></textarea>
      <button class="btn btn-primary" style="margin-top:0.75rem;font-size:0.85rem;">Submit Idea 💡</button>
    </div>
  </div>
</div>
'''))

print("Teacher pages batch 2 created")
