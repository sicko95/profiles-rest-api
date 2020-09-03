from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #Lista status kodova

from . import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapepd mannually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        #serializer objektu dodeljujemo definisanu serializer kalsu sa podacima koje zelimo da prosledimo
        serializers = self.serializer_class(data=request.data)

        #Vrsimo proveru da li je serializer validan
        if serializers.is_valid():
            #Kreiramo atribut koji dobija vrednost validiranog imena iz serializer
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            #Vraca sve errore koji su se pojavili tokom validacije
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
