from dj_rest_auth import views
from django.http import Http404

from rest_framework import request, viewsets
from rest_framework import filters
from .serializers import PostSerializer, CommentSerializer, PostListSerializer, PostDetailSerializer
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, get_object_or_404
from .permissions import IsAuthorOrReadOnl
from .models import Post, Comment
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.response import Response


# Create your views here.
# POST
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', 'body']


class PostPopularList(ListAPIView):
    queryset = Post.objects.all().order_by('-count_seen')[:7]
    serializer_class = PostListSerializer


class PostBannerList(ListAPIView):
    queryset = Post.objects.all().order_by('-count_seen')[:3]
    serializer_class = PostListSerializer


class PostDetail(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        obj.count_seen = obj.count_seen + 1
        obj.save()
        serializer = PostDetailSerializer(obj)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


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
