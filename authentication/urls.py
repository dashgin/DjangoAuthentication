from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts_mvt/', include('accounts.urls')),
    path('accounts_api/', include('auth_api.urls')),
]
