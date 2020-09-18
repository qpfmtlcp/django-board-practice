from django.contrib import admin
from .models import Board, User, History


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'contents', 'owner')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')


admin.site.register(Board, BoardAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(History, HistoryAdmin)
