"""
Theft Detection Module

Provides the interface for theft detection within
the surveillance system.

Version 1 uses a placeholder implementation.
The detection logic can be extended in future
versions using object tracking and behaviour analysis.
"""

from src.utils.logger import logger


class TheftDetector:
    """Detects potential theft events."""

    def __init__(self) -> None:
        """Initialize the theft detector."""

        logger.info("Theft detector initialized.")

    def detect_theft(self, frame) -> bool:
        """
        Detect suspicious theft activity.

        Args:
            frame: Current video frame.

        Returns:
            bool:
                False for Version 1.
        """

        # Version 1:
        # Placeholder implementation.
        # Advanced theft detection will be
        # introduced in a future version.

        return False