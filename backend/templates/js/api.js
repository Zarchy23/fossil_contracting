// API Configuration - Use relative path since frontend and backend run on same port
const API_BASE_URL = '/api';

// Fetch company stats
async function fetchCompanyStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/stats/`);
        const stats = await response.json();
        return stats;
    } catch (error) {
        console.error('Error fetching stats:', error);
        return null;
    }
}

// Submit anonymous feedback
async function submitFeedback(feedbackData) {
    try {
        const response = await fetch(`${API_BASE_URL}/feedback/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(feedbackData),
        });
        return await response.json();
    } catch (error) {
        console.error('Error submitting feedback:', error);
        return { error: 'Failed to submit feedback' };
    }
}

// Fetch blog posts
async function fetchBlogPosts() {
    try {
        const response = await fetch(`${API_BASE_URL}/blog/posts/`);
        const posts = await response.json();
        return posts;
    } catch (error) {
        console.error('Error fetching blog posts:', error);
        return [];
    }
}

// Create blog post
async function createBlogPost(postData) {
    try {
        const response = await fetch(`${API_BASE_URL}/blog/posts/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData),
        });
        return await response.json();
    } catch (error) {
        console.error('Error creating blog post:', error);
        return { error: 'Failed to create post' };
    }
}

// Add comment to blog post
async function addComment(postId, commentData) {
    try {
        const response = await fetch(`${API_BASE_URL}/blog/posts/${postId}/comments/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(commentData),
        });
        return await response.json();
    } catch (error) {
        console.error('Error adding comment:', error);
        return { error: 'Failed to add comment' };
    }
}

// Like a blog post
async function likePost(postId) {
    try {
        const response = await fetch(`${API_BASE_URL}/blog/posts/${postId}/like/`, {
            method: 'POST',
        });
        return await response.json();
    } catch (error) {
        console.error('Error liking post:', error);
        return { error: 'Failed to like post' };
    }
}

// Fetch projects
async function fetchProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects/`);
        const projects = await response.json();
        return projects;
    } catch (error) {
        console.error('Error fetching projects:', error);
        return [];
    }
}

// Fetch services
async function fetchServices() {
    try {
        const response = await fetch(`${API_BASE_URL}/services/`);
        const services = await response.json();
        return services;
    } catch (error) {
        console.error('Error fetching services:', error);
        return [];
    }
}
