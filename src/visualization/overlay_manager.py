"""
Overlay Manager

Draws bounding boxes, labels and alerts
on the video frame.
"""

import cv2

from src.utils.logger import logger


# ---------------------------------------------------
# Drawing Colours (BGR)
# ---------------------------------------------------

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)


class OverlayManager:
    """Draws visual overlays for the surveillance system."""

    def __init__(self) -> None:
        """Initialize the overlay manager."""

        logger.info("Overlay manager initialized.")

    def draw_people(self, frame, person_boxes):
        """
        Draw bounding boxes around detected people.

        Args:
            frame: Current video frame.
            person_boxes: List of bounding boxes.

        Returns:
            Updated frame.
        """

        for x1, y1, x2, y2 in person_boxes:

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                GREEN,
                2
            )

        return frame

    def draw_people_count(self, frame, count):
        """
        Draw the total number of detected people.

        Args:
            frame: Current video frame.
            count: Number of detected people.

        Returns:
            Updated frame.
        """

        cv2.putText(
            frame,
            f"People: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            WHITE,
            2
        )

        return frame

    def draw_alert(self, frame, message):
        """
        Draw the current surveillance status.

        Args:
            frame: Current video frame.
            message: Alert message.

        Returns:
            Updated frame.
        """

        cv2.putText(
            frame,
            message,
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            RED,
            3
        )

        return frame