# models.py

from django.db import models


class Gym(models.Model):
    """
    Model representing a gym.
    """
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    """
    Model representing a trainer.
    """
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    Model representing a client.
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    """
    Model representing a workout session.
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.client.name} - {self.date}"
