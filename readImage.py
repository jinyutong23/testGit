import cv2

def read(imagePath):
    image = cv2.imread(imagePath)
    
    return image