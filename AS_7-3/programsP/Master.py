import sys
import os
def service_func():
   DL = []
   #if files exist in unanalyzed then move them to photographs
   print("Please ensure that all photos are in the proper folder")
   #print("Would you like your photos to be cropped automatically? (y/n)")
   #autoCrop = input(":")
   #DL.autoCrop
   return ['y']

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    DL = service_func()
    sys.path.insert(0, dir_path + '/preprocessing')
    if DL[0] == 'y':
       import cpy 
       cpy.exSave()
       import RCZ
       RCZ.exrez()
       import rotate
       rotate.exrot()
       import sblobdec
       sblobdec.exblob()
       sys.path.insert(0, dir_path + '/posprocessing') 
       import SquareCSV
       SquareCSV.exS()
    else:
       import rotate
       rotate.exrot()
       import imager
       imager.eximager()
       import cropallphotos
       cropallphotos.ex()
       sys.exit()
