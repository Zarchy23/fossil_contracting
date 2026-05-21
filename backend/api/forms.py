from django import forms
from .models import Project, BlogPost, BlogComment, Feedback, CompanyStat, Service

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'client', 'description', 'value_usd', 'status', 
                  'completion_percentage', 'is_featured', 'start_date', 'end_date', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'value_usd': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Value in USD'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'completion_percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '/static/images/...'}),
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'is_pinned']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'is_pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CompanyStatForm(forms.ModelForm):
    class Meta:
        model = CompanyStat
        fields = ['label', 'value', 'icon', 'suffix', 'order']
        widgets = {
            'label': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '📊'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'icon', 'image_url', 'order', 'is_featured']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fas fa-briefcase'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '/static/images/...'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
