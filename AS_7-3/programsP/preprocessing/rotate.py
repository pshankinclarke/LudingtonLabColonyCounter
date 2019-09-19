from  MasterPath import *


def exrot():

   photolist = [f for f in listdir(rotpath) if isfile(join(rotpath, f))]

   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         print('rotating' + ' ' + photo)
         img = Image.open(rotpath + '/' + photo )
         rotated = img.rotate(180)
         rotated.save(photo)

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


   folder = rotpath
   for the_file in os.listdir(folder):
      file_path = os.path.join(folder, the_file)
      try:
         if os.path.isfile(file_path):
            os.unlink(file_path)
      except Exception as e:
         print(e)
   print('***********************')
   print('***********************')
   print('***********************')
if __name__ == '__main__':
    exrot()
