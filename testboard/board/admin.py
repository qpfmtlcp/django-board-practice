from django.contrib import admin
from .models import Board, User, History

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'contents', 'created', 'modified','owner')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('currentUser','modifiedDate')

admin.site.register(Board, BoardAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(History, HistoryAdmin)
