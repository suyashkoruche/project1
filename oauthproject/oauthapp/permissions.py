from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserIsAuthenticatedorReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
    

class UserIsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwnerorReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_authenticated == obj.created_by