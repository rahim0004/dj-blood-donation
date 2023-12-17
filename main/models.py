from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from .choices import (
    GenderChoices,
    BloodGroupChoices,
    TongueChoices,
    CountryChoices,
    DivistionChoice,
    RelationshipChoice,
)
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9]+$",
                message="Username must only contain alphanumeric characters",
                code="invalid_username",
            )
        ],
    )
    # Add fields specific to candidates
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5, choices=BloodGroupChoices.choices)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        choices=GenderChoices.choices, max_length=20, blank=True, null=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    verification_token = models.UUIDField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = f"{settings.DB_PREFIX}user"

    def __str__(self):
        return self.email

    @property
    def is_email_verified(self):
        return False if self.verification_token else True


class StemCellDonor(models.Model):
    gender = models.CharField(
        max_length=8,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )

    first_name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    mother_tongue = models.CharField(
        max_length=10, choices=TongueChoices.choices, blank=True, null=True
    )
    on_whatsapp = models.BooleanField(verbose_name="Can We Connect On Whatsapp")
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=155)

    class Meta:
        db_table = f"{settings.DB_PREFIX}stem_cell_donor"

    def __str__(self):
        return self.email


class SCDonorShippingAddress(models.Model):
    donor = models.OneToOneField(StemCellDonor, on_delete=models.CASCADE)
    country = models.CharField(
        max_length=100,
        choices=CountryChoices.choices,
        default=CountryChoices.BANGLADESH,
    )
    divistion = models.CharField(max_length=255, choices=DivistionChoice.choices)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    class Meta:
        db_table = f"{settings.DB_PREFIX}stem_cell_donor_shipping"

    def __str__(self):
        return self.donor.email


class SCDonorContactPerson1(models.Model):
    donor = models.ForeignKey(StemCellDonor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    relationship = models.CharField(max_length=20, choices=RelationshipChoice.choices)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = f"{settings.DB_PREFIX}stem_cell_donor_contact_1"

    def __str__(self):
        return self.donor.email


class SCDonorContactPerson2(models.Model):
    donor = models.ForeignKey(StemCellDonor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    relationship = models.CharField(max_length=20, choices=RelationshipChoice.choices)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = f"{settings.DB_PREFIX}stem_cell_donor_contact_2"

    def __str__(self):
        return self.donor.email
