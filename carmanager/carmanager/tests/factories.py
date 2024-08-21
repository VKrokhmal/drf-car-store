import factory
from factory.django import DjangoModelFactory
from carmanager.cars.models import Category, Brand, Car

starting_seq_num = 200


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    @classmethod
    def _setup_next_sequence(cls):
        # Instead of defaulting to starting with 0, start with starting_seq_num.
        return starting_seq_num

    name = factory.Sequence(lambda x: f"Category {x}")


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda b: f"Brand {b}")


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    model = "suzuki"
    category = factory.SubFactory(CategoryFactory)
    make = factory.SubFactory(BrandFactory)
