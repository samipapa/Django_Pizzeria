from django.shortcuts import render, redirect

from .models import Pizza, Topping, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")


@login_required
def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by("date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("-date_added")

    if pizza.owner != request.user:
        raise Http404

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)


@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != "POST":
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect("pizzas:pizza", pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza}
    return render(request, "pizzas/new_comment.html", context)


@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    pizza = comment.pizza

    if pizza.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("pizzas:pizza", pizza_id=pizza.id)

    context = {"comment": comment, "pizza": pizza, "form": form}
    return render(request, "pizzas/edit_comment.html", context)
