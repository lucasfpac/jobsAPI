from rest_framework import serializers # type: ignore
from .models import JobPost


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ["id", "title", "amount", "type", "date", "WO"]
