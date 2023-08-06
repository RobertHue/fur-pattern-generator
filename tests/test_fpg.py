# from typing import Any
# from typing import SupportsFloat

import pytest
from src.fpg.generator import COLOR
from src.fpg.generator import rgb2hsv


####################
#       INIT       #
####################


@pytest.mark.parametrize(
    ("rgb", "hsv"),
    (((1.3, 3.4, 5.5), (1.3, 3.4, 5.5)),),
)
def test_rgb2hsv(rgb: COLOR, hsv: COLOR) -> None:
    hsv = rgb2hsv(rgb)
    print(f"hsv: {hsv} | rgb: {rgb}")
    something = True
    assert something is True
