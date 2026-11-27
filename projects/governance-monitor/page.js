// Governance Monitor page: owner review card loop, pause button, hero score count-up.
(() => {
  // Owner review card: Archive is picked, the confirmation shows, then it starts again.
  const review = document.getElementById('review');
  const pause = document.getElementById('pause');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let timer = null, step = 0;
  const states = ['', 'pick', 'done'];
  function tick() {
    step = (step + 1) % states.length;
    review.dataset.state = states[step];
  }
  function play() { if (!timer) timer = setInterval(tick, 1300); }
  function stop() { clearInterval(timer); timer = null; }
  if (reduce) { review.dataset.state = 'done'; pause.hidden = true; }
  else {
    play();
    review.addEventListener('pointerenter', () => { step = 0; review.dataset.state = ''; });
    pause.addEventListener('click', () => {
      const paused = pause.getAttribute('aria-pressed') === 'true';
      pause.setAttribute('aria-pressed', String(!paused));
      pause.textContent = paused ? 'Pause animation' : 'Play animation';
      document.documentElement.classList.toggle('paused', !paused);
      const svg = document.querySelector('.diagram svg');
      if (paused) { play(); svg.unpauseAnimations(); } else { stop(); svg.pauseAnimations(); }
    });
  }

  // Hero score counts up once on load.
  const el = document.querySelector('[data-count]');
  if (el && !reduce) {
    const end = +el.dataset.count, t0 = performance.now();
    const run = now => {
      const p = Math.min(1, (now - t0) / 1100);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(run);
    };
    requestAnimationFrame(run);
  }
})();
