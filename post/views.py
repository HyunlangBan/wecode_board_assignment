from rest_framework import viewsets
from post.serializers import PostSerializer
from rest_framework.response import Response
from post.models import Post

class PostViewSet(viewsets.ViewSet):
    def get(self, request):
        queryset = Post.objects.all()
        serializer_class = PostSerializer(queryset, many=True)
        return Response(serializer_class.data)
        
    def create(self, request):
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response({'error': 'INVALID REQUEST'})

class DetailViewSet(viewsets.ViewSet):

    def get(self, request, pk):
        post = Post.objects.get(id = pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)
    
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer_class = PostSerializer(post)
        password = request.data.get('password', None)
        if password == post.password:
            post.delete()
            return Response(serializer_class.data)
        return Response({"error": "INVALID PASSWORD"})

    def update(self, request, pk):
        post = Post.objects.get(id=pk)
        author = request.data.get('author', post.author)
        title = request.data.get('title', post.title)
        content = request.data.get('content', post.content)
        password = request.data.get('password', None)
        if password == post.password:
            post.author = author
            post.title = title
            post.content = content
            post.save()
            serializer_class = PostSerializer(post)
            return Response(serializer_class.data)
        return Response({'error': 'INVALID PASSWORD'})
