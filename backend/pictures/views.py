from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser

from .serializers import PictureSerializer


class PictureUpload(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PictureSerializer
    parser_classes = [MultiPartParser, FormParser]
