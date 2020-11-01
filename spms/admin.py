from django.contrib import admin
from .models import User,Worker,ConstructionSite
# Register your models here.


admin.site.register(User)
admin.site.register(Worker)
admin.site.register(ConstructionSite)