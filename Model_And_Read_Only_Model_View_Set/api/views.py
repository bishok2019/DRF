from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer  # Ensure this is set correctly
    authentication_classes = [SessionAuthentication]    
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if not self.serializer_class:
            raise AssertionError("serializer_class is not set!")
        print(f"Serializer Class: {self.serializer_class}")
        return self.serializer_class
    
# class StudentModelViewSet2(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer  # Ensure this is set correctly
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [IsAdminUser]


#     def get_serializer_class(self):
#         if not self.serializer_class:
#             raise AssertionError("serializer_class is not set!")
#         print(f"Serializer Class: {self.serializer_class} ")
#         return self.serializer_class
