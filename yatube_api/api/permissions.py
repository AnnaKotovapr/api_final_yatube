from rest_framework.permissions import SAFE_METHODS
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверяет, что пользователь является автором объекта.
    Разрешает чтение для любого пользователя.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'DELETE' and obj.author != request.user:
            return False
        return obj.author == request.user
