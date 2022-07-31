from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    iso3 = models.TextField(null=True, blank=True)
    iso2 = models.TextField(null=True, blank=True)
    numeric_code = models.TextField(null=True, blank=True)
    phone_code = models.TextField(null=True, blank=True)
    capital = models.TextField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    currency_name = models.TextField(null=True, blank=True)
    currency_symbol = models.TextField(null=True, blank=True)
    tld = models.TextField(null=True, blank=True)
    native = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    subregion = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    emoji = models.TextField(null=True, blank=True)
    emojiU = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{str(id)} {self.name}"


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    state_code = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    country_id = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{str(id)} {self.name}"


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    state_id = models.ForeignKey(
        State, null=True, blank=True, on_delete=models.CASCADE)
    country_id = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{str(id)} {self.name}"
