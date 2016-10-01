from metabet_core.schema import Query as CoreQuery
import graphene


class Query(CoreQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
