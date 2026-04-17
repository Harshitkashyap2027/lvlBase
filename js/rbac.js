// ===== RBAC & DATA MODULE =====
// Role-Based Access Control + localStorage data management

export const ROLES = {
  STUDENT: 'student',
  TEACHER: 'teacher',
  PARENT: 'parent',
  SCHOOL_ADMIN: 'school_admin',
  ADMIN: 'admin'
};

export const STATUS = {
  PENDING: 'pending',
  APPROVED: 'approved',
  REJECTED: 'rejected',
  VERIFIED: 'verified'
};

// ── Storage keys ──
const KEYS = {
  SCHOOLS: 'lvlbase_schools',
  ALL_USERS: 'lvlbase_all_users',
  CURRENT_USER: 'lvlbase_current_user',
  NOTIFICATIONS: 'lvlbase_notifications',
  LEGACY_PROFILE: 'lvlbase_user_profile'
};

// ── ADMIN credentials (platform super admin) ──
const ADMIN_EMAIL = 'admin@lvlbase.com';
const ADMIN_PASSWORD = 'admin123';
const ADMIN_WHATSAPP = '919258837596';

// ── Helpers ──
function getSchools() { return JSON.parse(localStorage.getItem(KEYS.SCHOOLS) || '[]'); }
function saveSchools(s) { localStorage.setItem(KEYS.SCHOOLS, JSON.stringify(s)); }

function getAllUsers() { return JSON.parse(localStorage.getItem(KEYS.ALL_USERS) || '[]'); }
function saveAllUsers(u) { localStorage.setItem(KEYS.ALL_USERS, JSON.stringify(u)); }

function getNotifications() { return JSON.parse(localStorage.getItem(KEYS.NOTIFICATIONS) || '[]'); }
function saveNotifications(n) { localStorage.setItem(KEYS.NOTIFICATIONS, JSON.stringify(n)); }

export function getCurrentUser() {
  return JSON.parse(localStorage.getItem(KEYS.CURRENT_USER) || 'null');
}

export function signOut() {
  localStorage.removeItem(KEYS.CURRENT_USER);
  localStorage.removeItem(KEYS.LEGACY_PROFILE);
  window.location.href = '/login.html';
}

// ── School CRUD ──
export function getSchoolById(id) {
  return getSchools().find(s => s.id === id) || null;
}

export function registerSchool(data) {
  const schools = getSchools();
  const school = {
    id: 'school_' + Date.now(),
    name: data.name,
    address: data.address,
    city: data.city,
    state: data.state,
    pincode: data.pincode,
    principal: data.principal,
    phone: data.phone,
    email: data.email,
    website: data.website || '',
    totalStudents: data.totalStudents || '',
    adminEmail: data.adminEmail,
    adminPassword: data.adminPassword,
    adminName: data.adminName,
    status: STATUS.PENDING,
    createdAt: new Date().toISOString(),
    verifiedAt: null
  };
  schools.push(school);
  saveSchools(schools);
  return school;
}

export function updateSchoolStatus(schoolId, status) {
  const schools = getSchools();
  const idx = schools.findIndex(s => s.id === schoolId);
  if (idx !== -1) {
    schools[idx].status = status;
    if (status === STATUS.VERIFIED) schools[idx].verifiedAt = new Date().toISOString();
    saveSchools(schools);
    return schools[idx];
  }
  return null;
}

export function getPendingSchools() {
  return getSchools().filter(s => s.status === STATUS.PENDING);
}

export function getAllSchoolsList() {
  return getSchools();
}

export function getVerifiedSchools() {
  return getSchools().filter(s => s.status === STATUS.VERIFIED);
}

// ── User CRUD ──
export function getUserByEmail(email) {
  if (!email) return null;
  const lower = email.toLowerCase().trim();
  // Check if it's the super admin
  if (lower === ADMIN_EMAIL) {
    return {
      uid: 'admin_super',
      email: ADMIN_EMAIL,
      displayName: 'Platform Admin',
      role: ROLES.ADMIN,
      status: STATUS.APPROVED,
      schoolId: null
    };
  }
  const all = getAllUsers();
  return all.find(u => u.email && u.email.toLowerCase() === lower) || null;
}

export function getUserById(uid) {
  if (uid === 'admin_super') {
    return { uid: 'admin_super', email: ADMIN_EMAIL, displayName: 'Platform Admin', role: ROLES.ADMIN, status: STATUS.APPROVED, schoolId: null };
  }
  return getAllUsers().find(u => u.uid === uid) || null;
}

export function registerUser(data) {
  const all = getAllUsers();
  // Check duplicate email
  const existing = all.find(u => u.email && u.email.toLowerCase() === data.email.toLowerCase());
  if (existing) throw new Error('Email already registered');

  const user = {
    uid: 'user_' + Date.now() + '_' + Math.random().toString(36).slice(2, 7),
    email: data.email.toLowerCase().trim(),
    displayName: data.displayName,
    role: data.role,
    schoolId: data.schoolId || null,
    status: STATUS.PENDING,
    // Student fields
    grade: data.grade || null,
    guild: data.guild || null,
    totalXP: 20,
    streak: 1,
    quizzesCompleted: 0,
    battlesWon: 0,
    battlesPlayed: 0,
    goalsCompleted: 0,
    perfectScores: 0,
    achievements: [],
    subjectProgress: { math: 0, science: 0, english: 0 },
    // Teacher fields
    subject: data.subject || null,
    qualification: data.qualification || null,
    // Parent fields
    studentEmail: data.studentEmail || null,
    childUid: null,
    createdAt: new Date().toISOString(),
    lastLogin: new Date().toISOString()
  };
  all.push(user);
  saveAllUsers(all);
  return user;
}

export function updateUserStatus(uid, status) {
  const all = getAllUsers();
  const idx = all.findIndex(u => u.uid === uid);
  if (idx !== -1) {
    all[idx].status = status;
    saveAllUsers(all);
    // Update current session if it's the same user
    const cur = getCurrentUser();
    if (cur && cur.uid === uid) {
      cur.status = status;
      localStorage.setItem(KEYS.CURRENT_USER, JSON.stringify(cur));
    }
    return all[idx];
  }
  return null;
}

export function updateUserProfile(uid, updates) {
  const all = getAllUsers();
  const idx = all.findIndex(u => u.uid === uid);
  if (idx !== -1) {
    all[idx] = { ...all[idx], ...updates };
    saveAllUsers(all);
    const cur = getCurrentUser();
    if (cur && cur.uid === uid) {
      const updated = { ...cur, ...updates };
      localStorage.setItem(KEYS.CURRENT_USER, JSON.stringify(updated));
    }
    return all[idx];
  }
  return null;
}

export function getUsersBySchool(schoolId) {
  return getAllUsers().filter(u => u.schoolId === schoolId);
}

export function getPendingUsersBySchool(schoolId) {
  return getAllUsers().filter(u => u.schoolId === schoolId && u.status === STATUS.PENDING);
}

export function getPendingUsersAll() {
  return getAllUsers().filter(u => u.status === STATUS.PENDING);
}

// ── Authentication ──
export function loginUser(email, password) {
  const lower = email.toLowerCase().trim();
  // Super admin check
  if (lower === ADMIN_EMAIL && password === ADMIN_PASSWORD) {
    const adminProfile = {
      uid: 'admin_super',
      email: ADMIN_EMAIL,
      displayName: 'Platform Admin',
      role: ROLES.ADMIN,
      status: STATUS.APPROVED,
      schoolId: null
    };
    localStorage.setItem(KEYS.CURRENT_USER, JSON.stringify(adminProfile));
    return adminProfile;
  }
  // School admin check
  const schools = getSchools();
  const school = schools.find(s => s.adminEmail && s.adminEmail.toLowerCase() === lower && s.adminPassword === password);
  if (school) {
    const profile = {
      uid: 'school_admin_' + school.id,
      email: school.adminEmail,
      displayName: school.adminName || school.principal,
      role: ROLES.SCHOOL_ADMIN,
      status: school.status === STATUS.VERIFIED ? STATUS.APPROVED : STATUS.PENDING,
      schoolId: school.id,
      schoolStatus: school.status
    };
    localStorage.setItem(KEYS.CURRENT_USER, JSON.stringify(profile));
    return profile;
  }
  // Regular users
  const user = getUserByEmail(lower);
  if (!user) throw new Error('No account found with this email. Please sign up first.');
  // Demo mode: any password works. In production, compare hashed passwords.
  user.lastLogin = new Date().toISOString();
  updateUserProfile(user.uid, { lastLogin: user.lastLogin });
  localStorage.setItem(KEYS.CURRENT_USER, JSON.stringify(user));
  // Also set legacy profile for backward compat with existing pages
  localStorage.setItem(KEYS.LEGACY_PROFILE, JSON.stringify(user));
  return user;
}

// ── Notifications ──
export function addNotification(note) {
  const notes = getNotifications();
  const n = {
    id: 'notif_' + Date.now(),
    ...note,
    read: false,
    createdAt: new Date().toISOString()
  };
  notes.unshift(n);
  saveNotifications(notes);
  return n;
}

export function getNotificationsForSchool(schoolId) {
  return getNotifications().filter(n => n.schoolId === schoolId);
}

export function getNotificationsForUser(uid) {
  return getNotifications().filter(n => n.userId === uid);
}

export function markNotificationRead(id) {
  const notes = getNotifications();
  const idx = notes.findIndex(n => n.id === id);
  if (idx !== -1) { notes[idx].read = true; saveNotifications(notes); }
}

// ── WhatsApp helper ──
export function buildWhatsAppLink(message) {
  return `https://wa.me/${ADMIN_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

// ── Role Guards ──
// Returns null if OK, or an error descriptor {title, message, icon} if blocked
export function checkRoleAccess(allowedRoles, options = {}) {
  const user = getCurrentUser();
  if (!user) {
    return {
      icon: '🔒',
      title: 'Login Required',
      message: 'Please login to access this page.',
      loginRedirect: true
    };
  }
  if (!allowedRoles.includes(user.role)) {
    const roleLabels = {
      student: 'Student Dashboard',
      teacher: 'Teacher Dashboard',
      parent: 'Parent Dashboard',
      school_admin: 'School Dashboard',
      admin: 'Admin Panel'
    };
    const myDashboard = roleLabels[user.role] || 'Dashboard';
    const redirectUrl = getDashboardUrl(user.role);
    return {
      icon: '🚫',
      title: 'Access Denied',
      message: `You don't have permission to view this page. As a ${user.role}, you can only access the ${myDashboard}.`,
      redirectUrl,
      redirectLabel: `Go to My Dashboard`
    };
  }
  if (options.requireApproved && user.status !== STATUS.APPROVED) {
    return {
      icon: '⏳',
      title: 'Pending Approval',
      message: 'Your account is pending approval from your school or admin. Please wait.',
      soft: true
    };
  }
  return null;
}

export function getDashboardUrl(role) {
  const map = {
    student: 'dashboard.html',
    teacher: 'teacher-dashboard.html',
    parent: 'parent-dashboard.html',
    school_admin: 'school-dashboard.html',
    admin: 'admin/index.html'
  };
  return map[role] || 'login.html';
}

// ── Inline guard renderer ──
// Call this at the top of any protected page script:
// guardPage(['student']) or guardPage(['teacher', 'school_admin'])
export function guardPage(allowedRoles, options = {}) {
  const error = checkRoleAccess(allowedRoles, options);
  if (!error) return; // Access granted

  // Prevent any further page execution
  document.addEventListener('DOMContentLoaded', () => {
    // Hide everything
    document.body.innerHTML = '';

    const wrapper = document.createElement('div');
    wrapper.style.cssText = `
      min-height: 100vh;
      background: #0A0A1A;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Poppins', system-ui, sans-serif;
      padding: 2rem;
    `;

    const isLoginRedirect = error.loginRedirect;
    const borderColor = isLoginRedirect ? '#6C63FF' : '#FF4444';
    const bgColor = isLoginRedirect ? 'rgba(108,99,255,0.08)' : 'rgba(255,68,68,0.08)';

    wrapper.innerHTML = `
      <div style="
        background: #1A1A2E;
        border: 2px solid ${borderColor};
        border-radius: 28px;
        padding: 3rem 2.5rem;
        max-width: 480px;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, ${bgColor}, #1A1A2E);
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
      ">
        <div style="font-size: 4rem; margin-bottom: 1rem;">${error.icon}</div>
        <h1 style="color: ${borderColor}; font-size: 1.6rem; font-weight: 800; margin-bottom: 0.75rem;">${error.title}</h1>
        <p style="color: #8892A4; font-size: 0.95rem; line-height: 1.7; margin-bottom: 2rem;">${error.message}</p>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          ${error.redirectUrl ? `<a href="${error.redirectUrl}" style="
            display: block;
            padding: 0.85rem 1.5rem;
            background: linear-gradient(135deg, #6C63FF, #8B85FF);
            color: white;
            border-radius: 14px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.95rem;
          ">📊 ${error.redirectLabel}</a>` : ''}
          ${error.loginRedirect ? `<a href="login.html" style="
            display: block;
            padding: 0.85rem 1.5rem;
            background: linear-gradient(135deg, #6C63FF, #8B85FF);
            color: white;
            border-radius: 14px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.95rem;
          ">🔐 Login</a>` : ''}
          <a href="index.html" style="
            display: block;
            padding: 0.75rem 1.5rem;
            background: rgba(255,255,255,0.06);
            color: #8892A4;
            border-radius: 14px;
            font-weight: 600;
            text-decoration: none;
            font-size: 0.9rem;
            border: 1px solid rgba(255,255,255,0.08);
          ">← Back to Home</a>
        </div>
      </div>
    `;

    document.body.appendChild(wrapper);
  }, { once: true });

  // Stop scripts from running further by throwing (will be caught silently)
  throw new Error('ACCESS_DENIED');
}
