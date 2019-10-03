import os,sys
from MasterPath import *

def clean(folder):
   #print('cleaning')
   for the_file in os.listdir(folder):
      file_path = os.path.join(folder, the_file)
      try:
         if os.path.isfile(file_path):
            os.unlink(file_path)
      except Exception as e:
         print('EXCEPTION RAISED IN CLEAN OF MAKEDIR FOR {}'.format(e))
 
def main():
    dirNames = [pre_dir,pickle_dir,pickledb_dir,Acirc_dir,Acirc1_dir,Acirc2_dir,Acirc3_dir,csv_dir,photo_dir,photorot_dir,prog_dir,pos_dir,trainfilt_dir,trainfiltBGD_dir,trainfiltBGDrep_dir,trainfiltNP_dir,trainfiltNPrep_dir,trainfiltMCH_dir,trainfiltMCHrep_dir,trainfiltrepository_dir,receipts_dir,unanalyzed_dir,Acirc1M_dir,Acirc2M_dir, Acirc3M_dir,trainfilt2RLMCH_dir,trainfilt2RLNP_dir,trainfilt2RLBGD_dir,trainfilt2RLrepository_dir,trainfiltSYNrepository_dir,trainfiltSYNMCH_dir,trainfiltSYNNP_dir,trainfiltSYNBGD_dir,cropped_dir,croppedrep_dir,RAcirc1_dir,RAcirc2_dir,RAcirc3_dir]

    for di in dirNames:
       s = di.split('/')
       name = s[len(s) - 1]
       print('cleaning {}'.format(name))
       try:
          os.mkdir(di)
          print("Directory " , name ,  " Created ")
       except FileExistsError:
          print("Directory " , name ,  " already exists") 
          if di != pre_dir and di != prog_dir and di != pos_dir and di != unanalyzed_dir and di != trainfiltrepository_dir and di != photo_dir and di != photorot_dir and di != trainfiltBGD_dir and  di != trainfiltNP_dir and  di != trainfiltMCH_dir and di != Acirc1_dir and di != Acirc2_dir and di != Acirc3_dir and di != Acirc1M_dir and di != Acirc2M_dir  and di != Acirc3M_dir and di != trainfilt2RLMCH_dir and di != trainfilt2RLNP_dir  and di != trainfilt2RLBGD_dir and di != trainfilt2RLrepository_dir and di != trainfiltSYNrepository_dir  and di != trainfiltSYNMCH_dir and di != trainfiltSYNNP_dir and di != trainfiltSYNBGD_dir:
              clean(di)
          else: 
              print('cleaning witheld from {}'.format(name))








if __name__ == '__main__':
    main()
