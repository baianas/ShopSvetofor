#SELECT

# SELECT * FROM products;
# Product.objects.all()

# SELECT * FROM products WHERE ...;
# Product.objects.filter(...)

# SELECT * FROM product WHERE price = 10000;
# Product.objects.filter(price=10000)

# SELECT * FROM product WHERE price != 10000;
# Product.objects.filter(~Q(price=10000))
# Product.objects.exclude(price=10000)

# SELECT * FROM products WHERE price > 10000;
# Product.objects.filter(price__gt=10000)

# SELECT * FROM products WHERE price < 10000;
# Product.objects.filter(price__lt=10000)

# SELECT * FROM products WHERE price <= 10000;
# Product.objects.filter(price__lte=10000)

# SELECT * FROM products WHERE price >= 10000;
# Product.objects.filter(price__gte=10000)

# SELECT * FROM products WHERE category_id IN ('phones', 'tv')
# Product.object.filter(category_id__in=['phones', 'tv'])

# SELECT * FROM products WHERE price BETWEEN 2000 and 5000;
# Product.objects.filter(price__range=[2000, 5000])


#LIKE

# SELECT * FROM products WHERE name like 'test';
# Product.objects.filter(name__exact='test')

# SELECT * FROM products WHERE name ILIKE 'test';
# Product.objects.filter(name__iexact='test')

# SELECT * FROM products WHERE name like '%test%';
# Product.objects.filter(name__contains='test')

# SELECT * FROM products WHERE name ILIKE '%test%';
# Product.objects.filter(name__icontains='test')

# SELECT * FROM products WHERE name like 'test%';
# Product.objects.filter(name__startswith='test')

# SELECT * FROM products WHERE name ILIKE 'test%';
# Product.objects.filter(name__istartswith='test')

# SELECT * FROM products WHERE name like '%test';
# Product.objects.filter(name__endswith='test')

# SELECT * FROM products WHERE name ILIKE '%test';
# Product.objects.filter(name__iendswith='test')


# Получение одной записи
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id=1;

# ограничение набора полей
# SELECT name, price FROM products;
# Product.object.only('name', 'price')

# SELECT id, description, category_id FROM products;
# Product.objects.only('id', 'description', 'category_id')
# Product.objects.defer('name', 'price')

# SELECT * FROM products ORDER BY price;
# Product.objects.order_by('price')

# SELECT * FROM products ORDER BY price DESC;
# Product.objects.order_by('-price')

#INSERT

# INSERT INTO products (name, description, price, category) VALUES ('Mi 10', 'норм телефон', 40000, 'phones')
# Product.objects.create('Mi 10', 'норм телефон', 40000, 'phones')
#если несколько записей
# Product.objects.bulk_create(
#     [
#         Product(...),
#         Product(...)
#     ]
# )
#другой способ добваления продуктов (по одному)
# product = Product(...)
# product.save()

#UPDATE
# UPDATE products SET price = 10000;
# Product.objects.update(price=10000)
#
# UPDATE products SET price = 10000 WHERE category = 'phones'
# Product.objects.filter(category= 'phones').update(price = 10000)

#обновляем один объект
# product = Product.objects.get(id=1)
# product.price = 20000
# product.save()

#DELETE
# DELETE FROM Products;
#
# DELETE FROM products WHERE category = 'tv';
# Products.objects.filter(category = 'tv').delete()