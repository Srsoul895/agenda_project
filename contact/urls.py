from django.urls import path, include
from contact import views as contact_views


urlpatterns = [
    path('search/', contact_views.search, name='search'),
    path('', contact_views.home, name='home'),

    path('contact/<int:id_contact>/detail/', contact_views.contact, name='contact'),
    path('contact/create/', contact_views.create, name='create'),
    path('contact/<int:id_contact>/update/', contact_views.update, name='update'),
    path('contact/<int:id_contact>/delete/', contact_views.delete, name='delete'),
]