from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
# from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer, UserDetailSeerializer
from apps.users.permissions import UserPermission

class UserApiViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )


    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSeerializer
        
        return UserSerializer