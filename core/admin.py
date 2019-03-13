from django.contrib import admin
from core.models import Bowl, Necklace, Bead, Matron


# Pattern 1
admin.site.register(Bowl)
admin.site.register(Bead)
admin.site.register(Necklace)
admin.site.register(Matron)


# Pattern 2 for different displays for bulk management
# @admin.register(Bowl)
# class BowlAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id')