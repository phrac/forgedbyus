from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
