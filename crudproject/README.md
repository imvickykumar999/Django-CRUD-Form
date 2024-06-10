# `Modifications`

To create a Django model that uses `uuid4` as the primary key, you need to utilize Django's `UUIDField` with `default` set to `uuid.uuid4`. Here's how you can do it:

### Step-by-Step Guide

1. **Install Django**: If you haven't already installed Django, you can do so using pip.

    ```bash
    pip install django
    ```

2. **Create a Django Project**: Start a new Django project.

    ```bash
    django-admin startproject myproject
    cd myproject
    ```

3. **Create a Django App**: Create a new app within your project.

    ```bash
    python manage.py startapp myapp
    ```

4. **Add App to Installed Apps**: Add your new app to the `INSTALLED_APPS` list in `myproject/settings.py`.

    ```python
    INSTALLED_APPS = [
        ...
        'myapp',
    ]
    ```

5. **Create a Model with UUID Primary Key**: Define your model in `myapp/models.py`.

    ```python
    import uuid
    from django.db import models

    class MyModel(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
    ```

6. **Apply Migrations**: Create and apply migrations for your new model.

    ```bash
    python manage.py makemigrations myapp
    python manage.py migrate
    ```

7. **Admin Registration (Optional)**: If you want to manage your model via Django's admin interface, register it in `myapp/admin.py`.

    ```python
    from django.contrib import admin
    from .models import MyModel

    @admin.register(MyModel)
    class MyModelAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'created_at')
    ```

8. **Create a Superuser (Optional)**: To access the admin interface, create a superuser account.

    ```bash
    python manage.py createsuperuser
    ```

9. **Run the Development Server**: Start the Django development server.

    ```bash
    python manage.py runserver
    ```

### Example Usage

Here's how the files would look:

#### `myapp/models.py`

```python
import uuid
from django.db import models

class MyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

#### `myapp/admin.py`

```python
from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
```

### Testing the Model

1. **Access the Admin Interface**: Open a web browser and navigate to `http://127.0.0.1:8000/admin/`. Log in using the superuser account you created.

2. **Add Records**: Add new records to `MyModel` and observe that the primary key is a UUID.

### Summary

Using `UUIDField` as the primary key in Django is straightforward and ensures that each record has a unique identifier, suitable for distributed systems and applications requiring high uniqueness guarantees.
