from django.urls import path
from .views import Register,LoginAPI
from knox import views as Knox_views ##

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',LoginAPI.as_view(),name="login"),
    path('logout/',Knox_views.LogoutView.as_view(),name="logout"),
    path('logoutall/',Knox_views.LogoutAllView.as_view(),name='logoutall'),
]
