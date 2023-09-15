import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")

import django
django.setup()

from models import Note, Attachment, Label
import os
import glob
import json
import zipfile
import sys


if len(sys.argv) < 2:
    raise Exception('Zip file path is not provided')
zip_file_path = sys.argv[1]

folder_to_extract_files_from = 'Takeout/Keep'
folder_with_extracted_files = os.path.join(os.getcwd())

print("Extracting")
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_file_list = zip_ref.namelist()
    for item in zip_file_list:
        if item.startswith(folder_to_extract_files_from + '/'):
            zip_ref.extract(item, folder_with_extracted_files)
            print(".", end="")
            
print()
extension = '*.json'
files_dir = os.path.join(folder_with_extracted_files, folder_to_extract_files_from)
file_paths = glob.glob(os.path.join(files_dir, extension))

print('Loading')
for filename in file_paths:
   with open(filename) as file:
        note_json = json.load(file)
        Note.from_dict(note_json).save()
        print(".", end="")

print()
