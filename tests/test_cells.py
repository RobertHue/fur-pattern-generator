# from typing import Any
# from typing import SupportsFloat

import numpy as np

import pytest
from fpg.generator.cells import Cells
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.colors import NP_RGBA_COLOR_D
from fpg.generator.colors import NP_RGBA_COLOR_U
from fpg.generator.colors import RGBA_COLOR_D
from fpg.generator.colors import RGBA_COLOR_U
from fpg.generator.image import export_pil
from fpg.generator.image import import_pil
from PIL import Image as im


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


moore_0_0_r0 = [(0, 0)]
moore_0_0_r1 = [*moore_0_0_r0, (0, 1), (1, 0), (1, 1)]
moore_0_0_r2 = [*moore_0_0_r1, (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]

moore_3_2_r0 = [(3, 2)]
moore_3_2_r1 = [
    *moore_3_2_r0,
    (2, 1),
    (3, 1),
    (4, 1),
    (2, 2),
    (4, 2),
    (2, 3),
    (3, 3),
    (4, 3),
]


@pytest.mark.parametrize(
    ("ndarray", "pos", "distance", "expected"),
    (
        (array_2d, (0, 0), 0, moore_0_0_r0),
        (array_2d, (0, 0), 1, moore_0_0_r1),
        (array_2d, (0, 0), 2, moore_0_0_r2),
        #####
        (array_2d, (3, 2), 0, moore_3_2_r0),
        (array_2d, (3, 2), 1, moore_3_2_r1),
    ),
)
def test_get_moore_neighborhood(
    ndarray: NP_RGBA_DTYPE, pos: tuple[int, int], distance: int, expected: int
) -> None:
    cells = Cells(ndarray=ndarray)
    result = cells.get_moore_neighborhood(pos, distance)
    print("pos: ", pos)
    print("distance: ", distance)
    print("result: ", result)
    print("expected: ", expected)
    assert len(result) == len(expected)
    assert set(result) == set(expected)


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
# def test_set_color() -> None:
#     # Define the values for the array and create a 2D numpy array
#     cells = Cells(res=(15, 15))
#     # cells = Cells(ndarray=array_2d)

#     cells.randomize_image()
#     cells.update_disc()
#     export_pil(cells, "tests/intermediate/test_cells1.png")

#     cells.develop(cells, 6, 3, 0.6)
#     print(cells)

#     # for debug:
#     export_pil(cells, "tests/intermediate/test_cells3.png")
#     # img2 = import_pil(image_name)
#     assert False
