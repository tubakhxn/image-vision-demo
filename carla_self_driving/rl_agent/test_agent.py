# Made by Tuba A.Khan
from lane_detection.lane_detector import LaneDetector
from obstacle_detection.obstacle_detector import ObstacleDetector
from agent import RLAgent

if __name__ == "__main__":
    lane_detector = LaneDetector()
    obstacle_detector = ObstacleDetector()
    agent = RLAgent(lane_detector, obstacle_detector)
    agent.run()
