from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# app_name = 'upload'

urlpatterns = [
    path('', views.filo, name='filo'),
]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)