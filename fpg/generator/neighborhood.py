"""Implements different strategies for neighborhood (NeighborStrategy) search.

Returns:
    _type_: _description_
"""
import math

from abc import ABC, abstractmethod

import numpy as np

from fpg.generator.image import Image


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


class MooreStrategy(NeighborStrategy):
    def get_neighborhood(
        self, image: Image, center: list[int, int], distance: int
    ) -> np.ndarray:
        center_x, center_y = center
        return [
            (x, y)
            for x in range(center_x - distance, center_x + distance + 1)
            for y in range(center_y - distance, center_y + distance + 1)
            if image.check_coords(x, y)
        ]


class NeumannStrategy(NeighborStrategy):  # TODO - still needs to be tested
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
            and image.check_coords(x, y)
        ]


class CircularStrategy(NeighborStrategy):  # TODO - still needs to be tested
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
