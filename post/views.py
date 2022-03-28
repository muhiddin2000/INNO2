from django.shortcuts import render
from rest_framework import filters
from .serializers import PostSerializer, CommentSerializer, PostListSerializer, PostDetailSerializer
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from .permissions import IsAuthorOrReadOnl
from .models import Post, Comment
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


# Create your views here.
# POST
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', 'body']


# GET
# class PostSearch(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^title', 'body']


# PUT and GET

class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdate(RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnl,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# POST
class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# DELETE
class PostDelete(DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnl,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^name', 'messages']
    pagination_class = PostPageNumberPagination


class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDelete(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
