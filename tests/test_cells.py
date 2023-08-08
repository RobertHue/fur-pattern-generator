# from typing import Any
# from typing import SupportsFloat

import pytest
import numpy as np

from fpg.generator.cells import Cells
from fpg.generator.image import Image
from fpg.generator.colors import RGB_Color

####################
#       INIT       #
####################

values = [
    [
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
    ],
    [
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
    ],
    [
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
    ],
    [
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
        RGB_Color(244, 222, 111, 55),
    ],
]


# @pytest.mark.parametrize(
#     ("x", "y", "expected"),
#     (
#         (0, 0, RGB_Color(244, 222, 111, 55)),
#         (0, 1, RGB_Color(244, 222, 111, 55)),
#         (1, 2, RGB_Color(244, 222, 111, 55)),
#         (1, 3, RGB_Color(244, 222, 111, 55)),
#         (2, 3, RGB_Color(244, 222, 111, 55)),
#     ),
# )
def test_set_color() -> None:
    # Define the values for the array and create a 2D numpy array
    img = Image(shape=(33, 33))
    img.randomize_image()
    # cells = Cells(img)

    from fpg.generator import generator as ca

    ca.cellular_automata(img, 5, 3, w=0.5)

    from PIL import Image as im

    print("type: ", type(img._img))
    # Image.fromarray(array_2d.astype('uint8'))
    print(img._img)
    from fpg.generator.image import test_dt

    data = im.fromarray(img._img, mode="RGBA")
    data.save("gfg_dummy_pic.png")

    assert True == True


# [ [[( 11,  13,  15, 255) ( 11,  13,  15, 255) ( 11,  13,  15, 255)
#    ( 11,  13,  15, 255)]
#   [(255, 111, 222, 255) (255, 111, 222, 255) (255, 111, 222, 255)
#    (255, 111, 222, 255)]
#   [( 11,  13,  15, 255) ( 11,  13,  15, 255) ( 11,  13,  15, 255)
#    ( 11,  13,  15, 255)]
#   ...
#   [(255, 111, 222, 255) (255, 111, 222, 255) (255, 111, 222, 255)
#    (255, 111, 222, 255)]
#   [( 11,  13,  15, 255) ( 11,  13,  15, 255) ( 11,  13,  15, 255)
#    ( 11,  13,  15, 255)]
#   [(255, 111, 222, 255) (255, 111, 222, 255) (255, 111, 222, 255)
#    (255, 111, 222, 255)]]]
