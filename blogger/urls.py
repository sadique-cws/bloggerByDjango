
from django.contrib import admin
from django.urls import path
from cms.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path("news/<slug>/",viewNews, name="viewNews"),
    path("category/<int:id>/",filterCategory, name="filterCategory"),
    path("delete/<slug>/",deleteNews, name="deleteNews"),
    path("insert/",insertNews, name="insertNews"),
    path("login/",signIn, name="signIn"),
    path("logout/",signOut, name="signOut"),
    path("register/",signUp, name="signUp"),
    path("edit/<slug>/",editNews, name="editNews"),
    path("search/",searchNews, name="search"),
 
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
