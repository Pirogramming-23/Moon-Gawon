from django.urls import path
from .views import review_list, review_read , review_create , review_update , review_delete

urlpatterns = [
    path('', review_list, name='review_list'),              # 리스트
    path('<int:pk>/', review_read, name='review_read'),  
    path("create/", review_create, name='review_create'),
    path("<int:pk>/update/", review_update, name='review_update'),
    path('<int:pk>/delete/', review_delete, name='review_delete')   # 상세 페이지
]