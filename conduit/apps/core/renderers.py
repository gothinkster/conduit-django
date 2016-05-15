import json

from rest_framework.renderers import JSONRenderer


class ConduitJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    namespace = 'object'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        import pdb; pdb.set_trace();

        if errors is not None:
            return super(ConduitJSONRenderer, self).render(data)

        return json.dumps({
            self.namespace: data
        })