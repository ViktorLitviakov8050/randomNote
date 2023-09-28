from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Attachment
from django.conf import settings
from helpers import copy_file


@receiver(post_save, sender=Attachment, dispatch_uid="copy attachment file")
def copy_attachment_file(sender, instance, **kwargs):
    copy_file(f"{settings.NOTES_SOURCE_DIR}/{instance.file_path}",
                          f"{settings.ATTACHMENTS_DIR}/{instance.file_path}")
    print("signal happens")

    