from django.db import models


class GenderChoices(models.TextChoices):
    FEMALE = "female"
    MALE = "male"


class BloodGroupChoices(models.TextChoices):
    A_POSITIVE = "A+", "A+"
    A_NEGATIVE = "A-", "A-"
    B_POSITIVE = "B+", "B+"
    B_NEGATIVE = "B-", "B-"
    AB_POSITIVE = "AB+", "AB+"
    AB_NEGATIVE = "AB-", "AB-"
    O_POSITIVE = "O+", "O+"
    O_NEGATIVE = "O-", "O-"


class TongueChoices(models.TextChoices):
    BANGLA = "bangla"
    ENGLISH = "english"


class CountryChoices(models.TextChoices):
    BANGLADESH = "bangladesh"
    OTHERS = "others"


class DivistionChoice(models.TextChoices):
    DHAKA = "Dhaka", "Dhaka"
    CHITTAGONG = "Chittagong", "Chittagong"
    KHULNA = "Khulna", "Khulna"
    RAJSHAHI = "Rajshahi", "Rajshahi"
    BARISAL = "Barisal", "Barisal"
    SYLHET = "Sylhet", "Sylhet"
    RANGPUR = "Rangpur", "Rangpur"
    MYMENSINGH = "Mymensingh", "Mymensingh"


class RelationshipChoice(models.TextChoices):
    BROTHER = "brother"
    SISTER = "sister"
    COUSIN = "cousin"
    FRIEND = "friend"
    HUSBAND = "husband"
    WIFE = "wife"
    AUNT = "aunt"
    UNCLE = "uncle"
