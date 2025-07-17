from django.contrib import admin
from .models import Idea, IdeaStar
from .models import DevTool  # 이미 있으면 생략해도 됨

admin.site.register(DevTool)
admin.site.register(Idea)
admin.site.register(IdeaStar)
DevTool.objects.all()  # 선택