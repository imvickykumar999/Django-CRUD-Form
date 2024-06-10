
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, GeeksForm, LoginForm
from .models import GeeksModel
import os


@login_required
def create_view(request):
    context = {}
    form = GeeksForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('list_view')
    
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context['dataset'] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}
    context["data"] = get_object_or_404(GeeksModel, id=id)
    return render(request, "detail_view.html", context)


@login_required
def update_view(request, id):
    obj = get_object_or_404(GeeksModel, id=id)
    old_image_path = obj.foto.path if obj.foto else None
    
    if request.method == "POST":
        form = GeeksForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():

            if 'foto' in request.FILES:
                if old_image_path and os.path.exists(old_image_path):
                    os.remove(old_image_path)
                    
            form.save()
            return redirect("detail_view", id=id)
    else:
        form = GeeksForm(instance=obj)
    
    context = {'form': form}
    return render(request, "update_view.html", context)


@login_required
def delete_view(request, id):
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        image_path = obj.foto.path
        
        if os.path.exists(image_path):
            os.remove(image_path)
        obj.delete()

        return redirect('list_view')
    return render(request, "delete_view.html", {})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_view')
            else:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('list_view')
    else:
        return redirect('list_view')
