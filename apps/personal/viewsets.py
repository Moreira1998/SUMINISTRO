from apps.personal.models import Personal, Area, Rol
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets


#  ------------------------------------------------------->
# Rest User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  ------------------------------------------------------->
# Rest Personal


class PersonalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'


class PersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

#  ------------------------------------------------------->
# Rest Rol


class RolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class RolViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


#  ------------------------------------------------------->
# Rest Area


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class AreaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
