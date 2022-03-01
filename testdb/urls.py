from django.urls import include, path
from .views import TeacherCreate, TeacherList, TeacherDetail, TeacherUpdate, TeacherDelete


urlpatterns = [
    path('create/', TeacherCreate.as_view(), name='create-customer'),
    path('', TeacherList.as_view()),
    path('<int:pk>/', TeacherDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', TeacherUpdate.as_view(), name='update-customer'),
    path('delete/<int:pk>/', TeacherDelete.as_view(), name='delete-customer')
]
