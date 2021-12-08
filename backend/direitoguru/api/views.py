from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import FeedSerializer
from django.shortcuts import render, redirect
from .models import Feed
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404


@api_view(['GET', 'POST'])
def api_feed(request, feed_id):
    try:
        feed = Feed.objects.get(id=feed_id)
    except Feed.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_feed_data = request.data
        feed.area = new_feed_data['area']
        feed.duvida = new_feed_data['duvida']
        feed.data = new_feed_data['data']
        feed.save()
        
    else:
        serialized_feed = FeedSerializer(feed)
        return Response(serialized_feed.data)


@api_view(['GET', 'POST'])
def api_feeds(request):
    if request.method == 'POST':
        feed = Feed()
        new_feed_data = request.data
        feed.area = new_feed_data['area']
        feed.duvida = new_feed_data['duvida']
        feed.data = new_feed_data['data']
        feed.save()
      
    feeds = Feed.objects.all()
    print(feeds)
    serialized_feed = FeedSerializer(feeds, many=True)
    return Response(serialized_feed.data)
    
def gotominhalista(request):
    return HttpResponse("Olá! Visite a lista de feeds na url:  ")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

