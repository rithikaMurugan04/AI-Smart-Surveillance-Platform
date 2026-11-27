"""
Fight Detection Module

Detects potential physical conflicts by checking
whether detected person bounding boxes overlap.
"""


class FightDetector:
    """Detects possible fights using bounding box overlap."""

    def detect_fight(self, person_boxes):
        """
        Determine whether any two detected people overlap.

        Args:
            person_boxes: List of person bounding boxes
                          in the format (x1, y1, x2, y2).

        Returns:
            bool:
                True if a possible fight is detected,
                otherwise False.
        """

        total_people = len(person_boxes)

        for first_index in range(total_people):

            x1, y1, x2, y2 = person_boxes[first_index]

            for second_index in range(first_index + 1, total_people):

                (
                    other_x1,
                    other_y1,
                    other_x2,
                    other_y2,
                ) = person_boxes[second_index]

                horizontal_overlap = (
                    max(x1, other_x1)
                    < min(x2, other_x2)
                )

                vertical_overlap = (
                    max(y1, other_y1)
                    < min(y2, other_y2)
                )

                if horizontal_overlap and vertical_overlap:
                    return True

        return False