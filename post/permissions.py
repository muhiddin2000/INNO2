from rest_framework import permissions


class IsAuthorOrReadOnl(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqat korish uchun GET
        if request.method in permissions.SAFE_METHODS:
            return True
        # o'zgartish uchun faqata mualiifga ruxsat beriladi PUT
        return obj.author == request.user


