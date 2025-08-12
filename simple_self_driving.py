# Simple Self-Driving Car Mini Project
# Made by Tuba A.Khan
# No CARLA required! Just OpenCV and numpy.

import cv2
import numpy as np

# Lane Detection Function
def detect_lanes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges

# Obstacle Detection Function (simple color threshold for red objects)
def detect_obstacles(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2
    return mask

if __name__ == "__main__":
    # Load a sample road image (add your own image as 'road.jpg')
    image = cv2.imread("road.jpg")
    if image is None:
        print("Please add a road image named 'road.jpg' in this folder.")
    else:
        lanes = detect_lanes(image)
        obstacles = detect_obstacles(image)
        # Show results
        cv2.imshow("Original", image)
        cv2.imshow("Lane Edges", lanes)
        cv2.imshow("Obstacles (Red Mask)", obstacles)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
