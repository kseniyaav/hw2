from django.core.management import BaseCommand
from product.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Молоко', 'description': 'Белый', 'category': 'Продукты питания', 'creation_date': '2023-12-05'},
            {'name': 'Стул', 'description': 'Черный', 'category': 'Интерьер', 'creation_date': '2023-12-05'},
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
