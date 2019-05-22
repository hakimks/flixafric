from tastypie.resources import ModelResource
from movies.models import Movie, Actor

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'

# class ActorResource(ModelResource):
#     class Meta:
#         queryset = Actor.objects.all()
#         resource_name = 'actor'