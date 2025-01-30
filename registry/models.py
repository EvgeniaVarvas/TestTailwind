from django.db import models

class Orders(models.Model):
    date = models.DateField(null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=5, null=True, blank=True)
    manager = models.CharField(max_length=15, null=False, blank=False)
    invoice = models.CharField(max_length=10, null=True, blank=True)
    client = models.CharField(max_length=30, null=False, blank=False)
    product = models.CharField(max_length=50,null=False, blank=False)
    compound = models.CharField(max_length=50, null=False, blank=False)
    tag = models.CharField(max_length=10, null=False, blank=False)
    length = models.PositiveIntegerField(null=False, blank=False)
    width = models.PositiveIntegerField(null=False, blank=False)
    height = models.PositiveIntegerField(null=True, blank=True)
    ril = models.PositiveIntegerField(null=True, blank=True)
    ril2 = models.PositiveIntegerField(null=True, blank=True)
    ril3 = models.PositiveIntegerField(null=True, blank=True)
    workpiece_width = models.IntegerField()
    workpiece_length = models.IntegerField()
    stock = models.CharField(max_length=15)
    quantity = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    number_tk = models.CharField(max_length=10, null=True, blank=True)
    shipping = models.DateField(null=True, blank=True)
    done = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.client} - {self.product}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


