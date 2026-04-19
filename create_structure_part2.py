import os

BASE = '/home/runner/work/lvlBase/lvlBase'

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f'Created: {path}')

# ===== CORE JS FILES =====

router_js = '''/**
 * lvlBase SPA Router
 * Handles client-side routing with history API and role-based guards
 */
const Router = (() => {
  const routes = {};
  const guards = [];
  let currentRoute = null;

  function register(path, handler, options = {}) {
    routes[path] = { handler, options };
  }

  function addGuard(guardFn) {
    guards.push(guardFn);
  }

  async function navigate(path, state = {}) {
    for (const guard of guards) {
      const result = await guard(path, currentRoute);
      if (result === false) return;
      if (typeof result === 'string') {
        return navigate(result);
      }
    }
    const route = matchRoute(path);
    if (!route) {
      console.warn('[Router] No route for:', path);
      return;
    }
    history.pushState(state, '', path);
    currentRoute = path;
    route.handler(state);
  }

  function matchRoute(path) {
    if (routes[path]) return routes[path];
    for (const [pattern, route] of Object.entries(routes)) {
      if (pattern.includes(':')) {
        const regex = new RegExp('^' + pattern.replace(/:[^/]+/g, '([^/]+)') + '$');
        if (regex.test(path)) return route;
      }
    }
    return null;
  }

  function addRoleGuard(allowedRoles) {
    addGuard(async (path) => {
      const user = window.currentUser;
      if (!user) return '/auth/portal-login.html';
      if (allowedRoles.length && !allowedRoles.includes(user.role)) {
        return '/app/student/dashboard.html';
      }
      return true;
    });
  }

  window.addEventListener('popstate', (e) => {
    const route = matchRoute(location.pathname);
    if (route) route.handler(e.state || {});
  });

  return { register, addGuard, addRoleGuard, navigate, current: () => currentRoute };
})();

window.Router = Router;
'''
write_file('core/js/core/router.js', router_js)

bento_drag_js = '''/**
 * lvlBase Bento Grid Drag & Drop
 * Enables drag-and-drop reordering of bento grid items
 */
const BentoDrag = (() => {
  let dragSrc = null;

  function init(gridSelector = '.bento-grid') {
    const grids = document.querySelectorAll(gridSelector);
    grids.forEach(grid => enableGrid(grid));
  }

  function enableGrid(grid) {
    const items = grid.querySelectorAll('.bento-item, .bento-card');
    items.forEach(item => {
      item.setAttribute('draggable', 'true');
      item.addEventListener('dragstart', onDragStart);
      item.addEventListener('dragover', onDragOver);
      item.addEventListener('drop', onDrop);
      item.addEventListener('dragend', onDragEnd);
      item.addEventListener('dragenter', onDragEnter);
      item.addEventListener('dragleave', onDragLeave);
    });
  }

  function onDragStart(e) {
    dragSrc = this;
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.outerHTML);
    this.classList.add('dragging');
    setTimeout(() => this.style.opacity = '0.4', 0);
  }

  function onDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    return false;
  }

  function onDragEnter(e) {
    this.classList.add('drag-over');
  }

  function onDragLeave(e) {
    this.classList.remove('drag-over');
  }

  function onDrop(e) {
    e.stopPropagation();
    if (dragSrc !== this) {
      const srcHTML = dragSrc.innerHTML;
      const dstHTML = this.innerHTML;
      dragSrc.innerHTML = dstHTML;
      this.innerHTML = srcHTML;
      const saved = JSON.parse(localStorage.getItem('bentoLayout') || '{}');
      saved[this.closest('.bento-grid')?.id || 'default'] = serializeLayout(this.closest('.bento-grid'));
      localStorage.setItem('bentoLayout', JSON.stringify(saved));
    }
    this.classList.remove('drag-over');
    return false;
  }

  function onDragEnd(e) {
    document.querySelectorAll('.dragging, .drag-over').forEach(el => {
      el.classList.remove('dragging', 'drag-over');
      el.style.opacity = '';
    });
    dragSrc = null;
  }

  function serializeLayout(grid) {
    if (!grid) return [];
    return [...grid.querySelectorAll('[data-widget-id]')].map(el => el.dataset.widgetId);
  }

  return { init, enableGrid };
})();

document.addEventListener('DOMContentLoaded', () => BentoDrag.init());
window.BentoDrag = BentoDrag;
'''
write_file('core/js/features/bento-drag.js', bento_drag_js)

webrtc_js = '''/**
 * lvlBase WebRTC Utility
 * Handles real-time peer connections for battles, proctoring, and collaboration
 */
const LvlRTC = (() => {
  const peers = {};
  const config = {
    iceServers: [
      { urls: 'stun:stun.l.google.com:19302' },
      { urls: 'stun:stun1.l.google.com:19302' }
    ]
  };

  async function createPeer(peerId, isInitiator = false) {
    const pc = new RTCPeerConnection(config);
    peers[peerId] = pc;

    pc.onicecandidate = (e) => {
      if (e.candidate) {
        window.dispatchEvent(new CustomEvent('rtc:ice', { detail: { peerId, candidate: e.candidate } }));
      }
    };

    pc.ontrack = (e) => {
      window.dispatchEvent(new CustomEvent('rtc:track', { detail: { peerId, streams: e.streams } }));
    };

    pc.onconnectionstatechange = () => {
      window.dispatchEvent(new CustomEvent('rtc:state', { detail: { peerId, state: pc.connectionState } }));
    };

    if (isInitiator) {
      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);
      window.dispatchEvent(new CustomEvent('rtc:offer', { detail: { peerId, offer } }));
    }

    return pc;
  }

  async function addStream(peerId, stream) {
    const pc = peers[peerId];
    if (!pc) return;
    stream.getTracks().forEach(track => pc.addTrack(track, stream));
  }

  async function handleOffer(peerId, offer) {
    const pc = await createPeer(peerId, false);
    await pc.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await pc.createAnswer();
    await pc.setLocalDescription(answer);
    window.dispatchEvent(new CustomEvent('rtc:answer', { detail: { peerId, answer } }));
    return pc;
  }

  async function handleAnswer(peerId, answer) {
    const pc = peers[peerId];
    if (pc) await pc.setRemoteDescription(new RTCSessionDescription(answer));
  }

  async function handleIce(peerId, candidate) {
    const pc = peers[peerId];
    if (pc) await pc.addIceCandidate(new RTCIceCandidate(candidate));
  }

  async function getUserMedia(video = true, audio = true) {
    return navigator.mediaDevices.getUserMedia({ video, audio });
  }

  async function getDisplayMedia() {
    return navigator.mediaDevices.getDisplayMedia({ video: true });
  }

  function closePeer(peerId) {
    if (peers[peerId]) {
      peers[peerId].close();
      delete peers[peerId];
    }
  }

  function closeAll() {
    Object.keys(peers).forEach(closePeer);
  }

  return { createPeer, addStream, handleOffer, handleAnswer, handleIce, getUserMedia, getDisplayMedia, closePeer, closeAll };
})();

window.LvlRTC = LvlRTC;
'''
write_file('core/js/features/webrtc.js', webrtc_js)

print("JS files created")
