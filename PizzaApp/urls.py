from django.urls import path

from . import views

app_name='PizzaApp'

urlpatterns=[
    path('', views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
    path('addcom/<int:pizza_id>/',views.addcom,name='addcom'),
]