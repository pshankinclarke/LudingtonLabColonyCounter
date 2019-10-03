from  MasterPath import *


def exrot():

   photolist = [f for f in listdir(photorot_dir) if isfile(join(photorot_dir, f))]

   for photo in photolist:
      if photo.endswith('.png') or photo.endswith('.JPG') or photo.endswith('.jpg'):
         print('rotating' + ' ' + photo)
         img = Image.open(photorot_dir + '/' + photo )
         rotated = img.rotate(180)
         rotated.save(photo)

   src = prog_dir
   dst = photo_dir
   files = os.listdir(src)
   for f in files:
      if f.endswith('.png') or f.endswith('.JPG') or f.endswith('.jpg'):
         try:
            shutil.move(src + '/' + f, dst)
         except:
            os.remove(dst + '/' + f)
            shutil.move(src + '/' + f, dst)


if __name__ == '__main__':
    exrot()
