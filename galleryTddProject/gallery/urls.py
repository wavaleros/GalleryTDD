from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('portfolios', views.list_portafolios, name='portfolios'),
    path('public-portfolios', views.list_public_porfolios_by_user, name='public_portfolios_by_user'),
    path('user/login/', views.user_login, name='user_login'),
]
