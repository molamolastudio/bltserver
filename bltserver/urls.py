from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from accounts.views import UserViewSet
from biolife.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'ethograms', EthogramViewSet)
router.register(r'behaviours', BehaviourViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'observations', ObservationViewSet)
router.register(r'individuals', IndividualViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bltserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
)
