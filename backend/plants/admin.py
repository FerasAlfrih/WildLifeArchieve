from django.contrib import admin
from .models import Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, Plant, PlantImages

# Register your models here.
admin.site.register(Domain)
admin.site.register(Kingdom)
admin.site.register(Phylum)
admin.site.register(Class)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(Plant)
admin.site.register(PlantImages)
