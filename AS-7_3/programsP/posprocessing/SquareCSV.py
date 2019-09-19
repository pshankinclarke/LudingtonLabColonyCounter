import re
import random
from PIL import Image
from os import listdir
from os.path import isfile, join
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

def exS():
   postprocess = os.path.dirname(os.path.realpath(__file__))
   photopath = postprocess.replace('/programsP/posprocessing','/photographs')

   files = [f for f in sorted(listdir(photopath)) if isfile(join(photopath, f))]
   photonames = [] 
   for photo in files: 
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         photonames.append(photo)
   print(photonames)
   _ccf = open('/Users/shankin-clarke/Desktop/AS-7_3/_pickle/_cellCounts', 'rb')      
   _cc = pickle.load(_ccf) 
   _ccf.close() 

   MML = []
   for i in range(len(photonames)):

      #chunks = [data[x:x+2] for x in range(0, len(data), 2)]
      chunks = _cc[i]
      headings = ['photograph','row','column','loc','ratio1','ratio2','CFUs','MCH','NP','BGD','date','time','treatment','cw/rw']
      arbNumb = []
      lyst = list(range(0,49)) + list(range(1,49))

      string = photonames[i]
      l = re.sub('.JPG', '', string)
      l = re.sub('48vials', '', l)
      l = re.split('_',l)
       
      import itertools
      
      a = ['a','b','c','d','e','f','g','h']
      
      b = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12]
  
      rac = [(x,y) for x in a for y in list(reversed(b))]
      
      ML = []
     
      
      for i in range(len(rac)):
         if string != 'control.png': 
            if i == 0 : 
               ML.append(headings)
               ML.append([string,rac[i][0],rac[i][1],rac[i],l[6],l[7],chunks[i][0] + chunks[i][1],chunks[i][0],chunks[i][1],chunks[i][2],l[4],l[8],l[9],l[10]]) 
            else: 
               ML.append([string,rac[i][0],rac[i][1],rac[i],l[6],l[7],chunks[i][0] + chunks[i][1],chunks[i][0],chunks[i][1],chunks[i][2],l[4],l[8],l[9],l[10]])
         else:
            if i == 0 :
               ML.append(['photograph','row','column','loc','CFUs','MCH','NP','BGD'])
               ML.append([string,rac[i][0],rac[i][1],rac[i],chunks[i][0] + chunks[i][1],chunks[i][0],chunks[i][1]])
            else:
               ML.append([string,rac[i][0],rac[i][1],rac[i],chunks[i][0] + chunks[i][1],chunks[i][0],chunks[i][1]])
      MML.append(ML)
   MMLf = [item for sublist in MML for item in sublist]

   import csv
   with open("database.csv", "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerows(MMLf)

   src = photopath.replace('photographs','programsP')
   dst = photopath.replace('photographs','csv')
   
   files = os.listdir(src)
   for f in files:
      if f.endswith('.csv'):
          try:
             shutil.move(src + '/' + f, dst)
          except:
             os.remove(dst + '/' + f)
             shutil.move(src + '/' + f, dst)

if __name__ == '__main__':
    exS()
