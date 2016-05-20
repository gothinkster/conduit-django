from conduit.apps.core.renderers import ConduitJSONRenderer


class ArticleJSONRenderer(ConduitJSONRenderer):
    namespace = 'article'
    namespace_plural = 'articles'