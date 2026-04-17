// ===== BATTLES MODULE =====
import { getUserProfile, saveUserProfile } from './auth.js';
import { awardXP } from './gamification.js';

export const OPPONENTS = [
  { id:'shadow_bot',   name:'Shadow Bot',   level:'E-Rank', avatar:'🤖', hp:80,  difficulty:0.3,  xpReward:30,  desc:'Easy starter' },
  { id:'quiz_golem',   name:'Quiz Golem',   level:'D-Rank', avatar:'🗿', hp:100, difficulty:0.45, xpReward:45,  desc:'Getting tougher' },
  { id:'logic_wyrm',   name:'Logic Wyrm',   level:'C-Rank', avatar:'🐉', hp:120, difficulty:0.6,  xpReward:60,  desc:'Intermediate' },
  { id:'mind_titan',   name:'Mind Titan',   level:'B-Rank', avatar:'🦁', hp:150, difficulty:0.7,  xpReward:80,  desc:'Advanced warrior' },
  { id:'sage_phantom', name:'Sage Phantom', level:'A-Rank', avatar:'👻', hp:180, difficulty:0.8,  xpReward:110, desc:'Elite challenger' },
  { id:'scholar_god',  name:'Scholar God',  level:'S-Rank', avatar:'⚡', hp:200, difficulty:0.9,  xpReward:150, desc:'Ultimate boss' }
];

// AI answer logic
export function aiAnswer(question, difficulty) {
  return Math.random() < difficulty;
}

// Calculate damage based on speed
export function calculateDamage(isCorrect, streak, timeLeft, maxTime) {
  if (!isCorrect) return 0;
  const base = 15;
  const speedBonus = Math.floor((timeLeft / maxTime) * 10);
  const streakBonus = Math.min(15, streak * 3);
  return base + speedBonus + streakBonus;
}

// Save battle result
export function saveBattleResult({ opponent, outcome, xpEarned, correct, rounds }) {
  const history = JSON.parse(localStorage.getItem('lvlbase_battle_history') || '[]');
  history.unshift({ opponent: opponent.name, outcome, xpEarned, correct, rounds, date: new Date().toISOString() });
  localStorage.setItem('lvlbase_battle_history', JSON.stringify(history.slice(0, 30)));

  const profile = getUserProfile();
  if (profile) {
    profile.battlesPlayed = (profile.battlesPlayed || 0) + 1;
    if (outcome === 'win') profile.battlesWon = (profile.battlesWon || 0) + 1;
    if (!profile.achievements) profile.achievements = [];
    if (outcome === 'win' && !profile.achievements.includes('battle_win')) profile.achievements.push('battle_win');
    if ((profile.battlesWon || 0) >= 10 && !profile.achievements.includes('battle_10')) profile.achievements.push('battle_10');
    const result = awardXP(profile, xpEarned, 'battle');
    saveUserProfile(profile);
    return result;
  }
  return null;
}

export default { OPPONENTS, aiAnswer, calculateDamage, saveBattleResult };
