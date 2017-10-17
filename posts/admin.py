from django.contrib import admin
from . models import Post

class PostAdmin(admin.ModelAdmin):
    list_display       = ("title","stamptime", "updated")
    list_display_links = ["updated"]
    list_filter        = ["updated", "stamptime"]
    search_fields      = ["title","content"]
    list_editable      = ["title"]
    model  = "Post"

admin.site.register(Post, PostAdmin)
