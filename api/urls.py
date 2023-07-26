from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home ),
    path('testing/', views.testing),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('posts/', views.all_posts),
    path('create/', views.create_post),
    path('trending/', views.trendingView),
    path('latest/', views.latestPosts),
    path('edit/<int:id>/', views.edit_post),
]