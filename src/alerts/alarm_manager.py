"""
Alarm Manager

Handles alarm notifications by playing
an alert sound whenever abnormal behaviour
is detected.
"""

import threading

from playsound import playsound

from src.utils.logger import logger


class AlarmManager:
    """Manages audio alarm notifications."""

    def __init__(self, sound_file: str = "voice.mp3") -> None:
        """
        Initialize the alarm manager.

        Args:
            sound_file: Path to the alarm audio file.
        """

        self.sound_file = sound_file

        logger.info("Alarm manager initialized.")

    def _play_sound(self) -> None:
        """Play the configured alarm sound."""

        playsound(self.sound_file)

    def play_alarm(self) -> None:
        """
        Play the alarm without blocking
        the video processing pipeline.
        """

        try:

            threading.Thread(
                target=self._play_sound,
                daemon=True
            ).start()

            logger.info("Alarm triggered.")

        except Exception as error:

            logger.error(
                f"Failed to play alarm: {error}"
            )