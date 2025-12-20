from rest_framework.response import Response 
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

''' Example for apiview in function base view 
# from rest_framework.decorators import api_view
# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def api_post_view(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(["GET", "PUT", "DELETE"])
# def api_post_detaile(request, id):
#     post = get_object_or_404(Post,id=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"this item temoved succesfully"}, status=status.HTTP_204_NO_CONTENT)
'''

''' Example for ApiView in Class Base View 

# class PostList(APIView):
    # """getting objects"""
    # def get(self, request):
    #     posts = Post.objects.filter(status=True)
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    # """posting objects"""
    # def post(self, request):
    #     serializer = PostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     """ getting post objects """
#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     """ updating post detail """
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     """ removing post """
#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         post.delete()
#         return Response({"detail":"this item temoved succesfully"}, status=status.HTTP_204_NO_CONTENT)
'''

''' Example for GenericApiView in Class Base View  

class PostList(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
'''

class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrive(self, request, pk=None):
        post_object = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        post = get_object_or_404(Post, status=True, pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        post = get_object_or_404(Post, status=True, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        post = Post.objects.filter(status=True, pk=pk)
        post.delete()
        return Response({'detail':'item removed succesfully'}, status=status.HTTP_204_NO_CONTENT)
