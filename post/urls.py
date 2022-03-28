from django.urls import path

from contact.views import UserList, UserDetail,UserCreate, ContactCreate, ContactList
from .views import PostList, PostDelete, PostDetail, PostCreate, CommentList, CommentCreate, CommentDelete

urlpatterns = [
    path('post/', PostList.as_view()),
    path('post/create', PostCreate.as_view()),
    path('post/detail/<int:pk>', PostDetail.as_view()),
    path('post/delete/<int:pk>', PostDelete.as_view()),
    path('user/', UserList.as_view()),
    path('user/create', UserCreate.as_view()),
    path('user/detail/<int:pk>', UserDetail.as_view()),
    path('contact/', ContactList.as_view()),
    path('contact/create/', ContactCreate.as_view()),
    # path('post/search/', PostSearch.as_view()),
    path('comment/create/', CommentCreate.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/delete/<int:pk>/', CommentDelete.as_view()),

]
