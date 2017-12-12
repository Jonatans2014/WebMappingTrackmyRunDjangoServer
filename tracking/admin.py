from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import location
from .models import image
# Register your models here.
admin.site.register(location)
admin.site.register(image)