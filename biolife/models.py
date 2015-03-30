from django.db import models

class BiolifeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='created_%(app_label)s_%(class)s_set')
    updated_by = models.ForeignKey('auth.User', related_name='updated_%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True

class Project(BiolifeModel):
    name = models.CharField(max_length=250)
    ethogram = models.ForeignKey('Ethogram', null=True, blank=True)
    members = models.ManyToManyField('auth.User', related_name='joined_project_set')
    admins = models.ManyToManyField('auth.User', related_name='administered_project_set')

class Ethogram(BiolifeModel):
    name = models.CharField(max_length=250)
    information = models.TextField(null=False, blank=True)

class Behaviour(BiolifeModel):
    name = models.CharField(max_length=200)
    ethogram = models.ForeignKey('Ethogram')
    information = models.TextField(null=False, blank=True)
    photo = models.ImageField(null=True, blank=True)

class Session(BiolifeModel):
    FOCAL = 'FCL'
    SCAN = 'SCN'
    SESSION_TYPE_CHOICES = (
        (FOCAL, 'Focal Sampling'),
        (SCAN, 'Scan Sampling'),
    )
    project = models.ForeignKey('Project')
    session_type = models.CharField(max_length=3, choices=SESSION_TYPE_CHOICES, default=SCAN)
    individuals = models.ManyToManyField('Individual')

class Observation(BiolifeModel):
    session = models.ForeignKey('Session')
    information = models.TextField(null=False, blank=True)
    recorded_behaviour = models.ForeignKey('Behaviour')
    photo = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField()
    individual = models.ForeignKey('Individual')
    location = models.CharField(max_length=200, null=False, blank=True)
    weather = models.CharField(max_length=200, null=False, blank=True)

class Individual(BiolifeModel):
    label = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField('Tag')
    project = models.ForeignKey('Project')

class Tag(BiolifeModel):
    name = models.CharField(max_length=100)


