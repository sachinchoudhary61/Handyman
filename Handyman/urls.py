"""Handyman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import include
from normaluser import views
import buisnessuser.views as view2

from django.views.generic import TemplateView
urlpatterns = [
                path('admin/', admin.site.urls),
                path('', views.home, name="handyman-home"),
                path('activeness/', view2.verifyuser),
                path('professional_user_signup', view2.signup, name="handyman-pu_signup"),
                path('login', views.login, name="handyman-login"),
                path('signup', views.signup, name="handyman-signup"),
                path('view-data', view2.viewdata, name="view-Professional-user")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
