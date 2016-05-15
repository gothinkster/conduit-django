import json

from rest_framework.renderers import JSONRenderer

from conduit.apps.core.renderers import ConduitJSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        return json.dumps({
            'profile': data
        })

class NewProfileJSONRenderer(ConduitJSONRenderer):
    namespace = 'profile'