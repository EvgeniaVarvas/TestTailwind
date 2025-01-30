from django.db import models

class Format(models.Model):
    name = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'