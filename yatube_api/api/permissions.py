from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IsAuthorOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

    # я сделал так, но не могу пройти тест яндекса при загрузке
    # def has_object_permission(self, request, view, obj):
    #     return (
    #             request.method in permissions.SAFE_METHODS
    #             or obj.author == request.user
    #     )
