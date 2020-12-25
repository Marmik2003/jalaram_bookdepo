from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_pub', views.PublisherAdd.as_view(), name='add_pub'),
    path('edit_pub/<int:pk>', views.PubCommonEdit.as_view(), name='edit_pub'),
    path('edit_ctg/<int:pk>', views.CategoryCommonEdit.as_view(), name='edit_ctg'),
    path('publisher_delete/<int:pub_id>', views.publisher_delete, name='publisher_delete'),
    path('category_delete/<int:ctg_id>', views.category_delete, name='category_delete'),
    path('add_book', views.BookAdd.as_view(), name='add_book'),
    path('edit_book/<int:pk>', views.BookEdit.as_view(), name='edit_book'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('booked_orders_list', views.booked_orders_list, name='booked_orders_list'),
    path('view_selling_reports', views.view_selling_reports, name='view_selling_reports'),
    path('view_buying_reports', views.view_buying_reports, name='view_buying_reports'),
    path('view_customer_list', views.view_customer_list, name='view_customer_list'),
]