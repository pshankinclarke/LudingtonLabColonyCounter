from PIL import Image
from os import listdir
from os.path import isfile, join
import getBlobLoc
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
import pickle
import sys


def exblob():
   dir_path = os.path.dirname(os.path.realpath(__file__))
   progpath = os.path.dirname(os.path.realpath(__file__))
   photopath = progpath.replace('/programsP','/photographs')
   #colonyList_L,colonyList,colonyList_H,AcolonyList_L,AcolonyList,AcolonyList_H 
   _list = []
   files = [f for f in sorted(listdir(photopath)) if isfile(join(photopath, f))]
   for fyle in files:
      if fyle.endswith(".png") or fyle.endswith(".jpg") or fyle.endswith('.JPG'):
         print("processing" + ' ' +  fyle)
         fNamePath = photopath +'/' + fyle
         im = Image.open(fNamePath)
         width,height = im.size
         SElist = getBlobLoc.SAE(width,height)
         RL = getBlobLoc.crp(SElist,fNamePath)
         colonyList_L,colonyList,colonyList_H,AcolonyList_L,AcolonyList,AcolonyList_H  = getBlobLoc.GBACp(fNamePath,SElist,RL)
         print(len(colonyList_L),len(colonyList),len(colonyList_H),len(AcolonyList_L),len(AcolonyList),len(AcolonyList_L))
         total = [colonyList_L,colonyList,colonyList_H,AcolonyList_L,AcolonyList,AcolonyList_H]
         _list.extend(total)
   f = '_cellCounts'
   _cc = open(f, 'ab')       
   pickle.dump(_list, _cc)                      
   _cc.close() 

   src = photopath.replace('photographs', 'programsP')
   dst = photopath.replace('photographs', '_pickle')
   try:
      shutil.move(src + '/' + f, dst)
   except:
      os.remove(dst + '/' + f)
      shutil.move(src + '/' + f, dst)

   #drawGrids.draw_grids()
if __name__ == '__main__':
   exblob()
