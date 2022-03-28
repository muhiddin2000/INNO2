from django.urls import path

from contact.views import UserList, UserDetail, UserCreate, ContactCreate, ContactList

urlpatterns = [

    path('user/', UserList.as_view()),
    path('register', UserCreate.as_view()),
    # path('login', UserLoginApiView.as_view()),
    path('user/detail/<int:pk>', UserDetail.as_view()),
    path('contact/', ContactList.as_view()),
    path('contact/create/', ContactCreate.as_view()),
]
