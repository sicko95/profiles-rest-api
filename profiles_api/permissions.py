from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    '''Svaki put kada je request trazen, django ce pozvati ovu funckiju kako bi video da li ima mogucnost pristupa
    starnici ili funckionalnosti'''
    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit their own prifle'''
        #provera koja metoda se vrsi (GET, PUT...), ukoliko je safe metoda (GET..), vraca se true
        if request.method in permissions.SAFE_METHODS:
            return True

        #proverava da li user menja svoj objekat ili tudji
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    '''Allow users to update their own status'''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to update their own status'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
