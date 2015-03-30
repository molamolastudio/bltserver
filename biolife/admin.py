from django.contrib import admin
from .models import (
        Project, Ethogram, Behaviour, Session, Observation, Individual, Tag 
)

admin.site.register(Project)
admin.site.register(Ethogram)
admin.site.register(Behaviour)
admin.site.register(Session)
admin.site.register(Observation)
admin.site.register(Individual)
admin.site.register(Tag)
