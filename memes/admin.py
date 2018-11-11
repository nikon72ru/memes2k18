from django.contrib import admin
# Register your models here.

from .models import Cluster

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'previews')



