from rest_framework import serializers
from .models import Genre, Review, Comment, Like, Bookmark


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', write_only=True
    )
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'genre', 'genre_id', 'book_title', 'author',
            'review_text', 'rating', 'image', 'like_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_like_count(self, obj):
        return obj.likes.count()
    


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'review', 'user', 'text', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'review', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'review', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']