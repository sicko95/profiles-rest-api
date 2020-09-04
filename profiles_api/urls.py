from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


"""Registracija routera pomocu ViewSet-a"""
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

'''Koriscenjem ModelViewSet ne moramo da definisemo base_name jer smo u queryset objetku vec definisali koji model koristimo
base_name atribut koristimo samo kada nismo definisali model, ili kada zelimo da override ime modela koji smo definisali'''
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
