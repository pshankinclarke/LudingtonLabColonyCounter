import os
import pickle
import cv2
from PIL import Image
from os import remove
import cv2
from os import listdir
from os.path import isfile, join
import csv
import os
from os import path
import shutil
from PIL import Image, ImageDraw
import numpy as np
import sys 

def exSave():
   dir_path = os.path.dirname(os.path.realpath(__file__))
   photopath = dir_path.replace('/programsP/preprocessing','/photographs')
   unanalpath = photopath.replace('photographs','unanalyzed') 
   photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   #put original photographs in the unanalyzed directory
   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         img = Image.open(photopath + '/' + photo)
         img.save(unanalpath + '/'  +  photo)

   rotdir = photopath + '/' + 'rot'
   photolist = [f for f in listdir(rotdir) if isfile(join(rotdir, f))]
   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         img = Image.open(rotdir + '/' + photo)
         img.save(unanalpath + '/'  +  photo)

if __name__ == '__main__':
    exSave()
