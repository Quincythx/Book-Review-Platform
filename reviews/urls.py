from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, GenreViewSet, CommentViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='review')
router.register('genres', GenreViewSet, basename='genre')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls