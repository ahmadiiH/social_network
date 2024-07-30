from rest_framework.views import APIView
from .serializers import PostSerializers
from .models import  Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def get(self,request , post_pk):
        try:
          post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializers(post)
        return Response(serializer.data)

class PostListView(APIView):
    def get(self,request, pk):
        posts =Post.objects.filter(is_active= True)
        serializer = PostSerializers(posts , many=True)
        return Response(serializer.data)

