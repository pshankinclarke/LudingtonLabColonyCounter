from MasterPath import *

def myround(x, base):
   return base * round(x/base)


def exrez():
   hw = []
   photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         if photo != 'control.png' and photo != 'test.JPG':
            img = cv2.imread(photopath +'/' + photo, cv2.IMREAD_UNCHANGED)
            height,width = img.shape[:2]
            hw = hw + [(height,width)]

   for photo in photolist :
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         if photo != 'control.png' and photo != 'test.JPG':
            print('resizing' + ' ' + photo)
            oldimg = cv2.imread(photopath +'/' + photo, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(oldimg,(hw[0][1], hw[0][0]))    
            height,width = img.shape[:2]      
            heightR = myround(height,8)
            widthR  = myround(width,12)
            name = photo
            ires = cv2.resize(img,(widthR, heightR))
            cv2.imwrite(name,ires)

   src = progpath
   dst = photopath

   files = os.listdir(src)
   for f in files:
      if f.endswith('.png') or f.endswith('.JPG') or f.endswith('.jpg'):
         try:
            shutil.move(src + '/' + f, dst)
         except:
            os.remove(dst + '/' + f)
            shutil.move(src + '/' + f, dst)

   print('***********************')
   print('***********************')
   print('***********************')
if __name__ == '__main__':
    exrez()
