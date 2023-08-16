from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    def __str__(self):
        return "{}".format(self.name)

class Username(models.Model):
    username = models.CharField(max_length=50)
    info = models.TextField(max_length=300, null=True, blank=True)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        ordering = ['username']
    def __str__(self):
        return "{}".format(self.username)