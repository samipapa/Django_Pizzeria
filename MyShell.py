import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()


for p in pizzas:
    print(f"Pizza ID: {p.id} and Pizza Name: {p}")
    print(f"Date added: {p.date_added}")

for t in toppings:
    print(f"Pizza: {t.pizza}")
    print(f"Topping: {t.text}")


from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)
