from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from api_app import views as api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('', include('myapp.urls')),
    path('stuinfo/<int:pk>',api_views.student_detail),
    path('stuinfo/',api_views.student_list),
    path('studentapi/',api_views.StudentAPI.as_view()),
    # path('stuget/',api_views.student_get),
    # path('stucreate/',api_views.student_create),
    # path('student_update/',api_views.student_update),

    


]
