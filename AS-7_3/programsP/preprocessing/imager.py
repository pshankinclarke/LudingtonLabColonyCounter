import cropallphotos
from  MasterPath import *
from crop import *

def eximager():
   mylist = tracker
   sliced = tracker

   dbfile = open('_croppedCoord', 'ab') 
   # source, destination 
   pickle.dump(sliced, dbfile)                      
   dbfile.close()

if __name__ == '__main__':
    eximager()
    

