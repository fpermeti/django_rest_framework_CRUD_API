
from django.http import request, Http404
from django.shortcuts import render
from pages.models import Book
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from pages.serializer import BookSerializer


def base(request):
    return render(request, 'base.html')


# this function is used in order to avoid code duplication
def get_object(id):
    try:
        obj = Book.objects.get(id=id)
        return obj
    except Book.DoesNotExist:
        raise Http404


# function based view
@csrf_exempt
# this decorator is used in order to return a Response, otherwise without it we should return a JsonResponse
@api_view(['GET', 'POST'])
def funcbased(request):
    if request.method == "GET":
        obj = Book.objects.all().order_by('id')
        serializer_obj = BookSerializer(obj, many=True)
        return Response(serializer_obj.data)
    elif request.method == "POST":
        data = request.data
        serializer_obj = BookSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        else:
            return Response(serializer_obj.errors)


# function based view
@csrf_exempt
# this decorator is used in order to return a Response, otherwise without it we should return a JsonResponse
@api_view(['GET', 'PUT', 'DELETE'])
def funcbasedid(request, id):
    if request.method == "GET":
        obj = get_object(id)
        serializer_obj = BookSerializer(obj)
        return Response(serializer_obj.data)
    elif request.method == "PUT":
        data = request.data
        obj = get_object(id)
        serializer_obj = BookSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        else:
            return Response(serializer_obj.errors)
    elif request.method == "DELETE":
        obj = get_object(id)
        obj.delete()
        return Response({"response": "Book was successfully deleted"})


# class based view(GET ALL, POST)
class BooksApi(APIView):

    def get(self, request):
        obj = Book.objects.all().order_by('id')
        serializer_obj = BookSerializer(obj, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        data = request.data
        serializer_obj = BookSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)


# class based view(GET BY ID, PUT, DELETE)
class BooksApiById(APIView):

    # this function is used in order to avoid code duplication
    def get_object(self, id):
        try:
            obj = Book.objects.get(id=id)
            return obj
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id):
        obj = self.get_object(id)
        serializer_obj = BookSerializer(obj)
        return Response(serializer_obj.data)

    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = BookSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "Book was successfully deleted"})
