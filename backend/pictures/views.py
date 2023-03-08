from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PictureSerializer


class PictureUpload(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PictureSerializer
    parser_classes = [MultiPartParser, FormParser]
