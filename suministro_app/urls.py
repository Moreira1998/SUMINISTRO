"""SUMINISTRO_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from suministro_app.views import IndexView
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', logout_then_login, name='logout'),
    path('admin/', admin.site.urls),
    path('home/', login_required(IndexView.as_view()), name='inicio'),
    path('producto/', include('apps.producto.urls')),
    path('solicitud/', include('apps.solicitud.urls')),
    path('combustible/', include('apps.combustible.urls')),
    path('mantenimiento/', include('apps.mantenimiento.urls')),
    path("select2/", include("django_select2.urls")),

]
