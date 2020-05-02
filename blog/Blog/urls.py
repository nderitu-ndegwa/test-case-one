from . import views
from django.urls import paths

urlpatterns = [
    path('', views.PostList, name='Home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
    
]
