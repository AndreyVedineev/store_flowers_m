from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from flowers.models import Flowers, Category, Blog_fl


class IndexListView(ListView):
    model = Flowers
    extra_context = {
        'title': 'Цветы - Django магазин'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects_list'] = Flowers.objects.all()
        return context


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

        # print(request.POST)
    return render(request, 'flowers/contacts.html', context)


# class Flowers_cardListView(ListView):
#     model = Flowers
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(category_id=self.kwargs.get('pk'))
#         return queryset
#
#     def get_context_data(self, *args, **kwargs):
#
#         context_date = super().get_context_data(*args, **kwargs)
#         category_item = Category.objects.get(pk=self.kwargs.get('pk'))
#         context_date['object'] = Flowers.objects.get(id=pk)
#         context_date['title'] = f'Карточка цветка - {category_item.name}'
#         }
#         return context_date


def flowers_card(request, pk):
    category_item = Category.objects.get(pk=pk)
    flowers_q = Flowers.objects.get(id=pk)

    context = {
        'object': flowers_q,
        'title': f'Карточка цветка - {category_item.name}'

    }
    return render(request, 'flowers/flowers_card.html', context)


class Blog_flCreateView(CreateView):
    model = Blog_fl
    fields = ('name', 'content', 'is_publication', 'number_of_views', 'Imag')
    success_url = reverse_lazy('flowers:flowers_list')


class Blog_flUpdateView(UpdateView):
    model = Blog_fl
    fields = ('name', 'content', 'is_publication', 'number_of_views', 'Imag')
    success_url = reverse_lazy('flowers:flowers_list')


class Blog_flListView(ListView):
    model = Blog_fl
    extra_context = {
        'title': 'Блог о цветах'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects_list'] = Blog_fl.objects.all()
        return context

    success_url = reverse_lazy('flowers:flowers_list')


class Blog_flDetailView(DetailView):
    model = Blog_fl

# def blog_fl_detall(request, pk):
#     flowers_q = Blog_fl.objects.get(id=pk)
#
#     context = {
#         'object': flowers_q,
#         'title': f'Карточка цветка - {flowers_q.name}'
#
#     }
#     return render(request, 'flowers/blod_fl_detall.html', context)
