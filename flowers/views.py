from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

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
    # category_item = Category.objects.get(pk=pk)
    flowers_q = Flowers.objects.get(id=pk)
    category_item = Category.objects.get(pk=flowers_q.pk)

    context = {
        'object': flowers_q,
        'title': f'Карточка цветка - {category_item.name}'

    }
    return render(request, 'flowers/flowers_card.html', context)


class Blog_flCreateView(CreateView):
    model = Blog_fl
    fields = ('name', 'content', 'is_publication', 'Imag')
    success_url = reverse_lazy('flowers:flowers_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class Blog_flUpdateView(UpdateView):
    model = Blog_fl
    fields = ('name', 'content', 'is_publication', 'number_of_views', 'Imag')
    success_url = reverse_lazy('flowers:flowers_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class Blog_flListView(ListView):
    model = Blog_fl
    extra_context = {
        'title': 'Блог о цветах'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects_list'] = Blog_fl.objects.all()
        return context

    success_url = reverse_lazy('flowers:flowers_list')


class Blog_flDetailView(DetailView):
    model = Blog_fl

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

    success_url = reverse_lazy('flowers:flowers_list')


class Blod_flDeleteView(DeleteView):
    model = Blog_fl
    success_url = reverse_lazy('flowers:flowers_list')


def toggle_activity(request, pk):
    blog_it = get_object_or_404(Blog_fl, pk=pk)
    if blog_it.is_publication:
        blog_it.is_publication = False
    else:
        blog_it.is_publication = True

    blog_it.save()

    return redirect(reverse('flowers:flowers_list'))
