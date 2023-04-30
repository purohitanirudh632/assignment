from rest_framework import serializers
from .models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField( source = "category.title")
    class Meta:
        model = Item
        fields = ( 'category', 'title', 'id', 'description', 'image', 'is_best_seller', 'is_available') 