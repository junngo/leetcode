1) proxy the request form 3000 to 8000
- added react package.json
- "proxy": "http://localhost:8000",

2) Install django-cors-headers
- pip install django-cors-headers

3) Add 'corsheaders' to INSTALLED_APPS
- at base.py

4) Add 'corsheaders.middleware.CorsMiddleware' before 'CommonMiddleware'
- at base.py

5) Add CORS_ORIGIN_ALLOW_ALL = True on base settings
- at base.py

6) Make Django load the bundles as static files with 'str(ROOT_DIR.path('frontend', 'build', 'static'))'
- at base.py

7) Create a views.py file on 'honey_lang' folder.

8) Create ReactAppView that reads the file.

9) Add the ReactAppView as a URL
