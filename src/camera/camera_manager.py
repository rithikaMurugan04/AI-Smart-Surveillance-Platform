"""
Camera Manager

Handles webcam initialization,
frame capture, and camera resource management.
"""

import cv2

from src.utils.config import CAMERA_ID
from src.utils.logger import logger


class CameraManager:
    """
    Manages webcam access for the surveillance system.
    """

    def __init__(self):

        logger.info("Opening camera...")

        self.cap = cv2.VideoCapture(CAMERA_ID)

        if not self.cap.isOpened():
            logger.error("Failed to open camera.")
            raise RuntimeError("Unable to access the webcam.")

        # Camera settings
        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            640
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            480
        )

        self.cap.set(
            cv2.CAP_PROP_FPS,
            30
        )

        logger.info("Camera opened successfully.")


    def read_frame(self):
        """
        Capture one frame from webcam.
        """

        success, frame = self.cap.read()

        if not success:
            logger.warning("Failed to read frame from camera.")
            return None

        return frame


    def release(self):
        """
        Release webcam resource.
        """

        if self.cap is not None:

            if self.cap.isOpened():

                logger.info("Releasing camera.")
                self.cap.release()