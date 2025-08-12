# Made by Tuba A.Khan
import cv2
from lane_detector import LaneDetector

if __name__ == "__main__":
    # Load a sample image (replace 'sample_road.jpg' with your own test image)
    image = cv2.imread("sample_road.jpg")
    if image is None:
        print("Test image not found. Please add 'sample_road.jpg' to this folder.")
    else:
        detector = LaneDetector()
        edges = detector.detect(image)
        cv2.imshow("Lane Edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
