from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
