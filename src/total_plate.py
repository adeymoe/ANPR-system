import cv2
import numpy as np
class PossiblePlate:   #represents a possible license plate that has been detected in an image.
    def __init__(self):
        self.imgPlate = None  #the image of the license plate
        self.imgGrayscale = None #the grayscale version of the license plate image
        self.imgThresh = None  #the thresholded version of the license plate image
        self.rrLocationOfPlateInScene = None  #the location of the license plate in the original image, represented as a rectangular region of interest (ROI)
        self.strChars = ""  #string that will contain the characters that are recognized on the license plate.
