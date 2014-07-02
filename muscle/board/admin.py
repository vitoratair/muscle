from django.utils.timezone import now
from django.contrib import admin
from muscle.board.models import *
from django.utils.translation import ugettext as _

# Register your models here.
class StructureAdmin(admin.ModelAdmin):
	list_display = ('id', 'dataVersion', 'timestamp', 'dataType', 'dataFormat', 'dataPayload')

admin.site.register(Structure, StructureAdmin)