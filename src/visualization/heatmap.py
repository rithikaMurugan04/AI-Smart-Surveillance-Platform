"""
HeatMap Visualization Module

Generates a cumulative heatmap showing
areas with the highest pedestrian activity.
"""

import cv2
import numpy as np


class HeatMap:
    """Creates and renders a crowd activity heatmap."""

    def __init__(self, width: int, height: int) -> None:
        """
        Initialize an empty heatmap.

        Args:
            width: Frame width.
            height: Frame height.
        """

        self.heatmap = np.zeros(
            (height, width),
            dtype=np.float32
        )

    def update(self, centroids) -> None:
        """
        Update the heatmap using detected
        person centroid coordinates.

        Args:
            centroids: List of (x, y) coordinates.
        """

        for x, y in centroids:

            if (
                0 <= y < self.heatmap.shape[0]
                and
                0 <= x < self.heatmap.shape[1]
            ):
                self.heatmap[y, x] += 1

    def draw(self, frame):
        """
        Overlay the heatmap onto the frame.

        Args:
            frame: Current video frame.

        Returns:
            Frame with heatmap overlay.
        """

        blurred_heatmap = cv2.GaussianBlur(
            self.heatmap,
            (51, 51),
            0
        )

        normalized_heatmap = cv2.normalize(
            blurred_heatmap,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        colored_heatmap = cv2.applyColorMap(
            normalized_heatmap.astype(np.uint8),
            cv2.COLORMAP_JET
        )

        colored_heatmap = cv2.resize(
            colored_heatmap,
            (frame.shape[1], frame.shape[0])
        )

        output_frame = cv2.addWeighted(
            frame,
            0.7,
            colored_heatmap,
            0.3,
            0
        )

        return output_frame