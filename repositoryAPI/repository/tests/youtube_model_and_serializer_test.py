from django.test import TestCase, Client
from ..models import YouTube
from ..serializers import YouTubeSerializer


class TestYouTubeModelAndSerializer(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.youtube1 = YouTube.objects.create(
            title="YouTube title 1", description="YouTube description 1", link="https://www.youtube.com/link1"
        )
        self.youtube2 = YouTube.objects.create(
            title="YouTube title 2", description="YouTube description 2", link="https://www.youtube.com/link2"
        )
        self.youtube1_data = YouTubeSerializer(self.youtube1).data
        self.youtube2_data = YouTubeSerializer(self.youtube2).data

    def test_get_youtube_list(self):
        response = self.client.get("/api/youtube/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, [self.youtube1_data, self.youtube2_data])

    def test_post_youtube(self):
        new_youtube_data = {
            "title": "New YouTube Video",
            "description": "This is a new video description",
            "link": "https://www.youtube.com/newlink"
        }
        response = self.client.post("/api/youtube/", data=new_youtube_data, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_put_youtube(self):
        update_data = {'title': 'updated youtube title'}
        response = self.client.put(f"/api/youtube/{self.youtube1_data['id']}/", update_data, content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_delete_youtube(self):
        response = self.client.delete(f"/api/youtube/{self.youtube1_data['id']}")
        self.assertEqual(response.status_code, 204)

    def test_post_youtube_invalid_data(self):
        invalid_data = {"title": "Invalid Video", "description": "This is invalid."}
        response = self.client.post("/api/youtube/", data=invalid_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_put_nonexistent_youtube(self):
        update_data = {'title': 'updated youtube title'}
        response = self.client.put("/api/youtube/999/", update_data, content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_youtube(self):
        response = self.client.delete("/api/youtube/999/")
        self.assertEqual(response.status_code, 404)

    def test_title_length_validation(self):
        long_title = "This is a very long title that exceeds the 100-character limit " * 5
        data = {"title": long_title, "description": "Test description", "link": "https://example.com"}
        response = self.client.post("/api/youtube/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_get_single_youtube(self):
        response = self.client.get(f"/api/youtube/{self.youtube1.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.youtube1_data)
