from rest_framework import serializers # type: ignore
from .models import BlogPost # type: ignore


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]
