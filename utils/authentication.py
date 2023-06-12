from rest_framework.exceptions import AuthenticationFailed
import jwt
from users.models import User


def extract_user_from_request_jwt(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Unauthenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated")
    print(payload)
    return User.objects.filter(id=payload['id']).first()


def authenticate(request):
    try:
        return extract_user_from_request_jwt(request)
    except AuthenticationFailed:
        return None

