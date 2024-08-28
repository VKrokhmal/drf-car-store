import factory
from factory.django import DjangoModelFactory
from carmanager.cars.models import Category, Brand, Car


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category

    @classmethod
    def _setup_next_sequence(cls):
        starting_seq_num = 200
        # Instead of defaulting to starting with 0, start with starting_seq_num.
        return starting_seq_num

    category_name = factory.Sequence(lambda x: f"Category {x}")


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    brand = factory.Sequence(lambda b: f"Brand {b}")


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    model = factory.Faker("text", max_nb_chars=500)
    category_name = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
