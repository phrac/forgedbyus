from django.db import models

class Affiliate(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField()

    def __unicode__(self):
        return self.name
