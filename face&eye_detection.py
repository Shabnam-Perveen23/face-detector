# # Import OpenCV library
# import cv2

# # Load the XML file which contain pre define classifiers for face and eye detection
# # Face detection classifier
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # eye detection classifier
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# # starting  webcam for video capture
# camera = cv2.VideoCapture(0)

# #to use a video file as input
# #camera = cv2.VideoCapture('input file')

# # Processing the video in real time
# while True:

#     # get a image from the camera
#     success, image = camera.read()

#     # Converting the image to grayscale image 
#     grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # find out the faces in the grayscale image
#     detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=4)

#     # for loop for Iterate through  faces and drawing rectangles around it
#     for (a, b, width, height) in detected_faces:

#         # Draw a rectangles around each face
#         cv2.rectangle(image, (a, b), (a + width, b + height), (0, 0, 255), 2)

#         # Region of Interest (ROI) for detecting eyes within the face
#         face_region_gray = grayscale_image[b:b + height, a:a + width]
#         face_region_color = image[b:b + height, a:a + width]

#         # Detecting eyes within the face 
#         detected_eye = eye_cascade.detectMultiScale(face_region_gray)

#         # Drawing rectangles around detected eyes
#         for (ae, be, we, he) in detected_eye:
#             cv2.rectangle(face_region_color, (ae, be), (ae + we, be + he), (0, 225, 0), 2)

#     # Showing the the resulting image in a window
#     cv2.imshow('Face and smile Detection', image)

#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xff==ord('q'):
#        break
      
# # Releaseing the camera and close all  windows
# camera.release()
# cv2.destroyAllWindows()



#for detecting faces through input images file

import cv2

# load the required XML fies 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read the input image
image = cv2.imread('image5.webp')

# converting into grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detecting face
faces = face_cascade.detectMultiScale(grayscale_image, 1.1, 4)
#  drawing rectangular around the face
for(x,y,width,height) in faces:
    cv2.rectangle(image, (x,y), (x+width, y+height), (0,0,225), 2)

#displaying the output
cv2.imshow('Face and smile Detection' , image)
cv2.waitKey(0)
#close all windows
cv2.destroyAllWindows()


#uncomment the code which you want to run