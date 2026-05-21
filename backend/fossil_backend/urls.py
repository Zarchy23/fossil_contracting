from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import (
    index, about, services, land_development, projects_page, project_detail, contact,
    anonymous_feedback_page, community_blog_page,
    # Dashboard views
    dashboard, dashboard_login, dashboard_logout,
    projects_list, project_create, project_edit, project_delete,
    blog_list, blog_create, blog_edit, blog_delete,
    feedback_list_view, feedback_detail,
    stats_list, stat_create, stat_edit, stat_delete,
    services_list, service_create, service_edit, service_delete
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('services/land-development/', land_development, name='land_development'),
    path('projects/', projects_page, name='projects'),
    path('projects/<str:project_slug>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('anonymous-feedback/', anonymous_feedback_page, name='anonymous_feedback'),
    path('community-blog/', community_blog_page, name='community_blog'),
    
    # Admin Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/login/', dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', dashboard_logout, name='dashboard_logout'),
    
    # Projects Management
    path('dashboard/projects/', projects_list, name='projects_list'),
    path('dashboard/projects/create/', project_create, name='project_create'),
    path('dashboard/projects/<int:pk>/edit/', project_edit, name='project_edit'),
    path('dashboard/projects/<int:pk>/delete/', project_delete, name='project_delete'),
    
    # Blog Management
    path('dashboard/blog/', blog_list, name='blog_list'),
    path('dashboard/blog/create/', blog_create, name='blog_create'),
    path('dashboard/blog/<int:pk>/edit/', blog_edit, name='blog_edit'),
    path('dashboard/blog/<int:pk>/delete/', blog_delete, name='blog_delete'),
    
    # Feedback Management
    path('dashboard/feedback/', feedback_list_view, name='feedback_list_view'),
    path('dashboard/feedback/<int:pk>/', feedback_detail, name='feedback_detail'),
    
    # Statistics Management
    path('dashboard/stats/', stats_list, name='stats_list'),
    path('dashboard/stats/create/', stat_create, name='stat_create'),
    path('dashboard/stats/<int:pk>/edit/', stat_edit, name='stat_edit'),
    path('dashboard/stats/<int:pk>/delete/', stat_delete, name='stat_delete'),
    
    # Services Management
    path('dashboard/services/', services_list, name='services_list'),
    path('dashboard/services/create/', service_create, name='service_create'),
    path('dashboard/services/<int:pk>/edit/', service_edit, name='service_edit'),
    path('dashboard/services/<int:pk>/delete/', service_delete, name='service_delete'),
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
