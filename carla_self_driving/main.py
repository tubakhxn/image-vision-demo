
# Made by Tuba A.Khan
import sys
from lane_detection.lane_detector import LaneDetector
from obstacle_detection.obstacle_detector import ObstacleDetector
from rl_agent.agent import RLAgent

# Entry point for the self-driving simulation

def main():
    print("Starting CARLA Self-Driving Simulation...")
    lane_detector = LaneDetector()
    obstacle_detector = ObstacleDetector()
    agent = RLAgent(lane_detector, obstacle_detector)
    agent.run()

if __name__ == "__main__":
    main()
