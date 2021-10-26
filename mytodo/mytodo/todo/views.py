from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

@api_view(['GET'])
def apiDocumentation(request):
	api_urls = {
            'LIST' : '/person-list',
            'CREATE' : '/person-create'
    };  return Response(api_urls)


@api_view(['GET'])
def personList(request):
	person = Person.objects.all()
	serializer = PersonSerializer(person, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def personCreate(request):
	serializer = PersonSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)