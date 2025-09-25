from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

class LoginView(View):
    def get(self, request):
        next_url = request.GET.get('next', '/caaordserv/')
        return render(request, 'authentication/login.html', {'next': next_url})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next') or request.GET.get('next', '/caaordserv/')

        user = authenticate(request, username=username, password=password)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Resposta AJAX (JSON)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'redirect_url': next_url})
            else:
                return JsonResponse({'success': False, 'error': 'Usuário ou senha inválidos'})
        else:
            # Resposta normal (form tradicional)
            if user is not None:
                login(request, user)
                messages.success(request, 'Bem-vindo de volta!')
                return redirect(next_url)
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return render(request, 'authentication/login.html', {'next': next_url})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
