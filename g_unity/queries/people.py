from graphene import List

from g_unity.types import Person


class PeopleQuery:
    people = List(Person)

    @staticmethod
    def resolve_people(root: None, info):
        return [
            Person(
                id=1,
                first_name='Aaron',
                last_name='Boman',
                age=30,
            ),
            Person(
                id=2,
                first_name='Nick',
                last_name='Van Santana',
                age=76,
            ),
        ]

