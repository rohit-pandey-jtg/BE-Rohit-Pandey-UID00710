from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo
from users.serializers import UserSerializer

# Add your serializer(s) here
class TodoSerializer(serializers.ModelSerializer):
    creator = UserSerializer(source="users", read_only=True)
    status = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["id", "name", "creator"]

    def get_status(self, obj):
        return "Done" if obj.done else "To Do"
    
    def get_created_at(self, obj):
        return obj.date_created.strftime("%I:%M %p, %d %b, %Y")