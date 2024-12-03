

from django.urls import path

from . import views

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

urlpatterns = [

    path('index/', views.index, name = 'index'),

    path('',views.product_list, name = 'product_list'),

    path('add/',views.add_product, name = 'add_product'),

    path('edit/<int:p_id>',views.edit_product, name = 'edit_product'),

    path('delete/<int:p_id>',views.delete_product, name = 'delete_product'),

    path('one/<int:maybe_delete_p_id>',views.one_product, name = 'one_product'),

    path('one_delete/<int:p_id>',views.one_delete_product, name = 'one_delete_product')

]