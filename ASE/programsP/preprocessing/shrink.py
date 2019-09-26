import sys
import os
from MasterPath import *


def exSHR(): 
   files = [f for f in listdir(photo_dir) if isfile(join(photo_dir, f))]

   for fyle in files:
      if fyle.endswith('.png') or fyle.endswith('.jpg') or fyle.endswith('.JPG'):
         img = Image.open(photo_dir + '/' + fyle)
         width,height = img.size
         if width > 2000:
            new_img = img.resize((int(width/4),int(height/4)))
            new_img.save(fyle.replace('.png','') + '_res' +'.png')
            '''
            try:
               shutil.move(cir_path + '/' + 'res' + fyle + '.png',dst)
            except:
               os.remove(path + '/' + 'res' + fyle + '.png')
               shutil.move(cir_path + '/' + 'res' + fyle + '.png',dst)
            '''
           
if __name__ == "__main__":
    exSHR()
