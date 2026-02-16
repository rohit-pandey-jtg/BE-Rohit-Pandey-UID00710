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
    

class TodoApiStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "first_name", "last_name", "email", "completed_count", "pending_count"]

class TodoApiFiveUsersMaxPendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class TodoApiUsersNPendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class TodoApiFetchUserWiseProjectStatus(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["first_name", "last_name", "email", "to_do_projects", "in_progress_projects", "completed_projects"]