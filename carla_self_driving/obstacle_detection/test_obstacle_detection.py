# Made by Tuba A.Khan
from obstacle_detector import ObstacleDetector

if __name__ == "__main__":
    detector = ObstacleDetector()
    # Simulate sensor data (empty for now)
    sensor_data = None
    obstacles = detector.detect(sensor_data)
    print(f"Detected obstacles: {obstacles}")
