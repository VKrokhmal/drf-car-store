import random

from django.core.management.base import BaseCommand, CommandError
from carmanager.tests.factories import BrandFactory


class Command(BaseCommand):
    help = "Create 'Brands' with factory-boy"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of brands to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            b = BrandFactory.create(brand=f"Tesla{i+random.randrange(10, 200)}")
            # print(b)
            self.stdout.write(f"Brand with name: {b} was created")
            # b.save()
