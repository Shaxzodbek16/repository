from django.test import TestCase, Client
from ..models import YouTube
from ..serializers import YouTubeSerializer


class TestYoTube(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.youtube1 = YouTube.objects.create(title="YouTube title 1", description="YouTube description 1", link="https://www.youtube.com/link1")
        self.youtube2 = YouTube.objects.create(title="YouTube title 2", description="YouTube description 2", link="https://www.youtube.com/link2")
        self.youtube1 = YouTubeSerializer(self.youtube1)
        self.youtube2 = YouTubeSerializer(self.youtube2)

    def test_get_youtube(self):
        response = self.client.get("/api/youtube/")
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0], self.youtube1.data)
        self.assertEqual(response.data[1], self.youtube2.data)

    def test_post_youtube(self):
        response = self.client.post("/api/youtube/")
        self.assertEqual(response.status_code, 400)

    def test_put_youtube(self):
        response = self.client.put("/api/youtube/")
        self.assertEqual(response.status_code, 404)

    def test_delete_youtube(self):
        response = self.client.delete("/api/youtube/1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.data), 1)
