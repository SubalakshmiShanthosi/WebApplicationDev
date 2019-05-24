from django.core.management.base import BaseCommand
from main.models import FormSchema,FormResponse

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        tlisp = Tag(name='Lisp')
        tlisp.save()

        tjava = Tag(name='Java')
        tjava.save()

    def handle(self, *args, **options):
        self._create_tags()
