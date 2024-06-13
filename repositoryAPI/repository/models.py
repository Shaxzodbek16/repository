from django.db import models


class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20, null=True, blank=True)
	photo = models.ImageField(upload_to='people/%Y/%m/%d/')
	birthday = models.DateField(null=True, blank=True)
	connected_at = models.DateField()
	field = models.CharField(max_length=50, null=True, blank=True)
	where_connected = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		db_table = 'Person'
		verbose_name = 'Person'


class Wish(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	photo = models.ImageField(upload_to='wish/%Y/%m/%d/')
	is_fulfilled = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return {self.title}

	class Meta:
		db_table = 'Wish'
		verbose_name = 'Wish'
		verbose_name_plural = 'Wishes'


class Shaxzodbek(models.Model):
	categories = (
		("shaxzodbek", "Shaxzodbek"),
		("wish", "Wish"),
		("people", "People"),
		("study", "Study"),
		("family", "Family"),
		("friends", "Friends"),
		("love", "Love")
	)

	title = models.CharField(max_length=100)
	description = models.TextField()
	photo = models.ImageField(upload_to='shaxzodbek/%Y/%m/%d/')
	created_at = models.DateTimeField(auto_now_add=True)
	views = models.PositiveIntegerField(default=0)
	people = models.ManyToManyField(Person)
	category = models.CharField(max_length=15, choices=categories, default=categories[0][1])
	wish = models.ForeignKey(Wish, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return {self.title}

	class Meta:
		db_table = 'Shaxzodbek'


class YouTube(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	link = models.URLField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return {self.title}

	class Meta:
		db_table = 'YouTube'
		verbose_name = 'YouTube'
