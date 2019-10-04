from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import numpy as np
import pickle
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from matplotlib.image import imread
from matplotlib.patches import Circle
import imageio
import math
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import cv2
import sys
from pylab import figure, text, scatter, show
import os
from os import listdir
from os.path import isfile, join
import shutil


print('Collecting training data')
print('*************************')
print('*************************')
print('*************************')

def analyze(path):
   cir_path = os.path.dirname(os.path.realpath(__file__))
   files = [f for f in listdir(path) if isfile(join(path, f))]
   loglist = []
   for fyle in files:
      if fyle.endswith('.JPG') or fyle.endswith('.jpg') or fyle.endswith('.png') or fyle.endswith('.jpeg') :
         fNamePath = path + '/' + fyle
         img = plt.imread(fNamePath)
         image_gray = rgb2gray(img)
         image = Image.open(fNamePath)
         width,height = image.size
         rgb_im = image.convert('RGB')


         blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)

         # Compute radii in the 3rd column.
         blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

         blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
         blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
         
         #blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)
         blobs_doh = []
         blobs_list = [blobs_log, blobs_dog, blobs_doh]
         colors = ['yellow', 'lime', 'red']
         titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
	  'Determinant of Hessian']
         sequence = zip(blobs_list, colors, titles)

         fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
         ax = axes.ravel()

         for idx, (blobs, color, title) in enumerate(sequence):
            ax[idx].set_title(title)
            ax[idx].imshow(image)
            for blob in blobs:
               y, x, r = blob
               c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
               ax[idx].add_patch(c)
         ax[idx].set_axis_off()
         fule = 'recp' + fyle
         plt.tight_layout()
         plt.savefig(fule)
         try:
            shutil.move(cir_path + '/' + fule,path + '/' + 'rep')
         except:
            os.remove(path + '/' + 'rep' + '/' +  fule)
            shutil.move(cir_path + '/' + fule,path + '/' + 'rep')
         loglist.append([blobs_log,fyle])
   return loglist


def main():
   cir_path = os.path.dirname(os.path.realpath(__file__))
   radpath1 = cir_path.replace('programsP','Acirc/10^-1')
   radpath2 = cir_path.replace('programsP','Acirc/10^-2')
   radpath3 = cir_path.replace('programsP','Acirc/10^-3')
   radpath4 = cir_path.replace('programsP','Acirc/ND')
   #/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL/BGD
   SynMCH = cir_path + '/' + 'filt2Data/trainfiltSYN/MCH'
   SynNP = cir_path + '/' + 'filt2Data/trainfiltSYN/NP'
   SynBGD = cir_path + '/' + 'filt2Data/trainfiltSYN/BGD'

   RMCH = cir_path + '/' + 'filt2Data/trainfilt2RL/MCH'
   RNP = cir_path + '/' + 'filt2Data/trainfilt2RL/NP'
   RBGD = cir_path + '/' + 'filt2Data/trainfilt2RL/BGD'

   pathList = [cir_path + '/filt2Data/trainfilt2/NP',cir_path + '/filt2Data/trainfilt2/MCH',cir_path + '/filt2Data/trainfilt2/BGD',radpath1,radpath2,radpath3,SynNP,SynMCH,SynBGD,RNP,RMCH,RBGD,radpath4]
   dbN = ['dbNf2','dbf2M','dbf2B','dbr1','dbr2','dbr3','dbS_N','dbS_M','dbS_B','dbR_N','dbR_M','dbR_B','dbr4']

   for path,dbNi in zip(pathList,dbN):
      blobs_dog = analyze(path)
      dbfile = open(dbNi, 'ab') 
      pickle.dump(blobs_dog, dbfile)                     
      dbfile.close() 
      try:
         shutil.move(cir_path + '/' + dbNi , path)
      except: 
         os.remove(path + '/' + dbNi)
         shutil.move(cir_path + '/' + dbNi,path)
      
if __name__ == '__main__':
    main()
