from django.contrib import admin
from .models import Store, User, UserAction, Announcement

# Register your models here.
admin.site.register(Store)
admin.site.register(User)
admin.site.register(UserAction)
admin.site.register(Announcement)
