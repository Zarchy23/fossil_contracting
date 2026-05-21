import hashlib
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('COMPLAINT', 'Complaint'),
        ('SUGGESTION', 'Suggestion'),
        ('PRAISE', 'Praise'),
        ('INQUIRY', 'Inquiry'),
        ('FEEDBACK', 'Feedback'),
    ]
    
    name = models.CharField(max_length=100, default='Anonymous', blank=True)
    type = models.CharField(max_length=20, choices=FEEDBACK_TYPES, default='FEEDBACK')
    message = models.TextField()
    ip_hash = models.CharField(max_length=64, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    display_on_homepage = models.BooleanField(default=False, help_text="Display this feedback on the home page")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default='Anonymous')
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_pinned', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.CharField(max_length=100, default='Anonymous')
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment on {self.post.title}"

class Project(models.Model):
    STATUS_CHOICES = [
        ('PLANNING', 'Planning'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
    ]
    
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    value_usd = models.DecimalField(max_digits=15, decimal_places=2)
    completion_percentage = models.IntegerField(default=0)
    client = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ONGOING')
    image_url = models.CharField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
    
    def __str__(self):
        return self.name

class CompanyStat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=10, blank=True)
    suffix = models.CharField(max_length=10, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.label}: {self.value}"

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('👍', '👍 Like'),
        ('❤️', '❤️ Love'),
        ('😂', '😂 Haha'),
        ('😮', '😮 Wow'),
        ('😢', '😢 Sad'),
        ('😠', '😠 Angry'),
    ]
    
    emoji = models.CharField(max_length=10, choices=REACTION_CHOICES)
    ip_hash = models.CharField(max_length=64, blank=True, null=True)
    
    # Generic Foreign Key to allow reactions on different models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        unique_together = ('content_type', 'object_id', 'ip_hash', 'emoji')
    
    def __str__(self):
        return f"{self.emoji} on {self.content_type} {self.object_id}"
