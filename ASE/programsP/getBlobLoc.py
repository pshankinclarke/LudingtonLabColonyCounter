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

def GBACp(fylepath,comblist):
  
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
       ff = '/Users/parkershankin-clarke/Desktop/take/AS_7-3/_pickle/databases/databasecontrol'
       dbfile = open(ff, 'rb')
       db = pickle.load(dbfile)
       dbfile.close()

    colonycountL = []
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
    if stub != 'controlRL' and stub != 'controlSYN' and stub != 'controlSYN_rec' and stub != 'controlRL_rec':
       dilution = fyle.split('_')[4]
    
    
    if stub == 'controlRL':
       circleArea = 1590.43
    elif stub == 'controlSYN':
        circleArea = 5026.55
    else:
        if dilution == '10^-1':
           circleArea = AreaFinder.Getarea('10^-1')
        elif dilution == '10^-2':
           circleArea = AreaFinder.Getarea('10^-2')
        else:
           circleArea = AreaFinder.Getarea('10^-3')
    
    if fyle.split('_')[len(fyle.split('_')) - 1] == 'res':
       print('intiated')
       circleArea = circleArea/16
    
    for i in range(len(mxMCH)):
       colonycountL.append([len(mxMCH[i])/circleArea,len(mxNP[i])/circleArea,len(mx[i])/circleArea])
    filtest.draw(transpredL,transcord,photopath,comblist,colonycountL)
    return colonycountL 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
        
        
        
        
        
        
        
        
