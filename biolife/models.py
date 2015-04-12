from django.db import models

class BiolifeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)
    created_by = models.ForeignKey('auth.User', related_name='created_%(app_label)s_%(class)s_set')
    updated_by = models.ForeignKey('auth.User', related_name='updated_%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True

class Project(BiolifeModel):
    name = models.CharField(max_length=250)
    ethogram = models.ForeignKey('Ethogram', null=True, blank=True)
    members = models.ManyToManyField('auth.User', related_name='joined_project_set')
    admins = models.ManyToManyField('auth.User', related_name='administered_project_set')
    individuals = models.ManyToManyField('Individual')

class Ethogram(BiolifeModel):
    name = models.CharField(max_length=250)
    information = models.TextField(null=False, blank=True)
    behaviours = models.ManyToManyField('Behaviour')

class Behaviour(BiolifeModel):
    name = models.CharField(max_length=200)
    information = models.TextField(null=False, blank=True)
    photo = models.ForeignKey('Photo', blank=True, null=True, on_delete=models.SET_NULL)

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
    photo = models.ForeignKey('Photo', blank=True, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField()
    individual = models.ForeignKey('Individual')
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.SET_NULL)
    weather = models.ForeignKey('Weather', blank=True, null=True, on_delete=models.SET_NULL)

class Individual(BiolifeModel):
    label = models.CharField(max_length=200)
    photo = models.ForeignKey('Photo', blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')

class Tag(BiolifeModel):
    name = models.CharField(max_length=100)

class Photo(BiolifeModel):
    image = models.ImageField()

class Location(BiolifeModel):
    location = models.TextField()

class Weather(BiolifeModel):
    weather = models.TextField()

class Dummy(BiolifeModel):
    stringProperty = models.TextField()
    intProperty = models.IntegerField()
    dateProperty = models.DateTimeField()
    optionalStringProperty = models.TextField(null=True, blank=True)
    imageProperty = models.ImageField(null=True, blank=True)
    friends = models.ManyToManyField('Dummy')

