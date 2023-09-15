"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from backend import views

urlpatterns = [
    path("", views.uploadFile),
    path("admin/", admin.site.urls),
    path("upload-file/", views.uploadFile),
    # path("downloadFile/", views.downloadFile),
    path("downloadFile/", views.download_file),
    path("external/", views.external),
    path("allExternals/", views.getAllExternals),
    path("student/", views.student),
    path("supervisor/", views.supervisor),
    path("allSupervisors/", views.getAllSupervisors),
    # path("generate/", views.generate),
    path("generate/", views.new_algo),
    path("get_iterations/", views.get_iterations),
    path("allInternals/", views.getAllInternals),
    path("internal/", views.internal),
]
