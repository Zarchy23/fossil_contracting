// Emoji reactions - using Unicode escape sequences
const reactionEmojis = ['\uD83D\uDC4D', '\u2764\uFE0F', '\uD83D\uDE02', '\uD83D\uDE2E', '\uD83D\uDE22', '\uD83D\uDE20'];

// Helper function to get CSRF token from cookies or meta tag
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    // If not found in cookies, try meta tag
    if (!cookieValue) {
        const metaToken = document.querySelector('meta[name="csrf-token"]');
        if (metaToken) {
            cookieValue = metaToken.getAttribute('content');
        }
    }
    return cookieValue;
}

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    initializeHeroCarousel();
    initializeHeader();
    initializeStats();
    loadServices();
    loadProjects();
    initializeMobileMenu();
    initializeCommunitySection();
});

// Hero image carousel
function initializeHeroCarousel() {
    const heroImages = document.querySelectorAll('.hero-bg-image');
    if (heroImages.length === 0) return;
    
    // Set first image as active
    if (heroImages[0]) {
        heroImages[0].classList.add('active');
    }
    
    let currentIndex = 0;
    
    // Rotate images every 8 seconds
    setInterval(() => {
        heroImages.forEach(img => img.classList.remove('active'));
        currentIndex = (currentIndex + 1) % heroImages.length;
        heroImages[currentIndex].classList.add('active');
    }, 8000);
}

// Header scroll effect
function initializeHeader() {
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// Load company stats from API
async function initializeStats() {
    const statsGrid = document.getElementById('statsGrid');
    if (!statsGrid) return;
    
    const stats = await fetchCompanyStats();
    
    if (stats && stats.length > 0) {
        statsGrid.innerHTML = stats.map(stat => `
            <div class="stat-card">
                <div class="stat-icon">${stat.icon || getStatIcon(stat.label)}</div>
                <div class="stat-value">${stat.value}${stat.suffix || ''}</div>
                <div class="stat-label">${stat.label}</div>
            </div>
        `).join('');
    } else {
        // Fallback stats
        statsGrid.innerHTML = `
            <div class="stat-card">
                <div class="stat-icon">🏆</div>
                <div class="stat-value">25+</div>
                <div class="stat-label">Years Experience</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <div class="stat-value">500+</div>
                <div class="stat-label">Projects Completed</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">⭐</div>
                <div class="stat-value">Category A</div>
                <div class="stat-label">ZBCA & CIFOZ</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🛡️</div>
                <div class="stat-value">100%</div>
                <div class="stat-label">Safety Commitment</div>
            </div>
        `;
    }
}

function getStatIcon(label) {
    const icons = {
        'Years Experience': '🏆',
        'Projects Completed': '📊',
        'ZBCA & CIFOZ': '⭐',
        'Safety Commitment': '🛡️'
    };
    return icons[label] || '📈';
}

// Load services
async function loadServices() {
    const servicesGrid = document.getElementById('servicesGrid');
    if (!servicesGrid) return;
    
    try {
        const services = await fetchServices();
        console.log('Services loaded:', services);
        
        if (!Array.isArray(services) || services.length === 0) {
            console.log('No services found');
            return;
        }
        
        // Display only featured services (first 4)
        const displayServices = services.slice(0, 4);
        
        servicesGrid.innerHTML = displayServices.map(service => `
            <div class="service-card">
                <div class="service-image">
                    <img src="${service.image_url}" alt="${service.name}">
                </div>
                <div class="service-content">
                    <h3>${service.name}</h3>
                    <p>${service.description}</p>
                    <a href="/services/#${service.id}" class="service-link">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error in loadServices:', error);
    }
}

// Load featured projects
async function loadProjects() {
    const projectsGrid = document.getElementById('featuredProjects');
    if (!projectsGrid) {
        console.log('Featured Projects grid not found');
        return;
    }
    
    try {
        const projects = await fetchProjects();
        console.log('Projects loaded:', projects);
        
        if (!Array.isArray(projects)) {
            console.error('Projects is not an array:', projects);
            return;
        }
        
        const featuredProjects = projects.filter(p => p.is_featured).slice(0, 4);
        console.log('Featured projects:', featuredProjects);
        
        // Icon mapping for projects
        const projectIconMap = {
            'Harare-Chirundu Highway': '🛣️',
            'Lorraine Drive Road': '🏗️',
            'Trabablas Interchange': '🚧',
            'Harare-Beitbridge Road': '🛣️'
        };
        
        if (featuredProjects.length > 0) {
            projectsGrid.innerHTML = featuredProjects.map(project => `
                <div class="project-card">
                    <div class="project-image">
                        ${project.image_url ? `<img src="${project.image_url}" alt="${project.name}">` : `<span>🏗️</span>`}
                    </div>
                    <div class="project-content">
                        <h3>${project.name}</h3>
                        <p>${project.description.substring(0, 85)}...</p>
                        <a href="/projects/${project.name.toLowerCase().replace(/ /g, '-').replace(/–/g, '-')}/" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            `).join('');
        } else {
            console.log('No featured projects found');
        }
    } catch (error) {
        console.error('Error in loadProjects:', error);
    }
}

// Mobile menu toggle
function initializeMobileMenu() {
    const menuBtn = document.getElementById('mobileMenuBtn');
    const navMenu = document.getElementById('navMenu');
    
    if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }
}

// Hero image rotation is handled by HTML img elements with CSS transitions
// Images are already being rotated properly in the DOM
/*
let heroIndex = 0;
const heroImages = [
    '/static/images/DJI_20250530162006_0002_V.jpg',
    '/static/images/DJI_20250530162737_0039_V.jpg',
    '/static/images/DJI_20250529171556_0077_D.jpg',
    '/static/images/DJI_20250529171427_0071_D.jpg',
];

if (document.querySelector('.hero')) {
    setInterval(() => {
        heroIndex = (heroIndex + 1) % heroImages.length;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.backgroundImage = `url(${heroImages[heroIndex]})`;
        }
    }, 10000);
}
*/

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '') {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// Community Section - Feedback and Blog
function initializeCommunitySection() {
    const feedbackForm = document.getElementById('feedbackForm');
    const blogForm = document.getElementById('blogForm');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const feedbackMessage = document.getElementById('feedbackMessage');
    const blogContent = document.getElementById('blogContent');

    // Tab switching
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tab = btn.getAttribute('data-tab');
            
            // Update active button
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Update active tab content
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(tab + '-tab').classList.add('active');
        });
    });

    // Load existing feedback and blog posts
    loadFeedback();
    loadBlog();

    // Feedback form submission
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = document.getElementById('feedbackMessage').value;

            if (!message.trim()) return;

            try {
                const csrftoken = getCookie('csrftoken');
                const response = await fetch('/api/feedback/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken || '',
                    },
                    body: JSON.stringify({
                        message: message
                    })
                });

                if (response.ok) {
                    document.getElementById('feedbackMessage').value = '';
                    loadFeedback();
                    alert('Thank you! Your feedback has been submitted.');
                } else {
                    const errorData = await response.json();
                    alert('Error submitting feedback: ' + (errorData.error || 'Please try again'));
                }
            } catch (error) {
                console.error('Error submitting feedback:', error);
                alert('Error submitting feedback: ' + error.message);
            }
        });
    }

    // Blog form submission
    if (blogForm) {
        blogForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('blogTitle').value;
            const content = document.getElementById('blogContent').value;

            if (!title.trim() || !content.trim()) return;

            try {
                const csrftoken = getCookie('csrftoken');
                const response = await fetch('/api/blog/posts/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken || '',
                    },
                    body: JSON.stringify({
                        title: title,
                        content: content
                    })
                });

                if (response.ok) {
                    document.getElementById('blogTitle').value = '';
                    document.getElementById('blogContent').value = '';
                    loadBlog();
                    alert('Thank you! Your discussion has been posted.');
                } else {
                    const errorData = await response.json();
                    alert('Error posting discussion: ' + (errorData.error || 'Please try again'));
                }
            } catch (error) {
                console.error('Error submitting blog post:', error);
                alert('Error posting discussion: ' + error.message);
            }
        });
    }
}

// Load reaction counts for an item
async function loadReactionCounts(contentType, itemId) {
    try {
        const response = await fetch(`/api/reactions/get/?content_type=${contentType}&object_id=${itemId}`);
        if (!response.ok) return {};
        return await response.json();
    } catch (error) {
        console.error('Error loading reactions:', error);
        return {};
    }
}

// Add a reaction to feedback or blog post
async function addReaction(contentType, itemId, emoji) {
    try {
        const response = await fetch('/api/reactions/add/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                emoji: emoji,
                content_type: contentType,
                object_id: itemId
            })
        });
        if (response.ok) {
            if (contentType === 'feedback') {
                loadFeedback();
            } else if (contentType === 'blogpost') {
                loadBlog();
            }
        }
    } catch (error) {
        console.error('Error adding reaction:', error);
    }
}

// Load feedback messages - Show only 5 most recent
async function loadFeedback() {
    try {
        const container = document.getElementById('feedbackMessages');
        if (!container) return;

        const response = await fetch('/api/feedback/?limit=5');
        const feedbackList = await response.json();

        if (!feedbackList || feedbackList.length === 0) {
            container.innerHTML = '<div class="empty-state"><p class="empty-title">No feedback yet.</p><p class="empty-subtitle">Be the first to share!</p></div>';
            return;
        }

        container.innerHTML = feedbackList.map(feedback => `
            <div class="message-card">
                <div class="message-header">
                    <strong>${feedback.name || 'Anonymous'}</strong>
                    <span class="message-date">${new Date(feedback.created_at).toLocaleDateString()}</span>
                </div>
                <p class="message-content">${feedback.message}</p>
                <div class="message-reactions">
                    <div class="reaction-buttons">
                        ${reactionEmojis.map(emoji => `
                            <button class="reaction-btn" onclick="addReaction('feedback', ${feedback.id}, '${emoji}')" title="React with ${emoji}">
                                <span class="emoji">${emoji}</span>
                                <span class="reaction-count" id="count-feedback-${feedback.id}-${emoji}">0</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
            </div>
        `).join('');

        // Load and display reaction counts
        for (const feedback of feedbackList) {
            const reactions = await loadReactionCounts('feedback', feedback.id);
            reactionEmojis.forEach(emoji => {
                const countElement = document.getElementById(`count-feedback-${feedback.id}-${emoji}`);
                if (countElement) {
                    countElement.textContent = reactions[emoji] || 0;
                }
            });
        }
    } catch (error) {
        console.error('Error loading feedback:', error);
    }
}

// Load blog posts - Show only 5 most recent
async function loadBlog() {
    try {
        const container = document.getElementById('blogMessages');
        if (!container) return;

        const response = await fetch('/api/blog/posts/?limit=5');
        const posts = await response.json();

        if (!posts || posts.length === 0) {
            container.innerHTML = '<div class="empty-state"><p class="empty-title">No discussions yet.</p><p class="empty-subtitle">Start the conversation!</p></div>';
            return;
        }

        container.innerHTML = posts.map(post => `
            <div class="blog-card">
                <div class="blog-header">
                    <h4>${post.title}</h4>
                    <span class="blog-date">${new Date(post.created_at).toLocaleDateString()}</span>
                </div>
                <p class="blog-content">${post.content}</p>
                <div class="blog-footer">
                    <div class="reaction-buttons">
                        ${reactionEmojis.map(emoji => `
                            <button class="reaction-btn" onclick="addReaction('blogpost', ${post.id}, '${emoji}')" title="React with ${emoji}">
                                <span class="emoji">${emoji}</span>
                                <span class="reaction-count" id="count-blogpost-${post.id}-${emoji}">0</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
            </div>
        `).join('');

        // Load and display reaction counts
        for (const post of posts) {
            const reactions = await loadReactionCounts('blogpost', post.id);
            reactionEmojis.forEach(emoji => {
                const countElement = document.getElementById(`count-blogpost-${post.id}-${emoji}`);
                if (countElement) {
                    countElement.textContent = reactions[emoji] || 0;
                }
            });
        }
    } catch (error) {
        console.error('Error loading blog:', error);
    }
}
