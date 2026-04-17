// ============================================================
// lvlBase Super Admin — Shared Functions & Sidebar Layout
// ============================================================

var CREDS_KEY = 'lvlbase_admin_creds';

// ── Session Check ─────────────────────────────────────────
function checkSession() {
  var u = JSON.parse(localStorage.getItem('lvlbase_current_user') || 'null');
  if (u && u.role === 'admin') return true;
  try {
    var d = JSON.parse(localStorage.getItem('lvlbase_admin_session') || 'null');
    return d && d.loggedIn && Date.now() - d.loginTime < 28800000;
  } catch(e) { return false; }
}

// ── Logout ───────────────────────────────────────────────
function doLogout() {
  localStorage.removeItem('lvlbase_admin_session');
  localStorage.removeItem('lvlbase_current_user');
  localStorage.removeItem('lvlbase_user_profile');
  auditLog('Admin logout', '-');
  try {
    Promise.all([
      import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js'),
      import('https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js')
    ]).then(function(m) {
      var apps = m[0].getApps ? m[0].getApps() : [];
      if (apps.length) m[1].getAuth(apps[0]).signOut().catch(function(){});
    }).catch(function(){});
  } catch(e) {}
  window.location.href = 'login.html';
}

// ── HTML Escape ───────────────────────────────────────────
function esc(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// ── Data Helpers ──────────────────────────────────────────
function getAllUsers()    { return JSON.parse(localStorage.getItem('lvlbase_all_users')    || '[]'); }
function getAllSchools()  { return JSON.parse(localStorage.getItem('lvlbase_schools')      || '[]'); }
function getQuizHistory(){ return JSON.parse(localStorage.getItem('lvlbase_quiz_history') || '[]'); }
function saveUsers(u)    { localStorage.setItem('lvlbase_all_users',  JSON.stringify(u)); }
function saveSchools(s)  { localStorage.setItem('lvlbase_schools',    JSON.stringify(s)); }
function getCreds()      {
  var def = { email: 'admin@lvlbase.in', password: 'Admin@123' };
  try { return JSON.parse(localStorage.getItem(CREDS_KEY)) || def; } catch(e) { return def; }
}
function getSchoolName(id) {
  var s = getAllSchools().find(function(x){ return x.id === id; });
  return s ? esc(s.name) : (id ? esc(String(id).slice(0, 10)) + '…' : '–');
}
function getRank(xp) {
  if (xp >= 30000) return 'SS-Rank';
  if (xp >= 15000) return 'S-Rank';
  if (xp >= 7000)  return 'A-Rank';
  if (xp >= 3500)  return 'B-Rank';
  if (xp >= 1500)  return 'C-Rank';
  if (xp >= 500)   return 'D-Rank';
  return 'E-Rank';
}

// ── Audit Log ─────────────────────────────────────────────
function auditLog(action, detail) {
  var log = JSON.parse(localStorage.getItem('lvlbase_audit_log') || '[]');
  log.push({ action: action, detail: detail || '', ts: new Date().toISOString(), ip: 'admin' });
  if (log.length > 500) log.splice(0, log.length - 500);
  localStorage.setItem('lvlbase_audit_log', JSON.stringify(log));
}

// ── Pending Badges ────────────────────────────────────────
function updateBadges() {
  var ps = getAllSchools().filter(function(s){ return s.status === 'pending'; }).length;
  var sb = document.getElementById('school-badge');
  if (sb) { sb.textContent = ps; sb.style.display = ps > 0 ? 'flex' : 'none'; }
  var pu = getAllUsers().filter(function(u){ return u.status === 'pending'; }).length;
  var ub = document.getElementById('user-badge');
  if (ub) { ub.textContent = pu; ub.style.display = pu > 0 ? 'flex' : 'none'; }
}

// ── Clock ─────────────────────────────────────────────────
function startClock() {
  function tick() {
    var el = document.getElementById('admin-clock');
    if (el) el.textContent = new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }
  tick(); setInterval(tick, 1000);
}

// ── Shared User Actions ───────────────────────────────────
function banUser(uid, name) {
  lvlPopup.confirm('Ban User', 'Ban ' + name + ' from the platform?', { confirmLabel: 'Ban', confirmStyle: 'danger', type: 'error' }).then(function(c) {
    if (!c) return;
    var u = getAllUsers(), i = u.findIndex(function(x){ return x.uid === uid; });
    if (i !== -1) { u[i].status = 'banned'; saveUsers(u); }
    lvlPopup.toast(name + ' banned.', 'warning');
    auditLog('User banned', name);
    if (typeof renderUsersTable    === 'function') renderUsersTable();
    if (typeof renderTeachersTable === 'function') renderTeachersTable();
    if (typeof renderParentsTable  === 'function') renderParentsTable();
    if (typeof renderOverview      === 'function') renderOverview();
  });
}
function unbanUser(uid, name) {
  var u = getAllUsers(), i = u.findIndex(function(x){ return x.uid === uid; });
  if (i !== -1) { u[i].status = 'approved'; saveUsers(u); }
  lvlPopup.toast(name + ' unbanned', 'success');
  auditLog('User unbanned', name);
  if (typeof renderUsersTable    === 'function') renderUsersTable();
  if (typeof renderTeachersTable === 'function') renderTeachersTable();
  if (typeof renderParentsTable  === 'function') renderParentsTable();
}
function boostUserXP(uid, name) {
  lvlPopup.confirm('Boost XP', 'Send +500 bonus XP to ' + name + '?', { confirmLabel: 'Boost', confirmStyle: 'success' }).then(function(c) {
    if (!c) return;
    var u = getAllUsers(), i = u.findIndex(function(x){ return x.uid === uid; });
    if (i !== -1) { u[i].totalXP = (u[i].totalXP || 0) + 500; saveUsers(u); }
    lvlPopup.toast('+500 XP to ' + name + '!', 'success');
    auditLog('XP boost', '+500 to ' + name);
    if (typeof renderUsersTable === 'function') renderUsersTable();
    if (typeof renderOverview   === 'function') renderOverview();
  });
}

// ── Sidebar Builder ───────────────────────────────────────
function buildSidebarHTML(activePage) {
  function navLink(page, href, icon, label, badgeId) {
    var badge = badgeId
      ? '<span id="' + badgeId + '" class="sa-nav-badge" style="display:none">0</span>'
      : '';
    return '<a href="' + href + '" class="sa-nav-link' + (activePage === page ? ' active' : '') +
      '" data-page="' + page + '"><span class="sa-nav-icon">' + icon + '</span>' + label + badge + '</a>';
  }
  return (
    '<aside class="sa-sidebar" id="sa-sidebar">' +
      '<div class="sa-sidebar-brand">' +
        '<div class="sa-logo">lvlBase &#x26A1;</div>' +
        '<div class="sa-logo-badge">Super Admin</div>' +
      '</div>' +
      '<nav class="sa-nav" style="overflow-y:auto;flex:1">' +
        '<div class="sa-nav-label">Overview</div>' +
        navLink('overview',       'index.html',            '&#x1F4CA;', 'Dashboard') +
        navLink('analytics',      'analytics.html',        '&#x1F4C8;', 'Analytics') +
        '<div class="sa-nav-label">Approvals</div>' +
        navLink('schools',        'schools.html',          '&#x1F3EB;', 'Schools &nbsp;', 'school-badge') +
        navLink('user-approvals', 'user-approvals.html',   '&#x23F3;',  'User Approvals &nbsp;', 'user-badge') +
        '<div class="sa-nav-label">Management</div>' +
        navLink('users',          'users.html',            '&#x1F465;', 'All Users') +
        navLink('teachers',       'teachers.html',         '&#x1F468;&#x200D;&#x1F3EB;', 'Teachers') +
        navLink('parents',        'parents.html',          '&#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;', 'Parents') +
        navLink('content',        'content.html',          '&#x1F4DA;', 'Content') +
        navLink('events',         'events.html',           '&#x1F389;', 'Events') +
        navLink('announcements',  'announcements.html',    '&#x1F4E2;', 'Announcements') +
        '<div class="sa-nav-label">Engagement</div>' +
        navLink('leaderboard',    'leaderboard-admin.html','&#x1F3C6;', 'Leaderboard') +
        navLink('badges',         'badges-admin.html',     '&#x1F396;&#xFE0F;', 'Badges &amp; Achievements') +
        '<div class="sa-nav-label">System</div>' +
        navLink('reports',        'reports.html',          '&#x1F4CB;', 'Reports') +
        navLink('platform',       'platform.html',         '&#x2699;&#xFE0F;', 'Platform Controls') +
        navLink('audit',          'audit.html',            '&#x1F6E1;&#xFE0F;', 'Audit Log') +
        '<button class="sa-nav-link" style="color:#FF4444;margin-top:0.5rem;width:100%;text-align:left" onclick="doLogout()">' +
          '<span class="sa-nav-icon">&#x1F6AA;</span>Logout' +
        '</button>' +
      '</nav>' +
    '</aside>'
  );
}

// ── Page Init (call from every admin page) ────────────────
function initAdminPage(pageId) {
  // Inject sidebar
  var root = document.getElementById('sa-sidebar-root');
  if (root) root.innerHTML = buildSidebarHTML(pageId);

  // Populate badges
  updateBadges();

  // Start live clock
  startClock();

  // Mobile hamburger visibility
  var mq = window.matchMedia('(max-width:768px)');
  function applyMQ(m) {
    var hb = document.getElementById('hamburger-btn');
    if (hb) hb.style.display = m.matches ? 'block' : 'none';
  }
  applyMQ(mq);
  if (mq.addEventListener) mq.addEventListener('change', applyMQ);

  // Close sidebar on outside click (mobile)
  document.addEventListener('click', function(e) {
    var sidebar = document.getElementById('sa-sidebar');
    var hb = document.getElementById('hamburger-btn');
    if (sidebar && sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== hb) {
      sidebar.classList.remove('open');
    }
  });


}
