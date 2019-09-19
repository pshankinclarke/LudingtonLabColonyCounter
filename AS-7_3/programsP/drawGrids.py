from PIL import Image, ImageDraw
from os import remove 
import cv2 
from os import listdir
from os import listdir
from os.path import isfile, join
import csv 
import os
from os import path
import shutil
from PIL import Image, ImageDraw


def draw_grids():
   pl = []
   progpath = os.path.dirname(os.path.realpath(__file__))
   photopath = progpath.replace('/programsP','/photographs')
   photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   for photo in photolist :
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         print('gridding' + ' ' + photo)
         im = Image.open(photopath + '/' + photo)
         d = ImageDraw.Draw(im)
         width,height = im.size
   
         for i in range(0,width,int(width/12)):
            d.line((i,0,i,height),fill=(46,167,125),width = 5)

         for i in range(0,height,int(height/8)):
            d.line((0,i,width,i),fill = (46,167,125),width = 5)

         name = 'grided' + photo
         pl.append(name)
         im.save(name)
             
   src = photopath.replace( 'photographs', 'programsP')
   dst = photopath.replace('photographs', 'receipts')

   for f in pl:
       if f.endswith('.png') or f.endswith('.JPG') or f.endswith('.jpg'):
          try:
             shutil.move(src + '/' + f, dst)
          except:
              os.remove(dst + '/' + f)
              shutil.move(src + '/' + f, dst)



