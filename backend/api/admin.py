
from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Feedback, BlogPost, BlogComment, Project, CompanyStat, Service

# Customize admin site
admin.site.site_header = "Fossil Contracting Admin Panel"
admin.site.site_title = "Admin"
admin.site.index_title = "Welcome to Fossil Contracting Management"

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_badge', 'message_preview', 'read_status', 'is_read', 'display_on_homepage', 'created_at']
    list_filter = ['type', 'is_read', 'display_on_homepage', 'created_at']
    list_editable = ['is_read', 'display_on_homepage']
    search_fields = ['message', 'name']
    readonly_fields = ['ip_hash', 'created_at', 'id']
    actions = ['mark_as_read', 'mark_as_unread', 'display_on_homepage_true', 'display_on_homepage_false']
    
    fieldsets = (
        ('Message Information', {
            'fields': ('id', 'name', 'type', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'display_on_homepage')
        }),
        ('System Data', {
            'fields': ('ip_hash', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def message_preview(self, obj):
        return obj.message[:100] + '...' if len(obj.message) > 100 else obj.message
    message_preview.short_description = 'Message'
    
    def type_badge(self, obj):
        colors = {
            'COMPLAINT': '#ef4444',
            'SUGGESTION': '#3b82f6',
            'PRAISE': '#22c55e',
            'INQUIRY': '#f59e0b',
            'FEEDBACK': '#8b5cf6',
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 12px; border-radius: 50px; font-weight: 600;">{}</span>',
            colors.get(obj.type, '#666'),
            obj.get_type_display()
        )
    type_badge.short_description = 'Type'
    
    def read_status(self, obj):
        if obj.is_read:
            return mark_safe('<span style="color: green;">✓ Read</span>')
        else:
            return mark_safe('<span style="color: red;">✕ Unread</span>')
    read_status.short_description = 'Status'
    
    def homepage_status(self, obj):
        if obj.display_on_homepage:
            return mark_safe('<span style="color: green; font-weight: bold;">🏠 Homepage</span>')
        else:
            return mark_safe('<span style="color: gray;">—</span>')
    homepage_status.short_description = 'Homepage'
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"
    
    def display_on_homepage_true(self, request, queryset):
        queryset.update(display_on_homepage=True)
    display_on_homepage_true.short_description = "✅ Display on homepage"
    
    def display_on_homepage_false(self, request, queryset):
        queryset.update(display_on_homepage=False)
    display_on_homepage_false.short_description = "❌ Hide from homepage"

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'view_count', 'like_count', 'pinned_status', 'created_at']
    list_filter = ['is_pinned', 'created_at']
    search_fields = ['title', 'content', 'author']
    
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'content', 'author')
        }),
        ('Settings', {
            'fields': ('is_pinned',)
        }),
        ('Statistics', {
            'fields': ('view_count', 'like_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    def pinned_status(self, obj):
        if obj.is_pinned:
            return mark_safe('<span style="color: #f59e0b;">📌 Pinned</span>')
        return "—"
    pinned_status.short_description = 'Status'

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'content_preview', 'like_count', 'created_at']
    list_filter = ['post', 'created_at']
    search_fields = ['content', 'author']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Comment', {
            'fields': ('post', 'content', 'author')
        }),
        ('Statistics', {
            'fields': ('like_count',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'value_usd', 'completion_badge', 'status_badge', 'featured_status']
    list_filter = ['status', 'is_featured', 'created_at']
    search_fields = ['name', 'client', 'location']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('name', 'location', 'client', 'description')
        }),
        ('Financial Information', {
            'fields': ('value_usd',)
        }),
        ('Project Status', {
            'fields': ('status', 'completion_percentage', 'is_featured')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Media', {
            'fields': ('image_url',),
            'classes': ('collapse',)
        }),
        ('System', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at']
    
    def completion_badge(self, obj):
        if obj.completion_percentage >= 100:
            color = '#22c55e'
            text = '✓ Complete'
        elif obj.completion_percentage >= 75:
            color = '#3b82f6'
            text = f'{obj.completion_percentage}%'
        elif obj.completion_percentage >= 50:
            color = '#f59e0b'
            text = f'{obj.completion_percentage}%'
        else:
            color = '#ef4444'
            text = f'{obj.completion_percentage}%'
        
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 12px; border-radius: 50px; font-weight: 600;">{}</span>',
            color, text
        )
    completion_badge.short_description = 'Progress'
    
    def status_badge(self, obj):
        colors = {
            'PLANNING': '#9ca3af',
            'ONGOING': '#3b82f6',
            'COMPLETED': '#22c55e',
            'ON_HOLD': '#f59e0b',
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 12px; border-radius: 50px; font-weight: 600;">{}</span>',
            colors.get(obj.status, '#666'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def featured_status(self, obj):
        if obj.is_featured:
            return mark_safe('<span style="color: #f59e0b;">⭐ Featured</span>')
        return "—"
    featured_status.short_description = 'Featured'

@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'icon', 'order']
    list_editable = ['order']
    
    fieldsets = (
        ('Statistic', {
            'fields': ('label', 'value', 'icon', 'suffix', 'order')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'featured_status', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['order']
    
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'description')
        }),
        ('Presentation', {
            'fields': ('icon', 'image_url', 'order', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    def featured_status(self, obj):
        if obj.is_featured:
            return mark_safe('<span style="color: #f59e0b;">⭐ Featured</span>')
        return "—"
    featured_status.short_description = 'Featured'
