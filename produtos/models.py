from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.IntegerField()
    category_id = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price) + ' - ' + str(self.storage) + ' - ' + self.category_id.name