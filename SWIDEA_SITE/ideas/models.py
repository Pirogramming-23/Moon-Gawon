from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    DEV_TOOL_CHOICES = [
    ('django', 'Django'),
    ('react', 'React'),
    ('javascript', 'JavaScript'),
    ('vue', 'Vue'),
    ('spring', 'Spring'),
    ('flask', 'Flask'),
    ('fastapi', 'FastAPI'),
    ('other', '기타'),
    ]
    title = models.CharField(max_length=100)
    dev_tool = models.ForeignKey('DevTool', on_delete=models.CASCADE)
    interest = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='idea_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='stars')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')

class DevTool(models.Model):
    name = models.CharField(max_length=100)           # 툴 이름
    type = models.CharField(max_length=100, blank=True, null=True)          # 툴 종류 (이전: 공식 URL)
    description = models.TextField(blank=True)        # 툴 설명

    def __str__(self):
        return self.name