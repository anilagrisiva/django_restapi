from django.shortcuts import render

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def create_employee(request):
    try:
        serializer = EmployeeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        if Employee.objects.filter(email=email).exists():
            return Response({"message": "Employee already exists", "success": False}, status=status.HTTP_200_OK)

        employee = serializer.save()

        return Response({
            "message": "Employee created successfully",
            "regid": f"EMP{employee.id:03d}",
            "success": True
        }, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Exception: {str(e)}")
        return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_employee(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            "message": "Employee updated successfully",
            "success": True
        }, status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return Response({"message": "Employee not found", "success": False}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        print(f"Exception: {str(e)}")
        return Response({"message": "Employee update failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_employees(request):
    try:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response({
            "employees": serializer.data,
            "success": True
        }, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Exception: {str(e)}")
        return Response({"message": "Failed to retrieve employees", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_employee(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)
        employee.delete()

        return Response({
            "message": "Employee deleted successfully",
            "success": True
        }, status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return Response({"message": "Employee not found", "success": False}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        print(f"Exception: {str(e)}")
        return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
















# # views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee
# from .serializers import EmployeeSerializer

# class EmployeeAPIView(APIView):
#     def post(self, request):
#         try:
#             # Validate request data
#             serializer = EmployeeSerializer(data=request.data)
#             if not serializer.is_valid():
#                 return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

#             # Check for duplicate email
#             email = serializer.validated_data['email']
#             if Employee.objects.filter(email=email).exists():
#                 return Response({"message": "Employee already exists", "success": False}, status=status.HTTP_200_OK)

#             # Create employee
#             employee = serializer.save()
            
#             return Response({"message": "Employee created successfully", "regid": f"EMP{employee.id:03d}", "success": True}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
