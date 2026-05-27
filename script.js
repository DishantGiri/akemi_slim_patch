// Akemi Slim Patch - Hero Section Scripts

document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== Navbar Sticky Scroll Effect =====
    const header = document.querySelector('.header');
    if (header) {
        const checkScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('header--scrolled');
            } else {
                header.classList.remove('header--scrolled');
            }
        };
        
        // Run on initial load and on scroll
        checkScroll();
        window.addEventListener('scroll', checkScroll);
    }

    // ===== Mobile Navigation Menu Toggle =====
    const navToggle = document.querySelector('.nav-toggle');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const bodyElement = document.body;

    if (navToggle && mobileNavOverlay) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            mobileNavOverlay.classList.toggle('active');
            bodyElement.classList.toggle('no-scroll');
        });
        
        // Close menu when clicking mobile links
        const mobileLinks = mobileNavOverlay.querySelectorAll('.mobile-nav-link, .mobile-nav-cta');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                mobileNavOverlay.classList.remove('active');
                bodyElement.classList.remove('no-scroll');
            });
        });
    }

    // ===== Scrollspy: Active Navbar Link Highlight on Scroll =====
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    if (sections.length && navLinks.length) {
        const scrollspy = () => {
            let currentActiveSectionId = '';
            const scrollPosition = window.scrollY + 120; // Match scrolling offset

            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                    currentActiveSectionId = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                const href = link.getAttribute('href');
                if (href === `#${currentActiveSectionId}`) {
                    link.classList.add('active');
                }
            });
        };

        window.addEventListener('scroll', scrollspy);
        scrollspy(); // run once on load
    }


    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Add subtle parallax to floating cards on mouse move
    const heroSection = document.querySelector('.hero');
    const floatCards = document.querySelectorAll('.hero-float-card');

    if (heroSection && floatCards.length) {
        heroSection.addEventListener('mousemove', (e) => {
            const rect = heroSection.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;

            floatCards.forEach((card, index) => {
                const intensity = (index + 1) * 8;
                const moveX = x * intensity;
                const moveY = y * intensity;
                card.style.transform = `translate(${moveX}px, ${moveY}px)`;
            });
        });

        heroSection.addEventListener('mouseleave', () => {
            floatCards.forEach(card => {
                card.style.transform = 'translate(0, 0)';
                card.style.transition = 'transform 0.5s ease-out';
                setTimeout(() => {
                    card.style.transition = '';
                }, 500);
            });
        });
    }

    // ===== FAQ Accordion Interactivity =====
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('is-active');
            
            // Close all items
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('is-active');
                otherItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
                otherItem.querySelector('.faq-answer').style.maxHeight = null;
            });
            
            // Toggle active item
            if (!isActive) {
                item.classList.add('is-active');
                question.setAttribute('aria-expanded', 'true');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
});

