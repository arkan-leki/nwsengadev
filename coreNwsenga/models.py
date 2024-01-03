from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=350)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(max_length=350)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    link = models.URLField(null=True, default="")

    def __str__(self):
        return self.name


class Bill(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Buy(models.Model):
    PSWLA = 'pswla'
    XANU = 'xanu'
    BAX = 'bax'
    ZAWI = 'zawi'

    REQUEST_TYPE_CHOICES = [
        (PSWLA, "پسولە"),
        (XANU, "خانوو"),
        (BAX, "باخ"),
        (ZAWI, "زەوی"),

    ]

    type = models.CharField(
        max_length=20,
        choices=REQUEST_TYPE_CHOICES,
        default=PSWLA,
        verbose_name=('جۆری کڕین')
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    area = models.FloatField(max_length=10, null=True, default=0)
    documentation = models.CharField(null=True, default="", max_length=350)
    direction = models.CharField(max_length=255, null=True, default="")
    max_price = models.FloatField(null=True, default=0)
    min_price = models.FloatField(null=True, default=0)
    owner_name = models.CharField(max_length=350, null=True, default="")
    owner_phone = models.CharField(max_length=11, null=True, default="")
    notes = models.TextField(null=True, default="")
    link = models.URLField(null=True, default="")

    # bax
    fence = models.BooleanField(default=False)
    electric = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    water_depth = models.FloatField(null=True, default=0)
    house = models.BooleanField(default=False)
    tree = models.BooleanField(default=False)

    # pslwa
    bill = models.ForeignKey(Bill, null=True, on_delete=models.CASCADE)
    installment = models.FloatField(default=0, null=True)
    advance_payment = models.FloatField(default=0, null=True)

    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
