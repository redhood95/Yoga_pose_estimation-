
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
    counter= 0
    folder_name = file.split(".")[0]
    if not os.path.isdir(os.path.join(dataset_path,folder_name)):
        os.mkdir(os.path.join(dataset_path,folder_name))
    txt_path = os.path.join(path,file)
    with open(txt_path, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            url = line.split(',')[1]
            filename = os.path.join(os.path.join(dataset_path,folder_name),str(counter)+'.jpg')
            counter = counter + 1
            print(url)
            r = requests.get(url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived')
