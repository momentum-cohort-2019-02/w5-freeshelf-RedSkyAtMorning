from django.contrib import admin
from core.models import Bowl, Necklace, Bead, Matron, Status, Collecting, Stringing, Dressing, Outfitting, Beat, Drumming, Shoe, Dress


# Pattern 1
admin.site.register(Bowl)
admin.site.register(Bead)
admin.site.register(Necklace)
admin.site.register(Matron)
admin.site.register(Status)
admin.site.register(Collecting)
admin.site.register(Stringing)
admin.site.register(Dressing)
admin.site.register(Outfitting)
admin.site.register(Beat)
admin.site.register(Drumming)
admin.site.register(Shoe)
admin.site.register(Dress)

# Pattern 2 for different displays for bulk management
# @admin.register(Bowl)
# class BowlAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id')