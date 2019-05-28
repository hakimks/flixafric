from tastypie.resources import ModelResource
from movies.models import Movie, Actor
from tastypie import fields


class ActorResource(ModelResource):
    class Meta:
        queryset = Actor.objects.all()
        resource_name = 'actor'

class MovieResource(ModelResource):
    actor = fields.ForeignKey(ActorResource, 'actor')
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
