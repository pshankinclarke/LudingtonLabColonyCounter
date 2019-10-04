from os import listdir
import os
import sys
from os.path import isfile, join
import statistics
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/preprocessing')
from MasterPath import *
import pickle

def Getarea(dil):
    dilr = []
    dilrM = []
    PI = 3.142
    
    if dil == '10^-1':
       print('**************')
       print('**************')
       print('**************')
       print('Grabbing areas for 10^-1')
       mypath =  Acirc1M_dir
       dilfilesM = [f for f in listdir(mypath) if isfile(join(mypath, f))]
       for fyle in dilfilesM:
          if fyle.endswith('.png') or fyle.endswith('.JPG') or fyle.endswith('.jpg'):
             im = Image.open( mypath  + '/' + fyle)
             width,height = im.size
             radw = width/2
             radh = height/2
             rad = (radw + radh)/2
             dilr.append(rad) 
       mypath =  Acirc1_dir
       _fyle = mypath + '/'  + 'dbr1'
       dbfile = open(_fyle, 'rb') 
       db = pickle.load(dbfile)                       
       dbfile.close() 

       for info in db:
           blobs = info[0] 
           photo = info[1]
           for blob in blobs:
              y,x,r = blob
              dilr.append(r)
       lr = min(dilr)
       mr = statistics.median(dilr)
       hr = max(dilr)

       Area_L = PI * (lr * lr)
       Area = PI * (mr * mr)
       Area_H = PI * (hr * hr)
       return Area_L , Area , Area_H
    
    if dil == '10^-2':
       print('**************')
       print('**************')
       print('**************')
       print('Grabbing areas for 10^-2')
       mypath =  Acirc2M_dir
       dilfilesM = [f for f in listdir(mypath) if isfile(join(mypath, f))]
       for fyle in dilfilesM:
          if fyle.endswith('.png') or fyle.endswith('.JPG') or fyle.endswith('.jpg'):
             im = Image.open( mypath  + '/' + fyle)
             width,height = im.size
             radw = width/2
             radh = height/2
             rad = (radw + radh)/2
             dilr.append(rad) 
       mypath =  Acirc2_dir
       _fyle = mypath + '/'  + 'dbr2'
       dbfile = open(_fyle, 'rb')
       db = pickle.load(dbfile)
       dbfile.close()

       for info in db:
           blobs = info[0]
           photo = info[1]
           for blob in blobs:
              y,x,r = blob
              dilr.append(r)
       lr = min(dilr)
       mr = statistics.median(dilr)
       hr = max(dilr)

       Area_L = PI * (lr * lr)
       Area = PI * (mr * mr)
       Area_H = PI * (hr * hr)
       return Area_L , Area , Area_H
              
    if dil == '10^-3':
       print('**************')
       print('**************')
       print('**************')
       print('Grabbing areas for 10^-3')
       mypath =  Acirc3M_dir
       dilfilesM = [f for f in listdir(mypath) if isfile(join(mypath, f))]
       for fyle in dilfilesM:
          if fyle.endswith('.png') or fyle.endswith('.JPG') or fyle.endswith('.jpg'):
             im = Image.open( mypath  + '/' + fyle)
             width,height = im.size
             radw = width/2
             radh = height/2
             rad = (radw + radh)/2
             dilr.append(rad)
       mypath =  Acirc3_dir
       _fyle = mypath + '/'  + 'dbr3'
       dbfile = open(_fyle, 'rb')
       db = pickle.load(dbfile)
       dbfile.close()

       for info in db:
           blobs = info[0]
           photo = info[1]
           for blob in blobs:
              y,x,r = blob
              dilr.append(r)
       lr = min(dilr)
       mr = statistics.median(dilr)
       hr = max(dilr)

       Area_L = PI * (lr * lr)
       Area = PI * (mr * mr)
       Area_H = PI * (hr * hr)
       return Area_L , Area , Area_H 
    
    if dil == 'ND':
       print('**************')
       print('**************')
       print('**************')
       print('Grabbing areas for ND')
       mypath =  AcircND_dir
       dilfilesM = [f for f in listdir(mypath) if isfile(join(mypath, f))]
       for fyle in dilfilesM:
          if fyle.endswith('.png') or fyle.endswith('.JPG') or fyle.endswith('.jpg'):
             im = Image.open( mypath  + '/' + fyle)
             width,height = im.size
             radw = width/2
             radh = height/2
             rad = (radw + radh)/2
             dilr.append(rad)
       mypath =  AcircND_dir
       _fyle = mypath + '/'  + 'dbr4'
       dbfile = open(_fyle, 'rb')
       db = pickle.load(dbfile)
       dbfile.close()

       for info in db:
           blobs = info[0]
           photo = info[1]
           for blob in blobs:
              y,x,r = blob
              dilr.append(r)
       lr = min(dilr)
       mr = statistics.median(dilr)
       hr = max(dilr)

       Area_L = PI * (lr * lr)
       Area = PI * (mr * mr)
       Area_H = PI * (hr * hr)
       return Area_L , Area , Area_H

if __name__ == '__main__':
    Getarea(None)
