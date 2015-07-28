from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MusicianPost)
admin.site.register(MusicianResponse)
admin.site.register(NonMusicianPost)
admin.site.register(NonMusicianResponse)
admin.site.register(Vote)