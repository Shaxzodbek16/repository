from django.db import models
from .choices import catagory_options


class Information(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.Choices(catagory_options)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Information'

