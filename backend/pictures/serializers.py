from rest_framework.serializers import ModelSerializer
from.models import Picture


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = ["title", "picture", "uploaded_at"]
        read_only_fields = ["uploaded_at"]
        extra_kwargs = {
            "picture": {
                "use_url": True,
                "allow_empty_file": False,
            }
        }
