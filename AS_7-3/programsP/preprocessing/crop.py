# Write Python code here 
# import the necessary packages 
import cv2 
import argparse 
import random as rand
import os



prepath = os.path.dirname(os.path.realpath(__file__))
root_path = prepath.replace('/programsP/preprocessing','')
photopath = root_path + '/' + 'photographs'  
# now let's initialize the list of reference point 
ref_point, tracker = ([] for i in range(2))

crop = False
global color3 
color3 = 26
global color2 
color2 = 107
global color1
color1 = 13
  
def shape_selection(event, x, y, flags, param): 
    # grab references to the global variables 
    global ref_point, crop,colorList  
    # if the left mouse button was clicked, record the starting 
    # (x, y) coordinates and indicate that cropping is being performed 
    if event == cv2.EVENT_LBUTTONDOWN: 
        ref_point = [(x, y)]
        tracker.append((x,y))
    # check to see if the left mouse button was released 
    elif event == cv2.EVENT_LBUTTONUP: 
        # record the ending (x, y) coordinates and indicate that 
        # the cropping operation is finished 
        ref_point.append((x, y)) 
        tracker.append((x,y))
        # draw a rectangle around the region of interest 
        cv2.rectangle(image, ref_point[0], ref_point[1], (color1, color2,color3), thickness = 25) 
        cv2.imshow("image", image) 
    return ref_point
  
# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help ="Path to the image") 
args = vars(ap.parse_args()) 
  
# load the image, clone it, and setup the mouse callback function 
print(photopath + '/' + args["image"])
image = cv2.imread(photopath + '/' + args["image"]) 
clone = image.copy() 
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", shape_selection) 
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    # press 'r' to reset the window 
    if key == ord("r"): 
        image = clone.copy() 
    elif key == ord("m"):
        color1 = rand.randint(0,256)
        color2 = rand.randint(0,256)
        color3 = rand.randint(0,256)

    # if the 'c' key is pressed, break from the loop 
    elif key == ord("c"): 
        break
  
# close all open windows 
cv2.destroyAllWindows() 
