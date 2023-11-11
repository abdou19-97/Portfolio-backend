from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Post, Comment
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, status
from .serializers import PostSerializer, CommentSerializer
# importing jasonresponse
from django.http import JsonResponse

# Create your views here.
# Create class for Post and Comment views
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def comments(self, request, pk=None):
        post = self.get_object()
        if request.method == 'GET':
            comments = post.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer


@api_view(['POST'])
def comment_create(request, pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, safe=False)
    
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(serializer.errors, safe=False)


# @api_view(['GET'])
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)

# # the purpose of this function is to get all the comments for a post
# @api_view(['GET'])
# def comment_list(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()  # Use the related name to get all comments
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)
