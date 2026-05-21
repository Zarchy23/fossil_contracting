import hashlib
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Feedback, BlogPost, BlogComment, Project, CompanyStat, Service
from .serializers import (
    FeedbackSerializer, BlogPostSerializer, BlogCommentSerializer,
    ProjectSerializer, CompanyStatSerializer
)
from .forms import ProjectForm, BlogPostForm, CompanyStatForm, ServiceForm

# ========== FEEDBACK VIEWS ==========
@api_view(['GET', 'POST'])
def feedback_list(request):
    if request.method == 'GET':
        limit = int(request.GET.get('limit', 100))  # Default to 100 if not specified
        # Filter by display_on_homepage unless explicitly fetching all (for admin)
        homepage_only = request.GET.get('homepage_only', 'true').lower() == 'true'
        
        if homepage_only:
            feedbacks = Feedback.objects.filter(display_on_homepage=True)[:limit]
        else:
            feedbacks = Feedback.objects.all()[:limit]
        
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Add default type if not provided
        data = request.data.copy()
        if 'type' not in data or not data['type']:
            data['type'] = 'FEEDBACK'
        
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            # Get IP address and hash it for anonymity
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            ip_hash = hashlib.sha256(ip.encode()).hexdigest()
            
            # Check for spam (max 5 submissions per hour)
            recent_count = Feedback.objects.filter(
                ip_hash=ip_hash,
                created_at__gte=datetime.now() - timedelta(hours=1)
            ).count()
            
            if recent_count >= 5:
                return Response(
                    {'error': 'Too many submissions. Please try again later.'},
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )
            
            # Auto-display anonymous praise messages on homepage
            is_anonymous = not data.get('name') or data.get('name', '').strip() == '' or data.get('name', '').lower() == 'anonymous'
            is_praise = data.get('type') == 'PRAISE'
            display_on_homepage = is_anonymous and is_praise
            
            serializer.save(ip_hash=ip_hash, display_on_homepage=display_on_homepage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ========== BLOG POST VIEWS ==========
@api_view(['GET', 'POST'])
def blog_posts(request):
    if request.method == 'GET':
        limit = int(request.GET.get('limit', 100))  # Default to 100 if not specified
        posts = BlogPost.objects.all()[:limit]
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Increment view count
        post.view_count = F('view_count') + 1
        post.save()
        post.refresh_from_db()
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BlogPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def blog_post_like(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk)
        post.like_count = F('like_count') + 1
        post.save()
        post.refresh_from_db()
        return Response({'like_count': post.like_count})
    except BlogPost.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

# ========== BLOG COMMENT VIEWS ==========
@api_view(['GET', 'POST'])
def blog_comments(request, post_id):
    if request.method == 'GET':
        comments = BlogComment.objects.filter(post_id=post_id)
        serializer = BlogCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def blog_comment_like(request, pk):
    try:
        comment = BlogComment.objects.get(pk=pk)
        comment.like_count = F('like_count') + 1
        comment.save()
        comment.refresh_from_db()
        return Response({'like_count': comment.like_count})
    except BlogComment.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

# ========== PROJECT VIEWS ==========
@api_view(['GET'])
def projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def featured_projects(request):
    projects = Project.objects.filter(is_featured=True)[:6]
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

# ========== STATS VIEWS ==========
@api_view(['GET'])
def company_stats(request):
    stats = CompanyStat.objects.all()
    serializer = CompanyStatSerializer(stats, many=True)
    return Response(serializer.data)

# ========== FRONTEND VIEWS ==========
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def land_development(request):
    return render(request, 'land-development.html')

def projects_page(request):
    return render(request, 'projects.html')

def project_detail(request, project_slug):
    # Map slug to template
    project_templates = {
        'harare-chirundu': 'harare-chirundu.html',
        'lorraine-drive': 'lorraine-drive.html',
        'trabablas-interchange': 'trabablas-interchange.html',
        'harare-beitbridge': 'harare-beitbridge.html',
    }
    
    template = project_templates.get(project_slug, 'projects.html')
    return render(request, template)

def contact(request):
    return render(request, 'contact.html')

def anonymous_feedback_page(request):
    return render(request, 'anonymous-feedback.html')

def community_blog_page(request):
    return render(request, 'community-blog.html')

# ========== ADMIN DASHBOARD VIEWS ==========
@login_required(login_url='dashboard_login')
def dashboard(request):
    """Main admin dashboard"""
    stats = {
        'projects': Project.objects.count(),
        'blog_posts': BlogPost.objects.count(),
        'feedback': Feedback.objects.filter(is_read=False).count(),
        'company_stats': CompanyStat.objects.count(),
    }
    # Get recent feedback (last 10)
    recent_feedback = Feedback.objects.all().order_by('-created_at')[:10]
    unread_feedback_count = Feedback.objects.filter(is_read=False).count()
    
    context = {
        'stats': stats,
        'recent_feedback': recent_feedback,
        'unread_feedback_count': unread_feedback_count,
    }
    return render(request, 'dashboard/index.html', context)

@require_http_methods(["GET", "POST"])
def dashboard_login(request):
    """Admin login page"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'dashboard/login.html')

@login_required(login_url='dashboard_login')
def dashboard_logout(request):
    """Admin logout"""
    logout(request)
    return redirect('dashboard_login')

# ========== PROJECT MANAGEMENT ==========
@login_required(login_url='dashboard_login')
def projects_list(request):
    """List all projects"""
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'dashboard/projects/list.html', {'projects': projects})

@login_required(login_url='dashboard_login')
def project_create(request):
    """Create new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/projects/form.html', {'form': form, 'title': 'Add Project'})

@login_required(login_url='dashboard_login')
def project_edit(request, pk):
    """Edit project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/projects/form.html', {'form': form, 'project': project, 'title': 'Edit Project'})

@login_required(login_url='dashboard_login')
def project_delete(request, pk):
    """Delete project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects_list')
    return render(request, 'dashboard/projects/confirm_delete.html', {'project': project})

# ========== BLOG MANAGEMENT ==========
@login_required(login_url='dashboard_login')
def blog_list(request):
    """List all blog posts"""
    posts = BlogPost.objects.all().order_by('-is_pinned', '-created_at')
    return render(request, 'dashboard/blog/list.html', {'posts': posts})

@login_required(login_url='dashboard_login')
def blog_create(request):
    """Create new blog post"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'dashboard/blog/form.html', {'form': form, 'title': 'New Blog Post'})

@login_required(login_url='dashboard_login')
def blog_edit(request, pk):
    """Edit blog post"""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'dashboard/blog/form.html', {'form': form, 'post': post, 'title': 'Edit Post'})

@login_required(login_url='dashboard_login')
def blog_delete(request, pk):
    """Delete blog post"""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'dashboard/blog/confirm_delete.html', {'post': post})

# ========== FEEDBACK MANAGEMENT ==========
@login_required(login_url='dashboard_login')
def feedback_list_view(request):
    """View all feedback"""
    feedbacks = Feedback.objects.all().order_by('-created_at')
    unread_count = feedbacks.filter(is_read=False).count()
    return render(request, 'dashboard/feedback/list.html', {
        'feedbacks': feedbacks,
        'unread_count': unread_count
    })

@login_required(login_url='dashboard_login')
@login_required(login_url='dashboard_login')
def feedback_detail(request, pk):
    """View single feedback"""
    feedback = get_object_or_404(Feedback, pk=pk)
    
    if request.method == 'POST':
        # Handle toggle homepage request
        toggle_homepage = request.POST.get('toggle_homepage')
        if toggle_homepage == 'true':
            feedback.display_on_homepage = True
        elif toggle_homepage == 'false':
            feedback.display_on_homepage = False
        feedback.save()
        
        # Redirect back to where the request came from
        redirect_url = request.POST.get('next', 'feedback_list_view')
        if redirect_url == 'dashboard':
            return redirect('dashboard')
        return redirect('feedback_list_view')
    
    if not feedback.is_read:
        feedback.is_read = True
        feedback.save()
    return render(request, 'dashboard/feedback/detail.html', {'feedback': feedback})

# ========== COMPANY STATS MANAGEMENT ==========
@login_required(login_url='dashboard_login')
def stats_list(request):
    """List company statistics"""
    stats = CompanyStat.objects.all().order_by('order')
    return render(request, 'dashboard/stats/list.html', {'stats': stats})

@login_required(login_url='dashboard_login')
def stat_create(request):
    """Create new statistic"""
    if request.method == 'POST':
        form = CompanyStatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats_list')
    else:
        form = CompanyStatForm()
    return render(request, 'dashboard/stats/form.html', {'form': form, 'title': 'New Statistic'})

@login_required(login_url='dashboard_login')
def stat_edit(request, pk):
    """Edit statistic"""
    stat = get_object_or_404(CompanyStat, pk=pk)
    if request.method == 'POST':
        form = CompanyStatForm(request.POST, instance=stat)
        if form.is_valid():
            form.save()
            return redirect('stats_list')
    else:
        form = CompanyStatForm(instance=stat)
    return render(request, 'dashboard/stats/form.html', {'form': form, 'stat': stat, 'title': 'Edit Statistic'})

@login_required(login_url='dashboard_login')
def stat_delete(request, pk):
    """Delete statistic"""
    stat = get_object_or_404(CompanyStat, pk=pk)
    if request.method == 'POST':
        stat.delete()
        return redirect('stats_list')
    return render(request, 'dashboard/stats/confirm_delete.html', {'stat': stat})

# ========== SERVICE MANAGEMENT ==========
@login_required(login_url='dashboard_login')
def services_list(request):
    """List all services"""
    services = Service.objects.all().order_by('order')
    return render(request, 'dashboard/services/list.html', {'services': services})

@login_required(login_url='dashboard_login')
def service_create(request):
    """Create new service"""
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/services/form.html', {'form': form, 'title': 'Add Service'})

@login_required(login_url='dashboard_login')
def service_edit(request, pk):
    """Edit service"""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/services/form.html', {'form': form, 'service': service, 'title': 'Edit Service'})

@login_required(login_url='dashboard_login')
def service_delete(request, pk):
    """Delete service"""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('services_list')
    return render(request, 'dashboard/services/confirm_delete.html', {'service': service})

# ========== REACTION VIEWS ==========
@csrf_exempt
@require_http_methods(["POST"])
def add_reaction(request):
    """Add a reaction to feedback or blog post"""
    from .models import Reaction
    import json
    
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    emoji = data.get('emoji')
    content_type = data.get('content_type')  # 'feedback' or 'blogpost'
    object_id = data.get('object_id')
    
    # Convert object_id to int
    try:
        object_id = int(object_id)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid object_id'}, status=400)
    
    if not emoji or not content_type:
        return JsonResponse({'error': 'Missing emoji or content_type'}, status=400)
    
    # Get IP address and hash it
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip_hash = hashlib.sha256(ip.encode()).hexdigest()
    
    try:
        from django.contrib.contenttypes.models import ContentType
        # Get the correct content type
        if content_type.lower() == 'feedback':
            ct = ContentType.objects.get(app_label='api', model='feedback')
        elif content_type.lower() == 'blogpost':
            ct = ContentType.objects.get(app_label='api', model='blogpost')
        else:
            return JsonResponse(
                {'error': f'Invalid content type: {content_type}'},
                status=400
            )
        
        # Try to create or get the reaction
        reaction, created = Reaction.objects.get_or_create(
            emoji=emoji,
            content_type=ct,
            object_id=object_id,
            ip_hash=ip_hash
        )
        
        if not created:
            # Already reacted with this emoji, so remove it (toggle)
            reaction.delete()
            return JsonResponse({'reacted': False})
        
        return JsonResponse({'reacted': True}, status=201)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def get_reactions(request):
    """Get reaction counts for a post or message"""
    from .models import Reaction
    from django.contrib.contenttypes.models import ContentType
    
    content_type = request.GET.get('content_type')  # 'feedback' or 'blogpost'
    object_id = request.GET.get('object_id')
    
    # Convert object_id to int
    try:
        object_id = int(object_id)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid object_id'}, status=400)
    
    if not content_type:
        return JsonResponse({'error': 'Missing content_type'}, status=400)
    
    try:
        # Get the correct content type
        if content_type.lower() == 'feedback':
            ct = ContentType.objects.get(app_label='api', model='feedback')
        elif content_type.lower() == 'blogpost':
            ct = ContentType.objects.get(app_label='api', model='blogpost')
        else:
            return JsonResponse({'error': 'Invalid content type'}, status=400)
        
        # Get reaction counts grouped by emoji
        reactions_data = Reaction.objects.filter(
            content_type=ct,
            object_id=object_id
        ).values('emoji').annotate(count=Count('id'))
        
        result = {reaction['emoji']: reaction['count'] for reaction in reactions_data}
        return JsonResponse(result)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)
