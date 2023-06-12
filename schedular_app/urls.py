from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('dashboard/<task_title>',views.dashboard,name='dashboard'),
    path('alltask/',views.alltask,name='alltasks'),
    path('newtask/',views.new_task,name='newtask'),
    path('notification/',views.notifications,name='notifications'),
    path('signout/',views.signout,name='signout'),
    path('complete/<int:id>',views.complete,name='complete'),
    path('delete/<title>', views.delete, name='delete'),
]