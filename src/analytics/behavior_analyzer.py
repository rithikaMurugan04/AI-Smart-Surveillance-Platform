"""
Behavior Analyzer

Combines the outputs from different detection modules
and determines the overall surveillance status.
"""

from src.utils.logger import logger


class BehaviorAnalyzer:
    """Determines the final behaviour detected in a video frame."""

    def __init__(self) -> None:
        """Initialize the behaviour analyzer."""

        logger.info("Behavior analyzer initialized.")

    def analyze(
        self,
        crowd_detected: bool,
        fight_detected: bool,
        theft_detected: bool,
    ) -> str:
        """
        Determine the overall surveillance status.

        Args:
            crowd_detected: True if crowd threshold is exceeded.
            fight_detected: True if a fight is detected.
            theft_detected: True if theft is detected.

        Returns:
            str: One of
                - "FIGHT"
                - "THEFT"
                - "CROWD"
                - "NORMAL"
        """

        if fight_detected:
            return "FIGHT"

        if theft_detected:
            return "THEFT"

        if crowd_detected:
            return "CROWD"

        return "NORMAL"