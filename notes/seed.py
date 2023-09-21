import shutil
from pathlib import Path
from django.conf import settings
import sys
import zipfile
import json
import glob
from randomNote.models import Note, Attachment, Label
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")

django.setup()


if len(sys.argv) < 2:
    raise Exception('Zip file path is not provided')
zip_file_path = sys.argv[1]

folder_to_extract_files_from = settings.NOTES_SOURCE_DIR
folder_with_extracted_files = settings.BASE_DIR

print("Extracting")
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_file_list = zip_ref.namelist()
    for item in zip_file_list:
        if item.startswith(folder_to_extract_files_from + '/'):
            zip_ref.extract(item, folder_with_extracted_files)
            print(".", end="")

print()
extension = '*.json'
files_dir = os.path.join(folder_with_extracted_files,
                         folder_to_extract_files_from)
file_paths = glob.glob(os.path.join(files_dir, extension))

models_to_reset = [Note, Attachment, Label]
print("Resetting notes, labels and attachments")
for model in models_to_reset:
    model.objects.all().delete()

print('Loading')
for filename in file_paths:
    with open(filename) as file:
        note_json = json.load(file)
        Note.from_dict(note_json).save()
        print(".", end="")

print()


extracted_temporary_folder_path = Path(
    settings.NOTES_SOURCE_DIR).resolve().parent
shutil.rmtree(extracted_temporary_folder_path)
