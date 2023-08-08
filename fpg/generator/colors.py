from colorsys import rgb_to_hsv
from typing import NamedTuple


# types
DEFAULT_ALPHA = 255


class RGB_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    r: int
    g: int
    b: int
    a: int = DEFAULT_ALPHA


class HSV_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    h: int
    s: int
    v: int
    a: int = DEFAULT_ALPHA


# ALIASES
T_RGB = tuple[int, int, int]
T_RGBA = tuple[int, int, int, int]

# Constants
RGBA_COLOR_D = RGB_Color(r=11, g=13, b=15, a=255)  # BLACK
RGBA_COLOR_U = RGB_Color(r=255, g=111, b=222, a=255)  # WHITE

color_tuple_d = (*rgb_to_hsv(*RGBA_COLOR_D[:3]), RGBA_COLOR_D[3])
color_tuple_u = (*rgb_to_hsv(*RGBA_COLOR_U[:3]), RGBA_COLOR_D[3])
inter_d = (int(value * 255) for value in color_tuple_d)
inter_u = (int(value * 255) for value in color_tuple_u)
HSV_COLOR_D = HSV_Color(*inter_d)
HSV_COLOR_U = HSV_Color(*inter_u)
