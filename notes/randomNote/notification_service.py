import requests
import datetime
# import os
# import django
# import sys

# # Determine the full path to the notes.settings module
# script_dir = os.path.dirname(os.path.abspath(__file__))
# settings_path = os.path.join(script_dir, '..', 'notes', 'settings')

# # Set the DJANGO_SETTINGS_MODULE environment variable with the full path
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)

# django.setup()


NATIVE_NOTIFY_URL = "https://app.nativenotify.com/api/notification"
APP_ID = 13004
APP_TOKEN = "mtizi9JKDcsxzzbsbpXdeY"
             

def send_note_as_notification(note):
    current_time = datetime.datetime.now()
    payload = {
      "appId": APP_ID,
      "appToken": APP_TOKEN,
      "title": note.title,
      "body": note.text_content,
      "dateSent": current_time
    }

    response = requests.post(NATIVE_NOTIFY_URL, json=payload)

    print(response.text)
    return response.status_code == 200

from randomNote.notification_service import send_note_as_notification
from randomNote.models import Note
random_note = Note.random_note()
if send_note_as_notification(random_note):
    print('Sent!')
  
"python3 randomNote/notification_service.py" # command to run this file