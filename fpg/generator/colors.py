from colorsys import rgb_to_hsv
from typing import NamedTuple


# types
DEFAULT_ALPHA = 1.0


class RGB_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    r: float
    g: float
    b: float
    a: float = DEFAULT_ALPHA


class HSV_Color(NamedTuple):
    """For Simplicity the pixel stores just rgba values."""

    h: float
    s: float
    v: float
    a: float = DEFAULT_ALPHA


# ALIASES
T_RGB = tuple[float, float, float]
T_RGBA = tuple[float, float, float, float]

# Constants
RGBA_COLOR_D = RGB_Color(r=0.2, g=0.3, b=0.0, a=1.0)  # BLACK
RGBA_COLOR_U = RGB_Color(r=0.9, g=1.0, b=1.0, a=1.0)  # WHITE
HSV_COLOR_D = HSV_Color(*rgb_to_hsv(*RGBA_COLOR_D[:3]), RGBA_COLOR_D[3])
HSV_COLOR_U = HSV_Color(*rgb_to_hsv(*RGBA_COLOR_U[:3]), RGBA_COLOR_D[3])
