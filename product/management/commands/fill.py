from django.core.management import BaseCommand
from product.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clear_database()
        product_list = [
            {'pk': '1', 'name': 'Молоко', 'description': 'Белый', 'category': 'Продукты питания',
             'piece_price': 'False', 'creation_date': '2023-12-05', 'update_date': '2023-12-05'},
            {'pk': '2', 'name': 'Стул', 'description': 'Черный', 'category': 'Интерьер', 'piece_price': 'False',
             'creation_date': '2023-12-05', 'update_date': '2023-12-05'},
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)

    def clear_database(self):
        Product.objects.all().delete()
