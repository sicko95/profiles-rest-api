from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        '''Nisu svi atributi potrebni za priakzivanje svakom korisniku, kao password,
        zato mozemo definisati posebno kako cemo obradaiti takve podatke. Ovde smo definisali
        da se password prikazuje samo prilikom kreiranja ili update-a, i stavili smo mu inputtype password'''

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    #Overridujemo metodu za kreiranje korisnika kako bi smo defilisali da password field ne cuva kao plain teks, vec kao hesiranu vrednost
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
