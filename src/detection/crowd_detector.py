"""
Crowd Detection Module

Detects people in a video frame using the YOLOv8 model
and returns bounding boxes and centroid coordinates.
"""

from ultralytics import YOLO


PERSON_CLASS_ID = 0


class CrowdDetector:
    """Detects people in video frames using YOLOv8."""

    def __init__(self) -> None:
        """Load the YOLOv8 detection model."""
        self.model = YOLO("yolov8s.pt")

    def detect_people(self, frame):
        """
        Detect people in a frame.

        Args:
            frame: Input video frame.

        Returns:
            tuple:
                - List of bounding boxes
                - List of centroid coordinates
        """

        results = self.model(frame, verbose=False)

        people_boxes = []
        people_centroids = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                if class_id == PERSON_CLASS_ID:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2

                    people_boxes.append(
                        (x1, y1, x2, y2)
                    )

                    people_centroids.append(
                        (center_x, center_y)
                    )

        return people_boxes, people_centroids