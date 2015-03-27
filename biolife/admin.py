from django.contrib import admin
from .models import (
        Project, Ethogram
)

admin.site.register(Project)
admin.site.register(Ethogram)
