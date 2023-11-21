from django.http import HttpResponse
from django.shortcuts import render

from main.models import Product
from main.utils import load_data


def product_list(request):
    """Отображает список продуктов, отсортированных по цене.
    Функция получает все продукты из базы данных, сортирует
    их по цене и отображает на странице product_list.html."""

    products = Product.objects.order_by('price')
    return render(request, 'product_list.html', {'products': products})


def load_data_view(request):
    """Загружает данные в базу данных и возвращает ответ с сообщением. Функция используется
    для загрузки данных в базу данных с использованием функции load_data(). После загрузки
    данных в базу данных, функция возвращает ответ с сообщением "Data loaded successfully."""
    load_data()
    return HttpResponse("Data loaded successfully.")
