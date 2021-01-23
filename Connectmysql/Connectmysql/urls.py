from django.contrib import admin
from rest_framework.routers import DefaultRouter
from App1 import views
from django.urls import path,include

router = DefaultRouter()
router.register('author',views.Author_view)
router.register('book',views.Book_view)

urlpatterns = [
    path('',include(router.urls)),
]
