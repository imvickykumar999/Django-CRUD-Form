from django.shortcuts import render, get_object_or_404, redirect
from .models import GeeksModel
from .forms import GeeksForm

def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_view')
    context['form'] = form
    return render(request, "create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = get_object_or_404(GeeksModel, id=id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('detail_view', id=id)
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_view')
    return render(request, "delete_view.html", context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
