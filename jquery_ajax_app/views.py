from django.shortcuts import render
from .models import Post

from jquery_ajax_app.serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class PostView(APIView):
    def get(self, request):
        objs = Post.objects.all()
        serializer = PostSerializer(objs, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        serializer = PostSerializer(data = data)
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

def PostListView(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'jquery_ajax_app/index.html', context)