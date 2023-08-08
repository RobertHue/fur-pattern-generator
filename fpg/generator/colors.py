from colorsys import rgb_to_hsv

from typing import NamedTuple


# types
class RGB_Color(NamedTuple):
    r: float
    g: float
    b: float


class RGBA_Color(NamedTuple):
    r: float
    g: float
    b: float
    a: float


class HSV_Color(NamedTuple):
    h: float
    s: float
    v: float


# ALIASES
COLOR = tuple[float, float, float]
COORD = tuple[float, float]
RGBA_COLOR = tuple[float, float, float, float]

# Constants
BLACK = RGBA_Color(r=0.0, g=0.0, b=0.0, a=1.0)
WHITE = RGBA_Color(r=1.0, g=1.0, b=1.0, a=1.0)
RGBA_COLOR_D = BLACK
RGBA_COLOR_U = WHITE
HSV_COLOR_D = HSV_Color(*rgb_to_hsv(*RGBA_COLOR_D[:3]))
HSV_COLOR_U = HSV_Color(*rgb_to_hsv(*RGBA_COLOR_U[:3]))
