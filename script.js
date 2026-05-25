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
});
