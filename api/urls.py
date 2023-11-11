# from django.conf.urls import include
from django.urls import path
# Import router from rest_framework
from rest_framework import routers
from . import views

# create a router object
router = routers.DefaultRouter()
# register the router for Post and Comment views
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
  path('posts/', views.PostViewSet.as_view(), name='posts'),
  path('comments/', views.CommentViewSet.as_view(), name='comments'),

]

 