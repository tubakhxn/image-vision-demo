# Simple Self-Driving Car Mini Project

**Made by Tuba A.Khan**

## What does this robot do?
This project simulates a basic self-driving robot car using computer vision. The robot:
- Detects road lanes automatically from a camera image (lane detection)
- Detects obstacles (red objects) on the road (obstacle detection)
- Shows the robot's "vision" in real time (original, lane edges, obstacles)

## How does it work?
- Uses OpenCV and numpy (no heavy simulators or hardware required)
- Lane detection is done using edge detection (Canny) and image processing
- Obstacle detection is done by finding red-colored objects in the image

## How to run
1. Place a road image named `road.jpg` in the same folder as the code.
2. Run:
   ```
   python simple_self_driving.py
   ```
3. Three windows will open showing:
   - The original road image
   - Lane edges detected
   - Obstacles (red objects) detected

## Why is this robotic?
- The code mimics how a self-driving robot car would see and make decisions
- All detection is automatic, just like a real robot
- You can expand it to make decisions (e.g., turn left/right, stop for obstacles)

---

This is a simple, educational project to demonstrate robotics and computer vision basics for self-driving cars.
