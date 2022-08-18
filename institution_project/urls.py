"""institution_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from institutions_app import views


urlpatterns = [
    path('', views.rendering, name='rendering'),
    path('admin/', admin.site.urls),
    path('institutions/', include('institutions_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register/", views.register_view, name="register"),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='site-logout'),
    path("profile/", views.user_update.as_view(), name="profile"),
]
