
"""
Video Pipeline

Coordinates the complete AI surveillance workflow:
Camera → Detection → Analysis → Visualization → Alarm
"""

import cv2

from src.alerts.alarm_manager import AlarmManager
from src.analytics.behavior_analyzer import BehaviorAnalyzer
from src.camera.camera_manager import CameraManager
from src.detection.crowd_detector import CrowdDetector
from src.detection.fight_detector import FightDetector
from src.detection.theft_detector import TheftDetector
from src.utils.logger import logger
from src.visualization.heatmap import HeatMap
from src.visualization.overlay_manager import OverlayManager


CROWD_THRESHOLD = 10


class VideoPipeline:
    """Coordinates the end-to-end surveillance pipeline."""

    def __init__(self) -> None:
        """Initialize all surveillance modules."""

        logger.info("Video pipeline initialized.")

        self.camera = CameraManager()
        self.crowd_detector = CrowdDetector()
        self.fight_detector = FightDetector()
        self.theft_detector = TheftDetector()
        self.behavior_analyzer = BehaviorAnalyzer()
        self.alarm_manager = AlarmManager()
        self.overlay = OverlayManager()

        self.heatmap = None
        self.previous_behavior = "NORMAL"

    def process_frame(self):
        """
        Process one video frame.

        Returns:
            dict | None:
                Processed frame and detection results.
        """

        frame = self.camera.read_frame()

        if frame is None:
            return None

        if self.heatmap is None:
            height, width = frame.shape[:2]
            self.heatmap = HeatMap(width, height)

        people_boxes, people_centroids = (
            self.crowd_detector.detect_people(frame)
        )

        people_count = len(people_boxes)

        fight_detected = self.fight_detector.detect_fight(
            people_boxes
        )

        theft_detected = self.theft_detector.detect_theft(
            frame
        )

        crowd_detected = (
            people_count > CROWD_THRESHOLD
        )

        behavior = self.behavior_analyzer.analyze(
            crowd_detected,
            fight_detected,
            theft_detected
        )

        if (
            behavior != "NORMAL"
            and behavior != self.previous_behavior
        ):
            self.alarm_manager.play_alarm()

        self.previous_behavior = behavior

        self.heatmap.update(
            people_centroids
        )

        frame = self.heatmap.draw(frame)

        frame = self.overlay.draw_people(
            frame,
            people_boxes
        )

        frame = self.overlay.draw_people_count(
            frame,
            people_count
        )

        frame = self.overlay.draw_alert(
            frame,
            behavior
        )

        return {
            "frame": frame,
            "people_count": people_count,
            "behavior": behavior,
            "alarm": behavior != "NORMAL",
            "fight_detected": fight_detected,
            "theft_detected": theft_detected,
            "crowd_detected": crowd_detected,
        }

    def start(self) -> None:
        """Run the surveillance pipeline continuously."""

        logger.info("Video pipeline started.")

        try:
            while True:

                result = self.process_frame()

                if result is None:
                    continue

                cv2.imshow(
                    "AI Smart Surveillance",
                    result["frame"]
                )

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        finally:
            self.camera.release()
            cv2.destroyAllWindows()