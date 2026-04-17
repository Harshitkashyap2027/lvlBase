// ===== AI ASSISTANT MODULE =====

const RESPONSES = {
  greeting: ["Hello, Champion! 👋 I'm Sage, your AI study companion. Ask me anything!", "Hey! ⚡ Ready to level up your knowledge today?"],
  math: "Great math question! 📐\n\n**Key Tips:**\n• Show every step for full marks\n• Isolate variables in algebra\n• Draw diagrams for geometry\n• Use BODMAS: Brackets, Orders, Division, Multiplication, Addition, Subtraction\n\nWhich topic? (algebra, geometry, trigonometry, statistics?)",
  math_algebra: "**Algebra Fundamentals** 📊\n\n**Golden Rule:** Whatever you do to one side, do to the other!\n\n**Example:** 2x + 5 = 13\n→ 2x = 8\n→ x = **4** ✅\n\n**Steps:**\n1. Identify the variable\n2. Move constants to one side\n3. Divide/multiply to isolate x\n4. Verify by substituting back",
  math_geometry: "**Geometry Essentials** 📐\n\n**Key Formulas:**\n• Circle: Area = πr², Perimeter = 2πr\n• Rectangle: Area = l×w, Perimeter = 2(l+w)\n• Triangle: Area = ½×b×h\n• Sum of angles = 180°\n• Pythagorean: a² + b² = c²\n\n**Pro Tip:** Always draw and label a diagram first! 🎨",
  science: "Science has three amazing branches! 🔬\n\n• **Biology** 🧬 – Life and living organisms\n• **Chemistry** ⚗️ – Matter and reactions\n• **Physics** ⚡ – Forces and energy\n\nWhich branch needs attention?",
  science_biology: "**Biology Key Concepts** 🧬\n\n**Cell Organelles:**\n• Nucleus: Control center (DNA)\n• Mitochondria: Powerhouse (ATP)\n• Ribosomes: Protein synthesis\n\n**Photosynthesis:**\n6CO₂ + 6H₂O + Light → C₆H₁₂O₆ + 6O₂\n\n**Mnemonic for kingdoms:** *Kings Play Chess On Fine Green Silk* 🌱",
  science_chemistry: "**Chemistry** ⚗️\n\n**Key Concepts:**\n• Periodic Table: Groups = valence electrons\n• Acid + Base → Salt + Water\n• Balancing: Add coefficients, NOT subscripts!\n• pH < 7 = Acid, pH > 7 = Base\n\n**Tip:** Always check units and balance both sides! ⚖️",
  science_physics: "**Physics Core** ⚡\n\n**Newton's Laws:**\n1. Inertia – Objects stay at rest/motion unless acted upon\n2. **F = ma** (Force = mass × acceleration)\n3. Action = Reaction\n\n**Key Formulas:**\n• Speed = Distance ÷ Time\n• KE = ½mv²\n• V = IR (Ohm's Law)\n\n**Tip:** Check units first – they guide formula selection! 🔭",
  english: "English opens every door! 📚\n\n**Four Areas:**\n• **Reading** – Comprehension & inference\n• **Writing** – Essays, letters, reports\n• **Grammar** – Rules for correctness\n• **Literature** – Analyzing text & poetry\n\nWhich area to focus on?",
  english_grammar: "**English Grammar** ✍️\n\n**Common Mistakes:**\n• Your vs **You're** (possessive vs 'you are')\n• Their/There/**They're**\n• Its vs **It's**\n\n**Tenses:** Simple (I go) → Continuous (I am going) → Perfect (I have gone)\n\n**Sentence structure:** Subject + Verb + Object ✅",
  english_literature: "**Literature Analysis** 📖\n\n**Literary Devices:**\n• Simile: 'brave *as* a lion'\n• Metaphor: 'life *is* a journey'\n• Personification: Non-human gets human traits\n• Alliteration: Peter Piper Picked...\n\n**Essay: PEEL Method:**\n**P**oint → **E**vidence → **E**xplain → **L**ink 🎭",
  study_tips: "**Ultimate Study Guide** 📚⚡\n\n**Pomodoro Technique:**\n• 25 min focus → 5 min break (×4)\n• Then 15-30 min long break\n\n**Active Recall** (50% more effective than re-reading!):\n• Close book → write what you remember\n• Use flashcards and self-quizzes\n\n**Spaced Repetition:** Review on Day 1→3→7→21\n\n🧠 **Best study time: 1-2 hours after waking!**",
  rank: "**Ranking System** 🏆\n\n• ⚫ **E-Rank** – 0 XP (Start)\n• 🟢 **D-Rank** – 500 XP\n• 🔵 **C-Rank** – 1,500 XP\n• 🟣 **B-Rank** – 3,500 XP\n• 🟡 **A-Rank** – 7,000 XP\n• 🔴 **S-Rank** – 15,000 XP\n• ⭐ **SS-Rank** – 30,000 XP\n\n**Earn XP:** Correct answers +10, Perfect quiz +50, Battle win +75, Daily login +20 🔥",
  battle: "**Battle Strategy** ⚔️\n\n**Tips:**\n1. Answer quickly = bonus damage\n2. Perfect streak multiplies damage\n3. Start with weaker opponents\n4. Use your guild's specialty subject\n5. Practice quizzes before battles!\n\n**Difficulty:** Easy → Intermediate → Hard → Boss 🎯",
  guild: "**Guild System** 🏰\n\n• 🌙 **Shadow Guild:** +15% Math XP\n• 💧 **Azure Order:** +15% Science XP\n• 🔥 **Inferno Legion:** +20% Battle XP\n• ⚡ **Titan Brotherhood:** +15% English XP\n• ✨ **Zenith Circle:** +10% All XP\n\n**Tip:** Choose based on your strongest subject! Change every 30 days. 🎯",
  fallback: ["That's interesting! 🤔 I specialize in:\n• 📐 **Mathematics**\n• 🔬 **Science**\n• 📚 **English**\n• 🎯 **Study strategies**\n• ⚔️ **Battle tips**\n\nCould you be more specific?", "Let me help you better! Try: 'Explain photosynthesis' or 'How to solve quadratics?' 💭"]
};

export function detectTopic(message) {
  const m = message.toLowerCase();
  if (['hello','hi','hey','howdy','greetings'].some(g => m.includes(g))) return 'greeting';
  if (m.includes('algebra') || m.includes('equation') || m.includes('variable')) return 'math_algebra';
  if (m.includes('geometry') || m.includes('triangle') || m.includes('circle') || m.includes('area')) return 'math_geometry';
  if (m.includes('biology') || m.includes('cell') || m.includes('photosynthesis') || m.includes('dna')) return 'science_biology';
  if (m.includes('chemistry') || m.includes('atom') || m.includes('periodic') || m.includes('reaction')) return 'science_chemistry';
  if (m.includes('physics') || m.includes('force') || m.includes('newton') || m.includes('energy')) return 'science_physics';
  if (m.includes('grammar') || m.includes('tense') || m.includes('verb') || m.includes('noun')) return 'english_grammar';
  if (m.includes('literature') || m.includes('poem') || m.includes('novel') || m.includes('metaphor')) return 'english_literature';
  if (m.includes('math') || m.includes('calculus') || m.includes('trigonometry')) return 'math';
  if (m.includes('science') || m.includes('chemical')) return 'science';
  if (m.includes('english') || m.includes('writing') || m.includes('vocabulary')) return 'english';
  if (m.includes('study') || m.includes('tip') || m.includes('focus') || m.includes('exam')) return 'study_tips';
  if (m.includes('rank') || m.includes('xp') || m.includes('level')) return 'rank';
  if (m.includes('battle') || m.includes('fight') || m.includes('duel')) return 'battle';
  if (m.includes('guild') || m.includes('shadow') || m.includes('azure') || m.includes('inferno')) return 'guild';
  return 'fallback';
}

export function getResponse(message) {
  const topic = detectTopic(message);
  const r = RESPONSES[topic];
  if (!r) return Array.isArray(RESPONSES.fallback) ? RESPONSES.fallback[0] : RESPONSES.fallback;
  if (Array.isArray(r)) return r[Math.floor(Math.random() * r.length)];
  return r;
}

export function formatMessage(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\n/g, '<br>')
    .replace(/• /g, '&bull; ');
}

export function addTypingDelay(message) {
  return new Promise(resolve => setTimeout(() => resolve(getResponse(message)), 600 + Math.random() * 800));
}

export default { detectTopic, getResponse, formatMessage, addTypingDelay, RESPONSES };
