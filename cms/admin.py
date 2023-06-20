from django.contrib import admin
from .models import *


admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}

admin.site.register(Post,PostAdmin)
# Register your models here.
