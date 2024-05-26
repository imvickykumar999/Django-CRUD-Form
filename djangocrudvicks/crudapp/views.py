from django.shortcuts import render, get_object_or_404, redirect
from .models import GeeksModel
from .forms import GeeksForm

# Create View
def create_view(request):
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_view')  # Redirect to the list view after saving
    return render(request, "create_view.html", {'form': form})

# List View
def list_view(request):
    dataset = GeeksModel.objects.all()
    return render(request, "list_view.html", {'dataset': dataset})

# Detail View
def detail_view(request, id):
    data = get_object_or_404(GeeksModel, id=id)
    return render(request, "detail_view.html", {'data': data})

# Update View
def update_view(request, id):
    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('detail_view', id=obj.id)  # Redirect to the detail view after updating
    return render(request, "update_view.html", {'form': form})

# Delete View
def delete_view(request, id):
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_view')  # Redirect to the list view after deleting
    return render(request, "delete_view.html", {'object': obj})
