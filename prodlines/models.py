from django.db import models

class ProdlineTable(models.Model):
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
