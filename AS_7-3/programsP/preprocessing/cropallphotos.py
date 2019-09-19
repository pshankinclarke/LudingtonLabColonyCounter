from  MasterPath import *


def ex():
   prepath = os.path.dirname(os.path.realpath(__file__))
   root_path = prepath.replace('/programsP/preprocessing','')
   progpath = prepath.replace('/preprocessing','')
   rotpath = root_path + '/' + 'photographs/rot'
   photopath = root_path + '/' + 'photographs'
   photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   unanalpath = root_path + '/' + 'unanalyzed'
   dbfile = open('_croppedCoord', 'rb')
   cropCoord = pickle.load(dbfile)
   dbfile.close()  

   photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
   
   #put original photographs in the unanalyzed directory
   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         img = Image.open(photopath + '/' + photo)
         img.save(unanalpath + '/'  +  photo)
       
   
   for photo in photolist:
      if photo != 'control.png' and photo != 'test.JPG':
         if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
            print('cropping' + ' ' + photopath + '/' + photo)
            img = Image.open(photopath + '/' + photo)
            pixels = img.load() 
            width, height = img.size
            rgb_im = img.convert('RGB')
            blank = Image.new('RGB', (abs(10000),abs(10000)), color = (0, 0, 0))
            xstart = cropCoord[0][0]
            ystart = cropCoord[0][1]
            xend   = cropCoord[1][0]
            yend   = cropCoord[1][1]
            for x in range(xstart,xend):
               for y in range(ystart,yend):
                  red, green, blue= rgb_im.getpixel((int(x),int(y)))
                  blank.putpixel( (int(x),int(y)), (red, green, blue))
            blank.save('blank.png')
            img = cv2.imread("blank.png")
            os.remove('blank.png')
            crop_img = img[ystart:yend,xstart:xend]
            cv2.imwrite(photo, crop_img)
            cv2.waitKey(0)
   src = progpath
   dst = photopath

   files = os.listdir(src)
   for f in files:
      if f.endswith('.png') or f.endswith('.JPG') or f.endswith('.jpg'):
         try:
            print(src + '/' + f)
            shutil.move(src + '/' + f, dst)
         except:
            os.remove(dst + '/' + f)
            shutil.move(src + '/' + f, dst)

   print('***********************')
   print('***********************')
   print('***********************')

def caller():
   return
if __name__ == '__main__':
    ex()
