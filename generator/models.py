from django.db import models


class Test(models.Model):
    test1 = models.CharField(max_length=100)
