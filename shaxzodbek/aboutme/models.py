from django.db import models
from .choices import catagory_options


class Wish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='wish_images')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Wish'


class People(models.Model):
    firstname = models.CharField(max_length=100,)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    who_is = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, name=True)
    email = models.CharField(max_length=100, blank=True, name=True)
    address = models.CharField(max_length=100, blank=True, name=True)
    city = models.CharField(max_length=100, blank=True, name=True)
    job_title = models.CharField(max_length=100, blank=True, name=True)
    image = models.ImageField(upload_to='people_images')

    def __str__(self):
        return f"My {self.who_is} who is {self.firstname} {self.lastname} was born in {self.birth_date}"

    class Meta:
        db_table = 'People'
        verbose_name = 'People'


class Information(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="information_images")
    category = models.Choices(catagory_options)
    date_created = models.DateTimeField(auto_now_add=True)
    connection = models.ManyToManyField(People, related_name='name', on_delete=models.CASCADE)
    wishes = models.ManyToManyField(Wish, related_name='name', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Information'
        verbose_name = 'Information'
