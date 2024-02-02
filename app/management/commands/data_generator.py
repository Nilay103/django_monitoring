import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Order, Product
from faker import Faker


class Command(BaseCommand):
    help = 'Insert dummy data into the database'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(1000):
            # Create an order
            order = Order.objects.create(
                customer_name=fake.name(),
                order_date=timezone.now()
            )

            # Assign a random number of products (between 1 and 5) to the order
            num_products = random.randint(1, 5)
            for _ in range(num_products):
                product = Product.objects.create(
                    name=fake.word(),
                    price=random.uniform(10.0, 100.0)
                )
                order.products.add(product)
