from django.shortcuts import render, redirect
from .forms import UserDataForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('registro_exitoso')  
    template_name = 'user_auth/registro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def register_user(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso') 
    else:
        form = UserDataForm()
    return render(request, {'form': form})


def registro_exitoso(request):
    return render(request, 'user_auth/registro_exitoso.html')
