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
   #colonyList_L,colonyList,colonyList_H,AcolonyList_L,AcolonyList,AcolonyList_H
   postprocess = os.path.dirname(os.path.realpath(__file__))
   photopath = postprocess.replace('/programsP/posprocessing','/photographs')
   picklepath = postprocess.replace('/programsP/posprocessing','/_pickle'    )
   files = [f for f in sorted(listdir(photopath)) if isfile(join(photopath, f))]
   photonames = [] 
   for photo in files: 
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         photonames.append(photo)
   _ccf = open(picklepath + '/' + '_cellCounts', 'rb')      
   _cc = pickle.load(_ccf) 
   _ccf.close()



   '''
   print(len(_cc))
   print(len(_cc[0]))
   print(len(_cc[1]))
   print(len(_cc[2]))
   print(len(_cc[3]))
   print(len(_cc[4]))
   print(len(_cc[5]))
   print(len(_cc))
   print(_cc[0][0])
   print(_cc[1][0])
   print(_cc[2][0])
   print(_cc[3][0])
   print(_cc[4][0])
   print(_cc[5][0])
   '''
   #MCH_#NP_#CFU
   MML = []
   
   import itertools
   s_cc = [_cc[x:x+6] for x in range(0, len(_cc), 6)]
   for i in range(len(photonames)):
      
      
      #chunks = [data[x:x+2] for x in range(0, len(data), 2)]
      Echunks_L = s_cc[i][0] 
      Echunks = s_cc[i][1]
      Echunks_H = s_cc[i][2]
      
      Dchunks_L = s_cc[i][3]
      Dchunks = s_cc[i][4]
      Dchunks_H = s_cc[i][5]
      headings = ['photograph','row','column','loc','ratio1','ratio2','date','time','treatment','cw/rw','CFUs lower','MCH lower','NP lower','CFUs middle','MCH middle','NP middle','CFUs upper','MCH upper','NP upper','alternative CFUs lower','alternative MCH lower',' alternative NP lower',' alternative CFUs middle',' alternative MCH middle','alternative NP middle','alternative CFUs upper','alternative MCH upper','alternative NP upper']
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
          if string != 'controlRL.png' and string != 'controlSYN.png':
            fullinner = [string,rac[i][0],rac[i][1],rac[i],l[2],l[3],l[5],l[7],l[6],l[len(l)-1].replace('.png',''),Echunks_L[i][2],Echunks_L[i][0],Echunks_L[i][1],Echunks[i][2],Echunks[i][0],Echunks[i][1],Echunks_H[i][2],Echunks_H[i][0],Echunks_H[i][1],Dchunks_L[i][2],Dchunks_L[i][0],Dchunks_L[i][1],Dchunks[i][2],Dchunks[i][0],Dchunks[i][1],Dchunks_H[i][2],Dchunks_H[i][0],Dchunks_H[i][1]]
            if i == 0 : 
               ML.append(headings)
               ML.append(fullinner) 
            else:
               ML.append(fullinner)   
          else:
            partialinner = [string,rac[i][0],rac[i][1],rac[i],Echunks_L[i][2],Echunks_L[i][0],Echunks_L[i][1],Echunks[i][2],Echunks[i][0],Echunks[i][1],Echunks_H[i][2],Echunks_H[i][0],Echunks_H[i][1],Dchunks_L[i][2],Dchunks_L[i][0],Dchunks_L[i][1],Dchunks[i][2],Dchunks[i][0],Dchunks[i][1],Dchunks_H[i][2],Dchunks_H[i][0],Dchunks_H[i][1]]
            if i == 0 :
               ML.append(['photograph','row','column','loc','CFUs lower','MCH lower','NP lower','CFUs middle','MCH middle','NP middle','CFUs upper','MCH upper','NP upper','alternative CFUs lower','alternative MCH lower',' alternative NP lower',' alternative CFUs middle',' alternative MCH middle','alternative NP middle','alternative CFUs upper','alternative MCH upper','alternative NP upper'])
               print('&&&&&&&&&&&&&&&&&&&&&')
               print(partialinner)
               ML.append(partialinner)
            else:
               ML.append(partialinner)
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
