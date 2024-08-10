from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet)
router.register("directors", views.DirectorViewSet)
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)


urlpatterns = router.urls
