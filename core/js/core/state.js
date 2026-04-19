// ===== DASHBOARD MODULE =====
import { getUserProfile, saveUserProfile, checkAuth } from './auth.js';
import { getRank, getRankProgress, getXPToNextRank, updateStreak, GUILDS, ACHIEVEMENTS, formatNumber } from './gamification.js';

export function initDashboard() {
  const user = checkAuth();
  if (!user) return;

  const profile = getUserProfile();
  if (!profile) return;

  // Update streak
  if (updateStreak(profile)) {
    profile.totalXP = (profile.totalXP || 0) + 20; // login bonus
    saveUserProfile(profile);
  }

  renderWelcome(profile);
  renderStats(profile);
  renderSubjectProgress(profile);
  renderLeaderboardMini();
  renderActivityFeed();
}

function renderWelcome(profile) {
  const rank = getRank(profile.totalXP);
  const progress = getRankProgress(profile.totalXP);
  const hour = new Date().getHours();
  const greeting = hour < 12 ? '☀️ Good Morning' : hour < 17 ? '👋 Good Afternoon' : '🌙 Good Evening';
  const guild = GUILDS[profile.guild];

  setInner('welcome-name', `${greeting}, ${profile.displayName?.split(' ')[0] || 'Champion'}!`);
  setInner('welcome-subtitle', guild ? `${guild.emoji} ${guild.name} Member • Grade ${profile.grade}` : 'Choose a guild to unlock XP bonuses!');
  setInner('welcome-xp', `⚡ ${formatNumber(profile.totalXP)} XP`);
  setStyle('welcome-xp-bar', 'width', progress + '%');
  setInner('xp-progress-text', progress + '%');

  const rankEl = document.getElementById('welcome-rank');
  if (rankEl) rankEl.innerHTML = `<span class="rank-badge rank-${rank.id.toLowerCase()}">${rank.label}</span>`;
  const streakEl = document.getElementById('welcome-streak');
  if (streakEl) streakEl.innerHTML = `<span class="streak-badge">🔥 ${profile.streak || 0} Day Streak</span>`;
}

function renderStats(profile) {
  const stats = [
    { id: 'stat-xp', icon: '⚡', color: '#6C63FF', value: formatNumber(profile.totalXP), label: 'Total XP', change: '+20 today' },
    { id: 'stat-streak', icon: '🔥', color: '#FF6B6B', value: profile.streak || 0, label: 'Day Streak', change: profile.streak > 1 ? 'Keep it up!' : 'Start today!' },
    { id: 'stat-quizzes', icon: '🎯', color: '#00D1B2', value: profile.quizzesCompleted || 0, label: 'Quizzes Done', change: 'Keep learning!' },
    { id: 'stat-battles', icon: '⚔️', color: '#FFD700', value: (profile.battlesWon || 0) + '/' + (profile.battlesPlayed || 0), label: 'Battles W/P', change: profile.battlesPlayed > 0 ? Math.round(profile.battlesWon/profile.battlesPlayed*100)+'% win rate' : 'No battles yet' }
  ];
  stats.forEach(s => {
    const el = document.getElementById(s.id);
    if (el) el.innerHTML = `<div class="stat-icon" style="background:${s.color}20">${s.icon}</div><div class="stat-info"><div class="value">${s.value}</div><div class="label">${s.label}</div><div class="change change-up">${s.change}</div></div>`;
  });
}

function renderSubjectProgress(profile) {
  const sp = document.getElementById('subject-progress');
  if (!sp) return;
  const subjects = [
    { key: 'math', name: 'Mathematics', emoji: '📐', color: '#6C63FF', total: 12 },
    { key: 'science', name: 'Science', emoji: '🔬', color: '#00D1B2', total: 15 },
    { key: 'english', name: 'English', emoji: '📚', color: '#FF6B6B', total: 10 }
  ];
  const progData = profile.subjectProgress || {};
  sp.innerHTML = subjects.map(s => {
    const pct = Math.round(progData[s.key] || 0);
    return `<div class="subject-card" onclick="location.href='learn.html?subject=${s.key}'" style="cursor:pointer">
      <div class="subject-header"><span class="subject-icon">${s.emoji}</span><div><div class="subject-name">${s.name}</div><div class="subject-chapters">${Math.floor(pct/100*s.total)}/${s.total} ch.</div></div></div>
      <div class="subject-progress-label"><span>Progress</span><span style="color:${s.color}">${pct}%</span></div>
      <div class="progress-bar-bg"><div class="progress-bar" style="background:${s.color};width:${pct}%"></div></div>
    </div>`;
  }).join('');
}

function renderLeaderboardMini() {
  const el = document.getElementById('leaderboard-mini');
  if (!el) return;
  const profile = getUserProfile() || {};
  const demo = [
    { name:'Arjun Sharma',xp:28500,avatar:'AS' },
    { name:'Priya Patel',xp:24200,avatar:'PP' },
    { name:'Rohan Mehta',xp:21800,avatar:'RM' },
    { name:'Anika Singh',xp:19500,avatar:'AS' },
    { name:profile.displayName||'You',xp:profile.totalXP||0,avatar:(profile.displayName||'P').substring(0,2).toUpperCase(),isYou:true }
  ].sort((a,b)=>b.xp-a.xp).slice(0,5);
  el.innerHTML = demo.map((item,i)=>`
    <div class="lb-item">
      <span class="lb-rank ${i===0?'top1':i===1?'top2':i===2?'top3':''}">${i<3?['🥇','🥈','🥉'][i]:'#'+(i+1)}</span>
      <div class="avatar" style="width:28px;height:28px;font-size:0.7rem">${item.avatar}</div>
      <span class="lb-name">${item.name}${item.isYou?' (You)':''}</span>
      <span class="lb-score">⚡${formatNumber(item.xp)}</span>
    </div>`).join('');
}

function renderActivityFeed() {
  const feed = document.getElementById('activity-feed');
  if (!feed) return;
  const quizH = JSON.parse(localStorage.getItem('lvlbase_quiz_history') || '[]');
  const battleH = JSON.parse(localStorage.getItem('lvlbase_battle_history') || '[]');
  const timeAgo = d => { const diff = Date.now()-new Date(d).getTime(); const m = Math.floor(diff/60000); return m<1?'Just now':m<60?m+'m ago':Math.floor(diff/3600000)+'h ago'; };
  let acts = [{ icon:'🔐', bg:'rgba(108,99,255,0.15)', text:'Daily login bonus earned', time:'Today', xp:'+20 XP' }];
  quizH.slice(0,3).forEach(h=>acts.push({ icon:'🎯', bg:'rgba(0,209,178,0.15)', text:`Scored ${h.score}% on ${h.subject} quiz`, time:timeAgo(h.date), xp:`+${h.xpEarned} XP` }));
  battleH.slice(0,2).forEach(b=>acts.push({ icon:'⚔️', bg:'rgba(255,107,107,0.15)', text:`${b.outcome==='win'?'Won':'Lost'} battle vs ${b.opponent}`, time:timeAgo(b.date), xp:`+${b.xpEarned} XP` }));
  feed.innerHTML = acts.slice(0,6).map(a=>`
    <div class="activity-item">
      <div class="activity-icon" style="background:${a.bg}">${a.icon}</div>
      <div style="flex:1"><div class="activity-text">${a.text}</div><div class="activity-time">${a.time}</div></div>
      <span class="badge badge-success">${a.xp}</span>
    </div>`).join('');
}

function setInner(id, html) { const el = document.getElementById(id); if (el) el.innerHTML = html; }
function setStyle(id, prop, val) { const el = document.getElementById(id); if (el) el.style[prop] = val; }

export default { initDashboard };
