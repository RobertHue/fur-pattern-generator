# Python Module Index
import random

# 3rd party
import numpy as np
import numpy.typing as npt

from PIL import Image as im

from .colors import NP_RGBA_COLOR_D
from .colors import NP_RGBA_COLOR_U
from .colors import NP_RGBA_DTYPE


NumpyType = npt.NDArray


class Image:
    """
    Class that is used for Images.

    Note:
        Wrapper around numpy array that simplifies its usage.
    """

    def __init__(
        self,
        ndarray: NumpyType | None = None,
        res: tuple[int, int] | None = None,
    ) -> None:
        """Construct a new 0-initalized img (defined by shape)
        or one from given np-array.

        Args:
            ndarray (NumpyType | None): the image as array
            res (tuple | None): the resolution of the image (width, height)
        """
        if (ndarray is None and res is None) or (
            ndarray is not None and res is not None
        ):
            raise ValueError("Either only pass img or only pass shape.")
        if ndarray is None:
            self._img = np.zeros(shape=(*res,), dtype=NP_RGBA_DTYPE)
        else:
            if ndarray.dtype != NP_RGBA_DTYPE:
                raise ValueError(
                    f"need of custom type NP_RGBA_DTYPE, but is {ndarray.ndim=}"
                    f" with {ndarray.shape=} with {ndarray.dtype=}"
                )
            if ndarray.ndim != 2:
                raise ValueError(
                    f"need 2-D input (X, Y), but is {ndarray.ndim=}"
                    f" with {ndarray.shape=} with {ndarray.dtype=}"
                )
            self._img = ndarray
        print(
            f"\nis {self._img.ndim=} with {self._img.shape=} with "
            f"{self._img.dtype=}"
        )

    @property
    def data(self) -> NumpyType:
        return self._img

    @property
    def height(self) -> int:
        return self._img.shape[0]

    @property
    def width(self) -> int:
        return self._img.shape[1]

    ############################################################################

    def validate_coords(self, x: int, y: int) -> None:
        """Raises an ValueError if the if the supplied coordinates are not
        inside the image (Bounds Check)."""
        x_inbound = x >= 0 and x < self.width
        y_inbound = y >= 0 and y < self.height
        if not (x_inbound and y_inbound):
            raise ValueError("The coordinates are not inside the image")

    def check_coords(self, x: int, y: int) -> bool:
        """Returns True if inside the image, otherwhise False."""
        x_inbound = x >= 0 and x < self.width
        y_inbound = y >= 0 and y < self.height
        if not (x_inbound and y_inbound):
            return False
        return True

    ############################################################################

    def __str__(self) -> str:
        """str for user output"""
        result = ""
        for index, val in np.ndenumerate(self._img):
            print(f"{index[0]}, {index[1]}, {val}")
        return result

    def __repr__(self) -> str:
        """Repr for Debug (Fallback for str)"""
        result = f"Image Details: {self._img.size=} {self._img.shape=} "
        f"{self._img.ndim=} Content: "
        result += str(self)
        return repr(result)

    ############################################################################

    def get_color(self, x: int, y: int) -> NP_RGBA_DTYPE:
        """Gets the pixel's color at 'x' 'y' as RGBA."""
        return self._img[y, x]

    def set_color(self, x: int, y: int, rgba: NP_RGBA_DTYPE) -> None:
        """Sets the pixel's color at 'x' 'y' with RGBA."""
        self._img[y, x] = rgba

    ############################################################################

    def randomize_image(self) -> None:
        """Randomizes the image with U & D pixels."""
        for y in range(self.height):
            for x in range(self.width):
                random_bool = random.choice([True, False])
                if random_bool is True:
                    self.set_color(x, y, NP_RGBA_COLOR_D)
                else:
                    self.set_color(x, y, NP_RGBA_COLOR_U)


################################################################################
# EX-/IM-PORTERS


def export_pil(image: Image, name: str, mode: str = "RGBA") -> None:
    """Exports to PIL"""
    pil = im.fromarray(image.data, mode)
    pil.save(name)


def import_pil(name: str, mode: str = "RGBA") -> Image:
    """Factory. Imports from PIL"""
    with im.open(name).convert(mode) as img:
        img.convert(mode=mode)
        np_img = np.array(img)
        # print("np_img: ", np_img)
        # print("np_img shape: ", np_img.shape)
        # print("np_img size: ", np_img.size)
        # print("img mode: ", img.mode)
        # print("img format: ", img.format)
        np_img = np.rec.fromarrays(np_img.T, dtype=NP_RGBA_DTYPE).T
    return Image(np_img)
