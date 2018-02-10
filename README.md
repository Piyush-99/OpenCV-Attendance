# OpenCV-Attendance

Python3

# Process
1. Train the model with pictures you want to recognize
2. Click a group photo and save it in "files" directory
3. OpenCV will recognize the people on which it was trained

# Scripts
1. train.py -- Trains the model with the pictures provided in directory "training-data/(s1 /s2 /s3....)"
               Saves the model as trained_data.yml
2. crop_pp.py -- Crops the faces from the image saved in "files" directory
3. recognize_all_faces.py -- Recognizes the cropped images and prints the names

# Usage ( In Order )
1. To train the model execute
   python train.py
2. To crop the image execute
   python crop_pp.py test.1.jpg
3. To recognize faces
   python recognize_all_faces.py
   
Images are taken from google images. They may be subject to copyright. Used here for educational purpose.   
