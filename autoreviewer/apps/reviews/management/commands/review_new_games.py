from django.core.management.base import BaseCommand
from datetime import date

from ...utils import review
from .....giantbomb import GiantBombAPI


api = GiantBombAPI()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for game in api.get(
            'games',
            filter='original_release_date:'
            '2000-1-1 00:00:00|{0} 00:00:00'.format(
                date.today().isoformat()
            ),
            sort='original_release_date:desc',
            limit=100,
            field_list='name,original_release_date',
        )['results']:
            print (
                u'{name} - {score:.1f}/10\n'
                u'Pros: {pros}\n'
                u'Cons: {cons}'
            ).format(**review(game))
