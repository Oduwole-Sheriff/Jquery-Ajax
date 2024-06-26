import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from jquery_ajax_app.models import Post
from DependentDropDownList.models import Person
from Language.models import Entry

from api.serializer import PostSerializer
from api.serializer import PersonSerializer
from api.serializer import LanguageSerializer

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

class PersonView(APIView):
    def get(self, request):
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)
    
    def put(self, request):
        data = request.data
        try:
            person = Person.objects.get(id=data['id'])
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(objs, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': "this is a Patch request"})

    def delete(self, request):
        data = request.data
        objs = Person.objects.get(id = data['id'])
        objs.delete()
        return Response({'message' : 'post deleted'})

   
class LanguageView(APIView):
    def get(self, request):
        objs = Entry.objects.all()
        serializer = LanguageSerializer(objs, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = LanguageSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)
    
    def put(self, request):
        data = request.data
        try:
            entry = Entry.objects.get(id=data['id'])
        except Entry.DoesNotExist:
            return Response({'error': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LanguageSerializer(entry, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data = request.data
        objs = Entry.objects.get(id = data['id'])
        serializer = LanguageSerializer(objs, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': "this is a Patch request"})

    def delete(self, request):
        data = request.data
        objs = Entry.objects.get(id = data['id'])
        objs.delete()
        return Response({'message' : 'Entry deleted'})
