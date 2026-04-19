import os, re

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

def read_file(path):
    full = os.path.join(BASE, path)
    if not os.path.exists(full):
        return None
    with open(full) as f:
        return f.read()

def copy_and_update(src, dst, depth_prefix):
    content = read_file(src)
    if content is None:
        print(f'  SKIP (src not found): {src}')
        return None
    replacements = [
        ('css/main.css', depth_prefix + 'core/css/base.css'),
        ('css/dashboard.css', depth_prefix + 'core/css/data.css'),
        ('css/battle.css', depth_prefix + 'core/css/gamification.css'),
        ('css/quiz.css', depth_prefix + 'core/css/gamification.css'),
        ('css/admin-bento.css', depth_prefix + 'core/css/bento-grid.css'),
        ('css/admin.css', depth_prefix + 'core/css/data.css'),
        ('js/firebase-config.js', depth_prefix + 'core/js/firebase/init.js'),
        ('js/auth.js', depth_prefix + 'core/js/firebase/auth.js'),
        ('js/firebase-bridge.js', depth_prefix + 'core/js/firebase/firestore.js'),
        ('js/rbac.js', depth_prefix + 'core/js/core/security.js'),
        ('js/gamification.js', depth_prefix + 'core/js/features/gamification.js'),
        ('js/dashboard.js', depth_prefix + 'core/js/core/state.js'),
        ('js/popup.js', depth_prefix + 'core/js/core/ui-components.js'),
        ('js/ai-assistant.js', depth_prefix + 'core/js/features/ai-proctor.js'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    write_file(dst, content)
    return content

# PUBLIC copies
copy_and_update('index.html', 'public/index.html', '../')
copy_and_update('certificate.html', 'public/verify-certificate.html', '../')

# AUTH copies
copy_and_update('portal-login.html', 'auth/portal-login.html', '../')
copy_and_update('signup.html', 'auth/signup-student.html', '../')
copy_and_update('school-signup.html', 'auth/school-onboarding.html', '../')

# STUDENT copies
copy_and_update('dashboard.html', 'app/student/dashboard.html', '../../')
copy_and_update('learn.html', 'app/student/quest-map.html', '../../')
copy_and_update('settings.html', 'app/student/profile.html', '../../')
copy_and_update('battles.html', 'app/student/arena/battle-stage.html', '../../../')
copy_and_update('competition.html', 'app/student/arena/tournaments.html', '../../../')
copy_and_update('leaderboard.html', 'app/student/arena/leaderboard.html', '../../../')
copy_and_update('guild-wars.html', 'app/student/guilds/guild-wars.html', '../../../')
copy_and_update('ai-assistant.html', 'app/student/ai/sage-chat.html', '../../../')
copy_and_update('quiz.html', 'app/student/ai/smart-flashcards.html', '../../../')
copy_and_update('homework-scanner.html', 'app/student/ai/notes.html', '../../../')
copy_and_update('science-lab.html', 'app/student/workspace/python-lab.html', '../../../')

# TEACHER copies
copy_and_update('teacher-dashboard.html', 'app/teacher/dashboard.html', '../../')
copy_and_update('teacher-tasks.html', 'app/teacher/assessments/assignments.html', '../../../')
copy_and_update('teacher-tests.html', 'app/teacher/assessments/quiz-builder.html', '../../../')

# SCHOOL ADMIN copies
copy_and_update('school-dashboard.html', 'app/school-admin/dashboard.html', '../../')

# PARENT copies
copy_and_update('parent-dashboard.html', 'app/parent/dashboard.html', '../../')
copy_and_update('parent-analytics.html', 'app/parent/child-report.html', '../../')
copy_and_update('parent-complaints.html', 'app/parent/teacher-connect.html', '../../')

# SUPER ADMIN copies
copy_and_update('admin/index.html', 'app/super-admin/dashboard.html', '../../')

print("\nAll copy-based HTML files created!")
