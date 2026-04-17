// ===== GOALS MODULE =====
import { getUserProfile, saveUserProfile } from './auth.js';
import { awardXP } from './gamification.js';

export const GOAL_CATEGORIES = {
  study:   { label:'Study',   emoji:'📚', color:'#6C63FF' },
  quiz:    { label:'Quiz',    emoji:'🎯', color:'#00D1B2' },
  battle:  { label:'Battle',  emoji:'⚔️', color:'#FF6B6B' },
  streak:  { label:'Streak',  emoji:'🔥', color:'#FFA500' },
  xp:      { label:'XP',      emoji:'⚡', color:'#FFD700' },
  reading: { label:'Reading', emoji:'📖', color:'#10B981' }
};

export const GOAL_TEMPLATES = [
  { title:'Complete 5 quizzes this week',  category:'quiz',    target:5,   unit:'quizzes',    days:7 },
  { title:'Maintain a 7-day streak',        category:'streak',  target:7,   unit:'days',        days:7 },
  { title:'Earn 500 XP this week',          category:'xp',      target:500, unit:'XP',          days:7 },
  { title:'Win 3 battles',                  category:'battle',  target:3,   unit:'battles',     days:7 },
  { title:'Study 30 mins daily',            category:'study',   target:30,  unit:'min/day',     days:1 },
  { title:'Read 1 chapter per day',         category:'reading', target:1,   unit:'chapters',    days:1 }
];

export function loadGoals() {
  return JSON.parse(localStorage.getItem('lvlbase_goals') || '[]');
}

export function saveGoals(goals) {
  localStorage.setItem('lvlbase_goals', JSON.stringify(goals));
}

export function createGoal({ title, category, target, unit, deadline, xpReward }) {
  return {
    id: 'goal_' + Date.now(),
    title, category, target, unit: unit || '',
    current: 0, completed: false,
    deadline: deadline || getDeadline(7),
    createdAt: new Date().toISOString(),
    xpReward: xpReward || Math.round(100 * (1 + target/50))
  };
}

export function completeGoal(goalId) {
  const goals = loadGoals();
  const goal = goals.find(g => g.id === goalId);
  if (!goal || goal.completed) return null;
  goal.completed = true;
  goal.completedAt = new Date().toISOString();
  saveGoals(goals);

  const profile = getUserProfile();
  if (profile) {
    profile.goalsCompleted = (profile.goalsCompleted || 0) + 1;
    if (!profile.achievements) profile.achievements = [];
    if (!profile.achievements.includes('goal_complete')) profile.achievements.push('goal_complete');
    awardXP(profile, goal.xpReward || 100, 'goal');
    saveUserProfile(profile);
  }
  return goal;
}

export function getDaysLeft(deadline) {
  return Math.ceil((new Date(deadline) - new Date()) / 86400000);
}

export function getDeadline(days) {
  const d = new Date(); d.setDate(d.getDate() + days);
  return d.toISOString().split('T')[0];
}

export default { GOAL_CATEGORIES, GOAL_TEMPLATES, loadGoals, saveGoals, createGoal, completeGoal, getDaysLeft, getDeadline };
