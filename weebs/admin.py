from django.contrib import admin
from .models import Post , manhua , manhwa , ManhwaPost

admin.site.register(Post)
admin.site.register(manhua)
admin.site.register(manhwa)

admin.site.register(ManhwaPost)



