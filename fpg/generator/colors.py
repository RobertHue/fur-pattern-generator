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
RGBA_COLOR_D = RGB_Color(r=255, g=0, b=0, a=255)  # BLACK
RGBA_COLOR_U = RGB_Color(r=0, g=0, b=255, a=255)  # WHITE
RGBA_COLOR_ND = [int(value / 255) for value in RGBA_COLOR_D]  # N = normalized
RGBA_COLOR_NU = [int(value / 255) for value in RGBA_COLOR_U]  # N = normalized
color_tuple_d = (*rgb_to_hsv(*RGBA_COLOR_ND[:3]), RGBA_COLOR_ND[3])
color_tuple_u = (*rgb_to_hsv(*RGBA_COLOR_NU[:3]), RGBA_COLOR_NU[3])
HSV_COLOR_D = HSV_Color(*color_tuple_d)
HSV_COLOR_U = HSV_Color(*color_tuple_u)
