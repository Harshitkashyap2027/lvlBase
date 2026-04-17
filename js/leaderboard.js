// ===== LEADERBOARD MODULE =====
import { getUserProfile } from './auth.js';
import { getRank, GUILDS } from './gamification.js';

export const DEMO_PLAYERS = [
  { name:'Arjun Sharma',  xp:28500, rankId:'SS', guild:'shadow', avatar:'AS', streak:45, school:'DPS Delhi' },
  { name:'Priya Patel',   xp:24200, rankId:'S',  guild:'azure',  avatar:'PP', streak:32, school:'Ryan International' },
  { name:'Rohan Mehta',   xp:21800, rankId:'S',  guild:'inferno',avatar:'RM', streak:28, school:'Kendriya Vidyalaya' },
  { name:'Anika Singh',   xp:19500, rankId:'S',  guild:'titan',  avatar:'AS', streak:21, school:'DPS Noida' },
  { name:'Dev Kapoor',    xp:17300, rankId:'A',  guild:'zenith', avatar:'DK', streak:18, school:'Modern School' },
  { name:'Sneha Iyer',    xp:15100, rankId:'A',  guild:'shadow', avatar:'SI', streak:15, school:'CBSE Chennai' },
  { name:'Karan Malhotra',xp:13400, rankId:'A',  guild:'azure',  avatar:'KM', streak:12, school:'St. Xavier\'s' },
  { name:'Ritika Gupta',  xp:11200, rankId:'B',  guild:'inferno',avatar:'RG', streak:9,  school:'Amity Pune' },
  { name:'Vikram Rao',    xp:9800,  rankId:'B',  guild:'titan',  avatar:'VR', streak:7,  school:'MIT Hyderabad' },
  { name:'Meera Nair',    xp:8600,  rankId:'B',  guild:'zenith', avatar:'MN', streak:6,  school:'DPS Bangalore' }
];

export function getIndividualBoard() {
  const profile = getUserProfile();
  const board = [...DEMO_PLAYERS];
  if (profile && profile.totalXP > 0) {
    const exists = board.find(u => u.name === profile.displayName);
    if (!exists) {
      const rank = getRank(profile.totalXP);
      board.push({ name: profile.displayName || 'You', xp: profile.totalXP, rankId: rank.id, guild: profile.guild || 'none', avatar: (profile.displayName||'P').substring(0,2).toUpperCase(), streak: profile.streak || 0, isCurrentUser: true });
    }
  }
  return board.sort((a,b) => b.xp - a.xp).map((u,i) => ({ ...u, rank: i+1 }));
}

export function getGuildBoard() {
  return [
    { rank:1, name:'Shadow Guild', emoji:'🌙', guild:'shadow', members:234, avgXP:12500, totalXP:2925000, wins:89 },
    { rank:2, name:'Inferno Legion', emoji:'🔥', guild:'inferno', members:198, avgXP:11800, totalXP:2336400, wins:76 },
    { rank:3, name:'Azure Order', emoji:'💧', guild:'azure', members:215, avgXP:10900, totalXP:2343500, wins:71 },
    { rank:4, name:'Titan Brotherhood', emoji:'⚡', guild:'titan', members:178, avgXP:9800, totalXP:1744400, wins:63 },
    { rank:5, name:'Zenith Circle', emoji:'✨', guild:'zenith', members:156, avgXP:8900, totalXP:1388400, wins:55 }
  ];
}

export default { DEMO_PLAYERS, getIndividualBoard, getGuildBoard };
