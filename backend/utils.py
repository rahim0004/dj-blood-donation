# decorators.py

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def redirect_if_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return view_func(request, *args, **kwargs)
    return wrapper
