import json
from django.db import models


class ToJson(object):

    def to_json(self):
        data = {}
        print('******self._meta.fields: ', self._meta.fields)
        for i in self._meta.fields:
            data[i] = self.i
        return json.dumps(data)


    # MyModel._meta.fields


class baseModel(models.Model):
    def __str__(self):
        """String representation of model."""
        return "Not so fast."
