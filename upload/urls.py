from .views import upload_file_view
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'upload'

urlpatterns = [
    path('', upload_file_view, name='upload_view'),
]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)