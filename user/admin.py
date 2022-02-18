from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Certification)
admin.site.register(Feed)
admin.site.register(HashTag)