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
import sys

def draw_grids():
   pl = []

   p = os.path.dirname(os.path.realpath(__file__))
   progpath =  p.replace('programsP/posprocessing','programsP')
   folder = p.replace('programsP/posprocessing','receipts')
   subfolders = [f.path for f in os.scandir(folder) if f.is_dir() ] 
   
   for fold in subfolders: 
      photolist = [f for f in listdir(fold) if isfile(join(fold, f))]


      for photo in photolist :
         if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
            print('gridding' + ' ' + photo)
            im = Image.open(fold + '/' + photo)
            d = ImageDraw.Draw(im)
            width,height = im.size
   
            for i in range(0,width,int(width/12)):
               d.line((i,0,i,height),fill=(46,167,125),width = 5)

            for i in range(0,height,int(height/8)):
               d.line((0,i,width,i),fill = (46,167,125),width = 5)

            im.save(photo) 
            src = progpath
            dst = fold
            os.remove(dst + '/' + photo)
            shutil.move(src + '/' + photo, dst)
         
   

if __name__ == '__main__':
   draw_grids()
