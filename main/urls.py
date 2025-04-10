from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('accounts', include('django.contrib.auth.urls')),
    path('Keirsi/', include('Test.urls'), name="Keirsi"),
    path('motivation/', include('Test.urls'), name="motivation")
]
