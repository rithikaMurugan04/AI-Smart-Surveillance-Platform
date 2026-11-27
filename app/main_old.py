"""
Main Entry Point

AI Smart Surveillance Platform
"""

import cv2

from src.utils.logger import logger
from src.camera.camera_manager import CameraManager
from src.detection.crowd_detector import CrowdDetector
from visualization.overlay_manager import OverlayManager
from src.visualization.heatmap import HeatMap
from src.detection.fight_detector import FightDetector
from src.detection.theft_detector import TheftDetector
from src.analytics.behavior_analyzer import BehaviorAnalyzer
from src.alerts.alarm_manager import AlarmManager


logger.info("Application Started")
print("AI Smart Surveillance Platform Started")

# -----------------------------
# Create Objects
# -----------------------------
camera = CameraManager()
crowd_detector = CrowdDetector()
overlay_manager = OverlayManager()

heatmap = HeatMap(640, 480)
fight_detector = FightDetector()
theft_detector = TheftDetector()
behavior_analyzer = BehaviorAnalyzer()
alarm_manager = AlarmManager()

print("All Modules Loaded Successfully")

# -----------------------------
# Read One Frame
# -----------------------------
frame = camera.read_frame()

if frame is not None:

    print("Camera is working!")

    person_boxes, person_centroids = crowd_detector.detect_people(frame)

    print(f"People Detected: {len(person_boxes)}")

    frame = overlay_manager.draw_people(frame, person_boxes)

    cv2.imshow("AI Smart Surveillance", frame)

    cv2.waitKey(0)

camera.release()
cv2.destroyAllWindows()