from django.contrib import admin

from .models import English, German, Spanish, Russian

admin.site.register(English)
admin.site.register(German)
admin.site.register(Spanish)
admin.site.register(Russian)