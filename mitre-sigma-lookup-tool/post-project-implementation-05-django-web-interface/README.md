## Post Project Implmentation #5: Django web interface setup
- This implementation required creating the Djano project structure and all commands are detailed below

### 1. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```
### 2. Create the Django layout
```bash
pip install django
django-admin startproject security_lookup_project .
python manage.py startapp lookup
```
Note: You can name these components whatever you prefer but here `security_lookup_project` represents the primary configuration project directory, and `lookup` represents the specific application module

### 3. Add your app to the `INSTALLED_APPS` block in `security_lookup_project/settings.py`
```python
INSTALLED_APPS = [
    # other apps go here
    'lookup',
]
```
- After completing the above steps, I refactored the backend logic into a Django View in `lookup/views.py` and created the web frontend layout (which is the search bar) inside `lookup/templates/lookup/index.html`

- For creating `index.html` these were the commands
```bash
mkdir -p lookup/templates/lookup
touch lookup/templates/lookup/index.html
```
- I also hooked up my URL routing path in `lookup/urls.py`. To create the file, just type `touch lookup/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_dashboard, name='dashboard'),
]
```
- What this code is doing is if a user types in `http://localhost:8000/`, Django receives the incoming HTTP `GET /` request and this path matches the empty string rule `''` and so Django calls the `search_dashboard(request)` view controller and then in `views.py`, the backend calls `render(request, 'lookup/index.html', context)` which injects the threat datasets into the template and sends that information to the HTML browser to display the content
- Then I added this code in `security_lookup_project/urls.py` which basically points to `lookup/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')),
]
```
### 4. Start the local development deployment environment server engine
```bash
python manage.py migrate
python manage.py runserver
```
### Demo
<img width="800" height="434" alt="Mitre_Demo" src="https://github.com/user-attachments/assets/7f2309a3-e114-4641-b3ce-06460b6f6488" />




