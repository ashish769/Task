from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "updated_at",
            "is_published",
        ]
        read_only_fields = ["author", "created_at", "updated_at"]
