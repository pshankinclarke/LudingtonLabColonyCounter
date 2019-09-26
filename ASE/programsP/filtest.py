import numpy as np
import pickle
import os
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
import shutil
from PIL import ImageFont
from PIL import ImageDraw
def MakeData(datalist,pathh):
   blob = datalist[0]
   photograph = datalist[1]
   try:
      flat_blob = [item for sublist in blob for item in sublist]
      y,x,radius = flat_blob
   except: 
      y,x,radius = blob
   center = (x,y)
   coord = []
   percents = [0,.05,.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.65,.7,.75,.8,.85,.9,.95,]
   rightCord = []
   leftCord = []
   for percent in percents:
      rightCord.append((radius * percent + center[0],center[1]))
      leftCord.append((center[0] - (radius * percent),center[1]))
   upCord = []
   downCord = []
   for percent in percents:
      upCord.append((center[0],radius * percent + center[1]))
      downCord.append((center[0], center[1] - (radius * percent)))

   coord = coord + [rightCord, upCord,leftCord,downCord]
   flat_list = [item for sublist in coord for item in sublist]
   FList = getColor(flat_list,photograph,pathh)
   return FList,photograph


def getColor(cordList,photo,dbpathh):
   
   cir_path = os.path.dirname(os.path.realpath(__file__))
   pathList = [cir_path + '/filt2Data/trainfilt2/MCH',cir_path + '/filt2Data/trainfilt2/NP',cir_path + '/filt2Data/trainfilt2/BGD',cir_path + '/filt2Data/trainfilt2RL/MCH',cir_path + '/filt2Data/trainfilt2RL/NP',cir_path +'/filt2Data/trainfilt2RL/BGD',cir_path + '/filt2Data/trainfiltSYN/MCH',cir_path + '/filt2Data/trainfiltSYN/NP',cir_path + '/filt2Data/trainfiltSYN/BGD',cir_path + '/filt2Data/trainfilt2/NPMK']
   

   if dbpathh == 'dbf2M' or dbpathh == 'dbNf2' or dbpathh == 'B': 
      if photo[0] == 'M':
         path = pathList[0]
      elif photo[0] == 'N':
          path = pathList[1]
      else:
         path = pathList[2]
   if dbpathh == 'KNPM': 
       path = pathList[len(pathList) - 1]
   if dbpathh == 'dbS_M' or dbpathh == 'dbS_N' or dbpathh == 'BS':
      if photo[0] == 'M':
         path = pathList[6]
      elif photo[0] == 'N':
         path = pathList[7]
      else:  
         path = pathList[8]
   
   if dbpathh == 'dbR_M' or dbpathh == 'dbR_N' or dbpathh == 'BR':
      if photo[0] == 'M':
         path = pathList[3]
      elif photo[0] == 'N':
         path = pathList[4]
      else:  
         path = pathList[5]
   FList = []
   im = Image.open(path + '/' + photo)
   pix = im.load()
   width,height = im.size
   for cord in cordList:
      x = cord[0]
      y = cord[1]

      if cord[0] >= width:
         x = width - 1
      if cord[1] >= height:
         y = height - 1
      if cord[0] <= 0:
         x = 1
      if cord[1] <= 0:
         y = 1
      n = ( pix[x,y][0] + pix[x,y][1]  + pix[x,y][2] ) / 3
      FList.append(n)
   return FList
  
def makeLabels(compList,pathh):
   labelList = [] 
   featureList2 = []
   labelList2 = [] 
   featureList = []
   
   SlabelList = []
   SfeatureList2 = []
   SlabelList2 = []
   SfeatureList = []

   RlabelList = []
   RfeatureList2 = []
   RlabelList2 = []
   RfeatureList = []

   C = []
   CR = []
   CS = []

   for pa,co in zip(pathh,compList):
      if pa == 'dbf2M' or pa == 'dbNf2' or pa == 'B':
         C.append(co)
      if pa == 'dbS_M' or pa == 'dbS_N' or pa == 'BS':
         CS.append(co)   
      if pa == 'dbR_M' or pa == 'dbR_N' or pa == 'BR':
         CR.append(co)

   for comp in C:
      clr,pht = comp
      if pht[0] == 'N' or pht[0] == 'M' :
         lfl = [1] * len(clr)
         labelList.extend(lfl)
         featureList.extend(clr)
      else :
         lfl = [2] * len(clr)
         labelList.extend(lfl)
         featureList.extend(clr)
   for comp in compList:
      clr,pht = comp
      if pht[0] == 'N':
         lfl = [1] * len(clr)
         labelList2.extend(lfl)
         featureList2.extend(clr)
      elif pht[0] == 'M':
         lfl = [2] * len(clr)
         labelList2.extend(lfl)
         featureList2.extend(clr)


   for comp in CR:
      clr,pht = comp
      if pht[0] == 'N' or pht[0] == 'M' :
         lfl = [1] * len(clr)
         RlabelList.extend(lfl)
         RfeatureList.extend(clr)
      else :
         lfl = [2] * len(clr)
         RlabelList.extend(lfl)
         RfeatureList.extend(clr)
   for comp in compList:
      clr,pht = comp
      if pht[0] == 'N':
         lfl = [1] * len(clr)
         RlabelList2.extend(lfl)
         RfeatureList2.extend(clr)
      elif pht[0] == 'M':
         lfl = [2] * len(clr)
         RlabelList2.extend(lfl)
         RfeatureList2.extend(clr)


   for comp in CS:
      clr,pht = comp
      if pht[0] == 'N' or pht[0] == 'M' :
         lfl = [1] * len(clr)
         SlabelList.extend(lfl)
         SfeatureList.extend(clr)
      else :
         lfl = [2] * len(clr)
         SlabelList.extend(lfl)
         SfeatureList.extend(clr)
   for comp in compList:
      clr,pht = comp
      if pht[0] == 'N':
         lfl = [1] * len(clr)
         SlabelList2.extend(lfl)
         SfeatureList2.extend(clr)
      elif pht[0] == 'M':
         lfl = [2] * len(clr)
         SlabelList2.extend(lfl)
         SfeatureList2.extend(clr)
   return [featureList,labelList,featureList2,labelList2,RfeatureList,RlabelList,RfeatureList2,RlabelList2,SfeatureList,SlabelList,SfeatureList2,SlabelList2]
#trainn(features,labels,features2,labels2,Rfeatures,Rlabels,Rfeatures2,Rlabels2,Sfeatures,Slabels,Sfeatures2,Slabels2)
def trainn(features,labels,features2,labels2,Rfeatures,Rlabels,Rfeatures2,Rlabels2,Sfeatures,Slabels,Sfeatures2,Slabels2): 
   from sklearn.linear_model import LogisticRegression
   clfLR = LogisticRegression(solver='lbfgs').fit(features, labels)
   clfLR2 = LogisticRegression(solver='lbfgs').fit(features2, labels2)

   RclfLR = LogisticRegression(solver='lbfgs').fit(Rfeatures, Rlabels)
   RclfLR2 = LogisticRegression(solver='lbfgs').fit(Rfeatures2, Rlabels2)

   SclfLR = LogisticRegression(solver='lbfgs').fit(Sfeatures, Slabels)
   SclfLR2 = LogisticRegression(solver='lbfgs').fit(Sfeatures2, Slabels2)
   
   return clfLR,clfLR2,RclfLR,RclfLR2,SclfLR,SclfLR2

def predict(classifier,classifier2,fule):
   cir_path = os.path.dirname(os.path.realpath(__file__))
   path = cir_path.replace('programsP','photographs')
   onlyfiles = [fule]
   cordL = []
   fetList = []
   predL = []
   transpredL = []
   transfet = []
   transcord = []
   photopath  = []
   for fyle in onlyfiles: 
      if fyle.endswith('.png') or fyle.endswith('.jpg') or fyle.endswith('.JPG'):
         photopath.append(fyle)
         im = Image.open(fyle)
         width,height = im.size
         for x in range(width):
            for y in range(height):
               cordL.append([x,y])
   pix = im.load()
   for cord in cordL:
      x = cord[0]
      y = cord[1]
      n = ( pix[x,y][0] + pix[x,y][1]  + pix[x,y][2] ) / 3
      fetList.append(n)  
   features = [fetList[i:i+1] for i in range(0, len(fetList), 1)]
   features = [features[i:i+1] for i in range(0, len(features), 1)]
   for feat in features: 
      predL.append(classifier.predict(feat)) 
   for i in range(len(features)):
      feat = features[i]
      pred = predL[i]
      cord = cordL[i]
      if pred[0] == 1: 
         transfet.append(feat)
         transcord.append(cord) 
      else: 
         continue
   for tfeat in transfet:
       transpredL.append(classifier2.predict(tfeat))
   
   
   #draw(transpredL,transcord,photopath)
   return [transpredL,transcord,photopath]

def draw(predictionList,coordinates,img,combList,count):
   spl = img[0].split('/')
   fyle = spl[len(spl)-1]
   im = Image.open(img[0])
   imgg = Image.open(img[0])
   imggg = Image.open(img[0])
   pixels = im.load() # create the pixel map
   for i in range(len(coordinates)):
      cord = coordinates[i]
      pred = predictionList[i]
      if pred[0] == 1:
         pixels[cord[0],cord[1]] = (119, 78 ,252)
   
   pixels = imgg.load()  
   for i in range(len(coordinates)):
      cord = coordinates[i]
      pred = predictionList[i]
      if pred[0] == 2:
         pixels[cord[0],cord[1]] = (242, 87 ,87)
   pixels = imggg.load()
   for i in range(len(coordinates)):
      cord = coordinates[i]
      pred = predictionList[i]
      if pred[0] == 2:
         pixels[cord[0],cord[1]] = (242, 87 ,87)
      elif pred[0] == 1:
         pixels[cord[0],cord[1]] = (119, 78 ,252)

   textsize = 65 
   move = 35
   draw = ImageDraw.Draw(imggg)
   font_type = ImageFont.truetype("arial.ttf", textsize)
   # draw.text((x, y),"Sample Text",(r,g,b))
   for comb,c in zip(combList,count):
       xstart = comb[0][0] 
       xend = comb[1][0]
       ystart = comb[0][1]
       yend = comb[1][1]
       midx = int((xstart + xend)/2) - move
       midy = int((ystart + yend)/2)
       #round(answer, 2)
       draw.text((midx, midy),str(round(c[2],2)),(255,255,255),font=font_type)
   imggg.save('recp_TLT_' + fyle)

   draw = ImageDraw.Draw(imgg)
   # draw.text((x, y),"Sample Text",(r,g,b))
   for comb,c in zip(combList,count):
       xstart = comb[0][0] 
       xend = comb[1][0]
       ystart = comb[0][1]
       yend = comb[1][1]
       midx = int((xstart + xend)/2) - move
       midy = int((ystart + yend)/2)
       #round(answer, 2)
       draw.text((midx, midy),str(round(c[0],2)),(255,255,255),font=font_type)
   imgg.save('recp_MP_' + fyle)

   draw = ImageDraw.Draw(im)
   # draw.text((x, y),"Sample Text",(r,g,b))
   for comb,c in zip(combList,count):
       xstart = comb[0][0]
       xend = comb[1][0]
       ystart = comb[0][1]
       yend = comb[1][1]
       midx = int((xstart + xend)/2) - move
       midy = int((ystart + yend)/2)
       #round(answer, 2)
       draw.text((midx, midy),str(round(c[1],2)),(255,255,255),font=font_type)
   im.save('recp_NP_' + fyle)


   FName = ['recp_NP_' + fyle ,'recp_MP_' + fyle ,'recp_TLT_' + fyle ]

   src = os.path.dirname(os.path.realpath(__file__))
   dst = src.replace('programsP','receipts')
   for name in FName:
       try:
          shutil.move(src + '/' +  name, dst)
       except:
           os.remove(dst + '/' + name)
           shutil.move(src + '/' +  name, dst)


   return

def makeBGD(datum,pL): 
    cir_path = os.path.dirname(os.path.realpath(__file__))
    pathlist = [cir_path + '/filt2Data/trainfilt2/BGD',cir_path + '/filt2Data/trainfilt2RL/BGD',cir_path + '/filt2Data/trainfiltSYN/BGD']
    identL  = ['B','BR','BS']         
    for path,iden in zip(pathlist,identL):
       p = path.split('/')
       onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
       for fyle in onlyfiles:
          if fyle.endswith('.JPG') or fyle.endswith('.jpg') or  fyle.endswith('.png'):
             im = Image.open(path + '/' + fyle)
             width,height = im.size
             datum.append([np.array([[int(height/2),int(width/2),(width)/2]]),fyle])
             pL.append(iden)
    return datum,pL


def makeNP(datum,pL):
    cir_path = os.path.dirname(os.path.realpath(__file__))
    pathlist = [cir_path + '/filt2Data/trainfilt2/NPMK']
    identL = ['KNPM']
    for path,iden in zip(pathlist,identL):
       p = path.split('/')
       onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
       for fyle in onlyfiles:
          if fyle.endswith('.JPG') or fyle.endswith('.jpg') or  fyle.endswith('.png'):
             im = Image.open(path + '/' + fyle)
             width,height = im.size
             datum.append([np.array([[int(height/2),int(width/2),(width)/2]]),fyle])
             pL.append(iden)
    return datum,pL


def main(fylepath):
   ss = fylepath.split('/')
   photograph = ss[len(ss)-1]
   traininput,pathinput,traincomposite = ([] for i in range(3))
   
   cir_path = os.path.dirname(os.path.realpath(__file__))
   pathList = [cir_path + '/filt2Data/trainfilt2/MCH/dbf2M',cir_path + '/filt2Data/trainfilt2/NP/dbNf2',cir_path + '/filt2Data/trainfilt2RL/MCH/dbR_M',cir_path + '/filt2Data/trainfilt2RL/NP/dbR_N',cir_path + '/filt2Data/trainfiltSYN/MCH/dbS_M',cir_path + '/filt2Data/trainfiltSYN/NP/dbS_N']
   
   for path in pathList:
      p = path.split('/')
      print('opening {} database'.format(p[len(p)-1]))
      dbfile = open(path, 'rb')      
      db = pickle.load(dbfile)
      dbfile.close()
      traininput.append(db)
      for i in range(len(db)):
         pathinput.append(p[len(p)-1])
   
   flat_trainput = [item for sublist in traininput for item in sublist]
   flat_trainput, pathinput = makeBGD(flat_trainput,pathinput)
   flat_trainput, pathinput = makeNP(flat_trainput,pathinput)
   
   for train,path in zip(flat_trainput,pathinput):
      colorList, pht = MakeData(train,path)
      traincomposite.append([colorList, pht])
   FL = makeLabels(traincomposite,pathinput)
   #[featureList,labelList,featureList2,labelList2,RfeatureList,RlabelList,RfeatureList2,RlabelList2,SfeatureList,SlabelList,SfeatureList2,SlabelList2]   
   features = [FL[0][i:i+1] for i in range(0, len(FL[0]), 1)]
   features2 = [FL[2][i:i+1] for i in range(0, len(FL[2]), 1)]
   features = np.array(features)
   features2 = np.array(features2)
   labels = np.array(FL[1])
   labels2 = np.array(FL[3])


   Rfeatures = [FL[4][i:i+1] for i in range(0, len(FL[4]), 1)]
   Rfeatures2 = [FL[6][i:i+1] for i in range(0, len(FL[6]), 1)]
   Rfeatures = np.array(Rfeatures)
   Rfeatures2 = np.array(Rfeatures2)
   Rlabels = np.array(FL[5])
   Rlabels2 = np.array(FL[7])

   Sfeatures = [FL[8][i:i+1] for i in range(0, len(FL[8]), 1)]
   Sfeatures2 = [FL[10][i:i+1] for i in range(0, len(FL[10]), 1)]
   Sfeatures = np.array(Sfeatures)
   Sfeatures2 = np.array(Sfeatures2)
   Slabels = np.array(FL[9])
   Slabels2 = np.array(FL[11])


   clf,clf2,Rclf,Rclf2,Sclf,Sclf2 = trainn(features,labels,features2,labels2,Rfeatures,Rlabels,Rfeatures2,Rlabels2,Sfeatures,Slabels,Sfeatures2,Slabels2)
   if photograph == 'controlRL.png':
      List = predict(Rclf,Rclf2,fylepath)

   elif photograph == 'controlSYN.png':
      List = predict(Sclf,Sclf2,fylepath)   
   else:
      List = predict(clf,clf2,fylepath)
   return List
if __name__ == "__main__":
    main(None)






