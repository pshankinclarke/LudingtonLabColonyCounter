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
import cropallphotos


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


prepath = os.path.dirname(os.path.realpath(__file__))
root_path = prepath.replace('/programsP/preprocessing','')
progpath = prepath.replace('/preprocessing','')
rotpath = root_path + '/' + 'photographs/rot'
photopath = root_path + '/' + 'photographs'
#photolist = [f for f in listdir(photopath) if isfile(join(photopath, f))]
unanalpath = root_path + '/' + 'unanalyzed'
