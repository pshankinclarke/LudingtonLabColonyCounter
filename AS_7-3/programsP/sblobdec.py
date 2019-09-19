from PIL import Image
from os import listdir
from os.path import isfile, join
import getBlobLoc
import drawGrids
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
   #mypath = '/Users/shankin-clarke/Desktop/AS-7_3/photographs'
   files = [f for f in sorted(listdir(photopath)) if isfile(join(photopath, f))]
   print(photopath)
   print(files)
   _list = []

   drawGrids.draw_grids()
   print('***********************')
   print('***********************')
   print('***********************')

   for fyle in files:
      if fyle.endswith(".png") or fyle.endswith(".jpg") or fyle.endswith('.JPG'):
         print("processing" + ' ' +  fyle)
         fNamePath = photopath +'/' + fyle
         im = Image.open(fNamePath)
         width,height = im.size
         SElist = getBlobLoc.SAE(width,height)
         blob_lyst,cl,track = getBlobLoc.GBAC(fNamePath,SElist) 
         getBlobLoc.draw_on_fig(blob_lyst,fyle)
      
         tempList,finaList= ([] for i in range(2)) 
         #the color counts for all the blobs in each cell need to be organized
         #we have all the color counts cl 
         #we also have a tracker that corresponds to the corresponding cell number
         #put them in their correct bin
         for j in range(96):
            idxs = [i for i, e in enumerate(track) if e == j]
            if not idxs:
               tempList.append(idxs)
            else:
               for idx in idxs: 
                  tempList.append(cl[idx])
            finaList.append(tempList)
            tempList = []
         # once the color counts are in their correct bin
         # reorganize them and make them into a single number for the final count
         reOrgan = [] 
         for lyst in finaList :
            if lyst == [[]]: 
               reOrgan.append([0,0,0])
            else: 
               sum1,sum2,sum3 = (0 for i in range(3))
               for i in range(len(lyst)):
                  sum1 += lyst[i][0]
                  sum2 += lyst[i][1]
                  sum3 += lyst[i][2]
               reOrgan.append([sum1,sum2,sum3])
         _list.append(reOrgan)


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

if __name__ == '__main__':
   exblob()
