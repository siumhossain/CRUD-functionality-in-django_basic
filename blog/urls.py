from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:pk>/',views.post_detail,name='post_detail'),
    path('create/',views.post_create,name='create'),
    path('update/<int:pk>',views.post_update,name='update'),
    path('delete/<int:pk>',views.post_delete,name='delete'),
]