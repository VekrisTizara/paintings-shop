from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Painting


def index(request):
    all_paintings = Painting.objects.all()
    username = str(request.user)
    greetings_text = "Hello mysterious " + username if username == "AnonymousUser" else "Hello dear " + username
    context = {
        'all_paintings': all_paintings,
        'greetings_text': greetings_text
    }
    return render(request, 'paintings/index.html', context=context)


class PaintingListView(ListView):
    model = Painting
    context_object_name = 'paintings'
    paginate_by = 15


class PaintingDetailView(DetailView):
    model = Painting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = 'painting'

        return context
