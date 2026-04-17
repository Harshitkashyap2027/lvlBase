// ===== SUBJECTS MODULE =====

export const SUBJECTS = {
  math: {
    id: 'math', name: 'Mathematics', emoji: '📐',
    gradient: 'linear-gradient(135deg, #6C63FF, #4A00E0)',
    color: '#6C63FF', totalChapters: 12,
    desc: 'Algebra, Geometry, Trigonometry & more',
    chapters: [
      { id:1,  title:'Number Systems',           topics:['Natural Numbers','Integers','Rational Numbers','Irrational Numbers','Real Numbers'], difficulty:'Easy', duration:'45 min', xp:50 },
      { id:2,  title:'Polynomials',               topics:['Definition','Types','Zeros','Division Algorithm','Factorisation'], difficulty:'Medium', duration:'60 min', xp:75 },
      { id:3,  title:'Linear Equations',          topics:['Introduction','Graphical Method','Substitution','Elimination'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:4,  title:'Quadratic Equations',       topics:['Factorisation','Completing Square','Quadratic Formula','Nature of Roots'], difficulty:'Hard', duration:'70 min', xp:100 },
      { id:5,  title:'Arithmetic Progressions',   topics:['nth Term','Sum of n Terms','Applications'], difficulty:'Medium', duration:'50 min', xp:75 },
      { id:6,  title:'Triangles',                 topics:['Similar Triangles','BPT Theorem','Pythagoras Theorem'], difficulty:'Medium', duration:'65 min', xp:75 },
      { id:7,  title:'Coordinate Geometry',       topics:['Distance Formula','Section Formula','Midpoint','Area of Triangle'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:8,  title:'Trigonometry',              topics:['Ratios','Complementary Angles','Identities','Heights & Distances'], difficulty:'Hard', duration:'80 min', xp:100 },
      { id:9,  title:'Circles',                   topics:['Tangent to Circle','Two Tangents','Properties'], difficulty:'Medium', duration:'50 min', xp:75 },
      { id:10, title:'Areas & Volumes',           topics:['Combination of Solids','Conversion of Shapes','Frustum'], difficulty:'Hard', duration:'75 min', xp:100 },
      { id:11, title:'Statistics',                topics:['Mean','Median','Mode','Cumulative Frequency'], difficulty:'Medium', duration:'60 min', xp:75 },
      { id:12, title:'Probability',               topics:['Classical Probability','Events','Sample Space'], difficulty:'Easy', duration:'45 min', xp:50 }
    ]
  },
  science: {
    id: 'science', name: 'Science', emoji: '🔬',
    gradient: 'linear-gradient(135deg, #00D1B2, #009B86)',
    color: '#00D1B2', totalChapters: 15,
    desc: 'Physics, Chemistry, Biology & Environment',
    chapters: [
      { id:1,  title:'Chemical Reactions & Equations',   topics:['Types of Reactions','Balancing','Oxidation','Corrosion'], difficulty:'Medium', duration:'60 min', xp:75 },
      { id:2,  title:'Acids, Bases & Salts',             topics:['Properties','pH Scale','Indicators','Salt Preparation'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:3,  title:'Metals & Non-Metals',              topics:['Physical Properties','Chemical Properties','Reactivity Series'], difficulty:'Medium', duration:'65 min', xp:75 },
      { id:4,  title:'Carbon Compounds',                 topics:['Covalent Bonds','Nomenclature','Properties'], difficulty:'Hard', duration:'70 min', xp:100 },
      { id:5,  title:'Periodic Classification',          topics:['Dobereiner\'s Triads','Mendeleev Table','Modern Table'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:6,  title:'Life Processes',                   topics:['Nutrition','Respiration','Transportation','Excretion'], difficulty:'Hard', duration:'75 min', xp:100 },
      { id:7,  title:'Control & Coordination',           topics:['Nervous System','Hormones','Plant Hormones'], difficulty:'Medium', duration:'60 min', xp:75 },
      { id:8,  title:'Reproduction',                     topics:['Asexual','Sexual','Human Reproduction'], difficulty:'Medium', duration:'65 min', xp:75 },
      { id:9,  title:'Heredity & Evolution',             topics:['Mendel\'s Laws','Variations','Evolution'], difficulty:'Hard', duration:'70 min', xp:100 },
      { id:10, title:'Light – Reflection & Refraction',  topics:['Reflection Laws','Mirrors','Refraction','Lenses'], difficulty:'Hard', duration:'80 min', xp:100 },
      { id:11, title:'Human Eye & Colourful World',      topics:['Eye Structure','Defects','Dispersion'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:12, title:'Electricity',                      topics:['Current','Ohm\'s Law','Resistance','Circuits','Power'], difficulty:'Hard', duration:'75 min', xp:100 },
      { id:13, title:'Magnetic Effects',                 topics:['Magnetic Field','Electromagnetic Induction','Motor'], difficulty:'Hard', duration:'70 min', xp:100 },
      { id:14, title:'Sources of Energy',                topics:['Conventional','Non-Conventional','Nuclear'], difficulty:'Easy', duration:'45 min', xp:50 },
      { id:15, title:'Our Environment',                  topics:['Ecosystem','Food Chain','Ozone Depletion'], difficulty:'Easy', duration:'40 min', xp:50 }
    ]
  },
  english: {
    id: 'english', name: 'English', emoji: '📚',
    gradient: 'linear-gradient(135deg, #FF6B6B, #CC0000)',
    color: '#FF6B6B', totalChapters: 10,
    desc: 'Grammar, Literature & Writing Skills',
    chapters: [
      { id:1,  title:'Parts of Speech',            topics:['Nouns','Pronouns','Verbs','Adjectives','Adverbs'], difficulty:'Easy', duration:'55 min', xp:50 },
      { id:2,  title:'Tenses',                     topics:['Present Tenses','Past Tenses','Future Tenses','Perfect Tenses'], difficulty:'Medium', duration:'65 min', xp:75 },
      { id:3,  title:'Active & Passive Voice',     topics:['Rules for Conversion','Tense-wise Practice','Common Errors'], difficulty:'Medium', duration:'50 min', xp:75 },
      { id:4,  title:'Direct & Indirect Speech',   topics:['Reporting Verbs','Rules','Time Changes'], difficulty:'Medium', duration:'55 min', xp:75 },
      { id:5,  title:'Reading Comprehension',      topics:['Main Idea','Inference','Vocabulary in Context','Summarising'], difficulty:'Hard', duration:'70 min', xp:100 },
      { id:6,  title:'Writing Skills',             topics:['Formal Letters','Informal Letters','Essays','Reports'], difficulty:'Hard', duration:'80 min', xp:100 },
      { id:7,  title:'Literature – Prose',         topics:['Character Analysis','Theme','Plot Summary'], difficulty:'Medium', duration:'65 min', xp:75 },
      { id:8,  title:'Literature – Poetry',        topics:['Figures of Speech','Rhyme Scheme','Tone & Mood'], difficulty:'Medium', duration:'60 min', xp:75 },
      { id:9,  title:'Vocabulary & Word Power',    topics:['Synonyms','Antonyms','Idioms','Phrasal Verbs'], difficulty:'Easy', duration:'50 min', xp:50 },
      { id:10, title:'Editing & Proofreading',     topics:['Common Errors','Sentence Correction','Editing Exercises'], difficulty:'Medium', duration:'60 min', xp:75 }
    ]
  }
};

export function getSubject(id) { return SUBJECTS[id] || SUBJECTS.math; }
export function getAllSubjects() { return Object.values(SUBJECTS); }
export function getChapter(subjectId, chapterId) {
  const sub = getSubject(subjectId);
  return sub.chapters.find(c => c.id === chapterId) || null;
}
export function getCompletedChapters(subjectId) {
  return JSON.parse(localStorage.getItem(`lvlbase_chapters_${subjectId}`) || '[]');
}
export function markChapterComplete(subjectId, chapterId) {
  const completed = getCompletedChapters(subjectId);
  if (!completed.includes(chapterId)) completed.push(chapterId);
  localStorage.setItem(`lvlbase_chapters_${subjectId}`, JSON.stringify(completed));
  return completed;
}

export default { SUBJECTS, getSubject, getAllSubjects, getChapter, getCompletedChapters, markChapterComplete };
