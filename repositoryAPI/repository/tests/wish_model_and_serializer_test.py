from django.test import TestCase, override_settings
from ..models import Wish
from ..serializers import WishSerializer
import tempfile
import io
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestWishModelAndSerializer(TestCase):

	def setUp(self):
		self.wish_data = {
			'title': 'Test Wish',
			'description': 'This is a test wish description.',
			'photo': self.generate_test_image(),
			'is_fulfilled': False,
		}
		self.wish = Wish.objects.create(**self.wish_data)

	def generate_test_image(self):
		file = io.BytesIO()
		image = Image.new('RGB', size=(100, 100), color=(155, 0, 0))
		image.save(file, 'jpeg')
		file.name = 'test.jpg'
		file.seek(0)
		return SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')

	def test_create_wish(self):
		wishes_count = Wish.objects.count()
		Wish.objects.create(**self.wish_data)
		self.assertEqual(Wish.objects.count(), wishes_count + 1)

	def test_get_wish(self):
		wish = Wish.objects.get(pk=self.wish.pk)
		self.assertEqual(wish.title, self.wish_data['title'])
		self.assertEqual(wish.description, self.wish_data['description'])
		self.assertEqual(wish.is_fulfilled, self.wish_data['is_fulfilled'])

	def test_update_wish(self):
		self.wish.title = 'Updated Wish'
		self.wish.is_fulfilled = True
		self.wish.save()

		updated_wish = Wish.objects.get(pk=self.wish.pk)
		self.assertEqual(updated_wish.title, 'Updated Wish')
		self.assertTrue(updated_wish.is_fulfilled)

	def test_delete_wish(self):
		wishes_count = Wish.objects.count()
		self.wish.delete()
		self.assertEqual(Wish.objects.count(), wishes_count - 1)

	def test_str_method(self):
		"""Test the __str__ method of the Wish model."""
		self.assertEqual(str(self.wish), self.wish_data['title'])

	def test_serializer(self):
		serializer = WishSerializer(self.wish)
		data = serializer.data

		self.assertEqual(set(data.keys()),
						 {'id', 'title', 'description', 'photo', 'is_fulfilled', 'created_at', 'views'})
		self.assertEqual(data['title'], self.wish.title)
		self.assertEqual(data['description'], self.wish.description)
		self.assertIsNotNone(data['photo'])
