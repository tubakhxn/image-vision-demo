
# Made by Tuba A.Khan
import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        pass

    def detect(self, image):
        # Simple lane detection using color thresholding and Canny edge
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)
        return edges
