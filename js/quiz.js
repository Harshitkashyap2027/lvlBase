// ===== QUIZ ENGINE MODULE =====
import { getUserProfile, saveUserProfile } from './auth.js';
import { awardXP, getRank } from './gamification.js';

export const QUESTION_BANK = {
  math: [
    { q:'2x + 6 = 14, x = ?', opts:['4','5','6','7'], ans:0, exp:'2x=8, x=4.', diff:'easy' },
    { q:'Which is prime?', opts:['15','21','17','25'], ans:2, exp:'17 only divisible by 1 and itself.', diff:'easy' },
    { q:'Area of circle r=7 (π=22/7)?', opts:['154 cm²','144 cm²','132 cm²','164 cm²'], ans:0, exp:'πr²=(22/7)×49=154', diff:'medium' },
    { q:'Simplify: a² - b²', opts:['(a+b)²','(a-b)(a+b)','(a-b)²','a²+b²'], ans:1, exp:'Difference of squares.', diff:'easy' },
    { q:'15% of 200 = ?', opts:['25','30','35','40'], ans:1, exp:'15/100×200=30', diff:'easy' },
    { q:'Slope through (2,3) and (4,7)?', opts:['1','2','3','4'], ans:1, exp:'(7-3)/(4-2)=4/2=2', diff:'medium' },
    { q:'LCM of 12 and 18?', opts:['24','36','48','54'], ans:1, exp:'LCM(12,18)=36', diff:'easy' },
    { q:'Speed: 240km in 3h?', opts:['60 km/h','70 km/h','80 km/h','90 km/h'], ans:2, exp:'240/3=80', diff:'easy' },
    { q:'√144 = ?', opts:['10','11','12','13'], ans:2, exp:'12×12=144', diff:'easy' },
    { q:'3x-7=2x+5, x=?', opts:['10','12','8','14'], ans:1, exp:'x=12', diff:'medium' },
    { q:'Perimeter: 8cm×5cm rect?', opts:['26 cm','24 cm','28 cm','30 cm'], ans:0, exp:'2(8+5)=26', diff:'easy' },
    { q:'6! = ?', opts:['360','480','600','720'], ans:3, exp:'6×120=720', diff:'medium' },
    { q:'HCF of 24 and 36?', opts:['6','8','12','18'], ans:2, exp:'HCF=12', diff:'easy' },
    { q:'Sum of angles in triangle?', opts:['90°','180°','270°','360°'], ans:1, exp:'Always 180°', diff:'easy' },
    { q:'∛27 = ?', opts:['2','3','4','5'], ans:1, exp:'3³=27', diff:'easy' }
  ],
  science: [
    { q:'Powerhouse of the cell?', opts:['Nucleus','Ribosome','Mitochondria','Vacuole'], ans:2, exp:'Mitochondria produce ATP.', diff:'easy' },
    { q:'Formula of water?', opts:['H₂O₂','HO','H₂O','H₃O'], ans:2, exp:'2H + 1O', diff:'easy' },
    { q:'Most abundant gas in atmosphere?', opts:['Oxygen','CO₂','Nitrogen','Argon'], ans:2, exp:'Nitrogen ≈ 78%', diff:'easy' },
    { q:"Newton's First Law?", opts:['F=ma','Law of Inertia','Action-Reaction','Gravitation'], ans:1, exp:'Law of Inertia', diff:'easy' },
    { q:'Plants make food via?', opts:['Respiration','Transpiration','Photosynthesis','Digestion'], ans:2, exp:'Photosynthesis', diff:'easy' },
    { q:'Atomic number of Carbon?', opts:['4','6','8','12'], ans:1, exp:'6 protons', diff:'easy' },
    { q:'Red Planet?', opts:['Venus','Jupiter','Mars','Saturn'], ans:2, exp:'Iron oxide surface', diff:'easy' },
    { q:'Lens for myopia?', opts:['Convex','Concave','Bifocal','Cylindrical'], ans:1, exp:'Concave corrects myopia', diff:'medium' },
    { q:'Speed of light in vacuum?', opts:['3×10⁶ m/s','3×10⁸ m/s','3×10¹⁰ m/s','3×10⁴ m/s'], ans:1, exp:'~3×10⁸ m/s', diff:'medium' },
    { q:'DNA stands for?', opts:['Deoxyribose Nucleic Acid','Deoxyribonucleic Acid','Diribonucleic','Dual Nucleic'], ans:1, exp:'Deoxyribonucleic Acid', diff:'medium' },
    { q:'Acid in stomach?', opts:['Sulphuric','Nitric','Hydrochloric','Citric'], ans:2, exp:'HCl for digestion', diff:'easy' },
    { q:'Unit of electric current?', opts:['Volt','Watt','Ohm','Ampere'], ans:3, exp:'Amperes (A)', diff:'easy' },
    { q:'Universal blood donor?', opts:['A','B','AB','O'], ans:3, exp:'O- universal donor', diff:'medium' },
    { q:'Ozone layer protects from?', opts:['Infrared','UV rays','X-rays','Radio waves'], ans:1, exp:'Absorbs UV radiation', diff:'easy' },
    { q:'SI unit of force?', opts:['Joule','Watt','Newton','Pascal'], ans:2, exp:'Newton (N)', diff:'easy' }
  ],
  english: [
    { q:'"She ___ to school every day."', opts:['go','goes','going','gone'], ans:1, exp:'Third-person singular: goes', diff:'easy' },
    { q:'Synonym of "eloquent"?', opts:['Quiet','Articulate','Confused','Abrupt'], ans:1, exp:'Eloquent = Articulate', diff:'easy' },
    { q:'Passive voice example?', opts:['Dog chased cat.','Cat was chased by dog.','I ate cake.','She writes books.'], ans:1, exp:'Subject receives action', diff:'medium' },
    { q:'Antonym of "benevolent"?', opts:['Kind','Generous','Malevolent','Charitable'], ans:2, exp:'Malevolent = wishing evil', diff:'easy' },
    { q:'"Stars danced in sky" – figure of speech?', opts:['Simile','Metaphor','Personification','Hyperbole'], ans:2, exp:'Human quality = personification', diff:'medium' },
    { q:'Correct spelling?', opts:['Accomodation','Accommodation','Acommodation','Acomodation'], ans:1, exp:'Double c, double m', diff:'easy' },
    { q:'"Kill two birds with one stone" means?', opts:['Harm animals','Two goals, one action','Be wasteful','Be unlucky'], ans:1, exp:'Two goals, one effort', diff:'easy' },
    { q:'"The book is mine" – "mine" is?', opts:['Personal pronoun','Possessive pronoun','Reflexive','Demonstrative'], ans:1, exp:'Mine shows possession', diff:'medium' },
    { q:'Correct sentence?', opts:['Me and him went.','Him and I went.','He and I went to store.','I and he went.'], ans:2, exp:'Subject: "He and I"', diff:'medium' },
    { q:'"Life is a roller coaster" – device?', opts:['Simile','Metaphor','Alliteration','Onomatopoeia'], ans:1, exp:'Direct comparison = metaphor', diff:'easy' },
    { q:'Plural of "analysis"?', opts:['Analysises','Analysi','Analyses','Analysis'], ans:2, exp:'-is → -es', diff:'medium' },
    { q:'Adverb in "She speaks very softly"?', opts:['She','speaks','very','Both very and softly'], ans:3, exp:'Both are adverbs', diff:'medium' },
    { q:'Correct?', opts:["There going.","They're going to the park.","Their going.","Theyre going."], ans:1, exp:"They're = they are", diff:'easy' },
    { q:'Interrogative sentence ends with?', opts:['.','!','?',';'], ans:2, exp:'Questions end with ?', diff:'easy' },
    { q:'"Pedagogy" relates to?', opts:['Cooking','Medicine','Teaching','Plants'], ans:2, exp:'Pedagogy = teaching method', diff:'hard' }
  ]
};

export function getQuestions(subject = 'math', count = 10) {
  const bank = subject === 'mixed'
    ? [...QUESTION_BANK.math, ...QUESTION_BANK.science, ...QUESTION_BANK.english]
    : (QUESTION_BANK[subject] || QUESTION_BANK.math);
  return [...bank].sort(() => Math.random() - 0.5).slice(0, Math.min(count, bank.length));
}

export function calculateQuizXP(correct, total, mode, timeBonus = 0) {
  const base = correct * 10;
  const completion = 25;
  const perfect = correct === total ? 50 : 0;
  const modeBonus = mode === 'speed' ? 20 : mode === 'exam' ? 10 : 0;
  return base + completion + perfect + modeBonus + timeBonus;
}

export function saveQuizResult({ subject, mode, score, correct, total, xpEarned, questions, answers }) {
  const history = JSON.parse(localStorage.getItem('lvlbase_quiz_history') || '[]');
  history.unshift({ subject, mode, score, correct, total, xpEarned, date: new Date().toISOString(), questions: questions.length });
  localStorage.setItem('lvlbase_quiz_history', JSON.stringify(history.slice(0, 50)));

  const profile = getUserProfile();
  if (profile) {
    profile.quizzesCompleted = (profile.quizzesCompleted || 0) + 1;
    if (correct === total) profile.perfectScores = (profile.perfectScores || 0) + 1;
    const result = awardXP(profile, xpEarned, subject);
    if (!profile.subjectProgress) profile.subjectProgress = { math: 0, science: 0, english: 0 };
    if (subject !== 'mixed') profile.subjectProgress[subject] = Math.min(100, (profile.subjectProgress[subject] || 0) + (score/100*5));
    if (!profile.achievements) profile.achievements = [];
    if (profile.quizzesCompleted === 1) profile.achievements.push('first_quiz');
    if (profile.quizzesCompleted >= 10 && !profile.achievements.includes('quiz_10')) profile.achievements.push('quiz_10');
    if (correct === total && !profile.achievements.includes('perfect_score')) profile.achievements.push('perfect_score');
    saveUserProfile(profile);
    return { profile, ...result };
  }
  return null;
}

export default { QUESTION_BANK, getQuestions, calculateQuizXP, saveQuizResult };
