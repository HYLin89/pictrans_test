import glob
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
pic_root = os.environ.get("des")
jpg = glob.glob(f'{pic_root}*.[wW][eE][bB][pP]')

# print(jpg)
if jpg:
    for i in jpg:
        im = Image.open(i)
        name = i.lower().split('\\')[1]
        new = name.replace('webp','png')
        im.save(f'{pic_root}{new}','png')
        
    print('all set')
else:
    print('no file to transfile')