from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


@method_decorator(login_required(login_url='/'), name='dispatch')
class AppView(TemplateView):
    template_name = 'app.html'


def logout(request):
    auth_logout(request)
    return redirect('/')
