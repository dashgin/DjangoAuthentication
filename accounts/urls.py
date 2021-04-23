from django.urls import path, include

from .views import ProfileView, ProfileSettingsView, AccountDeleteView

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/settings/', ProfileSettingsView.as_view(), name="profile-settings"),
    path('profile/settings/delete/<int:pk>/', AccountDeleteView.as_view(), name='account-delete')
]
