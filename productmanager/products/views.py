from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AddProductForm

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# 6. Настройте маршруты
# Создайте файл products/urls.py и настройте маршруты для:
# Списка товаров ('').
# Добавления нового товара ('add/').
# Редактирования товара ('edit/<int:id>/').
# Удаления товара ('delete/<int:id>/').

# 7. Реализуйте представления
# В файле products/views.py создайте функции:
# product_list — отображение всех товаров.
# add_product — добавление нового товара.
# edit_product — обновление информации о товаре.
# delete_product — удаление товара.

    

def product_list(request):
    products = Product.objects.all()

    return  render(request, "products/product_list.html",{'products': products})

def add_product(request):
    if request.method != 'POST':
        # данные не отправлялись. Создается новая форма.
        form = AddProductForm()

    else:
        # отправлены данные POST - обработать данные
        form = AddProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    # Выводим пустую или недействительную фрорму:
    context = {'form': form}
    return render(request,'products/add_product.html',context)

    return HttpResponse("Добавить продукт")

def edit_product(request, p_id):

    product = Product.objects.get(id = p_id)

    if request.method != 'POST':
        # Исходный запрос. Форма заполняется данными текущей записи.
        form = AddProductForm(instance=product)
    else:
        # Отправка данных POST, обработать данные.
        form = AddProductForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    context = {'form': form, 'product': product}
    return render(request,'products/edit_product.html',context)


def delete_product(request, id):
    return HttpResponse("Удалить продукт")
        
    