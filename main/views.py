from .models import User
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.contrib.auth import logout, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from backend.utils import redirect_if_logged_in


# Create your views here.
class HomeView(TemplateView):
    template_name = "main/index.html"


class AboutUsView(TemplateView):
    template_name = "main/about.html"


@method_decorator(redirect_if_logged_in, name="dispatch")
class UserSignUpView(FormView):
    template_name = "main/signup.html"
    form_class = UserRegistrationForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SignUp"
        context["btn_text"] = "Submit"
        return context


@method_decorator(redirect_if_logged_in, name="dispatch")
class UserSignInView(FormView):
    template_name = "main/signup.html"
    form_class = UserLoginForm
    success_url = "/"

    def form_valid(self, form):
        form.login_user(self.request)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign In"
        context["btn_text"] = "Signin"
        return context


class DonorsListView(ListView):
    template_name = "main/all_donors.html"
    queryset = User.objects.filter(is_admin=False, is_active=True).order_by("id")
    context_object_name = "donors"
    paginate_by = 10


class SearchView(ListView):
    template_name = "main/search.html"
    context_object_name = "donors"
    paginate_by = 10

    def get_queryset(self):
        division = self.request.GET.get("division")
        blood_group = self.request.GET.get("blood_group")
        users = User.objects.filter(
            is_admin=False, is_active=True, division=division, blood_group=blood_group
        ).order_by("id")
        return users


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "main/update.html"
    form_class = ProfileUpdateForm
    success_url = "/profile"

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = "/profile"
    template_name = "main/password_change.html"


class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = "main/delete.html"

    def post(self, request, *args, **kwargs):
        delete = request.POST.get("delete")
        if delete:
            user_id = self.request.user.id
            logout(request)
            User.objects.get(id=user_id).delete()
            # self.request.user.delete()
        return HttpResponseRedirect(reverse("index"))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
