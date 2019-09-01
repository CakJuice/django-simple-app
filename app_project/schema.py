from graphene import ObjectType, Schema

from .res import schema as res_schema


class Query(res_schema.Query, ObjectType):
    pass


schema = Schema(query=Query)
