from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated

from .serializers import HelloSerializers,UserProfileSerializer,ProfileFeedItemSerializer
from .models import UserProfile,ProfileFeedItem
from .permissions import UpdateOwnProfile,UpdateOwnStatus


#APIView
class HelloApiView(APIView):
    """ testing apiview """

    serializer_class=HelloSerializers

    def get(self,request,format=None):
        """return list of features of APIView"""
        apiview=[
        'usess http functions(get post patch delete put)',
        'mapped manually to URLs',
        'similar to django view',]
        return Response({'message':'Hello','apiview':apiview})

    def post(self,request):
        """create hello message with name"""
        s=self.serializer_class(data=request.data)  #serializer_class is in APIView
        if s.is_valid():
            name=s.validated_data.get('name')
            msg=f"Hello {name}"
            return Response({'msg':msg})
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """updating objects"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ updating objects partially """  # if we have first name and last name we have raise to change the last name so it will change last name only
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deleting objects"""
        return Response({'method':'DELETE'})




#Viewset

class HelloViewSet(viewsets.ViewSet):
    """ test Api viewset """

    serializer_class=HelloSerializers
    def list(self,request):
        """return hello message"""
        viewset=[
        'action (list,create,retrieve,update,partial_update)',
        'automatic map with urlusing routers',
        'provides more functionality with less code ']
        return Response({'message':'Hello','viewset':viewset})

    def create(self,request):
        """create new hello msg"""
        s=self.serializer_class(data=request.data)
        if s.is_valid():
            name=s.validated_data.get('name')
            m=f'Hello {name}'
            return Response({'message':m})
        else:
            return Response(s.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ getting object by id """
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ update objects"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """ update object partially """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """ handle removing an object """
        return Response({'http_method':'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """ handle creating and updating profiles """
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    authentication_class=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """ creating user tokens """
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """creating editing reading fedd """
    authentication_class=(TokenAuthentication,)
    serializer_class= ProfileFeedItemSerializer
    queryset=ProfileFeedItem.objects.all()
    permission_classes=(UpdateOwnStatus,IsAuthenticated, )


    def perform_create(self,serializer):
        """ sets the user profile to the loggef in user"""
        serializer.save(user_profile=self.request.user)
