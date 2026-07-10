from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, GenreViewSet, CommentViewSet, LikeViewSet, BookmarkViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='review')
router.register('genres', GenreViewSet, basename='genre')
router.register('comments', CommentViewSet, basename='comment')
router.register('likes', LikeViewSet, basename='like')
router.register('bookmarks', BookmarkViewSet, basename='bookmark')


urlpatterns = router.urls