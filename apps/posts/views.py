from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from apps.posts.models import Post, PostComment, PostLike, PostFavorite
from apps.posts.serializers import PostSerializer, PostDetailserializer, PostCommentSerializer, PostLikeSerializer, PostFavoriteSerializer
from .permissions import PostPermission

class PostApiViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission, )

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailserializer
        return PostSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class PostCommetApiViewSet(GenericViewSet,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (PostPermission, )


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class PostLikeApiViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action in ('retrieve'):
            return PostDetailserializer
        return PostSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class PostFavoriteApiViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin):
    queryset = PostFavorite
    serializer_class = PostFavoriteSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    
    