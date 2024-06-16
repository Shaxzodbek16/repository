from django.urls import path
from .views import terms, ShaxzodbekApiView, PersonApiView, YouTubeApiView, WishApiView, GameApiView

urlpatterns = [

	# for API
	path('shaxzodbek/', ShaxzodbekApiView.as_view(), name='shaxzodbek'),
	path('shaxzodbek/<int:pk>', ShaxzodbekApiView.as_view(), name='shaxzodbek-pk'),
	path('person/', PersonApiView.as_view(), name='person'),
	path('person/<int:pk>', PersonApiView.as_view(), name='person-pk'),
	path('wish/', WishApiView.as_view(), name='wish'),
	path('wish/<int:pk>', WishApiView.as_view(), name='wish-pk'),
	path("youtube/", YouTubeApiView.as_view(), name="youtube"),
	path("youtube/<int:pk>", YouTubeApiView.as_view(), name="youtube-pk"),
	path("game/", GameApiView.as_view(), name="game"),
	path("game/<int:pk>", GameApiView.as_view(), name="game-pk"),

	# with templates
	path("terms/", terms, name="terms"),
]
