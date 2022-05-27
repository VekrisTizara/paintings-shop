from django.views.generic import CreateView

from .forms import MyUserCreateForm
from .models import MyUser


class MyUserCreateView(CreateView):
    model = MyUser
    success_url = '/'
    form_class = MyUserCreateForm