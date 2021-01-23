from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from App1 import views

router = DefaultRouter()
router.register('',views.Employee_viewset)

urlpatterns = [
    path('',include(router.urls)),
]
