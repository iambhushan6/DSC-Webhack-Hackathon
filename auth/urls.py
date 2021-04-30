from django.contrib import admin
from django.urls import path
from auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Loginkar.as_view()),
    path('logout/', views.Logoutkar.as_view()),
]