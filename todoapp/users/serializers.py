from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser
from projects.models import Project


# Add your serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]
        
class UserStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "completed_count", "pending_count"]

class FetchFiveUserWithMaxPendingTodoSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class FetchUserWithNPendingTodoSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class FetchUserWiseProjectStatusSerializer(serializers.ModelSerializer):
    to_do_projects = serializers.ListField(child=serializers.CharField())
    in_progress_projects = serializers.ListField(child=serializers.CharField())
    completed_projects = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "to_do_projects", "in_progress_projects", "completed_projects"]

class MemberReportSerializer(serializers.ModelSerializer):
    pending_count =   serializers.IntegerField()
    completed_count = serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "pending_count", "completed_count"]

class ProjectReportSerializer(serializers.ModelSerializer):
    report = MemberReportSerializer(source = "computed_members_data", many = True)
    project_title = serializers.CharField(source = "name")
    class Meta:
        model = Project
        fields = ["project_title", "report"]



class UserApiSerializer(serializers.ModelSerializer):
    password  = serializers.CharField()
    class Meta:
        model = CustomUser
        fields=["email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

