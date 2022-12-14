from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'PizzaApp/index.html')

def pizzas(request):
    pizzas=Pizza.objects.order_by('pizza_name')
    context={'all_pizzas':pizzas}

    return render(request, 'PizzaApp/pizzas.html', context)

def pizza(request, pizza_id):
    pid=Pizza.objects.get(id=pizza_id)
    toppings=Topping.objects.filter(pizza=pid)
    all_comments=Comment.objects.filter(pizza=pid)

    image=Image.objects.filter(pizza=pid)

    context={'pizza':pid,'toppings':toppings,'all_comments':all_comments,'image':image}

    return render(request, 'PizzaApp/pizza.html', context)

def addcom(request, pizza_id):
    pizza=Pizza.objects.get(id=pizza_id)
    if request.method!= 'POST':
        form=CommentForm()
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.pizza=pizza
            comment.save()
            form.save()
            return redirect('PizzaApp:pizza',pizza_id=pizza_id)
    context={'form':form, 'pizza':pizza}

    return render(request, 'PizzaApp/addcom.html', context)
