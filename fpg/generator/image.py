# Python Module Index
import random
from io import StringIO

# 3rd party
import numpy as np
import numpy.typing as npt

from loguru import logger
from PIL import Image as im

from .colors import NP_RGBA_DTYPE
from .colors import RGBA_COLOR_D
from .colors import RGBA_COLOR_U
from .colors import RGB_Color


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
            if not isinstance(ndarray, np.ndarray):
                raise ValueError(
                    f"need of custom type NumpyType, but is {type(ndarray)}"
                )
            if ndarray.dtype is not NP_RGBA_DTYPE:
                raise ValueError(
                    f"need of custom type NP_RGBA_DTYPE, but is {type(ndarray)}"
                )
            if ndarray.ndim != 2:
                raise ValueError(
                    f"need 2-D input (X, Y), but is {ndarray.ndim=}"
                    f" with {ndarray.shape=} with {ndarray.dtype=}"
                )
            self._img = ndarray
        logger.info(
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

    @property
    def shape(self) -> tuple[int, ...]:
        return self._img.shape

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
        result = StringIO()
        for index, val in np.ndenumerate(self._img):
            result.write(f"{index[0]}, {index[1]}, {val}")
        return result.read()

    def __repr__(self) -> str:
        """Repr for Debug (Fallback for str)"""
        result = f"Image Details: {self._img.size=} {self._img.shape=} "
        f"{self._img.ndim=} Content: "
        result += str(self)
        return repr(result)

    ############################################################################

    def get_color(self, x: int, y: int) -> RGB_Color:
        """Gets the pixel's color at 'x' 'y' as RGBA."""
        return self._img[y, x]

    def set_color(self, x: int, y: int, rgba: RGB_Color) -> None:
        """Sets the pixel's color at 'x' 'y' with RGBA."""
        self._img[y, x] = rgba

    ############################################################################

    def randomize(self) -> None:
        """Randomizes the image with U & D pixels."""
        for y in range(self.height):
            for x in range(self.width):
                random_bool = random.choice([True, False])
                if random_bool is True:
                    self.set_color(x, y, RGBA_COLOR_D)
                else:
                    self.set_color(x, y, RGBA_COLOR_U)


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
        np_img = np.rec.fromarrays(np_img.T, dtype=NP_RGBA_DTYPE).T
        np_img = np.array(np_img, dtype=NP_RGBA_DTYPE)
    return Image(np_img)


def flatlist_to_numpy(
    flatlist: list[float], height: int, width: int
) -> NumpyType:
    # Convert the flat list to a NumPy array with proper dimensions
    image_array = np.array(flatlist).reshape((height, width, 4))
    image_array = np.multiply(image_array, 255).astype(np.uint8)
    logger.info("a: ", image_array)
    image_array = image_array.view(NP_RGBA_DTYPE).squeeze()
    logger.debug("image_array: ", image_array)
    logger.debug("image_array type: ", type(image_array))
    logger.debug("image_array dtype: ", image_array.dtype)
    return image_array


def numpy_to_flatlist(numpy_arr: NumpyType) -> list[float]:
    # Numpy -> Blender Image Array:
    flat_array = numpy_arr.view(np.uint8).flatten().astype(np.float64)
    flat_adjusted = np.divide(flat_array, 255)
    flatlist = flat_adjusted.tolist()
    logger.debug("flatlist: ", flatlist)
    logger.debug("flatlist type: ", type(flatlist))
    return flatlist
