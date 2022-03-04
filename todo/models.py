from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    what=models.CharField(max_length=255)
    where=models.TextField()
    when=models.DateField()
    time=models.TimeField()
    why=models.TextField(null=True, blank=True)
    how=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.what

    class Meta:
        db_table='To Do List'

class Suggestions(models.Model):
    suggestwhat=models.CharField(max_length=255)
    suggestwhere=models.TextField()
    suggestwhen=models.DateField()
    suggesttime=models.TimeField()
    suggestwhy=models.TextField(null=True, blank=True)
    suggesthow=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.suggestwhat

    class Meta:
        db_table='Suggestions'
