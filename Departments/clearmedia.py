import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Delete all static files in the media directory'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        for root, dirs, files in os.walk(media_root):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        self.stdout.write(self.style.SUCCESS('All static files in the media directory have been deleted.'))
