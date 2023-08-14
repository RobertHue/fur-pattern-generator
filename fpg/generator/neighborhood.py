"""Implements different strategies for neighborhood (NeighborStrategy) search.

Returns:
    _type_: _description_
"""
from abc import ABC, abstractmethod
from fpg.generator.image import Image
import numpy as np
import math


class NeighborStrategy(ABC):
    @abstractmethod
    def get_neighborhood(
        self, image: Image, center: list[int, int], distance: int
    ) -> np.ndarray:
        """Gets the Moore neighborhood as a list of pixels around pos.

        Note:
            Also see https://mathworld.wolfram.com/CellularAutomaton.html
        """
        pass

    ############################################################################

    def _tree_search(
        self,
        image: Image,
        center: list[int, int],
        distance: int,
        lookup: list[tuple],
    ) -> np.ndarray:
        result_n = []  # the neighboorhood result
        _visited = np.zeros(
            image.shape, dtype=np.bool_
        )  # to memorize that the cell has been visited once
        queue = []  # create a queue for BFS

        if not image.check_coords(*center):
            return result_n

        # Mark the source_pixel as visited and enqueue it
        queue.append(center)
        _visited[center[1], center[0]] = True

        while distance >= 0:
            distance -= 1

            level_size = len(queue)
            while level_size > 0:
                level_size -= 1

                # dequeue a pixel as src_pixel from queue
                src_pixel = queue.pop(0)
                result_n += [src_pixel]

                # get all adjacent pixels of that dequeued src_pixel
                # if a adjacent has not been visited, then mark it visited and
                # enqueue it
                for cur_l in lookup:
                    new_x = src_pixel[0] + cur_l[0]
                    new_y = src_pixel[1] + cur_l[1]
                    new_pos = (new_x, new_y)

                    # Are valid coords inside the image:
                    if not image.check_coords(*new_pos):
                        continue

                    # cell got already visited
                    if _visited[center[1], center[0]]:
                        continue

                    queue.append(new_pos)
                    _visited[new_pos[1], new_pos[0]] = True
        return result_n


class NeumannStrategy(NeighborStrategy):
    def get_neighborhood(
        self, image: Image, center: list[int, int], distance: int
    ) -> np.ndarray:
        center_x, center_y = center
        return [
            (x, y)
            for x in range(center_x - distance, center_x + distance + 1)
            for y in range(center_y - distance, center_y + distance + 1)
            if abs(center_x - x) + abs(center_y - y) <= distance
            and abs(center_x - x) + abs(center_y - y) != 2 * distance
        ]


class MooreStrategy(NeighborStrategy):
    def get_neighborhood(
        self, image: Image, center: list[int, int], distance: int
    ) -> np.ndarray:
        center_x, center_y = center
        return [
            (x, y)
            for x in range(center_x - distance, center_x + distance + 1)
            for y in range(center_y - distance, center_y + distance + 1)
            if abs(center_x - x) + abs(center_y - y) <= distance
        ]


class CircularStrategy(NeighborStrategy):
    def get_neighborhood(
        self, image: Image, center: list[int, int], distance: int
    ) -> np.ndarray:
        center_x, center_y = center
        return [
            (x, y)
            for x in range(center_x - distance, center_x + distance + 1)
            for y in range(center_y - distance, center_y + distance + 1)
            if math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= distance
            and image.check_coords(x, y)
        ]

    # def draw_circle(
    #     image: type[Image], color: RGB_Color, x: int, y: int, radius: float
    # ) -> None:
    #     """Draws a circle into image."""
    #     Image.Image.getdata(image)
    #     # Reading an image in default mode
    #     cv_img = image.export_CV()

    #     # draw a circle as mask
    #     center_coordinates = (x, y)
    #     thickness = 1
    #     new_img = cv2.circle(cv_img, center_coordinates, radius, color, thickness)

    #     # write back image with circle into image
    #     image.import_CV(new_img)
