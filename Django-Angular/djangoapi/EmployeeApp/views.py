from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Employees
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework import status



class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Employees.objects.all()
        serializer = EmployeeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























# from EmployeeApp.models import Departments,Employees
# # Create your views here.

# @csrf_exempt
# def departmentApi(request,id=0):
#     if request.method=='GET':
#         departments = Departments.objects.all()
#         departments_serializer = DepartmentSerializer(departments, many=True)
#         return JsonResponse(departments_serializer.data, safe=False)
#     elif request.method=='POST':
#         department_data=JSONParser().parse(request)
#         department_serializer = DepartmentSerializer(data=department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add.", safe=False)

#     elif request.method=='PUT':
#         department_data = JSONParser().parse(request)
#         department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
#         department_serializer=DepartmentSerializer(department,data=department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         department=Departments.objects.get(DepartmentId=id)
#         department.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)
