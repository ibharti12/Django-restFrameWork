from django.urls import path
from .views import user_list, create_user, get_user, update_user, delete_user

urlpatterns = [
    path('', user_list, name='user_list'),  
    path('create/', create_user, name='create_user'), 
    path('<int:id>/', get_user, name='get_user'),  
   
    path('update_user/<int:id>/', update_user, name='update_user'),
    path('delete_user/<int:id>/', delete_user, name='delete_user'),
]
