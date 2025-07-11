from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 새로 추가한 필드들 (기본값 추가)
    year = models.PositiveIntegerField(default=2000)        # 개봉년도
    genre = models.CharField(max_length=32, default="기타") # 장르
    rating = models.FloatField(default=0.0)                 # 별점
    actor = models.CharField(max_length=64, default="")         # 주연
    running_time = models.PositiveIntegerField(default=0)       #러닝타임

    from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=32)
    user = models.CharField(max_length=32)       # 감독
    actor = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    rating = models.FloatField(default=0.0)
    running_time = models.PositiveIntegerField()
    content = models.TextField()
    year = models.PositiveIntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ 이미지 필드 추가 (media/reviews/ 에 저장됨)
    img = models.ImageField(upload_to='reviews/', null=True, blank=True)