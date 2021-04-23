from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None


class RegisterSerializer(RegisterSerializer):
    username = None
