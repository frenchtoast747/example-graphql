from graphene import String, NonNull, ObjectType, Int, ID


class Person(ObjectType):
    id = NonNull(ID)
    first_name = NonNull(String)
    last_name = NonNull(String)
    age = NonNull(Int)
    profile_url = NonNull(String)

    @staticmethod
    def resolve_profile_url(root: 'Person', info):
        return info.context.loaders.person_profile_pictures.load(root.id)
