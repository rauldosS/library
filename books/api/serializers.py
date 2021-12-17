from rest_framework import serializers
from books import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = ['title', 'author', 'release_year', 'state', 'pages', 'publishing_company', 'create_at']