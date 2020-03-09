from django.urls import path

from . import views

# Define all urls for /listings app
urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.listings, name='listings'),
    path('account', views.account_management, name='account_management'),
    path('<int:app_id>/', views.detail, name='detail'),
    path('<str:username>', views.user_page, name='user_page'),
]
