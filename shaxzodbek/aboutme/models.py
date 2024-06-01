from django.db import models
from .choices import catagory_options


class Wish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/wish_images')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Wish'


class People(models.Model):
    firstname = models.CharField(max_length=100, )
    lastname = models.CharField(max_length=100, )
    birth_date = models.DateField()
    who_is = models.CharField(max_length=100, )
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/people_images')

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'People'


class Information(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/information_images")
    category = models.CharField(max_length=50, choices=catagory_options)
    date_created = models.DateTimeField(auto_now_add=True)
    connection = models.ManyToManyField(People, blank=True)
    wishes = models.ManyToManyField(Wish, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Information'
