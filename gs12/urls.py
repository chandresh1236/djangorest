from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('allsong/', views.SongsAPI.as_view()),
    path('platforms/<slug:pk>/', views.SongsAPI.as_view()),
]