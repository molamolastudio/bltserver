from django.db import models

class BiolifeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey('auth.User', related_name='%(app_label)s_%(class)s_updated')

    class Meta:
        abstract = True

class Project(BiolifeModel):
    name = models.CharField(max_length=250)
    ethogram = models.ForeignKey('Ethogram', null=True)
    members = models.ManyToManyField('auth.User', related_name='projects_joined')
    admins = models.ManyToManyField('auth.User', related_name='projects_administered')

class Ethogram(BiolifeModel):
    name = models.CharField(max_length=250)
    information = models.TextField()

class Behaviour(BiolifeModel):
    name = models.CharField(max_length=200)
    ethogram = models.ForeignKey('Ethogram')
    information = models.TextField()
    #photo = models.ImageField()

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
    information = models.TextField(default='')
    recorded_behaviour = models.ForeignKey('Behaviour')
    # photo = models.ImageField()
    timestamp = models.DateTimeField()
    individual = models.ForeignKey('Individual')
    location = models.CharField(max_length=200)
    weather = models.CharField(max_length=200)

class Individual(BiolifeModel):
    label = models.CharField(max_length=200)
    # photo = models.ImageField()
    tags = models.ManyToManyField('Tag')
    project = models.ForeignKey('Project')

class Tag(BiolifeModel):
    name = models.CharField(max_length=100)


