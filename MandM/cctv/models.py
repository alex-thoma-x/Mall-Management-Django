from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length = 200)

    def __str__(self):
        return self.name