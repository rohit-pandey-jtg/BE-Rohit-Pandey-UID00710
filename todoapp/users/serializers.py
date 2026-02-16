from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser


# Add your serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]
        
class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "completed_count", "pending_count"]

class FetchFiveUserWithMaxPendingTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class FetchUserWithNPendingTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class FetchUserWiseProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "to_do_projects", "in_progress_projects", "completed_projects"]