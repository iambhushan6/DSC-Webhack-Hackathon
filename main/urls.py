from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Homehtml.as_view()),

    path('covidupdates/', views.Page2html.as_view()),

    path('guidelines/', views.Page3html.as_view()),

    path('registration/', views.Page4html.as_view()),
    
    path('beneficiary/', views.beneficiary),

    path('vaccine_center/', login_required(views.Vaccinecenter.as_view())),

    path('centers/', login_required(views.Centerlist.as_view())),

    path('centers/<int:pk>', login_required(views.Center.as_view()),name='centerdetail'),

    path('token/', views.token),
    ]