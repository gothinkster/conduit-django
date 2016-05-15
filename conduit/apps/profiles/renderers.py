import json

from conduit.apps.core.renderers import ConduitJSONRenderer


class ProfileJSONRenderer(ConduitJSONRenderer):
    namespace = 'profile'