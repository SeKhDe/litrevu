from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #TICKETS
    path('ticket/create', views.ticket_create, name='ticket-create'),
    path('ticket/<int:id>/update', views.ticket_update, name='ticket-update'),
    path('ticket/<int:id>/delete', views.ticket_delete, name='ticekt-delete'),
    path('ticket/test', views.ticket_test, name='ticket-test'),
    #REVIEWS
    path('review/create', views.review_create, name='review-create'),
    path('review/create-response', views.review_create_response, name='review-create-response'),
    path('review/<int:id>/update', views.review_update, name='review-update'),
    path('review/<int:id>/delete', views.review_delete, name='review-delete'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)