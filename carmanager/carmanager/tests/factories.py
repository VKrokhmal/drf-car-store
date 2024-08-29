import random

import factory
from attr.validators import max_len
from django.template.defaultfilters import length
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from carmanager.cars.models import Category, Brand, Car


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("category_name",)

    category_name = FuzzyChoice(Category.CarTypes._member_names_)


car_brands = [
    "Acura",
    "Alfa Romeo",
    "Aston Martin",
    "Audi",
    "Bentley",
    "BMW",
    "Bugatti",
    "Buick",
    "Cadillac",
    "Chevrolet",
    "Chrysler",
    "Citroën",
    "Dacia",
    "Daewoo",
    "Daihatsu",
    "Dodge",
    "Ferrari",
    "Fiat",
    "Ford",
    "Genesis",
    "GMC",
    "Honda",
    "Hyundai",
    "Infiniti",
    "Isuzu",
    "Jaguar",
    "Jeep",
    "Kia",
    "Lamborghini",
    "Lancia",
    "Land Rover",
    "Lexus",
    "Lincoln",
    "Lotus",
    "Maserati",
    "Mazda",
    "McLaren",
    "Mercedes-Benz",
    "Mini",
    "Mitsubishi",
    "Nissan",
    "Opel",
    "Peugeot",
    "Porsche",
    "RAM",
    "Renault",
    "Rolls-Royce",
    "Saab",
    "SEAT",
    "Škoda",
    "Smart",
    "Subaru",
    "Suzuki",
    "Tesla",
    "Toyota",
    "Vauxhall",
    "Volkswagen",
    "Volvo",
]
car_brands_dict = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["F-150", "Mustang", "Explorer"],
    "Chevrolet": ["Silverado", "Malibu", "Equinox"],
    "BMW": ["3 Series", "X5", "M4"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLE"],
    "Audi": ["A4", "Q5", "A6"],
    "Tesla": ["Model S", "Model 3", "Model X"],
    "Nissan": ["Altima", "Sentra", "Rogue"],
    "Hyundai": ["Elantra", "Santa Fe", "Tucson"],
}


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand
        django_get_or_create = ("brand",)

    # brand = FuzzyChoice(car_brands_dict.keys())
    brand = factory.Iterator(
        [
            "Toyota",
            "Honda",
            "Ford",
            "Chevrolet",
            "BMW",
            "Mercedes-Benz",
            "Audi",
            "Tesla",
            "Nissan",
            "Hyundai",
        ]
    )


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    # model = FuzzyChoice(list(car_brands_dict.values())[0])

    category = factory.SubFactory(CategoryFactory)
    # brand = factory.SubFactory(BrandFactory)
    brand = factory.SubFactory(BrandFactory)
    model = factory.LazyAttribute(
        lambda car: random.choice(car_brands_dict[car.brand.brand])
    )
