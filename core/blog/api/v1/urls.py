from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = router.urls

# urlpatterns = [
#     # path('post/', views.api_post_view, name="post-api"),
#     # path('post/<int:id>/', views.api_post_detaile, name="post-detaile")

#     # path('post/', views.PostList.as_view(), name='post-list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail')

#     path('post/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrive', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-detail')
# ]