from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import ProfilePage, RegisterView

urlpatterns = [

    path('', views.index, name='home'),
    path('additional_info/<int:id>', views.add_info, name='add_info'),
    path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path(r'^accounts/login/$', LoginView.as_view(), name="login"),
    path(r'^accounts/logout/$', views.logout, name='logout'),
    path(r'^edit_password/$', views.edit_password, name='password'),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path(r'^about/$', views.about, name='about'),
    path(r'^forum/$', views.forum, name='forum'),
    path(r'^create/$', views.create, name='create')

]
