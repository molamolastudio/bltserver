# from rest_framework import permissions

# class IsStaffOrTargetUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # allow staff to list all users
#         return view.action == 'retrieve' or request.user.is_staff

#     def has_object_permission(self, request, view, obj):
#         # allow users to view own details, staff to view all records
#         return request.user.is_staff or obj == request.user

