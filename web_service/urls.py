from django.conf.urls.static import static
from FitCalendar.views import *
from django.contrib import admin
from django.urls import path, include
from web_service import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('FitCalendar.urls'))
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404=pageNotFound