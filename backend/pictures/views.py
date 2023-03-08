from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import PictureSerializer

# class PictureUpload(APIView):
#     permission_classes = [IsAdminUser]
#
#     def post(self, request):
#         serializer = PictureSerializer(data=request.data)
#         if serializer.is_valid()
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=HTTP_201_CREATED
#             )
#         return Response(status=HTTP_400_BAD_REQUEST)


class PictureUpload(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PictureSerializer
