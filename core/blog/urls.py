from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('cbv_index/', views.IndexViews.as_view(), name='index'),
    path('go-to-maktabkhoneh/<int:pk>/', views.RedirectToMaktab.as_view(), name='go-to-maktab'),
    path('post/', views.ListPost.as_view(), name='listpost'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='post-detail'),
    # path('post/create/', views.CreatePostView.as_view(), name='create-post')
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]