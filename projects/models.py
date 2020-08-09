from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    