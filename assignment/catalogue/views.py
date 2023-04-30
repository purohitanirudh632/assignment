from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_items(request, *args, **kwargs):
    items = Item.objects.all() 
    serializer = ItemSerializer(items, many=True)
    return Response(data=serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_item(request, *args, **kwargs):
    id = kwargs.get('id')
    item = Item.objects.filter(id__iexact = id)
    if not item.exists():
        return Response(data = {}, status = status.HTTP_404_NOT_FOUND )
    serializer = ItemSerializer(item.first())

    return Response(data = serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_items(request, *args, **kwargs ):
    lookup = kwargs.get("lookup")
    items = None
    if lookup == "best_seller":
        items = Item.objects.filter(is_best_seller = True)
    else:
        items = Item.objects.filter( category__title = lookup )

    if not items.exists():
        return Response(data = [], status = status.HTTP_404_NOT_FOUND)
    serializer = ItemSerializer(items, many=True)
    return Response(data = serializer.data, status=status.HTTP_200_OK)