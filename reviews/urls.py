from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, GenreViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='review')
router.register('genres', GenreViewSet, basename='genre')

urlpatterns = router.urls