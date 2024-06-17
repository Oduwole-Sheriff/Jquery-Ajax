import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from jquery_ajax_app.models import Post
from api.serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class PostView(APIView):
    def get(self, request):
        objs = Post.objects.all()
        serializer = PostSerializer(objs, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data = data)
        # time.sleep(20)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)
    
    def put(self, request):
        data = request.data
        objs = Post.objects.get(id = data['id'])
        serializer = PostSerializer(objs, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        objs = Post.objects.get(id = data['id'])
        serializer = PostSerializer(objs, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': "this is a Patch request"})

    def delete(self, request):
        data = request.data
        objs = Post.objects.get(id = data['id'])
        objs.delete()
        return Response({'message' : 'post deleted'})