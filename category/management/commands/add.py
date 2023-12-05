from django.core.management import BaseCommand
from category.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Продукты питания', 'description': 'Еда и напитки'},
            {'name': 'Интерьер', 'description': 'Все для дома'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)
