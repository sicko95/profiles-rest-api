from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #Lista status kodova
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrive(self, request, pk=None):
        """Retrives specific object by id"""
        return Response({'httl_method': 'GET'})


    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'httl_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'httl_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'httl_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    '''Ovim Django REST sam obavlja sve funckije za CRUD, nije potrebno definisati takve funcije, sem u slucaju overrideovanja '''

    '''Autentifikacija pomocu tokena, i permisija pomocu nase kreirane permisije klase'''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    '''Dodavanje filter_backenda za filtriranje prikaza i definisanja polja (search_fields) koja zelimo da filtriramo'''
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentication tokens'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
