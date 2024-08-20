import factory
from factory.django import DjangoModelFactory

from carmanager.cars import models


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Faker("name")


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
    payment_info = factory.Faker("text", max_nb_chars=500)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def teachers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for teacher in extracted:
                self.teachers.add(teacher)
