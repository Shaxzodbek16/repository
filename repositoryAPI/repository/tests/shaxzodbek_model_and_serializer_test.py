from django.test import TestCase, override_settings
from ..models import Person, Wish, Shaxzodbek, YouTube
from ..serializers import ShaxzodbekSerializer
import tempfile
import io
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestModels(TestCase):
	def setUp(self):
		self.person1 = Person.objects.create(
			first_name='John', last_name='Doe', photo=self.generate_test_image(), phone_number='+1234567890',
			birthday='1990-01-01', connected_at='2023-01-01', field='Engineer', where_connected='New York'
		)
		self.person2 = Person.objects.create(
			first_name='Jane', last_name='Smith', photo=self.generate_test_image(),
			birthday='1995-05-15', connected_at='2023-02-15', field='Designer', where_connected='London'
		)

		self.wish1 = Wish.objects.create(
			title='Travel the world', description='I want to see all the wonders of the world.',
			photo=self.generate_test_image()
		)
		self.wish2 = Wish.objects.create(
			title='Learn a new language', description='I want to become fluent in Spanish.',
			photo=self.generate_test_image()
		)

		self.youtube1 = YouTube.objects.create(
			title='First YouTube Video', description='This is my first video on YouTube.',
			link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
		)

		self.shaxzodbek1 = Shaxzodbek.objects.create(
			title='Memory 1', description='A special memory with friends.', photo=self.generate_test_image(),
			category='friends', wish=self.wish1
		)
		self.shaxzodbek1.people.add(self.person1, self.person2)

	def generate_test_image(self):
		file = io.BytesIO()
		image = Image.new('RGB', size=(100, 100), color=(155, 0, 0))
		image.save(file, 'jpeg')
		file.name = 'test.jpg'
		file.seek(0)
		return SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')

	def test_create_shaxzodbek(self):
		self.assertEqual(Shaxzodbek.objects.count(), 1)
		self.assertEqual(self.shaxzodbek1.title, 'Memory 1')

	def test_get_shaxzodbek(self):
		shaxzodbek = Shaxzodbek.objects.get(pk=self.shaxzodbek1.pk)
		self.assertEqual(shaxzodbek, self.shaxzodbek1)

	def test_update_shaxzodbek(self):
		self.shaxzodbek1.title = 'Updated Memory'
		self.shaxzodbek1.save()
		updated_shaxzodbek = Shaxzodbek.objects.get(pk=self.shaxzodbek1.pk)
		self.assertEqual(updated_shaxzodbek.title, 'Updated Memory')

	def test_delete_shaxzodbek(self):
		self.shaxzodbek1.delete()
		self.assertEqual(Shaxzodbek.objects.count(), 0)
