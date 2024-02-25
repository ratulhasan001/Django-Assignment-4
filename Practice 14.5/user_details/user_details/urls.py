
from django.contrib import admin
from django.urls import path, include
from all_details import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_details/', include('all_details.urls')),
    path('', views.home)
]