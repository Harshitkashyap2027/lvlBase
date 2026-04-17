// ===== LIVE GUILD WARS MODULE =====
// Real-time guild battle system.
// Uses BroadcastChannel for cross-tab/same-origin demo.
// Swap `openChannel()` for a real WebSocket when a backend is available.

const CHANNEL_NAME = 'lvlbase_guild_wars';

let bc = null;
let handlers = {};

// ── Channel helpers ────────────────────────────────────────────────────────

/** Open the communication channel. */
export function openChannel() {
  if (typeof BroadcastChannel === 'undefined') return;
  if (bc) return; // already open
  bc = new BroadcastChannel(CHANNEL_NAME);
  bc.onmessage = (event) => {
    const { type, payload } = event.data || {};
    if (type && handlers[type]) handlers[type](payload);
    if (handlers['*']) handlers['*'](event.data);
  };
}

/** Close the channel. */
export function closeChannel() {
  if (bc) { bc.close(); bc = null; }
}

/** Register a handler for a specific message type. Use '*' to catch all. */
export function on(type, handler) {
  handlers[type] = handler;
}

/** Remove a handler. */
export function off(type) {
  delete handlers[type];
}

/** Broadcast a message to all connected tabs / clients. */
export function broadcast(type, payload) {
  if (!bc) return;
  bc.postMessage({ type, payload, ts: Date.now() });
}

// ── Guild war state ────────────────────────────────────────────────────────

export const GUILD_WAR_EVENTS = {
  PLAYER_JOIN:    'player_join',
  PLAYER_LEAVE:   'player_leave',
  QUESTION_START: 'question_start',
  ANSWER_SUBMIT:  'answer_submit',
  ROUND_RESULT:   'round_result',
  GUILD_ATTACK:   'guild_attack',
  GAME_END:       'game_end',
  CHAT_MSG:       'chat_msg',
  HP_UPDATE:      'hp_update'
};

// ── Player / room helpers ──────────────────────────────────────────────────

let _room = null;
let _player = null;

export function createRoom(guildId, subject = 'mixed') {
  _room = {
    id: 'room_' + Date.now(),
    guildId,
    subject,
    round: 0,
    maxRounds: 10,
    state: 'waiting', // waiting | in_progress | ended
    guilds: {},
    players: {},
    chat: []
  };
  return _room;
}

export function getRoom() { return _room; }

export function joinRoom(room, profile) {
  _room = room;
  _player = { uid: profile.uid, name: profile.displayName, guild: profile.guild, xp: profile.totalXP, hp: 100 };
  broadcast(GUILD_WAR_EVENTS.PLAYER_JOIN, { player: _player, roomId: _room.id });
  return _player;
}

export function leaveRoom() {
  if (_player && _room) broadcast(GUILD_WAR_EVENTS.PLAYER_LEAVE, { uid: _player.uid, roomId: _room?.id });
  _room = null;
  _player = null;
}

export function submitAnswer(questionIndex, answerIndex, timeMs) {
  if (!_player || !_room) return;
  broadcast(GUILD_WAR_EVENTS.ANSWER_SUBMIT, {
    uid: _player.uid, guild: _player.guild, questionIndex, answerIndex, timeMs, roomId: _room.id
  });
}

export function sendChatMessage(text) {
  if (!_player) return;
  broadcast(GUILD_WAR_EVENTS.CHAT_MSG, { name: _player.name, guild: _player.guild, text, ts: Date.now() });
}

// ── AI opponent logic ──────────────────────────────────────────────────────

const AI_GUILDS = [
  { id: 'shadow', name: 'Shadow Guild', emoji: '🌙', strength: 80 },
  { id: 'azure',  name: 'Azure Order',  emoji: '💧', strength: 75 },
  { id: 'inferno',name: 'Inferno Legion',emoji: '🔥', strength: 90 }
];

export function getAIOpponent(excludeGuildId) {
  const choices = AI_GUILDS.filter(g => g.id !== excludeGuildId);
  return choices[Math.floor(Math.random() * choices.length)];
}

/**
 * Simulate an AI guild answering a question.
 * Returns the answer index and response time in ms.
 */
export function simulateAIAnswer(question, strength = 75) {
  const correct = question.ans;
  const hits = Math.random() * 100 < strength;
  const answer = hits ? correct : Math.floor(Math.random() * question.opts.length);
  const timeMs = 800 + Math.random() * (hits ? 3000 : 2000);
  return { answer, timeMs };
}

export default { openChannel, closeChannel, on, off, broadcast, GUILD_WAR_EVENTS,
                 createRoom, getRoom, joinRoom, leaveRoom, submitAnswer, sendChatMessage,
                 getAIOpponent, simulateAIAnswer };
