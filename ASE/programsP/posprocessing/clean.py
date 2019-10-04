import shutil
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path.replace('/posprocessing','/preprocessing'))


from MasterPath import *

def exC():
   from os import listdir
   from os.path import isfile, join
   print('cleaning')
   photopath = dir_path.replace('programsP/posprocessing','photographs')
   onlyfiles = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   
   for photo in onlyfiles:
       if photo.endswith('.jpg') or photo.endswith('.png') or photo.endswith('.JPG'):
           os.remove(photopath + '/' + photo)
   durs = [Acirc1_dir,Acirc2_dir,Acirc3_dir,Acirc1M_dir,Acirc2M_dir,Acirc3M_dir,AcircND_dir,AcircNDM_dir]
   dst_circ_dir = Acircrep_dir

   for dur in durs:
      try:
         shutil.move(dur,dst_circ_dir)
      except:
         continue
   '''
   durs = [trainfiltSYNMCH_dir,trainfiltSYNNP_dir,trainfiltSYNBGD_dir]

   dst = trainfiltSYNrepository_dir 

   for dur in durs:
      try:
         shutil.move(dur,dst)
      except:
         continue




   durs = [trainfilt2RLMCH_dir,trainfilt2RLNP_dir,trainfilt2RLBGD_dir]
   dst = trainfilt2RLrepository_dir 


   for dur in durs:
      try:
         shutil.move(dur,dst)
      except:
         continue



   '''
   durs = [trainfiltBGD_dir,trainfiltNP_dir,trainfiltMCH_dir]
   dst = trainfiltrepository_dir
   


   for dur in durs:
      try:
         shutil.move(dur,dst)
      except:
         continue
   
   #shutil.rmtree()



if __name__ == '__main__':
    exC()
