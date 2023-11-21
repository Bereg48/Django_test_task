from main.models import Category, Product


def load_data():
    """ Загружает данные в базу данных. Функция используется
    для загрузки категорий и продуктов в базу данных."""
    categories = """id:title:parent
    5:Товары для дома:None
    4:Посуда для кухни:5
    1:Велосипеды:None
    2:Кастрюли:4
    3:Тарелки:4"""

    for line in categories.split('\n')[1:]:
        id, title, parent = line.split(':')
        if not Category.objects.filter(id=id).exists():
            Category.objects.create(id=id, title=title, parent_id=parent if parent != 'None' else None)

    products = """id:title:category_id:count:cost
    1:Велосипед:1:100:100.50
    2:Кастрюля 1,5л:2:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:55,300.78"""

    for line in products.split('\n')[1:]:
        parts = line.split(':')
        if len(parts) < 4:
            continue
        id, title, category_id, count, cost = parts
        if not Product.objects.filter(id=id).exists():
            Product.objects.create(id=id, title=title, category_id=category_id, count=count, price=cost)