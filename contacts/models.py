from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField

# from django.db.models.fields import DateField
from django.forms import widgets


class Contact(models.Model):
    note = models.ForeignKey(
        "Note",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    ## add birthday
    birthday= models.DateField(null=True, blank=True)

class Note(models.Model):
    note_name = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)