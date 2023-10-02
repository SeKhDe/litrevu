from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ticket_create



urlpatterns = [
    path('ticket/create', ticket_create, name='ticket-create'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)