from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView

from accounts.models import CustomUser


class ProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'account/profile.html'


class ProfileSettingsView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'account/profile_settings.html'


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'account/account_delete.html'
    success_url = '/'

    # def test_func(self):
    #     user = self.get_object()
    #     if self.request.user == user:
    #         return True
    #     return False

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        response = redirect(reverse_lazy('account_logout'))
        response.status_code = 303
        return response
