// ===== VOICE AI MODULE =====
// Full Web Speech API integration: speech recognition (STT) + speech synthesis (TTS)

// ── Speech Recognition (STT) ──────────────────────────────────────────────────

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

export const STT_SUPPORTED = !!SpeechRecognition;

let recognition = null;
let isListening  = false;

/**
 * Start listening for voice input.
 * @param {object} options
 * @param {function} options.onResult  - called with final transcript string
 * @param {function} options.onInterim - called with interim transcript string
 * @param {function} options.onError   - called with error event
 * @param {function} options.onEnd     - called when recognition stops
 * @param {string}   options.lang      - BCP-47 language tag (default 'en-US')
 */
export function startListening({ onResult, onInterim, onError, onEnd, lang = 'en-US' } = {}) {
  if (!STT_SUPPORTED) {
    onError && onError({ message: 'Speech recognition not supported in this browser.' });
    return;
  }
  if (isListening) stopListening();

  recognition = new SpeechRecognition();
  recognition.continuous     = false;
  recognition.interimResults = true;
  recognition.lang           = lang;
  recognition.maxAlternatives = 1;

  recognition.onresult = (event) => {
    let interim = '';
    let final   = '';
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const t = event.results[i][0].transcript;
      if (event.results[i].isFinal) final += t;
      else interim += t;
    }
    if (interim && onInterim) onInterim(interim);
    if (final   && onResult)  onResult(final.trim());
  };

  recognition.onerror = (event) => {
    isListening = false;
    onError && onError(event);
  };

  recognition.onend = () => {
    isListening = false;
    onEnd && onEnd();
  };

  recognition.start();
  isListening = true;
}

/** Stop the active speech recognition session. */
export function stopListening() {
  if (recognition && isListening) {
    recognition.stop();
    isListening = false;
  }
}

export function getIsListening() { return isListening; }

// ── Speech Synthesis (TTS) ────────────────────────────────────────────────────

export const TTS_SUPPORTED = 'speechSynthesis' in window;

let currentUtterance = null;
let ttsEnabled = true;

/** Enable or disable TTS globally. */
export function setTTSEnabled(val) { ttsEnabled = !!val; }
export function getTTSEnabled()    { return ttsEnabled; }

/**
 * Speak the given text.
 * @param {string} text       - Plain text (HTML tags stripped automatically)
 * @param {object} [options]
 * @param {number} options.rate   - Speed (0.5–2, default 0.95)
 * @param {number} options.pitch  - Pitch (0–2, default 1)
 * @param {string} options.lang   - BCP-47 tag (default 'en-US')
 * @param {function} options.onEnd - called when speech finishes
 */
export function speak(text, { rate = 0.95, pitch = 1, lang = 'en-US', onEnd } = {}) {
  if (!TTS_SUPPORTED || !ttsEnabled) { onEnd && onEnd(); return; }
  stopSpeaking();

  // Convert text to speech-friendly plain text without using DOM APIs
  // (output goes to SpeechSynthesisUtterance only — not a DOM sink)
  const plain = text
    .replace(/\*\*(.+?)\*\*/g, '$1')          // strip markdown bold
    .replace(/<br\s*\/?>/gi, ' ')              // <br> → space
    .replace(/<\/(?:p|div|li|h[1-6])>/gi, '. ') // block end → period+space
    .replace(/<[^>]+>/g, '')                   // strip remaining tags
    .replace(/&amp;/gi, '&').replace(/&lt;/gi, '').replace(/&gt;/gi, '')
    .replace(/&[a-z]+;/gi, ' ')               // strip other entities
    .replace(/\s{2,}/g, ' ')
    .trim();
  if (!plain) { onEnd && onEnd(); return; }

  currentUtterance = new SpeechSynthesisUtterance(plain);
  currentUtterance.rate  = rate;
  currentUtterance.pitch = pitch;
  currentUtterance.lang  = lang;

  // Pick a female English voice if available
  const voices = window.speechSynthesis.getVoices();
  const preferred = voices.find(v => v.lang.startsWith('en') && /female|woman|girl/i.test(v.name))
    || voices.find(v => v.lang.startsWith('en'))
    || null;
  if (preferred) currentUtterance.voice = preferred;

  if (onEnd) currentUtterance.onend = onEnd;
  window.speechSynthesis.speak(currentUtterance);
}

/** Cancel any ongoing speech. */
export function stopSpeaking() {
  if (TTS_SUPPORTED) window.speechSynthesis.cancel();
  currentUtterance = null;
}

export function getIsSpeaking() {
  return TTS_SUPPORTED && window.speechSynthesis.speaking;
}

export default { STT_SUPPORTED, TTS_SUPPORTED, startListening, stopListening, getIsListening, speak, stopSpeaking, getIsSpeaking, setTTSEnabled, getTTSEnabled };
