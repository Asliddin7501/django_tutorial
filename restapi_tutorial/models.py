from django.db import models


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, default=None, null=True)
    name = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name.__add__(" ").__add__(self.last_name)