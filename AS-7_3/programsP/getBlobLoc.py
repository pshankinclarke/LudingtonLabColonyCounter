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

def detector(fyle):
   img = io.imread(fyle)
   image_gray = rgb2gray((img))
   blobs_log = blob_dog(image_gray, max_sigma=30, threshold=.1)
   blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
   blob_lyst = blobs_log
   return blob_lyst    

def GBAC(fyle,comblist):
   track,cl,ctl= ([] for i in range(3)) 
   blob_lyst = detector(fyle)
   for blob in blob_lyst:
      y,x,r = blob
      c = 0
      for comb in comblist: 
         if x < comb[1][0] and x >= comb[0][0] and y < comb[1][1] and y >= comb[0][1]:
            MCH,NP,BGD,bacList = colonyCounter(fyle,blob,True)
            cl.append([MCH,NP,BGD])
            ctl.append(bacList)
            track.append(c)
         c += 1
   return blob_lyst,cl,track 

def colonyCounter(fyle,blob,T):
   bacList = []
   MCH = NP = BGD = 0
   im = Image.open(fyle)
   rgb_im = im.convert('RGB')
   y,x,r = blob
   try:
      red, green, blue= rgb_im.getpixel((int(x),int(y)))
   except:
      print('raised exception')
   if red > 210 and green > 30:
      MCH += 1
      bacList.append('MCH')
   elif red < 210 and red > 100 and  green >= 0 and green < 40:
      NP += 1
      bacList.append('NP')
   else :
      BGD += 1
      bacList.append('BGD')
   if T:
      return MCH, NP, BGD, bacList  
   else: 
      return [MCH,NP,BGD]

def draw_on_fig(blob_list,fyle):
   
   progpath = os.path.dirname(os.path.realpath(__file__))
   photopath = progpath.replace('/programsP','/photographs')
   repfile =  progpath.replace('/programsP','/receipts') + '/'  + 'grided' + fyle
   
   img = plt.imread(repfile)
   im = Image.open(repfile)
   
   width,height = im.size
   fig,ax = plt.subplots(1,figsize = (width/100,height/100))
   ax.imshow(img)
   for blob in blob_list:
      y,x,r = blob
      countList = colonyCounter(repfile,blob,False)  
      if countList[0] == 1 :
         clr = 'white'
      elif countList[1] ==  1:
         clr = 'blue'
      else:
         clr = 'yellow'       
      circ = Circle((x, y), r, color = clr, linewidth=2, fill=False)
      ax.add_patch(circ)
   fig.savefig('receipt' + fyle)    
   os.remove(repfile)

   src = photopath.replace('photographs', 'programsP')
   dst = photopath.replace('photographs', 'receipts')
   try:
      shutil.move(src + '/' + 'receipt' + fyle, dst)
   except:
      os.remove(dst + '/' + 'receipt' + fyle)
      shutil.move(src + '/' + 'receipt' + fyle, dst)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
        
        
        
        
        
        
        
        
