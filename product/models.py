from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')



    def __str__(self):
        return self.name

# TODO: реализовать возможность хранить несколько изображений
class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='products')

# варианты on_delete
# CASCADE - при удалении категории, удаляются соответсвующие ей продукты
# RESTRICT -
# PROTECT - запрещает удаление категории, если есть связанные с ней продукты
# SET_NULL - при удалении категории, у продуктов категория становится NULL, если допуск, что катег мб пустой
# SET_DEFAULT - при удалении категории, продуктам присваивается дефолтная категория