from django.urls import path

from .views import PostList, PostDelete, PostDetail, PostCreate, CommentList, CommentCreate, CommentDelete, \
    PostPopularList, PostUpdate, PostBannerList

urlpatterns = [
    path('post/', PostList.as_view()),
    path('post/create', PostCreate.as_view()),
    path('post/detail/<int:pk>', PostDetail.as_view()),
    path('post/update/<int:pk>', PostUpdate.as_view()),
    path('post/delete/<int:pk>', PostDelete.as_view()),
    path('post/popular/', PostPopularList.as_view()),
    path('post/banner/', PostBannerList.as_view()),
    path('comment/create/', CommentCreate.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/delete/<int:pk>/', CommentDelete.as_view()),

]
