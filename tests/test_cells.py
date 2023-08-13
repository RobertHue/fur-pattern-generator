# from typing import Any
# from typing import SupportsFloat

import pytest
import numpy as np

from fpg.generator.cells import Cells
from fpg.generator.cells import cell_neighbors
from fpg.generator.cells import cellular_automata
from fpg.generator.image import Image
from fpg.generator.image import export_pil
from fpg.generator.image import import_pil
from fpg.generator.colors import RGB_Color

from fpg.generator.colors import HSV_COLOR_D
from fpg.generator.colors import HSV_COLOR_U
from fpg.generator.colors import NP_RGBA_DTYPE
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
    cells = Cells(res=(16, 16))
    # cells = Cells(ndarray=array_2d)
    cells.randomize_image()
    cells.update_disc()
    cellular_automata(cells, 6, 3, 0.6)

    # for debug:
    image_name = "tests/intermediate/test_cells1.png"
    export_pil(cells, image_name)
    # img2 = import_pil(image_name)
