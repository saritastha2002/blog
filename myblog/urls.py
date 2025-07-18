from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
]
