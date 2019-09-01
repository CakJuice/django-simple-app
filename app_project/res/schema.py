from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from .models import Country


class CountryNode(DjangoObjectType):
    class Meta:
        model = Country
        filter_fields = ['code', 'name']
        interfaces = (relay.Node,)

    def resolve_image(self, info, **kwargs):
        return info.context.build_absolute_uri(self.image.url)


class Query(ObjectType):
    country = relay.Node.Field(CountryNode)
    all_countries = DjangoFilterConnectionField(CountryNode)
