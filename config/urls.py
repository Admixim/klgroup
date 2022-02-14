"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from crm_kl.views import index, src,calendar

admin.site.site_header = "KL Group  Юридические услуги "
admin.site.site_title = "CRM Portal"
admin.site.index_title = "CRM KLGroup"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('calendar/', calendar, name ='calendar'),
    path('src/', src),
    path('accident/', include('accident.urls')),
    path('client/', include('client.urls')),
    path('auto/', include('auto.urls')),
    path('court/', include('court.urls')),
    path('expert/', include('expert.urls')),
    path('document/', include('document.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('price/', include('price.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
