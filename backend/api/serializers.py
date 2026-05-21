from rest_framework import serializers
from .models import Feedback, BlogPost, BlogComment, Project, CompanyStat

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'type', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['id', 'post', 'content', 'author', 'like_count', 'created_at']
        read_only_fields = ['id', 'like_count', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'view_count', 'like_count', 
                  'is_pinned', 'comment_count', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'view_count', 'like_count', 'created_at', 'updated_at']
    
    def get_comment_count(self, obj):
        return obj.comments.count()

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CompanyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStat
        fields = '__all__'
