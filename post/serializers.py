from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    author = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'about', 'body', 'image', 'create_at')

    def get_author(self, obj):
        return str(obj.author.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostListSerializer(ModelSerializer):
    author = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'about', 'image', 'author')

    def get_author(self, obj):
        return str(obj.author.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    image = SerializerMethodField()

    # comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'about', 'body', 'image', 'create_at')

    def get_author(self, obj):
        return str(obj.author.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    # def get_comments(self, obj):
    #     c_qs = Comment.objects.filter_by_instance(obj)
    #     comments = CommentSerializer(c_qs, many=True).data
    #     return comments



class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'name', 'messages', 'create_at', 'post_id', 'reply_count')

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.childen().count()
        return 0
