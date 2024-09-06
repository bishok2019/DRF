from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
# Creating Router Object
router = DefaultRouter()
#Register StudentVIewSet with Router
router.register('studentapi',views.StudentModelViewSet1, basename='student')

#Browsable API
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name = 'token_obtain_pair_view'),
    path('refreshtoken/', TokenRefreshView.as_view(), name = 'token_refresh_view'),
    path('verifytoken/', TokenVerifyView.as_view(), name = 'token_verify_view'),
    ]