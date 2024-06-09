>## `IPV4 Address` : http://192.168.0.100:8000/
>
> ```py
> ALLOWED_HOSTS = ['djangocrudvicks.pythonanywhere.com', '127.0.0.1', 'localhost', '192.168.0.100']
> ```
>
>     >>> python manage.py runserver 0.0.0.0:8000
>
> [![WhatsApp Image 2024-06-09 at 13 21 07_381d7831](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/4eeab633-c4c4-44bc-bf8e-7e138521c082)](http://192.168.0.100:8000/)
>
> ---
>
>     Run `ipconfig` and Use [IPV4 Address] to run server on PUBLIC Network and access project on mobile.
>
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/896dff5c-1caa-4d2b-904f-9ca5bebf9b81)
>
> ---
>
>## `HOSTED` : https://djangocrudvicks.pythonanywhere.com/
>
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/177247dc-de93-4ae7-a145-b1387d2ced93)
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/51e7e0e5-eddc-424d-a7cb-0e8958966c11)
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/ab492a9f-4c52-44c6-8e10-e7848f479668)
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/9278bb7e-9d33-4020-a586-e166c7c68bd6)
>![image](https://github.com/imvickykumar999/Django-CRUD-Form/assets/50515418/7d201a8b-9de6-4266-a9f4-77a000a56871)

Let's create a Django project named `crudproject` with an app named `crudapp` that implements CRUD functionality. Here are the step-by-step commands and instructions:

```bash
python -m venv .venv
.venv\Scripts\activate

deactivate
.venv\Scripts\activate
```

### 1. Install Django
Make sure Django is installed. If not, install it using pip:
```bash
pip install django
```

### 2. Create a Django Project
Create a new Django project named `crudproject`:
```bash
django-admin startproject crudproject
```

### 3. Navigate to the Project Directory
```bash
cd crudproject
```

### 4. Create a Django App
Create a new app named `crudapp`:
```bash
python manage.py startapp crudapp
```

### 5. Add the App to INSTALLED_APPS
Open `crudproject/settings.py` and add `crudapp` to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'crudapp',
]
```

### 6. Create the Model
In `crudapp/models.py`, define your model:
```python
from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
```

### 7. Create and Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a ModelForm
Create a file named `forms.py` in the `crudapp` folder and define the form:
```python
from django import forms
from .models import GeeksModel

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = ["title", "description"]
```

### 9. Create Views
In `crudapp/views.py`, add the CRUD views:

- **Create View**:
  ```python
  from django.shortcuts import render
  from .models import GeeksModel
  from .forms import GeeksForm

  def create_view(request):
      context = {}
      form = GeeksForm(request.POST or None)
      if form.is_valid():
          form.save()
      context['form'] = form
      return render(request, "create_view.html", context)
  ```

- **List View**:
  ```python
  from django.shortcuts import render
  from .models import GeeksModel

  def list_view(request):
      context = {}
      context["dataset"] = GeeksModel.objects.all()
      return render(request, "list_view.html", context)
  ```

- **Detail View**:
  ```python
  from django.shortcuts import render
  from .models import GeeksModel

  def detail_view(request, id):
      context = {}
      context["data"] = GeeksModel.objects.get(id=id)
      return render(request, "detail_view.html", context)
  ```

- **Update View**:
  ```python
  from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
  from .models import GeeksModel
  from .forms import GeeksForm

  def update_view(request, id):
      context = {}
      obj = get_object_or_404(GeeksModel, id=id)
      form = GeeksForm(request.POST or None, instance=obj)
      if form.is_valid():
          form.save()
          return HttpResponseRedirect("/" + id)
      context["form"] = form
      return render(request, "update_view.html", context)
  ```

- **Delete View**:
  ```python
  from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
  from .models import GeeksModel

  def delete_view(request, id):
      context = {}
      obj = get_object_or_404(GeeksModel, id=id)
      if request.method == "POST":
          obj.delete()
          return HttpResponseRedirect("/")
      return render(request, "delete_view.html", context)
  ```

### 10. Create Templates
Create a `templates` folder inside the `crudapp` app and add the following HTML files:

- **create_view.html**:
  ```html
  <form method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Submit">
  </form>
  ```

- **list_view.html**:
  ```html
  <div class="main">
      {% for data in dataset %}
      {{ data.title }}<br/>
      {{ data.description }}<br/>
      <hr/>
      {% endfor %}
  </div>
  ```

- **detail_view.html**:
  ```html
  <div class="main">
      {{ data.title }}<br/>
      {{ data.description }}<br/>
  </div>
  ```

- **update_view.html**:
  ```html
  <div class="main">
      <form method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="Update">
      </form>
  </div>
  ```

- **delete_view.html**:
  ```html
  <div class="main">
      <form method="POST">
          {% csrf_token %}
          Are you sure you want to delete this item?
          <input type="submit" value="Yes">
          <a href="/">Cancel</a>
      </form>
  </div>
  ```

### 11. Configure URLs
In `crudapp/urls.py`, define the URL patterns:
```python
from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('create/', create_view, name='create_view'),
    path('', list_view, name='list_view'),
    path('<id>/', detail_view, name='detail_view'),
    path('<id>/update/', update_view, name='update_view'),
    path('<id>/delete/', delete_view, name='delete_view'),
]
```

In `crudproject/urls.py`, include the app URLs:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudapp.urls')),
]
```

### 12. Run the Server
Start the development server:
```bash
python manage.py runserver
```

### 13. Access the Application
- Visit `http://localhost:8000/create/` to create a new entry.
- Visit `http://localhost:8000/` to see the list of entries.
- Visit `http://localhost:8000/<id>/` to see the detail of a specific entry.
- Visit `http://localhost:8000/<id>/update/` to update a specific entry.
- Visit `http://localhost:8000/<id>/delete/` to delete a specific entry.

By following these steps, you'll have a fully functional Django CRUD application named `crudproject` with an app named `crudapp`.

---

Running the Django development server with the command `python manage.py runserver 0.0.0.0:8000` will allow the server to be accessible on any network interface of the host machine. This means you can access your application from other devices on your local network using the IP address of the host machine.

### Step-by-Step Guide

1. **Run the Server:**
   Start the Django development server to listen on all available IP addresses:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

2. **Access the Application:**
   Open a web browser on any device connected to the same network as your Django server. Enter the following URL to access the application:

   ```http
   http://192.168.0.100:8000/
   ```

### Additional Notes

- **Network Configuration:**
  Ensure that your local network allows traffic on port 8000, and your host machine's firewall is configured to allow incoming connections on this port.

- **Finding Your Local IP Address:**
  If you don't know your local IP address, you can find it using the following methods:
  
  - **Windows:**
    Open Command Prompt and type `ipconfig`. Look for the `IPv4 Address`.
    
  - **macOS/Linux:**
    Open Terminal and type `ifconfig` or `ip a`. Look for the `inet` address in the relevant network interface section.

- **Security Considerations:**
  The Django development server is not intended for production use. It is recommended to use it only in a development environment. For a production environment, consider using a robust web server like Gunicorn or uWSGI, along with a reverse proxy server like Nginx or Apache.

By following these instructions, you can access and test your Django application on different devices within your local network.
