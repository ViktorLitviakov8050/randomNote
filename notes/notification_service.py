import requests
import datetime
import schedule
import time
import os
import django
import sys


# Determine the full path to the notes.settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")

django.setup()

from randomNote.models import Note
from randomNote.serializers import NoteSerializer

NATIVE_NOTIFY_URL = "https://exp.host/--/api/v2/push/send"
APP_ID = 13004
APP_TOKEN = "ExponentPushToken[KxFK2yJZNXIDFQzPrU5MCi]"
             

def send_note_as_notification(note):
    current_time = datetime.datetime.now()
    payload = {
      "to": APP_TOKEN,
      "sound": "default",
      "title": note.title,
      "body": note.text_content,
      "data": NoteSerializer(note).data
    }
    response = requests.post(NATIVE_NOTIFY_URL, json=payload)

    print(response.text)
    return response.status_code == 200


def sent_random_note():
  random_note = Note.random_note()
  send_note_as_notification(random_note)
  print(random_note.id)

schedule.every(1).seconds.do(sent_random_note)
# schedule.every(1).hour.do(sent_random_note)

while True:
  schedule.run_pending()
  
