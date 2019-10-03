from PIL import Image
from skimage.feature import blob_log, blob_doh,blob_dog 
from skimage.color import rgb2gray
from skimage import io
from skimage.transform import resize
from skimage.feature import blob_dog
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.patches import Circle
import os
import shutil
import sys
import filtest
import pickle
import cv2
from os import listdir
from os.path import isfile, join
from PIL import Image
import statistics


import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


'''
def normalizeCirc(xb,yb,x00,y00,InsideBlobList):
   normalizedBlobList = [] 
   for blob in InsideBlobList:
      ys,xs,rs = blob
      xd = xs - xb/2
      yd = ys - yb/2
      xn = x00 + xd
      yn = y00 + yd
      normalizedBlobList.append((yn,xn,rs))
   return normalizedBlobList
'''

def crp(SAE,photo):
    img = cv2.imread(photo)
    #image_name_split = img.split('/')
    #image_name = image_name_split[len(image_name_split) - 1]
    cur_path = os.path.dirname(os.path.realpath(__file__))
    idx = 0
    for crp_cord in SAE:
       cord1 = SAE[idx][0] 
       cord2 = SAE[idx][1]
       x_start = cord1[0]     
       y_start = cord1[1]    
       x_end = cord2[0]
       y_end = cord2[1]
       crop_img = img[SAE[idx][0][1]:SAE[idx][1][1],SAE[idx][0][0]:SAE[idx][1][0]]
       cv2.imwrite("cropped" + str(idx) + ".jpg", crop_img)
       try:
          shutil.move(cur_path + '/' + "cropped" + str(idx) + ".jpg"  ,cur_path.replace('programsP','cropped'))
       except:
          os.remove(cur_path.replace('programsP','cropped')  + '/' + "cropped" + str(idx) + ".jpg")
          shutil.move(cur_path + '/' + "cropped" + str(idx) + ".jpg"  ,cur_path.replace('programsP','cropped'))
       idx += 1
    RadiusList = detect()
    return RadiusList

def detect():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    mypath = cur_path.replace('programsP','cropped')
    cfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    cfiles.sort(key=natural_keys)
    globalRadius = []
    for fyle in cfiles:
       if fyle.endswith('.png') or fyle.endswith('.JPG') or fyle.endswith('.jpg'):
          print('making receipt for {}'.format(fyle))
          localRadius = []
          #image = Image.open(mypath + '/' + fyle) 
          #image = imread(mypath + '/' + fyle)
          image = plt.imread(mypath + '/' + fyle) 
          image_gray = rgb2gray(image)
          blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
          blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
          fig,ax = plt.subplots(1)
          ax.set_aspect('equal') 
          ax.imshow(image)
          for blob in blobs_log:
            y, x, r = blob
            if r > 3:
               c = plt.Circle((x, y), r, color='b', linewidth=2, fill=False)
               localRadius.append(r)
               ax.add_patch(c)
          globalRadius.append(localRadius)
          try:
             plt.savefig('rep' + fyle, bbox_inches='tight')
          except:
             print('EXCEPTION')
             print(fyle)
             continue
          try:
             shutil.move(cur_path + '/' + 'rep' + fyle,mypath + '/' + 'receipts' )
          except:
             os.remove(mypath + '/' + 'receipts' + '/' + 'rep' + fyle)
             shutil.move(cur_path + '/' + 'rep' + fyle,mypath + '/' + 'receipts')
          plt.close('all')
    return globalRadius




def SAE(width,height):
   widthIterator = 12
   heightIterator = 8
   Hstep= int(height/heightIterator)
   Wstep = int(width/widthIterator)
   Slist,Elist,combList = ([] for i in range(3))

   for y in range(0,(height-Hstep)+1,Hstep):
      for x in range(0,(width-Wstep)+1,Wstep):
         Slist = Slist + [(x,y)]
   for y in range(Hstep,(height)+1,Hstep):
      for x in range(Wstep,(width)+1,Wstep):
         Elist = Elist + [(x,y)]
   for pos in range(0,len(Slist)):
      combList = combList + [(Slist[pos],Elist[pos])]
   return combList

def GBACp(fylepath,comblist,RL):
  
    spl = fylepath.split('/')
    fyle = spl[len(spl)-1]

    pulldb = False
    if not pulldb:    
       db = filtest.main(fylepath)
       stub = fyle.replace('.png','')
       dbfile = open('database' + stub, 'ab')
       pickle.dump(db, dbfile)
       dbfile.close()
       src =  os.path.dirname(os.path.realpath(__file__))
       dst = src.replace('programsP','_pickle/databases')
       
       try:
          shutil.move(src + '/' + 'database' + stub , dst)
       except:
          os.remove(dst + '/' + 'database' + stub) 
          shutil.move(src + '/' + 'database' + stub, dst)
    else:
       print('pulling database')
       ff = '/Users/parkershankin-clarke/Desktop/LudingtonLabColonyCounter-master/ASE/_pickle/databases/databasecontrolSYN' 
       dbfile = open(ff, 'rb')
       db = pickle.load(dbfile)
       dbfile.close()

    transpredL = db[0]
    transcord = db[1] 
    photopath = db[2]
    
    mx = [[] for i in range(96)]
    mxMCH = [[] for i in range(96)]
    mxNP = [[] for i in range(96)]
    for pred,cord in zip(transpredL,transcord):
        x,y = cord
        for i in range(len(comblist)):
           comb = comblist[i]
           if x < comb[1][0] and x >= comb[0][0] and y < comb[1][1] and y >= comb[0][1] and pred == 2:
              mxMCH[i].append(1)
    for pred,cord in zip(transpredL,transcord):
        x,y = cord
        for i in range(len(comblist)):
           comb = comblist[i]
           if x < comb[1][0] and x >= comb[0][0] and y < comb[1][1] and y >= comb[0][1] and pred == 1:
              mxNP[i].append(1)

    for pred,cord in zip(transpredL,transcord):
        x,y = cord
        for i in range(len(comblist)):
           comb = comblist[i]
           if x < comb[1][0] and x >= comb[0][0] and y < comb[1][1] and y >= comb[0][1]:
              mx[i].append(1)


    import AreaFinder
    stub = fyle.replace('.png','')
    if stub != 'controlRL' and stub != 'controlSYN' and stub != 'controlSYN_rec' and stub != 'controlRL_rec':
       dilution = fyle.split('_')[4]
    
    
    if stub == 'controlRL':
       circleArea_H = 1590.43
       circleArea = 1590.43
       circleArea_L = 1590.43
    elif stub == 'controlSYN':
        circleArea_L = 5026.55
        circleArea = 5026.55
        circleArea_H = 5026.55
    else:
        if dilution == '10^-1':
           circleArea_L, circleArea,circleArea_H  = AreaFinder.Getarea('10^-1')
        elif dilution == '10^-2':
           circleArea_L, circleArea,circleArea_H  = AreaFinder.Getarea('10^-2')
        elif dilution == '10^-3': 
           circleArea_L, circleArea,circleArea_H  = AreaFinder.Getarea('10^-3')

    median_RL = []
    medianL_RL = []
    medianH_RL = []
    for radii in RL: 
       if radii != []:
          median_RL.append(statistics.median(radii))
          medianL_RL.append(statistics.median_low(radii))
          medianH_RL.append(statistics.median_high(radii))
       else:
          continue

    colonycountL_H = []
    colonycountL = []
    colonycountL_L = []

    AcolonycountL_H = []
    AcolonycountL = []
    AcolonycountL_L = []

    PI = 3.142
    for i in range(len(mxMCH)):
       colonycountL_H.append([len(mxMCH[i])/circleArea_H,len(mxNP[i])/circleArea_H,len(mx[i])/circleArea_H])
    for i in range(len(mxMCH)):
       colonycountL.append([len(mxMCH[i])/circleArea,len(mxNP[i])/circleArea,len(mx[i])/circleArea])
    for i in range(len(mxMCH)):
       colonycountL_L.append([len(mxMCH[i])/circleArea_L,len(mxNP[i])/circleArea_L,len(mx[i])/circleArea_L])
    
    for i in range(len(mxMCH)):
       if RL[i] != []:
          circleArea = max(RL[i]) * max(RL[i]) * PI 
          
          AcolonycountL_H.append([len(mxMCH[i])/circleArea,len(mxNP[i])/circleArea,len(mx[i])/circleArea])
       else:
           AcolonycountL_H.append([0,0,0])
    for i in range(len(mxMCH)):
       if RL[i] != []:
          circleArea = statistics.median(RL[i]) * statistics.median(RL[i]) * PI 
          AcolonycountL.append([len(mxMCH[i])/circleArea,len(mxNP[i])/circleArea,len(mx[i])/circleArea])
       else:
           AcolonycountL.append([0,0,0])
    for i in range(len(mxMCH)):
       if RL[i] != []:
          circleArea = min(RL[i]) * min(RL[i]) * PI 
          AcolonycountL_L.append([len(mxMCH[i])/circleArea,len(mxNP[i])/circleArea,len(mx[i])/circleArea])
       else:
           AcolonycountL_L.append([0,0,0]) 

    filtest.draw(transpredL,transcord,photopath,comblist,AcolonycountL_L,AcolonycountL,AcolonycountL_H,'D')
    filtest.draw(transpredL,transcord,photopath,comblist,colonycountL_L,colonycountL,colonycountL_H,'E') 
    return colonycountL_L,colonycountL,colonycountL_H,AcolonycountL_L,colonycountL,AcolonycountL_H
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
        
        
        
        
        
        
        
        
