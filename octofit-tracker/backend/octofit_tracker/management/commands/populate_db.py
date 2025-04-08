from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu', 'zerocool@mhigh.edu']),
            Team(name='Gold Team', members=['crashoverride@mhigh.edu', 'sleeptoken@mhigh.edu']),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user='thundergod@mhigh.edu', activity_type='Cycling', duration=60),
            Activity(user='metalgeek@mhigh.edu', activity_type='Crossfit', duration=120),
            Activity(user='zerocool@mhigh.edu', activity_type='Running', duration=90),
            Activity(user='crashoverride@mhigh.edu', activity_type='Strength', duration=30),
            Activity(user='sleeptoken@mhigh.edu', activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='thundergod@mhigh.edu', points=100),
            Leaderboard(user='metalgeek@mhigh.edu', points=90),
            Leaderboard(user='zerocool@mhigh.edu', points=95),
            Leaderboard(user='crashoverride@mhigh.edu', points=85),
            Leaderboard(user='sleeptoken@mhigh.edu', points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
