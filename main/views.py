from .models import User
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    ProfileUpdateForm,
    EligibleForm,
    StemCellDonorForm,
    SCDonorShippingAddressForm,
    SCDonorContactPerson1Form,
    SCDonorContactPerson2Form,
)
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
        context["eligible"] = "yes"

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


class StemCellDonateView(TemplateView):
    template_name = "main/stem_cell_donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["donor_form"] = StemCellDonorForm(prefix="donor")
        context["shipping_form"] = SCDonorShippingAddressForm(prefix="shipping")
        context["contact1_form"] = SCDonorContactPerson1Form(prefix="contact1")
        context["contact2_form"] = SCDonorContactPerson2Form(prefix="contact2")
        return context

    def post(self, request, *args, **kwargs):
        donor_form = StemCellDonorForm(request.POST, prefix="donor")
        shipping_form = SCDonorShippingAddressForm(request.POST, prefix="shipping")
        contact1_form = SCDonorContactPerson1Form(request.POST, prefix="contact1")
        contact2_form = SCDonorContactPerson2Form(request.POST, prefix="contact2")
        if (
            not donor_form.is_valid()
            or not shipping_form.is_valid()
            or not contact1_form.is_valid()
            or not contact2_form.is_valid()
        ):
            context = self.get_context_data()
            context["donor_form"] = donor_form
            context["shipping_form"] = shipping_form
            context["contact1_form"] = contact1_form
            context["contact2_form"] = contact2_form
            return self.render_to_response(context)

        donor = donor_form.save()
        shipping = shipping_form.save(commit=False)
        contact1 = contact1_form.save(commit=False)
        contact2 = contact2_form.save(commit=False)
        shipping.donor = donor
        contact1.donor = donor
        contact2.donor = donor
        shipping.save()
        contact1.save()
        contact2.save()
        return HttpResponseRedirect(reverse('result'))


class EligibleView(FormView):
    template_name = "main/signup.html"
    form_class = EligibleForm
    success_url = "/stem-cell-donate"

    def form_valid(self, form):
        return HttpResponseRedirect(reverse("stem_cell_donate"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "title"
        ] = "Fill this form to check if you are eligible to donate stem cell ?"
        context["btn_text"] = "Submit"
        context["eligible"] = "yes"
        return context

class ResultView(TemplateView):
    template_name = 'main/eligible.html'

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
