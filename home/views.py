from rest_framework.generics import CreateAPIView
from .serializers import SignUpSerializers

class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializers
    permission_classes = []




