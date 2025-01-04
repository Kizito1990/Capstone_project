from rest_framework import serializers
from .models import Review, User

from rest_framework import serializers
from .models import Review, User, Like

#User Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

#Creating a user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
   # Rview Serializers 
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user', 'created_at', 'likes_count']
        read_only_fields = ['user', 'created_at']

#Ensuring users can't rate above 5
    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
    
#Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'review', 'created_at']

