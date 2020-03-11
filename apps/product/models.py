from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    # slug = models.SlugField(null=True,blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        # __str__ method elaborated later in post.  use __unicode__ in place of

        # __str__ if you are using python 2

        # unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = self.name
        k = self.parent
        return str(k) + " -> " + str(full_path)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField('citrus',null=True, blank=True)

    def __str__(self):
        return self.name
