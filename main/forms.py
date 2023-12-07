from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=128)
    blood_group = forms.ChoiceField(choices=User.BloodGroupChoices.choices)
    DIVISION_CHOICES = [
        ("Dhaka", "Dhaka"),
        ("Chittagong", "Chittagong"),
        ("Khulna", "Khulna"),
        ("Rajshahi", "Rajshahi"),
        ("Barisal", "Barisal"),
        ("Sylhet", "Sylhet"),
        ("Rangpur", "Rangpur"),
        ("Mymensingh", "Mymensingh"),
    ]

    division = forms.ChoiceField(
        choices=DIVISION_CHOICES, required=True, label="Division"
    )
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "country",
            "city",
            "date_of_birth",
            "gender",
            "blood_group",
            "division",
            "password",
        ]

    def clean_blood_group(self):
        data = self.cleaned_data.get("blood_group")
        if data == "----":
            print("yes")
            raise forms.ValidationError("Invalid blood group selected.")
        return data

    def clean_password(self):
        password = self.cleaned_data["password"]
        try:
            validate_password(password)
        except Exception as e:
            raise e

        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("Password is required.")
        return password

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password.")
        cleaned_data["user"] = user
        return cleaned_data

    def login_user(self, request):
        login(request, self.cleaned_data["user"])


class ProfileUpdateForm(forms.ModelForm):
    blood_group = forms.ChoiceField(choices=User.BloodGroupChoices.choices)
    DIVISION_CHOICES = [
        ("Dhaka", "Dhaka"),
        ("Chittagong", "Chittagong"),
        ("Khulna", "Khulna"),
        ("Rajshahi", "Rajshahi"),
        ("Barisal", "Barisal"),
        ("Sylhet", "Sylhet"),
        ("Rangpur", "Rangpur"),
        ("Mymensingh", "Mymensingh"),
    ]

    division = forms.ChoiceField(
        choices=DIVISION_CHOICES, required=True, label="Division"
    )
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))


    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "country",
            "city",
            "date_of_birth",
            "gender",
            "blood_group",
            "division",
        ]
