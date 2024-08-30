import uuid
from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    class Meta:
        verbose_name = "Category"

    class MPTTMeta:
        order_insertion_by = ["category_name"]

    class CarTypes(models.TextChoices):
        Coupe = "Coupe"
        Cabriolet = "Cabriolet"
        Sedan = "Sedan"
        SUV = "SUV"

    category_name = models.CharField(
        max_length=20, choices=CarTypes.choices, unique=True
    )
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    class Meta:
        verbose_name = "Brand"

    brand = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand


class Car(models.Model):
    class Meta:
        verbose_name = "Car"

    brand = models.ForeignKey("Brand", on_delete=models.PROTECT)
    model = models.CharField(max_length=150)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.model


class CarItem(models.Model):
    class Meta:
        verbose_name = "CarItem"

    # Поле UUID для уникального идентификатора
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="car_items")

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    odometer = models.PositiveIntegerField(null=True, default=0)
    year = models.PositiveIntegerField(default=1970)
    description = models.CharField(max_length=150, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    """
    Улучшение валидации данных: Рассмотрите возможность добавления методов 
    валидации в модели или сериализаторы для 
    проверки допустимых значений полей, таких как year или odometer.
    """

    def __str__(self):
        return f"CarItem {self.uuid} by {self.user.username}"

    def mark_as_sold(self):
        """Метод для пометки автомобиля как проданного."""
        self.is_sold = True
        self.save()
