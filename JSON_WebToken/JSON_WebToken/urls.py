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
#Get Token
# http POST http://127.0.0.1:8000/gettoken/ username="User_1" password="Nouser@123"

#Verify Token with access token
# http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDc4MzY5LCJpYXQiOjE3MjU0NzgwNjksImp0aSI6ImUyNzUxYTRjZTUyYTQ3YjI4NWFhM2I3NjQ0NTI2MjVhIiwidXNlcl9pZCI6Mn0.rEQ8SM0c7Ggq9NhiA9uE3jI7bAQZ4UuOuYlbEwlGi_Y"

# Refresh Access Token with Refresh token
# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2NDQ2OSwiaWF0IjoxNzI1NDc4MDY5LCJqdGkiOiIwMTA3NTdlZGU5YTM0ZTNiOTQxOGNkMjRiYmM2NDgxYyIsInVzZXJfaWQiOjJ9.76j-A0edY4dlJ30jWWpG3aa9uCvVtouEyzM_UEJ1Y7k"

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDc4MzY5LCJpYXQiOjE3MjU0NzgwNjksImp0aSI6ImUyNzUxYTRjZTUyYTQ3YjI4NWFhM2I3NjQ0NTI2MjVhIiwidXNlcl9pZCI6Mn0.rEQ8SM0c7Ggq9NhiA9uE3jI7bAQZ4UuOuYlbEwlGi_Y",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2NDQ2OSwiaWF0IjoxNzI1NDc4MDY5LCJqdGkiOiIwMTA3NTdlZGU5YTM0ZTNiOTQxOGNkMjRiYmM2NDgxYyIsInVzZXJfaWQiOjJ9.76j-A0edY4dlJ30jWWpG3aa9uCvVtouEyzM_UEJ1Y7k"
}
