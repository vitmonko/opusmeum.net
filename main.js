document.getElementById('year').textContent = new Date().getFullYear();

// "Copy email address" button: handy for people who write from webmail.
const copyButton = document.querySelector('.copy-email');
if (copyButton) {
  if (navigator.clipboard) {
    const label = copyButton.textContent;
    copyButton.addEventListener('click', () => {
      navigator.clipboard.writeText(copyButton.dataset.email).then(() => {
        copyButton.textContent = copyButton.dataset.done;
        setTimeout(() => { copyButton.textContent = label; }, 2500);
      });
    });
  } else {
    copyButton.hidden = true;
  }
}

// Copilot readiness check promo: a small card that slides in after a few seconds or
// once the visitor scrolls. Not modal, closes with the X or Escape, and stays hidden for
// 14 days after closing (60 days after opening the check).
(() => {
  const BASE = 'https://vitmonko.github.io/opusmeum.ai/';
  const TEXT = {
    en: { title: 'Is your Microsoft 365 ready for Copilot?',
          body: 'Answer 15 questions in about five minutes and see what to fix first.',
          cta: 'Start the readiness check', close: 'Close', url: BASE + 'copilot-readiness/' },
    lt: { title: 'Ar jūsų Microsoft 365 aplinka pasirengusi Copilot?',
          body: 'Atsakykite į 15 klausimų per maždaug penkias minutes ir sužinokite, ką sutvarkyti pirmiausia.',
          cta: 'Pradėti patikrinimą', close: 'Uždaryti', url: BASE + 'lt/copilot-readiness/' },
    de: { title: 'Ist Ihr Microsoft 365 bereit für Copilot?',
          body: 'Beantworten Sie 15 Fragen in etwa fünf Minuten und sehen Sie, was Sie zuerst angehen sollten.',
          cta: 'Check starten', close: 'Schließen', url: BASE + 'de/copilot-readiness/' },
  };
  const t = TEXT[(document.documentElement.lang || 'en').slice(0, 2)] || TEXT.en;
  const KEY = 'om-readiness-promo';
  try {
    const saved = JSON.parse(localStorage.getItem(KEY));
    if (saved && Date.now() < saved.until) return;
  } catch (e) { /* storage unavailable: show the card */ }
  const remember = (days) => {
    try { localStorage.setItem(KEY, JSON.stringify({ until: Date.now() + days * 864e5 })); } catch (e) {}
  };

  const card = document.createElement('aside');
  card.className = 'promo';
  card.setAttribute('aria-labelledby', 'promo-title');
  card.innerHTML =
    '<svg class="promo-mark" viewBox="0 0 56 56" aria-hidden="true" focusable="false">' +
      '<circle cx="28" cy="28" r="22" fill="none" stroke="#3a3d42" stroke-width="7"/>' +
      '<path d="M28 6 A22 22 0 1 1 6 28" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>' +
      '<path d="M20 28.5 26 34 37 22" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>' +
    '</svg>' +
    '<div class="promo-text">' +
      '<p class="promo-title" id="promo-title"></p>' +
      '<p class="promo-body"></p>' +
      '<a class="promo-cta"></a>' +
    '</div>' +
    '<button class="promo-close" type="button">' +
      '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" focusable="false"><path d="M3.5 3.5l9 9m0-9-9 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>' +
    '</button>';
  card.querySelector('.promo-title').textContent = t.title;
  card.querySelector('.promo-body').textContent = t.body;
  const cta = card.querySelector('.promo-cta');
  cta.textContent = t.cta;
  cta.href = t.url;
  const closeButton = card.querySelector('.promo-close');
  closeButton.setAttribute('aria-label', t.close);
  document.body.appendChild(card);

  let shown = false;
  const show = () => {
    if (shown) return;
    shown = true;
    window.removeEventListener('scroll', onScroll);
    card.classList.add('is-open');
  };
  const hide = (days) => {
    card.classList.remove('is-open');
    remember(days);
    setTimeout(() => card.remove(), 400);
    document.removeEventListener('keydown', onKey);
  };
  const onScroll = () => { if (window.scrollY > window.innerHeight * 0.6) show(); };
  const onKey = (e) => { if (e.key === 'Escape' && shown) hide(14); };

  setTimeout(show, 8000);
  window.addEventListener('scroll', onScroll, { passive: true });
  document.addEventListener('keydown', onKey);
  closeButton.addEventListener('click', () => hide(14));
  cta.addEventListener('click', () => remember(60));
})();
