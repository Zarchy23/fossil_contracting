from django.urls import path
from . import views

urlpatterns = [
    # Feedback
    path('feedback/', views.feedback_list, name='feedback-list'),
    
    # Blog Posts
    path('blog/posts/', views.blog_posts, name='blog-posts'),
    path('blog/posts/<int:pk>/', views.blog_post_detail, name='blog-post-detail'),
    path('blog/posts/<int:pk>/like/', views.blog_post_like, name='blog-post-like'),
    
    # Blog Comments
    path('blog/posts/<int:post_id>/comments/', views.blog_comments, name='blog-comments'),
    path('blog/comments/<int:pk>/like/', views.blog_comment_like, name='blog-comment-like'),
    
    # Projects
    path('projects/', views.projects, name='projects'),
    path('projects/featured/', views.featured_projects, name='featured-projects'),
    
    # Stats
    path('stats/', views.company_stats, name='company-stats'),
    
    # Reactions
    path('reactions/add/', views.add_reaction, name='add-reaction'),
    path('reactions/get/', views.get_reactions, name='get-reactions'),
]
