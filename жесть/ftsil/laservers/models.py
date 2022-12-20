from django.db import models

class Servers(models.Model):
    title = models.CharField('Name', max_length=40)
    date = models.DateTimeField('Time', max_length=20)
    type = models.CharField('Type', max_length=20)
    email = models.TextField('Feedback', max_length=320)
    group = models.CharField('Group of Servers', max_length=100)
    stype = models.CharField('Type of group', max_length=30)
    location = models.CharField('Location', max_length=100)


    def __str__(self):
        return f'Servers: {self.title}'