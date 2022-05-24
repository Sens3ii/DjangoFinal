from rest_framework import serializers

from api.models import User, Book


class UserBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_joined', 'avatar', 'date_of_birth', 'password']


class BookSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'name',
            'price',
            'description',
            'created_at',
            'num_pages',
            'genre'
        ]


class JournalSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'name',
            'price',
            'description',
            'created_at',
            'type',
            'publisher'
        ]
