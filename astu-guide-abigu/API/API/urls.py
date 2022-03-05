from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('c_user.urls')),
    path('api/admin/', include('c_admin.urls')),
]
