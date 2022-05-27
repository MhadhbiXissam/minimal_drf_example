from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer 
from base.models import Person 


@api_view(['GET'])
def get_data(request) : 
	alldata = Person.objects.all() 
	persons = PersonSerializer(alldata , many = True)
	return Response(persons.data)


@api_view(['POST'])
def add_data(request) : 
	ser_person = PersonSerializer(data = request.data) 
	if ser_person.is_valid() : 
		ser_person.save()
	return Response(ser_person.data)

