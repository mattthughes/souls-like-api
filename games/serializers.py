from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'is_owner', 'title', 'slug', 'image', 'description'
        ]
