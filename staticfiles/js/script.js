    // ── MOBILE MENU ──
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    hamburger.addEventListener('click', function() {
      this.classList.toggle('active');
      navLinks.classList.toggle('open');
    });

    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('open');
      });
    });

    // ── NAV SCROLL SHADOW & ACTIVE SECTION ──
    const nav = document.getElementById('mainNav');
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', function() {
      // shadow
      if (window.scrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }

      // active section
      let current = '';
      sections.forEach(section => {
        const top = section.offsetTop - 100;
        const height = section.offsetHeight;
        if (window.scrollY >= top && window.scrollY < top + height) {
          current = section.getAttribute('id');
        }
      });

      navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === '#' + current) {
          item.classList.add('active');
        }
      });
    });

    // ── SMOOTH SCROLL FOR NAV LINKS ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
    function copyPhone() {
    const phone = "+989054770679";

    navigator.clipboard.writeText(phone).then(() => {
        alert("شماره تلفن کپی شد.");
    });
}