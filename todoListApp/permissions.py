from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Cho phép GET, HEAD, OPTIONS
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # Chỉ chủ sở hữu mới được phép sửa/xóa
        return obj.user == request.user