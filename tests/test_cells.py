# from typing import Any
# from typing import SupportsFloat

import numpy as np

import pytest
from fpg.generator.cells import Cells
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.colors import RGBA_COLOR_D
from fpg.generator.colors import RGBA_COLOR_U
from fpg.generator.image import export_pil


####################
#       INIT       #
####################


# create a 2D numpy array with defined values
array_2d = np.array(  # 6 x 6
    [
        [
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
        [
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
        [
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
        [
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
        [
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
        [
            RGBA_COLOR_D,
            RGBA_COLOR_D,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
            RGBA_COLOR_U,
        ],
    ],
    dtype=NP_RGBA_DTYPE,
)


@pytest.mark.parametrize(
    ("ndarray", "expected"),
    ((array_2d, 15),),
)
def test_count_cells(ndarray: NP_RGBA_DTYPE, expected: int) -> None:
    cells = Cells(ndarray=ndarray)
    result = cells.count_d_cells((0, 0), 32)
    assert result == expected


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
    cells = Cells(res=(100, 100))
    # # cells = Cells(ndarray=array_2d)
    # cells.randomize()

    # img = import_pil("tests/intermediate/test_cells1.png")
    # cells = Cells(img.data)
    cells.randomize()

    cells.print_discs()
    cells.develop(3, 6, w=0.5)
    cells.print_discs()

    # for debug:
    export_pil(cells, "tests/intermediate/test_cells2.png")
    # img2 = import_pil(image_name)
    # assert False
