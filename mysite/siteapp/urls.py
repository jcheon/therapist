from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls),
    # path('$/', views.signIn),
    # path('postsign/', views.postsign),
]