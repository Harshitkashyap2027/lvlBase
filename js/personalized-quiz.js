// ===== PERSONALIZED QUIZ GENERATOR =====
// Generates adaptive quizzes weighted towards the user's weak subjects and difficulty.

import { QUESTION_BANK } from './quiz.js';
import { getUserProfile } from './auth.js';

// ── Performance analysis ────────────────────────────────────────────────────

/**
 * Analyse a user's quiz history and return per-subject performance scores (0–100).
 * Higher score = stronger subject.
 */
export function analysePerformance(profile) {
  const history = JSON.parse(localStorage.getItem('lvlbase_quiz_history') || '[]');
  const stats = { math: { total: 0, score: 0 }, science: { total: 0, score: 0 }, english: { total: 0, score: 0 } };

  history.forEach((h) => {
    const subj = h.subject;
    if (stats[subj]) {
      stats[subj].total += 1;
      stats[subj].score += h.score || 0;
    }
  });

  const performance = {};
  for (const subj of Object.keys(stats)) {
    const s = stats[subj];
    if (s.total === 0) {
      // No data → use subjectProgress as proxy, or default to 50
      performance[subj] = Math.max(profile?.subjectProgress?.[subj] ?? 50, 5);
    } else {
      performance[subj] = Math.round(s.score / s.total);
    }
  }
  return performance;
}

/**
 * Identify the weakest subjects (score < threshold) in order.
 */
export function getWeakSubjects(performance, threshold = 60) {
  return Object.entries(performance)
    .filter(([, score]) => score < threshold)
    .sort(([, a], [, b]) => a - b) // weakest first
    .map(([subject]) => subject);
}

// ── Difficulty mapping ─────────────────────────────────────────────────────

function difficultyWeight(subjectScore) {
  if (subjectScore >= 80) return { easy: 0.1, medium: 0.4, hard: 0.5 };
  if (subjectScore >= 60) return { easy: 0.2, medium: 0.5, hard: 0.3 };
  if (subjectScore >= 40) return { easy: 0.4, medium: 0.4, hard: 0.2 };
  return { easy: 0.6, medium: 0.3, hard: 0.1 };
}

// ── Question selection ─────────────────────────────────────────────────────

function pickWeightedQuestions(subject, count, performanceScore) {
  const bank = QUESTION_BANK[subject] || [];
  const weights = difficultyWeight(performanceScore);

  const easy   = bank.filter(q => q.diff === 'easy');
  const medium = bank.filter(q => q.diff === 'medium');
  const hard   = bank.filter(q => q.diff === 'hard');

  const nEasy   = Math.round(count * weights.easy);
  const nMedium = Math.round(count * weights.medium);
  const nHard   = count - nEasy - nMedium;

  const shuffle = (arr) => [...arr].sort(() => Math.random() - 0.5);

  return [
    ...shuffle(easy).slice(0, nEasy),
    ...shuffle(medium).slice(0, nMedium),
    ...shuffle(hard).slice(0, Math.max(0, nHard))
  ].sort(() => Math.random() - 0.5);
}

// ── Subject weighting ──────────────────────────────────────────────────────

function computeSubjectDistribution(performance, totalQuestions) {
  const subjects = Object.keys(performance);
  // Invert scores so weaker subjects get more questions
  const inverted = subjects.map(s => ({ subject: s, weight: Math.max(100 - performance[s], 5) }));
  const totalWeight = inverted.reduce((sum, s) => sum + s.weight, 0);
  let remaining = totalQuestions;
  const dist = {};
  inverted.forEach((s, i) => {
    if (i === inverted.length - 1) {
      dist[s.subject] = remaining;
    } else {
      const n = Math.round((s.weight / totalWeight) * totalQuestions);
      dist[s.subject] = n;
      remaining -= n;
    }
  });
  return dist;
}

// ── Public API ─────────────────────────────────────────────────────────────

/**
 * Generate a fully personalised quiz.
 *
 * @param {object} options
 * @param {number} options.count          - Number of questions (default 10)
 * @param {'adaptive'|'weak_focus'|'balanced'} options.mode - Strategy
 * @param {string|null} options.forceSubject - Restrict to one subject (optional)
 * @returns {{ questions: object[], meta: object }}
 */
export function generatePersonalizedQuiz({ count = 10, mode = 'adaptive', forceSubject = null } = {}) {
  const profile = getUserProfile() || {};
  const performance = analysePerformance(profile);
  const weakSubjects = getWeakSubjects(performance);

  let questions = [];
  let meta = { mode, performance, weakSubjects, distribution: {} };

  if (forceSubject) {
    questions = pickWeightedQuestions(forceSubject, count, performance[forceSubject] ?? 50);
    meta.distribution = { [forceSubject]: questions.length };
  } else if (mode === 'weak_focus') {
    // All questions from the weakest subject
    const subj = weakSubjects[0] || 'math';
    questions = pickWeightedQuestions(subj, count, performance[subj] ?? 50);
    meta.distribution = { [subj]: questions.length };
  } else if (mode === 'balanced') {
    // Equal distribution across subjects
    const perSubj = Math.floor(count / 3);
    const subjects = ['math', 'science', 'english'];
    subjects.forEach((s, i) => {
      const n = i === subjects.length - 1 ? count - questions.length : perSubj;
      const qs = pickWeightedQuestions(s, n, performance[s] ?? 50);
      questions.push(...qs);
      meta.distribution[s] = qs.length;
    });
    questions.sort(() => Math.random() - 0.5);
  } else {
    // adaptive: weight questions towards weak areas
    const dist = computeSubjectDistribution(performance, count);
    meta.distribution = dist;
    for (const [subj, n] of Object.entries(dist)) {
      if (n <= 0) continue;
      const qs = pickWeightedQuestions(subj, n, performance[subj] ?? 50);
      questions.push(...qs.map(q => ({ ...q, _subject: subj })));
    }
    questions.sort(() => Math.random() - 0.5);
  }

  // Attach subject tag and ensure we have the right count
  questions = questions.slice(0, count);
  return { questions, meta };
}

/**
 * Build a difficulty label and description for the generated quiz.
 */
export function describeQuiz(meta) {
  const { performance, weakSubjects, distribution } = meta;
  const avgScore = Math.round(Object.values(performance).reduce((s, v) => s + v, 0) / Object.values(performance).length);

  let difficulty, desc;
  if (avgScore >= 80) { difficulty = '🔴 Hard'; desc = 'Great job! You\'re strong across subjects — challenging questions selected.'; }
  else if (avgScore >= 60) { difficulty = '🟡 Medium'; desc = 'Solid performance. Mixed difficulty to stretch your knowledge.'; }
  else { difficulty = '🟢 Easy-Medium'; desc = 'Focus on building your foundations. Easier questions with targeted practice.'; }

  const focus = weakSubjects.length
    ? `Focus areas: ${weakSubjects.join(', ')}`
    : 'All subjects performing well!';

  const distStr = Object.entries(distribution).map(([s, n]) => `${s}: ${n}Q`).join(' | ');

  return { difficulty, desc, focus, distStr, avgScore };
}

export default { generatePersonalizedQuiz, analysePerformance, getWeakSubjects, describeQuiz };
