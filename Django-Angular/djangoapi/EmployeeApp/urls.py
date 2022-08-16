from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns=[
    path('employee/', views.SnippetList.as_view()),
   

]