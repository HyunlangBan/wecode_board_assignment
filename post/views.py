from rest_framework import viewsets
from post.serializers import PostSerializer
from rest_framework.response import Response
from post.models import Post

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer_class = PostSerializer(queryset, many=True)
        return Response(serializer_class.data)
        
    def create(self, request):
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response({'error': 'INVALID REQUEST'})

    def get(self, request, pk=None):
        post = Post.objects.get(pk = pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)
    
    def delete(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        serializer_class = PostSerializer(post)
        password = request.data.get('password', None)
        if password == post.password:
            post.delete()
            return Response({"message":"success"})
        return Response({"error": "invalid password"})

    def update(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        author = request.data.get('author', post.author)
        title = request.data.get('title', post.title)
        content = request.data.get('content', post.content)
        password = request.data.get('password', none)
        if password == post.password:
            post.author = author
            post.title = title
            post.content = content
            post.save()
            serializer_class = PostSerializer(post)
            return Response(serializer_class.data)
        return Response({'error': 'invalid password'})
    

    
