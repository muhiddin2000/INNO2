from rest_framework.serializers import (ModelSerializer, ValidationError, SerializerMethodField)
from .models import Contact,CustomUser
# from django.contrib.auth import get_user_model
# User = get_user_model()


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'subject', 'messages')

class UserSerializer(ModelSerializer):
    class Meta:
        model =CustomUser
        fields = ('id', 'username', 'email', 'password','tel_raqam','iamge','kasbi','uz_haqida',
                  'twitter','teligram','linkedin','facebook',)

    extra_kwargs = {"password":
                        {"write_only": True}
                    }

    def validate(self, data):
        # username = validated_data['username']
        # email = validated_data['email']
        # password = validated_data['password']
        # user_obj = User(
        #     username=username,
        #     email=email,
        #     password=password
        # )
        # user_obj.set_password(password)
        # user_obj.save()
        return data

#
# class UserLoginSerializer(ModelSerializer):
#     token = CharField(allow_blank=True, ready_only=True)
#     username = CharField()
#     password = CharField()
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'token')
#
#     extra_kwargs = {"password":
#                         {"write_only": True}
#                     }
#
#     def validate(self, data):
#         return data
