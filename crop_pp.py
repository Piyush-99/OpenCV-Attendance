import cv2
import sys
import os

face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

root = os.path.dirname(os.path.realpath('__file__'))
cur_dir = os.listdir(".")

def detect_faces(f_cascade, colored_img, scaleFactor = 1.2):
   img_copy = colored_img.copy()          
   gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)          
   faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);
   i = 1;
   for (x, y, w, h) in faces:
      cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
      for dirs in cur_dir:
        if dirs.startswith("cropped"):      
           cv2.imwrite(os.path.join(root,dirs,"c" + str(i) + ".jpg"),img_copy[y:y+w,x:x+h])
           i+=1;
   return img_copy

flag = False
for dirs in cur_dir:
  if dirs.startswith("f"):
     img_path = os.path.join(root,dirs)
     if len(sys.argv) < 2:
       print("Please enter image name (eg. test1.jpg)")
     else:
       image = os.path.join(img_path, str(sys.argv[1]))
       img = cv2.imread(image)
       for fil in os.listdir(img_path):
         if fil == str(sys.argv[1]):
            flag = True
       if(flag == True):
         face = detect_faces(face_cascade,img,1.2)           
       else:
         print("Image not available in the desired location")
           
cv2.waitKey(0)
cv2.destroyAllWindows()
