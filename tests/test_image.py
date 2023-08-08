# from typing import Any
# from typing import SupportsFloat

import pytest

from fpg.generator import Image


####################
#       INIT       #
####################


@pytest.mark.parametrize(
    ("coords"),
    (
        [-4, 5],
        [111, 5],
    ),
)
def test_validate_coords(coords: list[int]) -> None:
    width = 100
    height = 100
    img = Image(width, height)
    with pytest.raises(ValueError):
        img.validate_coords(*coords)
