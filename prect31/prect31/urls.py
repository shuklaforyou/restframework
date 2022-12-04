
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',views.Studentlist.as_view()),
    # path('studentapi/',views.StudentListCreate.as_view()),
    path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>',views.RUDStudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrive.as_view()),
    path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>',views.StudentRUD.as_view()),
    path('studentapi/<int:pk>/',views.StudentDelete.as_view()),
]
