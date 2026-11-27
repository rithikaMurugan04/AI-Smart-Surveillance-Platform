"""
Main Entry Point

Starts the AI Smart Surveillance Platform.
"""

from src.pipeline.video_pipeline import VideoPipeline
from src.utils.logger import logger


def main() -> None:
    """Start the surveillance application."""

    logger.info("AI Smart Surveillance Platform Started")

    pipeline = VideoPipeline()
    pipeline.start()


if __name__ == "__main__":
    main()