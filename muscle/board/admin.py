from django.utils.timezone import now
from django.contrib import admin
from muscle.board.models import *
from django.utils.translation import ugettext as _

# Register your models here.
class StructureAdmin(admin.ModelAdmin):
	list_display = ('id', 'dataVersion', 'timestamp', 'dataType', 'dataFormat', 'dataPayload')

class UserAdmin(admin.ModelAdmin):
	list_display = ('nome', 'mac')

class TypeAdmin(admin.ModelAdmin):
	list_display = ('cod', 'nome')

admin.site.register(Structure, StructureAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Type, TypeAdmin)