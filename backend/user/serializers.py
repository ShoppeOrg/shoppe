from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer


class TokenResponseSerializer(Serializer):
    def to_representation(self, instance):
        user_id = self.initial_data["user_id"]
        user = get_user_model().objects.get(pk=user_id)
        return {"token": self.initial_data["key"], "username": user.username}
