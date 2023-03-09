
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiViewSet, PostCommetApiViewSet, PostLikeApiViewSet, PostFavoriteApiViewSet

router = DefaultRouter()
router.register('posts', PostApiViewSet, basename='posts')
router.register('comment', PostCommetApiViewSet, basename='comments')
router.register('likes', PostLikeApiViewSet, basename='likes')
router.register('favorites', PostFavoriteApiViewSet, basename='favorites')



urlpatterns = router.urls