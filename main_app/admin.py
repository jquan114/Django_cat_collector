from django.contrib import admin
from .models import Cat, Feeding

# Register your models here.

admin.site.register(Cat)
# register a new feeding model here
admin.site.register(Feeding)