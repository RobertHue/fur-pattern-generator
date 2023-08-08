# Python Module Index
import random

# 3rd party
import numpy as np
import numpy.typing as npt

from .colors import RGBA_COLOR_D
from .colors import RGBA_COLOR_U
from .colors import RGB_Color

img_dt = np.dtype([("pixel_color", np.int32, 4)])
ImageType = npt.NDArray


class Image:
    """
    Class that is used for Images.

    Note:
        Wrapper around numpy array that simplifies its usage.
    """

    def __init__(
        self,
        ndarray: ImageType | None = None,
        shape: tuple[int, int] | None = None,
    ) -> None:
        """Construct a new 0-initalized img (defined by shape)
        or one from given np-array.

        Args:
            ndarray (np.ndarray | None): the image as array
            shape (tuple | None): tuple consisting of (width, height)
        """
        if (ndarray is None and shape is None) or (
            ndarray is not None and shape is not None
        ):
            raise ValueError("Either only pass img or only pass shape.")
        if ndarray is None:
            self._img = np.zeros((*shape, 4), dtype=img_dt)
        else:
            self._img = ndarray

    @property
    def height(self) -> int:
        return self._img.shape[0]

    @property
    def width(self) -> int:
        return self._img.shape[1]

    def validate_coords(self, x: int, y: int) -> None:
        """Raises an ValueError if the if the supplied coordinates are not
        inside the image (Bounds Check)."""
        x_inbound = x >= 0 and x < self.width
        y_inbound = y >= 0 and y < self.height
        if not (x_inbound and y_inbound):
            raise ValueError("The coordinates are not inside the image")

    ############################################################################

    # def export_cv(self) -> None:
    #     """Exports to CV"""
    #     pixel_list = list(self._img.pixels)
    #     rgb_pixels = [x for i, x in enumerate(pixel_list) if (i + 1) % 4 != 0]
    #     a = np.array(rgb_pixels)
    #     b = np.reshape(a, (self.height, self.width, 3))
    #     rgba = np.ones((self.height, self.width, 3), dtype=np.float32)
    #     rgba[:, :, :] = np.uint8(b) * 255
    #     cv_image = np.flip(rgba, axis=[0, 2])
    #     return np.float32(cv_image)

    # def import_cv(self, cv_image: type[cv.cv]) -> None:
    #     """Imports from CV"""
    #     rgb = np.flip(cv_image, axis=[0, 2])
    #     rgba = np.ones((self.height, self.width, 4), dtype=np.float32)
    #     rgba[:, :, :-1] = np.float32(rgb) / 255
    #     self._img.pixels = rgba.flatten()

    ############################################################################

    def get_color(
        self,
        x: int,
        y: int,
    ) -> RGB_Color:
        """Gets the pixel's color at 'x' 'y' as RGBA."""
        return RGB_Color(*self._img[y, x])

    def set_color(self, x: int, y: int, rgba: RGB_Color) -> None:
        """Sets the pixel's color at 'x' 'y' with RGBA."""
        self._img[y, x] = rgba

    ############################################################################

    def randomize_image(self) -> None:
        """Randomizes the image with U & D pixels."""
        color_d = RGBA_COLOR_D
        color_u = RGBA_COLOR_U
        for y in range(self.height):
            for x in range(self.width):
                random_bool = random.choice([True, False])
                if random_bool is True:
                    self.set_color(x, y, color_d)
                else:
                    self.set_color(x, y, color_u)
