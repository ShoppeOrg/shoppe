from rest_framework.serializers import ModelSerializer, ImageField
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

    def to_representation(self, instance):
        result = super().to_representation(instance)
        return {
            "id": instance.id,
            "title": result["title"],
            "url": result["picture"],
            "uploaded_at": result["uploaded_at"]
        }