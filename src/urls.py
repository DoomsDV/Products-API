import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import productions
from dotenv import load_dotenv

load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.urls')),
]

if os.environ.get('DJANGO_ENV') == 'production':
    urlpatterns += static(productions.MEDIA_URL,
                          document_root=productions.MEDIA_ROOT)
