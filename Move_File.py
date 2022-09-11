import os
import shutil
from unicodedata import name
from_dir="C:/Users/HP/Downloads"
to_dir="D:/org"
list=os.listdir(from_dir)
print(list)
for file in list:
    name,extension=os.path.splitext(file)
    if extension == '':
        continue
    if extension in  [ '.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+'/'+file
        path2=to_dir+'/'+'image'
        path3=to_dir+'/'+'image'+'/'+file
        if os.path.exists(path2):
            print("Moving "+file+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving "+file+'...')
            shutil.move(path1,path3)
