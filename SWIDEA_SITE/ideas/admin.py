from django.contrib import admin
from .models import Idea, IdeaStar  # ← 둘 다 등록 가능

admin.site.register(Idea)
admin.site.register(IdeaStar)  # 선택