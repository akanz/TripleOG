from django.urls import path
from .views import HomeListView, ProfileListView, ContactListView

urlpatterns = [
    path('', HomeListView.as_view(), name = 'index'),
    path('profile/', ProfileListView.as_view(), name= 'about' ),
    path('contact/', ContactListView.as_view, name= 'contact us'),
]