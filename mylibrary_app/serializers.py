from rest_framework import serializers
from mylibrary_app.models import Libraries

class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libraries
        fields= ('username', 'password', 'books', 'price_of_books', 'budget', 'time_update')