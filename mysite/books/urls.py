from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.base,name='base'),
    #Url para Registrar user
    path('signup',views.signup,name="signup"),
    #URL para Logiar 
    path('signin',views.signin,name="signin"),
    #URL para Tares de los users
    path('tasks/',views.tasks_list_pending,name="tasks"),
    path('tasks_completed/',views.tasks_completed,name="task_completed"),
    path('create_task/',views.create_task,name="create_task"),
    path('task_detail/<int:task_id>/',views.task_detail,name="task_detail"),
    path('task_detail/<int:task_id>/complete',views.completed_task,name="completed_task"),
    path('task_delete/<int:task_id>',views.delete_task,name="delete_task"),
    #URl para cerrar la cessión 
    path('logout',views.cerrar_sesion,name="logout"),
    
    
]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)