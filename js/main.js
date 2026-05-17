// ========================
// Mobile Nav Toggle
// ========================
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  mobileNav.classList.toggle('open');
});

mobileNav.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileNav.classList.remove('open');
  });
});

// ========================
// Scroll Fade-In Animations
// ========================
const fadeObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll('.fade-in').forEach(el => fadeObserver.observe(el));

// ========================
// Active Nav Link on Scroll
// ========================
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.navbar-links a:not(.navbar-resume)');

const navObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => link.classList.remove('active'));
        const active = document.querySelector(`.navbar-links a[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  },
  { rootMargin: '-40% 0px -55% 0px' }
);

sections.forEach(section => navObserver.observe(section));

// ========================
// Expandable Descriptions
// ========================
document.querySelectorAll('.desc-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    const desc = btn.previousElementSibling;
    const isNowClamped = desc.classList.toggle('clamped');
    btn.textContent = isNowClamped ? 'Read more' : 'Show less';
    btn.setAttribute('aria-expanded', String(!isNowClamped));
  });
});

