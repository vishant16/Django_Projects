from rest_framework import serializers

from .models import UserProfileManager,UserProfile,ProfileFeedItem

class HelloSerializers(serializers.Serializer):

    """serializes a name filed for testing our APIview
    they are similar to django forms """
    name=serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ serializes user profile objects"""

    class Meta:
        model=UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
        'password':{
                'write_only':True,
                'style':{'input_type':'password'}
                }
        }
    def create(self,validated_data):
        """ create and return new user """
        user=UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ serializes profile feed items """

    class Meta:
        model=ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={
        'user_profile':{'read_only':True}}    
