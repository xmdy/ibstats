from django.core.management.base import BaseCommand, CommandError
from django_faker import Faker

from stats.models import Trader, Transaction


class Command(BaseCommand):
    help = 'Generate test data with faker'
    defaults = {
        'traders': 1000,
        'transactions': 100000,
        'deals': 10000000,
    }

    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--traders', action='store', dest='traders', default=self.defaults['traders'],
            type=int,
            help='traders num',
        )
        parser.add_argument(
            '-trans', '--trans', action='store', dest='transactions', default=self.defaults['transactions'],
            type=int,
            help='transactions num',
        )
        parser.add_argument(
            '-deals', '--deals', action='store', dest='deals', default=self.defaults['deals'],
            type=int,
            help='deals num',
        )

    def handle(self, *args, **options):
        print options
        populator = Faker.getPopulator()

        populator.addEntity(Trader, options['traders'])
        populator.addEntity(Transaction, options['transactions'])

        insertedPks = populator.execute()