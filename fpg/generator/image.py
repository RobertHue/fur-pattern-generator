# Python Module Index
import colorsys
import random

# 3rd party
import numpy as np

from .colors import HSV_Color
from .colors import RGBA_Color
from .colors import HSV_COLOR_D
from .colors import HSV_COLOR_U


class Image:
    """
    Class that is used for Images.

    Note:
        Wrapper around numpy array that simplifies its usage.
    """

    def __init__(self, width: int, height: int) -> None:
        self._img = np.zeros((height, width, 4), dtype=np.float32)

    def width(self) -> int:
        return self._img.shape[0]

    def height(self) -> int:
        return self._img.shape[1]

    # def export_cv(self) -> None:
    #     """Exports to CV"""
    #     pixel_list = list(self._img.pixels)
    #     rgb_pixels = [x for i, x in enumerate(pixel_list) if (i + 1) % 4 != 0]
    #     a = np.array(rgb_pixels)
    #     b = np.reshape(a, (self.height(), self.width(), 3))
    #     rgba = np.ones((self.height(), self.width(), 3), dtype=np.float32)
    #     rgba[:, :, :] = np.uint8(b) * 255
    #     cv_image = np.flip(rgba, axis=[0, 2])
    #     return np.float32(cv_image)

    # def import_cv(self, cv_image: type[cv.cv]) -> None:
    #     """Imports from CV"""
    #     rgb = np.flip(cv_image, axis=[0, 2])
    #     rgba = np.ones((self.height(), self.width(), 4), dtype=np.float32)
    #     rgba[:, :, :-1] = np.float32(rgb) / 255
    #     self._img.pixels = rgba.flatten()

    def validate_coords(self, x: int, y: int) -> None:
        """Raises an ValueError if the if the supplied coordinates are not
        inside the image."""
        if (x >= 0 and x < self.width()) and (y >= 0 and y < self.height()):
            return
        raise ValueError("The coordinates are not inside the image")

    def get_pixel_rgba(self, x: int, y: int) -> RGBA_Color:
        """Gets the pixel's color at 'x' 'y' as RGBA."""
        self.validate_coords(x, y)
        index = (y * self.width() + x) * 4
        return self._img.pixels[index : index + 4]

    def get_pixel_hsv(self, x: int, y: int) -> HSV_Color:
        """Gets the pixel's color at 'x' 'y' as HSV."""
        self.validate_coords(x, y)
        r, g, b = self.get_pixel_rgba(x, y)
        return colorsys.rgb_to_hsv(r, g, b)

    def set_pixel_rgba(self, x: int, y: int, rgba: RGBA_Color) -> None:
        """Sets the pixel's color at 'x' 'y' with RGBA."""
        self.validate_coords(x, y)
        index = (y * self.width() + x) * 4
        self._img.pixels[index : index + 4] = rgba

    def set_pixel_hsv(self, x: int, y: int, hsv: HSV_Color) -> None:
        """Sets the pixel's color at 'x' 'y' with HSV."""
        self.validate_coords(x, y)
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        rgba = list(rgb)
        rgba.append(1)
        self.set_pixel_rgba(x, y, rgba)


def generate_random(image: type[Image]) -> None:
    """Inplace generates random U & D pixels in image."""
    color_d = HSV_COLOR_D
    color_u = HSV_COLOR_U
    for u in range(image.height()):
        for v in range(image.width()):
            random_bool = random.choice([True, False])
            if random_bool is True:
                image.set_pixel_hsv(u, v, color_d)
            else:
                image.set_pixel_hsv(u, v, color_u)
