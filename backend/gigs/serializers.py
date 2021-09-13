from rest_framework import serializers
from .models import Gig, User, Group

class GigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gig
        fields = ('id', 'title', 'description', 'start_datetime', 'end_datetime')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']