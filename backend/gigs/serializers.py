from rest_framework import serializers
from .models import Gig, Todo

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ('id', 'title', 'description', 'start_datetime', 'end_datetime')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')