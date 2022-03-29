from django.contrib import admin
from .models import Contact, CustomUser


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'subject', 'messages', 'create_at']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'tel_raqam', 'image', 'kasbi', 'uz_haqida',
                    'twitter', 'teligram', 'linkedin', 'facebook', ]
