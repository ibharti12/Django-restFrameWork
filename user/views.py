from django.http import JsonResponse
from user.models import User
from user.forms import UserForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt  
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        # Prepare data in the format you need
        user_data = [{"id": user.id, "first_name": user.first_name, "last_name": user.last_name, 
                      "email": user.email, "contact": user.contact, "address": user.address} for user in users]
        return JsonResponse({"users": user_data}, safe=False)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"message": "User created successfully"}, status=201)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            print(form.errors)

            return JsonResponse({"error": form.errors}, status=400)

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"message": "User created successfully"}, status=201)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            return JsonResponse({"error": "Invalid data"}, status=400)

# GET request by id
@require_http_methods(["GET"])
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "contact": user.contact,
            "address": user.address
        }
        return JsonResponse({"user": user_data}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


# update User by ID
@csrf_exempt
def update_user(request, id):
    if request.method != 'PUT':
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    try:
        data = json.loads(request.body)
        for key, value in data.items():
            if hasattr(user, key):  
                setattr(user, key, value)
       
        user.save()
        return JsonResponse({"message": "User updated successfully"}, status=200)
       
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)


# Delete a user
@csrf_exempt
def delete_user(request, id):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
    try:
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
