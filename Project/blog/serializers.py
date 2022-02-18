from rest_framework import serializers
from .models import Article


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields= ('body',)
