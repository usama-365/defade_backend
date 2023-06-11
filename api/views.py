from django.http import JsonResponse


# Create your views here.
def index(request):
    response = {
        "message": "Hello World"
    }
    return JsonResponse(response)
