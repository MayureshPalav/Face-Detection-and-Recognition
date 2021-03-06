from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2

# construct the argument parser and parse the arguments
#image='Images\Mayur\IMG_2183.jpg'
#image=cv2.imread(image)
def alignment(image):
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
	fa = FaceAligner(predictor, desiredFaceWidth=256)
	image = imutils.resize(image, width=800)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# show the original input image and detect faces in the grayscale
	# image
	#cv2.imshow("Input", image)
	rects = detector(gray, 2)

	for rect in rects:
		# extract the ROI of the *original* face, then align the face
		# using facial landmarks
		(x, y, w, h) = rect_to_bb(rect)
		faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
		faceAligned = fa.align(image, gray, rect)
		# display the output images
		#cv2.imshow('',faceAligned)
		#cv2.waitKey(0)
		return faceAligned
		#cv2.imshow("Original", faceOrig)
		#cv2.imshow("Aligned", faceAligned)
		#cv2.waitKey(0)