from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.listings, name='listings'),
    path('<int:app_id>/', views.detail, name='detail'),
    path('<str:username>', views.user_page, name='user_page'),
]