from django.shortcuts import render

from flowers.models import Flowers, Category


def index(request):
    flowers_list = Flowers.objects.all()[:3]
    context = {
        'objects_list': flowers_list,
        'title': 'Цветик'
    }
    return render(request, 'flowers/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

        # print(request.POST)
    return render(request, 'flowers/contacts.html', context)


def flowers_card(request, pk):
    category_item = Category.objects.get(pk=pk)
    flowers_q = Flowers.objects.get(id=pk)

    context = {
        'object_list': flowers_q,
        'title': f'Карточка цветка - {category_item.name}'

    }
    return render(request, 'flowers/flowers_card.html', context)
