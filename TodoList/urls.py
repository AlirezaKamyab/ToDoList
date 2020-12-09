from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('crossout/<item_id>', views.crossout, name='cross'),
    path('edit/<item_id>', views.edit, name='edit'),
]