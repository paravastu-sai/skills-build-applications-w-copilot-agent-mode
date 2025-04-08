from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    members = serializers.JSONField()

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    activity_type = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
