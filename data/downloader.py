
## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os

path = 'Yoga-82/Yoga-82/yoga_dataset_links'
dataset_path = os.path.join(path,'dataset')
if not os.path.isdir(dataset_path):
    os.mkdir(dataset_path)

classes = os.listdir(path)
for file in classes:
    folder_name = file.split(".")[0]
    if not os.path.isdir(os.path.join(dataset_path,folder_name)):
        os.mkdir(os.path.join(dataset_path,folder_name))
    txt_path = os.path.join(path,file)
