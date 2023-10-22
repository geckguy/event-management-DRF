from rest_framework import permissions

class IsSameCollege(permissions.BasePermission):
    """
    Custom permission to only allow students of the same college to see the event
    """
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the event.
        return obj.college == request.user.college
