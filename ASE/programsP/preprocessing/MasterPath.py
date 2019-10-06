import pickle
import cv2
from PIL import Image
from os import remove
import cv2
from os import listdir
from os.path import isfile, join
import csv
import os
from os import path
import shutil
from PIL import Image, ImageDraw
import numpy as np


from PIL import Image, ImageDraw
import pickle


from os import remove
import cv2
from os import listdir
from os.path import isfile, join
import csv
import os
from os import path
import shutil
from PIL import Image, ImageDraw
import sys


from os import remove
import cv2
from os import listdir
from os.path import isfile, join
import csv
import os
from os import path
import shutil
from PIL import Image, ImageDraw

#/Users/parkershankin-clarke/Desktop/LudingtonLabColonyCounter-master/ASE/cropped

#/Users/parkershankin-clarke/Desktop/LudingtonLabColonyCounter-master/ASE/cropped/receipts



#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/preprocessing
root_dir =  os.path.dirname(os.path.realpath(__file__))
pre_dir = root_dir.replace('/MakeDir.py','')


#/Users/parkershankin-clarke/Desktop/LudingtonLabColonyCounter-master/ASE/cropped
cropped_dir = pre_dir.replace('programsP/preprocessing','cropped')
#/Users/parkershankin-clarke/Desktop/LudingtonLabColonyCounter-master/ASE/cropped/receipts
croppedrep_dir = cropped_dir + '/' + 'receipts'


#/Users/parkershankin-clarke/Desktop/take/AS_7-3/_pickle
pickle_dir = pre_dir.replace('programsP/preprocessing','_pickle')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/_pickle/databases
pickledb_dir = pickle_dir + '/' + 'databases'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc
Acirc_dir = pre_dir.replace('programsP/preprocessing','Acirc')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-1
Acirc1_dir = Acirc_dir + '/' + '10^-1'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-2
Acirc2_dir = Acirc_dir + '/' + '10^-2'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-3
Acirc3_dir = Acirc_dir + '/' + '10^-3'

#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-3
AcircND_dir = Acirc_dir + '/' + 'ND'


#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-1
RAcirc1_dir = Acirc_dir + '/' + '10^-1' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-2
RAcirc2_dir = Acirc_dir + '/' + '10^-2'+ '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-3
RAcirc3_dir = Acirc_dir + '/' + '10^-3'+ '/' + 'rep'


RAcircND_dir = Acirc_dir + '/' + 'ND'+ '/' + 'rep'


#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-1
Acirc1M_dir = Acirc_dir + '/' + '10^-1M'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-2
Acirc2M_dir = Acirc_dir + '/' + '10^-2M'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/Acirc/10^-3
Acirc3M_dir = Acirc_dir + '/' + '10^-3M'
Acircrep_dir = Acirc_dir + '/' + 'repository'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/csv
csv_dir = pre_dir.replace('programsP/preprocessing','csv')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/photographs
photo_dir = pre_dir.replace('programsP/preprocessing','photographs')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/photographs/rot
photorot_dir = photo_dir + '/' + 'rot'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP
prog_dir = pre_dir.replace('programsP/preprocessing','programsP')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/posprocessing
pos_dir = pre_dir.replace('preprocessing','posprocessing')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2
trainfilt_dir =  prog_dir + '/' + 'filt2Data/trainfilt2'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/BGD
trainfiltBGD_dir = trainfilt_dir + '/'  +'BGD'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/BGD/rep
trainfiltBGDrep_dir =  trainfilt_dir + '/'  +'BGD' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/NP
trainfiltNP_dir =  trainfilt_dir + '/'  +'NP'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/NP/rep
trainfiltNPrep_dir = trainfilt_dir + '/'  +'NP' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/MCH
trainfiltMCH_dir =  trainfilt_dir + '/'  +'MCH'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/MCH/rep
trainfiltMCHrep_dir = trainfilt_dir + '/'  +'MCH' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/repository
trainfiltrepository_dir =  trainfilt_dir + '/'  +'repository'


#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/receipts
receipts_dir = pre_dir.replace('programsP/preprocessing','receipts')
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2/unanalyzed
unanalyzed_dir = pre_dir.replace('programsP/preprocessing','unanalyzed')


#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RL_dir =  prog_dir + '/' + 'filt2Data/trainfilt2RL'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLMCH_dir = trainfilt2RL_dir + '/' + 'MCH'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLNP_dir =  trainfilt2RL_dir + '/' + 'NP'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLBGD_dir = trainfilt2RL_dir + '/' + 'BGD'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLMCHrep_dir = trainfilt2RL_dir + '/' + 'MCH' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLNPrep_dir =  trainfilt2RL_dir + '/' + 'NP' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLBGDrep_dir = trainfilt2RL_dir + '/' + 'BGD' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfilt2RLrepository_dir = trainfilt2RL_dir + '/' + 'repository' 


trainfiltSYN_dir =  prog_dir + '/' + 'filt2Data/trainfiltSYN'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNMCH_dir = trainfiltSYN_dir + '/' + 'MCH'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNNP_dir =  trainfiltSYN_dir + '/' + 'NP'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNBGD_dir = trainfiltSYN_dir + '/' + 'BGD'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNMCHrep_dir = trainfiltSYN_dir + '/' + 'MCH' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNNPrep_dir =  trainfiltSYN_dir + '/' + 'NP' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNBGDrep_dir = trainfiltSYN_dir + '/' + 'BGD' + '/' + 'rep'
#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfilt2RL
trainfiltSYNrepository_dir = trainfiltSYN_dir + '/' + 'repository'



#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfiltSYN

#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfiltSYN

#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfiltSYN

#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfiltSYN

#/Users/parkershankin-clarke/Desktop/take/AS_7-3/programsP/filt2Data/trainfiltSYN


