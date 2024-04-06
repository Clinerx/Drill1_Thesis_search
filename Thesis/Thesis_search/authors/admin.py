from django.contrib import admin
from .models import Thesis,Comment

class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "year",)
  
admin.site.register(Thesis, MemberAdmin)
admin.site.register(Comment)
