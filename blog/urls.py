from django.urls import path
from .import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('tastyroad/<int:tastyroad_id>/', views.detail, name='detail'),
    path('tastyroad/new/', views.tastyroad_new, name='new'),
    path('tastyroad/<int:tastyroad_id>/edit/',views.tastyroad_edit, name='edit'),
    path('tastyroad/<int:tastyroad_id>/delete/',views.tastyroad_delete, name='delete'),
    path('tastyroad/<int:tastyroad_id>/comment/',views.add_comment, name='add_comment'),
    path('tastyroad/<int:tastyroad_id>/delete',views.comment_delete, name="comment_delete"),
    ]