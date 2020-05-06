
## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os

import requests

def url_exists(url):
    """Check if resource exist?"""
    if not url:
        raise ValueError("url is required")
    try:
        resp = requests.head(url)
        return True if resp.status_code == 200 else False
    except Exception as e:
        return False


def download_url(url,filename):
  r = requests.get(url, stream=True)
  if r.status_code == requests.codes.ok:
    with open(filename, 'wb') as f:
      for data in r:
        f.write(data)

path = 'Yoga-82/Yoga-82/yoga_dataset_links'
dataset_path = os.path.join('Yoga-82/Yoga-82','dataset')
if not os.path.isdir(dataset_path):
    os.mkdir(dataset_path)

classes = os.listdir(path)
for file in classes:
    counter= 0
    folder_name = file.split(".")[0]
    if not os.path.isdir(os.path.join(dataset_path,folder_name)):
        os.mkdir(os.path.join(dataset_path,folder_name))
    txt_path = os.path.join(path,file)
    with open(txt_path, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            print(line)
            url = line.split(',')[1]
            filename = os.path.join(os.path.join(dataset_path,folder_name),str(counter)+'.jpg')
            print(url)
            print(filename)
            print(url_exists(url))
            if url_exists(url):
                download_url(url,filename)
                counter = counter + 1
