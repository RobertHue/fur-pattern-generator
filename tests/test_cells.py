# from typing import Any
# from typing import SupportsFloat

import numpy as np

import pytest
from fpg.generator.cells import Cells
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.image import export_pil
from fpg.generator.image import import_pil
from PIL import Image as im


####################
#       INIT       #
####################


# create a 2D numpy array with defined values
array_2d = np.array(
    [
        [
            (244, 222, 111, 55),
            (244, 222, 111, 55),
            (244, 222, 111, 55),
        ],
        [
            (244, 222, 111, 55),
            (244, 222, 111, 55),
            (244, 222, 111, 55),
        ],
    ],
    dtype=NP_RGBA_DTYPE,
)


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
    cells = Cells(res=(15, 15))
    # cells = Cells(ndarray=array_2d)

    cells.randomize_image()
    cells.update_disc()
    print(cells)
    export_pil(cells, "tests/intermediate/test_cells1.png")

    cells.develop(cells, 6, 3, 0.6)

    # for debug:
    export_pil(cells, "tests/intermediate/test_cells3.png")
    # img2 = import_pil(image_name)
    assert False
