from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home),
    path('index', views.home, name = 'index'),
    path('login', auth_views.LoginView.as_view(
        template_name='HomeScreen/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='HomeScreen/logout.html'), name='logout'),
    path('profile', views.profile, name = 'profile'),
    path('Compare', views.compare, name='Compare'),
    path('register', views.register),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='HomeScreen/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='HomeScreen/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='HomeScreen/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='HomeScreen/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('search_for_tos', views.search_for_tos),
    path('submit', views.submit, name = 'submit'),
    path('ViewTOS/<slug:tos_name>/', views.ViewTOS, name = 'ViewTOS'),
    path('ViewTOS/<slug:tos_name>/Edit', views.Edit_Page, name = 'Edit'),
    path('htmx/Edit-Form/', views.Create_Edit_Form, name='Edit-Form'),
    path('htmx/Edit/<pk>/', views.Detail_Edit, name='Detail-Edit'),
]
