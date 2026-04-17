// ===== GAMIFICATION SYSTEM =====

export const RANKS = [
  { id: 'E',  label: 'E-Rank',  minXP: 0,     maxXP: 500,   color: '#6B7280', emoji: '⚫', title: 'Novice' },
  { id: 'D',  label: 'D-Rank',  minXP: 500,   maxXP: 1500,  color: '#10B981', emoji: '🟢', title: 'Apprentice' },
  { id: 'C',  label: 'C-Rank',  minXP: 1500,  maxXP: 3500,  color: '#3B82F6', emoji: '🔵', title: 'Scholar' },
  { id: 'B',  label: 'B-Rank',  minXP: 3500,  maxXP: 7000,  color: '#8B5CF6', emoji: '🟣', title: 'Expert' },
  { id: 'A',  label: 'A-Rank',  minXP: 7000,  maxXP: 15000, color: '#F59E0B', emoji: '🟡', title: 'Master' },
  { id: 'S',  label: 'S-Rank',  minXP: 15000, maxXP: 30000, color: '#EF4444', emoji: '🔴', title: 'Legend' },
  { id: 'SS', label: 'SS-Rank', minXP: 30000, maxXP: Infinity, color: '#FFD700', emoji: '⭐', title: 'Mythic' }
];

export const GUILDS = {
  shadow: {
    id: 'shadow', name: 'Shadow Guild', emoji: '🌙', color: '#A855F7',
    gradient: 'linear-gradient(135deg, #4C1D95, #7C3AED)',
    tagline: 'Masters of stealth and cunning',
    traits: ['Strategic Thinkers', 'Night Owls', 'Problem Solvers'],
    bonus: '+15% XP on Logic & Math',
    xpBonus: { math: 1.15, logic: 1.15 }
  },
  azure: {
    id: 'azure', name: 'Azure Order', emoji: '💧', color: '#3B82F6',
    gradient: 'linear-gradient(135deg, #1E3A8A, #2563EB)',
    tagline: 'Wisdom flows like water',
    traits: ['Critical Thinkers', 'Fast Learners', 'Team Players'],
    bonus: '+15% XP on Science',
    xpBonus: { science: 1.15 }
  },
  inferno: {
    id: 'inferno', name: 'Inferno Legion', emoji: '🔥', color: '#EF4444',
    gradient: 'linear-gradient(135deg, #7F1D1D, #DC2626)',
    tagline: 'Burn bright, learn fast',
    traits: ['Speed Readers', 'Competitive', 'High Achievers'],
    bonus: '+20% XP in Battles',
    xpBonus: { battle: 1.20 }
  },
  titan: {
    id: 'titan', name: 'Titan Brotherhood', emoji: '⚡', color: '#22C55E',
    gradient: 'linear-gradient(135deg, #14532D, #16A34A)',
    tagline: 'Strength through knowledge',
    traits: ['Consistent Studiers', 'Goal Setters', 'Reliable'],
    bonus: '+15% XP on English',
    xpBonus: { english: 1.15 }
  },
  zenith: {
    id: 'zenith', name: 'Zenith Circle', emoji: '✨', color: '#F59E0B',
    gradient: 'linear-gradient(135deg, #78350F, #D97706)',
    tagline: 'Reach for the peak',
    traits: ['All-Rounders', 'Innovators', 'Leaders'],
    bonus: '+10% XP on Everything',
    xpBonus: { all: 1.10 }
  }
};

export const ACHIEVEMENTS = [
  { id: 'first_quiz',     emoji: '🎯', name: 'First Quiz',      desc: 'Complete your first quiz',           condition: (p) => p.quizzesCompleted >= 1 },
  { id: 'streak_3',       emoji: '🔥', name: '3-Day Streak',    desc: 'Log in 3 days in a row',             condition: (p) => p.streak >= 3 },
  { id: 'streak_7',       emoji: '🌟', name: 'Week Warrior',    desc: 'Maintain a 7-day streak',            condition: (p) => p.streak >= 7 },
  { id: 'perfect_score',  emoji: '💯', name: 'Perfectionist',   desc: 'Score 100% on a quiz',               condition: (p) => p.perfectScores >= 1 },
  { id: 'rank_up_d',      emoji: '📈', name: 'Rising Star',     desc: 'Reach D-Rank',                       condition: (p) => p.totalXP >= 500 },
  { id: 'rank_up_c',      emoji: '🎓', name: 'Scholar',         desc: 'Reach C-Rank',                       condition: (p) => p.totalXP >= 1500 },
  { id: 'rank_up_b',      emoji: '🏅', name: 'Expert',          desc: 'Reach B-Rank',                       condition: (p) => p.totalXP >= 3500 },
  { id: 'quiz_10',        emoji: '📚', name: 'Bookworm',        desc: 'Complete 10 quizzes',                condition: (p) => p.quizzesCompleted >= 10 },
  { id: 'quiz_50',        emoji: '🦉', name: 'Wise Owl',        desc: 'Complete 50 quizzes',                condition: (p) => p.quizzesCompleted >= 50 },
  { id: 'battle_win',     emoji: '⚔️',  name: 'Warrior',         desc: 'Win your first battle',             condition: (p) => p.battlesWon >= 1 },
  { id: 'battle_10',      emoji: '🏆', name: 'Champion',        desc: 'Win 10 battles',                     condition: (p) => p.battlesWon >= 10 },
  { id: 'goal_complete',  emoji: '🎯', name: 'Goal Setter',     desc: 'Complete your first goal',           condition: (p) => p.goalsCompleted >= 1 },
  { id: 'night_owl',      emoji: '🦉', name: 'Night Owl',       desc: 'Study after 10PM',                   condition: (p) => p.lateNightStudy >= 1 },
  { id: 'early_bird',     emoji: '🌅', name: 'Early Bird',      desc: 'Study before 7AM',                   condition: (p) => p.earlyMorningStudy >= 1 },
  { id: 'xp_1000',        emoji: '💫', name: 'XP Hunter',       desc: 'Earn 1000 total XP',                 condition: (p) => p.totalXP >= 1000 }
];

export const XP_REWARDS = {
  quizCorrect: 10,
  quizPerfect: 50,
  quizComplete: 25,
  battleWin: 75,
  battleLose: 15,
  battleDraw: 30,
  dailyLogin: 20,
  streakBonus: 10,
  goalComplete: 100,
  chapterComplete: 150,
  firstOfDay: 30
};

// Get rank info for a given XP amount
export function getRank(xp) {
  for (let i = RANKS.length - 1; i >= 0; i--) {
    if (xp >= RANKS[i].minXP) return RANKS[i];
  }
  return RANKS[0];
}

// Get progress percentage within current rank
export function getRankProgress(xp) {
  const rank = getRank(xp);
  if (rank.maxXP === Infinity) return 100;
  const progress = xp - rank.minXP;
  const range = rank.maxXP - rank.minXP;
  return Math.min(Math.round((progress / range) * 100), 100);
}

// Award XP with multipliers (profile first, then amount, then context)
export function awardXP(profile, amount, context = 'general') {
  if (!profile || !amount) return { finalXP: 0, bonus: 1 };
  let multiplier = 1;
  const guild = profile.guild ? GUILDS[profile.guild] : null;

  // Apply guild bonus
  if (guild) {
    if (guild.xpBonus.all) multiplier += guild.xpBonus.all;
    else if (guild.xpBonus[context]) multiplier += guild.xpBonus[context];
  }

  // Apply streak bonus
  const streakBonus = getStreakBonus(profile.streak || 0);
  multiplier += streakBonus;

  const finalXP = Math.round(amount * multiplier);
  profile.totalXP = (profile.totalXP || 0) + finalXP;
  return { finalXP, bonus: multiplier };
}

// Calculate streak bonus multiplier
export function getStreakBonus(streak) {
  if (streak >= 30) return 0.5;
  if (streak >= 14) return 0.3;
  if (streak >= 7)  return 0.2;
  if (streak >= 3)  return 0.1;
  return 0;
}

// Calculate overall power score
export function calculatePowerScore(profile) {
  const xpScore    = Math.min(profile.totalXP / 100, 300);
  const quizScore  = Math.min(profile.quizzesCompleted * 5, 200);
  const battleScore = Math.min(profile.battlesWon * 10, 200);
  const streakScore = Math.min(profile.streak * 3, 100);
  const goalScore  = Math.min((profile.goalsCompleted || 0) * 15, 100);
  const achievScore = Math.min((profile.achievements?.length || 0) * 10, 100);
  return Math.round(xpScore + quizScore + battleScore + streakScore + goalScore + achievScore);
}

// Check and return new unlocked badges
export function checkAchievements(profile) {
  const unlocked = profile.achievements || [];
  const newBadges = [];
  for (const ach of ACHIEVEMENTS) {
    if (!unlocked.includes(ach.id) && ach.condition(profile)) {
      newBadges.push(ach);
    }
  }
  return newBadges;
}

// Update streak (call on login)
export function updateStreak(profile) {
  const now = new Date();
  const lastLogin = profile.lastLogin ? new Date(profile.lastLogin) : null;
  let streak = profile.streak || 0;

  if (!lastLogin) {
    streak = 1;
  } else {
    const daysDiff = Math.floor((now - lastLogin) / (1000 * 60 * 60 * 24));
    if (daysDiff === 0) {
      // Same day, no change
    } else if (daysDiff === 1) {
      streak += 1;
    } else {
      streak = 1; // Reset streak
    }
  }
  return { streak, lastLogin: now.toISOString() };
}

// Get level from XP (every 100 XP = 1 level)
export function getLevel(xp) {
  return Math.floor(xp / 100) + 1;
}

// Format large numbers
export function formatNumber(n) {
  if (n >= 1000000) return (n / 1000000).toFixed(1) + 'M';
  if (n >= 1000) return (n / 1000).toFixed(1) + 'K';
  return n.toString();
}

// Generate demo leaderboard data
export function getDemoLeaderboard() {
  return [
    { rank: 1,  name: 'Arjun Sharma',   xp: 28500, rankId: 'SS', guild: 'shadow',  avatar: 'AS', streak: 45 },
    { rank: 2,  name: 'Priya Patel',    xp: 24200, rankId: 'S',  guild: 'azure',   avatar: 'PP', streak: 32 },
    { rank: 3,  name: 'Rohan Mehta',    xp: 21800, rankId: 'S',  guild: 'inferno', avatar: 'RM', streak: 28 },
    { rank: 4,  name: 'Anika Singh',    xp: 19500, rankId: 'S',  guild: 'titan',   avatar: 'AS', streak: 21 },
    { rank: 5,  name: 'Dev Kapoor',     xp: 17300, rankId: 'A',  guild: 'zenith',  avatar: 'DK', streak: 18 },
    { rank: 6,  name: 'Sneha Iyer',     xp: 15100, rankId: 'A',  guild: 'shadow',  avatar: 'SI', streak: 15 },
    { rank: 7,  name: 'Karan Malhotra', xp: 13400, rankId: 'A',  guild: 'azure',   avatar: 'KM', streak: 12 },
    { rank: 8,  name: 'Ritika Gupta',   xp: 11200, rankId: 'B',  guild: 'inferno', avatar: 'RG', streak: 9 },
    { rank: 9,  name: 'Vikram Rao',     xp: 9800,  rankId: 'B',  guild: 'titan',   avatar: 'VR', streak: 7 },
    { rank: 10, name: 'Meera Nair',     xp: 8600,  rankId: 'B',  guild: 'zenith',  avatar: 'MN', streak: 6 }
  ];
}

export default { RANKS, GUILDS, ACHIEVEMENTS, XP_REWARDS, getRank, getRankProgress, awardXP, getStreakBonus, calculatePowerScore, checkAchievements, updateStreak, getLevel, formatNumber, getDemoLeaderboard };
