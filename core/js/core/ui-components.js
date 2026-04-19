// ===== BENTO POPUP SYSTEM =====
// iPhone Bento-style custom popups & toasts

(function () {
  // Inject styles once
  if (!document.getElementById('popup-styles')) {
    const style = document.createElement('style');
    style.id = 'popup-styles';
    style.textContent = `
      /* ── Overlay ── */
      .lp-overlay {
        position: fixed; inset: 0; z-index: 99990;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        display: flex; align-items: center; justify-content: center;
        padding: 1.5rem;
        opacity: 0; transition: opacity 0.25s ease;
      }
      .lp-overlay.lp-open { opacity: 1; }

      /* ── Bento Card ── */
      .lp-card {
        background: rgba(26,26,46,0.98);
        border: 1px solid rgba(108,99,255,0.25);
        border-radius: 28px;
        padding: 2rem 1.75rem;
        max-width: 400px;
        width: 100%;
        text-align: center;
        box-shadow: 0 24px 80px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04) inset;
        transform: scale(0.88) translateY(20px);
        transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), opacity 0.25s ease;
        opacity: 0;
      }
      .lp-overlay.lp-open .lp-card { transform: scale(1) translateY(0); opacity: 1; }

      /* Types */
      .lp-card.lp-success { border-color: rgba(0,209,178,0.4); }
      .lp-card.lp-error   { border-color: rgba(255,68,68,0.4); }
      .lp-card.lp-warning { border-color: rgba(255,165,0,0.4); }
      .lp-card.lp-info    { border-color: rgba(108,99,255,0.4); }

      /* Icon pill */
      .lp-icon-wrap {
        width: 72px; height: 72px; border-radius: 22px;
        display: flex; align-items: center; justify-content: center;
        font-size: 2.2rem; margin: 0 auto 1.25rem;
      }
      .lp-success .lp-icon-wrap { background: rgba(0,209,178,0.15); }
      .lp-error   .lp-icon-wrap { background: rgba(255,68,68,0.15); }
      .lp-warning .lp-icon-wrap { background: rgba(255,165,0,0.15); }
      .lp-info    .lp-icon-wrap { background: rgba(108,99,255,0.15); }

      .lp-title {
        font-family: 'Poppins', system-ui, sans-serif;
        font-size: 1.2rem; font-weight: 800;
        color: #E8E8FF; margin-bottom: 0.6rem; line-height: 1.3;
      }
      .lp-message {
        font-family: 'Poppins', system-ui, sans-serif;
        font-size: 0.9rem; color: #8892A4; line-height: 1.65;
        margin-bottom: 1.5rem;
      }
      .lp-actions { display: flex; flex-direction: column; gap: 0.6rem; }
      .lp-btn {
        width: 100%; padding: 0.82rem 1.2rem;
        border: none; border-radius: 14px;
        font-family: 'Poppins', system-ui, sans-serif;
        font-size: 0.92rem; font-weight: 700;
        cursor: pointer; transition: all 0.2s ease;
        text-decoration: none; display: block;
      }
      .lp-btn:hover { transform: translateY(-1px); filter: brightness(1.1); }
      .lp-btn:active { transform: scale(0.97); }
      .lp-btn-primary   { background: linear-gradient(135deg,#6C63FF,#8B85FF); color: #fff; }
      .lp-btn-success   { background: linear-gradient(135deg,#00D1B2,#00B89C); color: #fff; }
      .lp-btn-danger    { background: linear-gradient(135deg,#FF4444,#FF6B6B); color: #fff; }
      .lp-btn-warning   { background: linear-gradient(135deg,#FFA500,#FFD700); color: #1A1A2E; }
      .lp-btn-whatsapp  { background: linear-gradient(135deg,#25D366,#128C7E); color: #fff; }
      .lp-btn-ghost {
        background: rgba(255,255,255,0.06);
        color: #8892A4;
        border: 1px solid rgba(255,255,255,0.1);
      }

      /* ── Toast Bento ── */
      .lp-toast-container {
        position: fixed; bottom: 1.5rem; right: 1.5rem;
        z-index: 99999; display: flex; flex-direction: column-reverse; gap: 0.6rem;
        pointer-events: none;
      }
      .lp-toast {
        background: rgba(26,26,46,0.98);
        border: 1px solid rgba(108,99,255,0.25);
        border-radius: 18px;
        padding: 0.85rem 1.1rem;
        display: flex; align-items: center; gap: 0.75rem;
        font-family: 'Poppins', system-ui, sans-serif;
        font-size: 0.88rem; color: #E8E8FF;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        max-width: 340px;
        pointer-events: all;
        transform: translateX(120%);
        transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1), opacity 0.3s;
        opacity: 0;
      }
      .lp-toast.lp-toast-show { transform: translateX(0); opacity: 1; }
      .lp-toast.lp-toast-hide { transform: translateX(120%); opacity: 0; }
      .lp-toast-icon { font-size: 1.3rem; flex-shrink: 0; }
      .lp-toast-msg { flex: 1; line-height: 1.4; }
      .lp-toast.lp-success { border-color: rgba(0,209,178,0.4); }
      .lp-toast.lp-error   { border-color: rgba(255,68,68,0.4); }
      .lp-toast.lp-warning { border-color: rgba(255,165,0,0.4); }
      .lp-toast.lp-info    { border-color: rgba(108,99,255,0.4); }

      /* warning overlay */
      .lp-card.lp-full-warning {
        max-width: 480px;
        border-color: rgba(255,68,68,0.5);
        background: linear-gradient(135deg, rgba(255,68,68,0.07), rgba(26,26,46,0.98));
      }
    `;
    document.head.appendChild(style);
  }

  // Ensure toast container
  function getToastContainer() {
    let c = document.getElementById('lp-toast-container');
    if (!c) {
      c = document.createElement('div');
      c.id = 'lp-toast-container';
      c.className = 'lp-toast-container';
      document.body.appendChild(c);
    }
    return c;
  }

  // ── Toast ──
  window.lvlPopup = window.lvlPopup || {};

  window.lvlPopup.toast = function (message, type = 'info', duration = 3500) {
    const icons = { success: '✅', error: '❌', warning: '⚠️', info: 'ℹ️' };
    const container = getToastContainer();
    const toast = document.createElement('div');
    toast.className = `lp-toast lp-${type}`;
    // Use textContent for the message to prevent XSS from user-supplied strings
    const iconEl = document.createElement('span');
    iconEl.className = 'lp-toast-icon';
    iconEl.textContent = icons[type] || 'ℹ️';
    const msgEl = document.createElement('span');
    msgEl.className = 'lp-toast-msg';
    msgEl.textContent = message;
    toast.appendChild(iconEl);
    toast.appendChild(msgEl);
    container.appendChild(toast);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => toast.classList.add('lp-toast-show'));
    });
    setTimeout(() => {
      toast.classList.add('lp-toast-hide');
      setTimeout(() => toast.remove(), 400);
    }, duration);
  };

  // ── Modal ──
  // options: { type, icon, title, message, buttons: [{label, style, action, href}], dismissable }
  window.lvlPopup.show = function (options) {
    return new Promise((resolve) => {
      const overlay = document.createElement('div');
      overlay.className = 'lp-overlay';

      const typeClass = options.type || 'info';

      // Build buttons HTML – button labels are developer-supplied strings only
      const buttons = options.buttons || [{ label: 'OK', style: 'primary', action: 'close' }];
      const escAttr = s => String(s || '').replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
      const btnsHtml = buttons.map(btn => {
        if (btn.href) {
          return `<a href="${escAttr(btn.href)}" class="lp-btn lp-btn-${escAttr(btn.style || 'primary')}" target="${escAttr(btn.target || '_self')}">${escAttr(btn.label)}</a>`;
        }
        return `<button class="lp-btn lp-btn-${escAttr(btn.style || 'primary')}" data-action="${escAttr(btn.action || 'close')}">${escAttr(btn.label)}</button>`;
      }).join('');

      // The icon, title, and message are developer-supplied strings.
      // title and message support intentional HTML markup (e.g. <strong>, <br>).
      // Callers must NOT pass raw user-supplied data here without escaping it first.
      const safeIcon = escAttr(options.icon || (typeClass === 'success' ? '✅' : typeClass === 'error' ? '❌' : typeClass === 'warning' ? '⚠️' : 'ℹ️'));
      const safeTypeClass = escAttr(typeClass);
      const safeExtraClass = escAttr(options.extraClass || '');
      overlay.innerHTML = `
        <div class="lp-card lp-${safeTypeClass} ${safeExtraClass}">
          <div class="lp-icon-wrap">${safeIcon}</div>
          <div class="lp-title">${options.title || ''}</div>
          <div class="lp-message">${options.message || ''}</div>
          <div class="lp-actions">${btnsHtml}</div>
        </div>
      `;

      document.body.appendChild(overlay);
      requestAnimationFrame(() => {
        requestAnimationFrame(() => overlay.classList.add('lp-open'));
      });

      function closeModal(result) {
        overlay.classList.remove('lp-open');
        setTimeout(() => overlay.remove(), 300);
        resolve(result);
      }

      // Button click handling
      overlay.querySelectorAll('.lp-btn[data-action]').forEach(btn => {
        btn.addEventListener('click', () => {
          const action = btn.getAttribute('data-action');
          closeModal(action);
        });
      });

      // Dismiss on overlay click
      if (options.dismissable !== false) {
        overlay.addEventListener('click', (e) => {
          if (e.target === overlay) closeModal('dismiss');
        });
      }
    });
  };

  // ── Confirm helper ──
  window.lvlPopup.confirm = function (title, message, options = {}) {
    return window.lvlPopup.show({
      type: options.type || 'warning',
      icon: options.icon || '❓',
      title,
      message,
      buttons: [
        { label: options.cancelLabel || 'Cancel', style: 'ghost', action: 'cancel' },
        { label: options.confirmLabel || 'Confirm', style: options.confirmStyle || 'primary', action: 'confirm' }
      ]
    }).then(r => r === 'confirm');
  };

  // ── Alert helper ──
  window.lvlPopup.alert = function (title, message, type = 'info', icon) {
    return window.lvlPopup.show({ type, icon, title, message });
  };

  // ── Pending Verification popup (school dashboard) ──
  window.lvlPopup.schoolPending = function (schoolData) {
    const whatsappMsg = `Hello Admin,\n\nNew School Registration Request:\n\n🏫 School Name: ${schoolData.name}\n👤 Principal: ${schoolData.principal}\n📍 Address: ${schoolData.address}, ${schoolData.city}, ${schoolData.state} - ${schoolData.pincode}\n📞 Phone: ${schoolData.phone}\n📧 Email: ${schoolData.email}\n🌐 Website: ${schoolData.website || 'N/A'}\n👨‍🎓 Students: ${schoolData.totalStudents || 'N/A'}\n\nPlease verify this school on the admin panel.\n\nThank you!`;
    const waLink = `https://wa.me/919258837596?text=${encodeURIComponent(whatsappMsg)}`;

    return window.lvlPopup.show({
      type: 'warning',
      icon: '⏳',
      title: 'Pending Admin Verification',
      message: `Your school <strong style="color:#E8E8FF">${schoolData.name}</strong> is awaiting verification from the platform admin.<br><br>All dashboard features are locked until verified. Tap the WhatsApp button below to contact the admin directly and speed up the process.`,
      dismissable: false,
      buttons: [
        { label: '💬 Message Admin on WhatsApp', style: 'whatsapp', href: waLink, target: '_blank' },
        { label: 'Close & Wait', style: 'ghost', action: 'close' }
      ]
    });
  };

  // ── Cheating warning popup ──
  window.lvlPopup.cheatWarning = function (warningNumber, isTerminal) {
    if (isTerminal) {
      return window.lvlPopup.show({
        type: 'error',
        icon: '🚫',
        title: 'Exam Terminated',
        message: 'You have been caught cheating twice. This exam has been ended automatically. A report has been sent to your parents and teachers. You cannot retake this exam until your school or teacher takes action.',
        dismissable: false,
        buttons: [
          { label: 'Go to Dashboard', style: 'danger', action: 'exit' }
        ]
      });
    }
    return window.lvlPopup.show({
      type: 'warning',
      icon: '⚠️',
      title: `Cheating Warning ${warningNumber}/2`,
      message: `You have been flagged for suspicious activity (tab switch / copy-paste detected). This is warning <strong>${warningNumber} of 2</strong>. A second warning will terminate your exam and notify your parents.`,
      dismissable: false,
      buttons: [
        { label: `Understood – Resume Exam`, style: 'warning', action: 'resume' }
      ]
    });
  };

  // ── Service Worker auto-registration ──
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      // Detect root path (for pages in subdirectories like /admin/)
      const swPath = window.location.pathname.includes('/admin/') ? '/sw.js' : 'sw.js';
      navigator.serviceWorker.register(swPath).catch(function () {});
    });
  }

})();
