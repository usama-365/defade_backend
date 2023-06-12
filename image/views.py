from django.http import JsonResponse
from utils.authentication import authenticate
from defade_backend.settings import BASE_DIR, MEDIA_ROOT
from utils.defade_image import check_image
from .models import Image

# Create your views here.
def ImageView(request):
    user = authenticate(request)
    if user:
        # POST
        if request.method == 'POST':
            if request.FILES.get('image'):
                # Extract and save the image
                image = request.FILES['image']
                image_name_updated = f"{user.email}+-+{image.name}"
                image_path = MEDIA_ROOT / image_name_updated
                with open(image_path, 'wb') as f:
                    for chunk in image.chunks():
                        f.write(chunk)

                # Check whether it's deep fake or not
                result = check_image(image_path.resolve().as_posix())

                image_record = Image(user=user, image_name=image_name_updated, result=result)
                image_record.save()

                return JsonResponse({
                    "status": "Success",
                    "result": result
                })
            else:
                return JsonResponse({
                    "status": "Failed",
                    "message": "No files attached"
                })
        # GET
        elif request.method == 'GET':
            images = Image.objects.filter(user=user).all()
            result = {}
            for i in range(len(images)):
                image = images[i]
                result[image.id] = {
                    "url": f"{request.get_host()}/media/{image.image_name}",
                    "created_at": image.created_at
                }
            return JsonResponse({
                "status": "Success",
                "data": result
            })
        # INVALID request
        else:
            return JsonResponse({
                "status": "Failed",
                "message": "Invalid request"
            })
    else:
        return JsonResponse({
            "status": "Unauthenticated"
        })
