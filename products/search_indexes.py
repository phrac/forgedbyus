from haystack import indexes
from products.models import Product

class ProductIndex (indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='short_description')
    features = indexes.CharField()

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(available=True)

    def prepare_features(self, obj):
        if obj.features:
            return ' '.join(obj.features)
        else:
            return None
