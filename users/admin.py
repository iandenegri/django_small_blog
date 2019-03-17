from django.contrib import admin
from .models import Profile, FriendRequest

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile


class FriendRequestResource(resources.ModelResource):
    class Meta:
        model = FriendRequest

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(FriendRequest)
class FriendRequestAdmin(ImportExportModelAdmin):
    pass
