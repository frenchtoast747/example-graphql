from typing import NamedTuple

from flask import Flask, Request
from flask_graphql import GraphQLView

from g_unity.dataloaders import Loaders, get_dataloaders
from g_unity.schema import schema

app = Flask(__name__)


class Context(NamedTuple):
    request: Request
    loaders: Loaders


class MyGraphQLView(GraphQLView):
    def get_context(self):
        # the base class just returns the magic Flask request object
        request = super().get_context()

        return Context(
            request=request,
            loaders=get_dataloaders(),
        )


app.add_url_rule('/graphql', view_func=MyGraphQLView.as_view('graphql', schema=schema, graphiql=True))
