from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('post/', views.api_post_view, name="post-api"),
    path('post/<int:id>/', views.api_post_detaile, name="post-detaile")
]