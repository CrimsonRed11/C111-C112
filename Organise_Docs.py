import os
import shutil
from_dir = "/Users/aryavkhurana/Downloads"
to_dir = "/Users/aryavkhurana/Downloads"
list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)
    if extention == '':
        continue
    if extention in ['.pdf', '.txt', '.doc', '.docx','.html']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "document_files"
        path3 = to_dir + '/' + "document_files" + '/' + file_name
        if os.path.exists(path2):
            print("Moving " + file_name  + "....")
            shutil.move(path1, path2)
        else:
            os.makedirs(path2)
            print("Moving " + file_name  + "....")
            shutil.move(path1, path2)