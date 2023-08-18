from colorsys import rgb_to_hsv
from typing import NamedTuple

import numpy as np


class RGB_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    r: int
    g: int
    b: int
    a: int = 255


class HSV_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    h: float
    s: float
    v: float
    a: float = 1.0


NP_RGBA_DTYPE = np.dtype(
    {
        "names": ["r", "g", "b", "a"],
        "formats": [np.uint8, np.uint8, np.uint8, np.uint8],
    }
)
dt = np.dtype(np.uint8)

NP_HSV_DTYPE = np.dtype(
    {
        "names": ["h", "s", "v", "a"],
        "formats": [np.uint8, np.uint8, np.uint8, np.uint8],
    }
)

# ALIASES
T_RGB = tuple[int, int, int]
T_RGBA = tuple[int, int, int, int]

# Constants
RGBA_COLOR_D = RGB_Color(r=0, g=0, b=0, a=255)  # BLACK
RGBA_COLOR_U = RGB_Color(r=255, g=255, b=255, a=255)  # WHITE
D_THRESHOLD = 0.5  # threshold of a D cell (value; HSV) that can be exceeded

NP_RGBA_COLOR_D = np.array([(0, 0, 0, 255)], dtype=NP_RGBA_DTYPE)  # BLACK
NP_RGBA_COLOR_U = np.array([(255, 255, 255, 255)], dtype=NP_RGBA_DTYPE)  # WHITE

RGBA_COLOR_ND = [float(value / 255) for value in RGBA_COLOR_D]  # N = normalized
RGBA_COLOR_NU = [float(value / 255) for value in RGBA_COLOR_U]  # N = normalized
color_tuple_d = rgb_to_hsv(*RGBA_COLOR_ND[:3])
color_tuple_u = rgb_to_hsv(*RGBA_COLOR_NU[:3])
HSV_COLOR_D = HSV_Color(*color_tuple_d)
HSV_COLOR_U = HSV_Color(*color_tuple_u)
