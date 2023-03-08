from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import PictureSerializer


class PictureUpload(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PictureSerializer
    parser_classes = [MultiPartParser, FormParser]
