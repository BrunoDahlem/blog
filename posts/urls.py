from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='posts-index'),
    path('categories/<str:category>',
         views.PostCategory.as_view(), name='posts-categories'),
    path('search/', views.PostSearch.as_view(), name='posts-search'),
    path('post-detail/<slug:pk>', views.PostDetail.as_view(),
         name='posts-detail'),
]
