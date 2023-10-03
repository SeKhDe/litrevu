from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ticket_create, ticket_update, ticket_delete, ticket_test



urlpatterns = [
    path('ticket/create', ticket_create, name='ticket-create'),
    path('ticket/<int:id>/update', ticket_update, name='ticket-update'),
    path('ticket/<int:id>/delete', ticket_delete, name='ticekt-delete'),
    path('ticket/test', ticket_test, name='ticket-test'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)