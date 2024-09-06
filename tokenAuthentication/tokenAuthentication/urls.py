from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

from api.tok import CustomAuthToken

# Creating Router Object
router = DefaultRouter()

#Register StudentVIewSet with Router
router.register('studentapi',views.StudentModelViewSet, basename='student')#require username and password to pass

router.register('studentapi-readonly', views.StudentModelViewSet2, basename='student-readonly')#require nothing to pass

router.register('student-token', views.token_auth, basename='student-token')#requires token to pass
router.register('custom-auth', views.Custom_Auth, basename='custom-auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework')),

    # URL to generate token in case of not created, 
    path('gettoken/', CustomAuthToken.as_view()),
]