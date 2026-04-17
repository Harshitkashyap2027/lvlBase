// ===== ADMIN MODULE =====

const ADMIN_CREDENTIALS = { email: 'admin@lvlbase.com', password: 'admin123' };

export function checkAdminAuth() {
  const session = localStorage.getItem('lvlbase_admin_session');
  if (!session) return false;
  try {
    const data = JSON.parse(session);
    return data.loggedIn && Date.now() - data.loginTime < 3600000; // 1hr
  } catch { return false; }
}

export function adminLogin(email, password) {
  if (email === ADMIN_CREDENTIALS.email && password === ADMIN_CREDENTIALS.password) {
    localStorage.setItem('lvlbase_admin_session', JSON.stringify({ loggedIn: true, loginTime: Date.now() }));
    return true;
  }
  return false;
}

export function adminLogout() {
  localStorage.removeItem('lvlbase_admin_session');
  window.location.reload();
}

export function getAnalytics() {
  const quizH = JSON.parse(localStorage.getItem('lvlbase_quiz_history') || '[]');
  const battleH = JSON.parse(localStorage.getItem('lvlbase_battle_history') || '[]');
  const goals = JSON.parse(localStorage.getItem('lvlbase_goals') || '[]');
  const profile = JSON.parse(localStorage.getItem('lvlbase_user_profile') || '{}');
  return {
    totalUsers: 1247,
    activeToday: 89,
    quizzesTotal: quizH.length + 12450,
    battlesTotal: battleH.length + 3892,
    avgScore: quizH.length > 0 ? Math.round(quizH.reduce((s,h)=>s+h.score,0)/quizH.length) : 72,
    totalXP: (profile.totalXP || 0) + 2450000,
    goalsCompleted: goals.filter(g=>g.completed).length + 5621,
    retentionRate: 78
  };
}

export function getTopUsers() {
  const profile = JSON.parse(localStorage.getItem('lvlbase_user_profile') || '{}');
  const users = [
    { name:'Arjun Sharma', email:'arjun@student.com', xp:28500, rank:'SS-Rank', status:'active', joined:'2024-01-15', quizzes:245 },
    { name:'Priya Patel',  email:'priya@student.com', xp:24200, rank:'S-Rank',  status:'active', joined:'2024-01-18', quizzes:198 },
    { name:'Rohan Mehta',  email:'rohan@student.com', xp:21800, rank:'S-Rank',  status:'active', joined:'2024-01-20', quizzes:175 }
  ];
  if (profile.displayName) users.push({ name:profile.displayName, email:profile.email||'demo@user.com', xp:profile.totalXP||0, rank:getRankLabel(profile.totalXP||0), status:'active', joined:profile.joinedAt?.split('T')[0]||'2024-01-01', quizzes:profile.quizzesCompleted||0 });
  return users;
}

function getRankLabel(xp) {
  if (xp>=30000) return 'SS-Rank';
  if (xp>=15000) return 'S-Rank';
  if (xp>=7000)  return 'A-Rank';
  if (xp>=3500)  return 'B-Rank';
  if (xp>=1500)  return 'C-Rank';
  if (xp>=500)   return 'D-Rank';
  return 'E-Rank';
}

export function createSystemEvent({ title, description, xpBonus, startDate, endDate }) {
  const events = JSON.parse(localStorage.getItem('lvlbase_events') || '[]');
  events.push({ id:'evt_'+Date.now(), title, description, xpBonus, startDate, endDate, active: true, createdAt: new Date().toISOString() });
  localStorage.setItem('lvlbase_events', JSON.stringify(events));
}

export function getEvents() {
  return JSON.parse(localStorage.getItem('lvlbase_events') || '[]');
}

export default { checkAdminAuth, adminLogin, adminLogout, getAnalytics, getTopUsers, createSystemEvent, getEvents };
