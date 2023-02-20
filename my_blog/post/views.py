from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse


def update(request):
    # author = Author.objects.get(id=1)
    # author.name = 'Jorge'
    # author.email = 'sandokan992000@gmail.com'
    # author.save()
    return HttpResponse('pepe')


def queries(request):
    # obtenes todos los datos de author
    authors = Author.objects.all()
    # obtener datos filtrando por condicion
    filtered = Author.objects.filter(email='melanie55@example.com')

    # Obtener un unico resultado
    author = Author.objects.get(id=1)

    # obtenes los 10 primeros los datos de author
    limit = Author.objects.all()[:10]

    # obtenes siguientes 10 reg de author
    offsets = Author.objects.all()[5:10]

    # obtenes todos los datos de author ordenados alfabeticamente
    orders = Author.objects.all().order_by('email')

    # obtener todos los elementos cuyo id sea menor o igual a 15
    filtereds2 = Author.objects.filter(id__lte=15)

    # obtener todos los elementos cuyo id sea menor o igual a 15
    contiene = Author.objects.filter(name__contains='yes')

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limit': limit, 'offsets': offsets, 'orders': orders, 'filtereds2': filtereds2, 'contiene': contiene})
