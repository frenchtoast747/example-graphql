import graphene

from g_unity.queries.people import PeopleQuery


class Query(
    PeopleQuery,
    graphene.ObjectType
):
    """
    The Root Query Object.

    Any documentation here will show up in the introspection (auto-documentation) schema query.
    """


schema = graphene.Schema(query=Query)
