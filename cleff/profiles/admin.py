from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Musician, NonMusician, Genre, TimeFrame, Video, ProfileModel, Location, InstrumentGroup
# Register your models here.
admin.site.register(Genre)
admin.site.register(TimeFrame)
admin.site.register(Video)
admin.site.register(Location)
admin.site.register(InstrumentGroup)



class MusicianInline(admin.StackedInline):
    model = Musician
    can_delete = False
    verbose_name_plural = 'musicians'
   # fk_name = 'user'

class NonMusicianInline(admin.StackedInline):
    model = NonMusician
    can_delete = False
    verbose_name_plural = 'nonMusicians'


class ProfileAdmin(UserAdmin):
    inlines = (MusicianInline, NonMusicianInline)
    list_display = ('username',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')



admin.site.unregister(User)  # Unregister user to add new inline ProfileInline
admin.site.register(User, ProfileAdmin)  # Register User with this inline profile
