from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_pub', views.PublisherAdd.as_view(), name='add_pub'),
    path('edit_pub/<int:pk>', views.PublisherEdit.as_view(), name='edit_pub'),
    path('publisher_delete/<int:pub_id>', views.publisher_delete, name='publisher_delete'),
]