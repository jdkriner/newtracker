from rest_framework import serializers
from .models import Food
from .models import Records

class Food_serializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'author', 'description', 'calories', 'protein', 'fat', 'carbs')

class Records_serializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('author', 'cals100', 'protein100', 'fat100', 'carbs100', 'food100')
