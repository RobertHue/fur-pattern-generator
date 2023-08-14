import numpy as np

import pytest
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.colors import RGBA_COLOR_D
from fpg.generator.colors import RGBA_COLOR_U
from fpg.generator.image import Image
from fpg.generator.neighborhood import MooreStrategy

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
def test_get_neighborhood(
    ndarray: NP_RGBA_DTYPE, pos: tuple[int, int], distance: int, expected: int
) -> None:
    img = Image(ndarray=ndarray)
    nstrategy = MooreStrategy()
    result = nstrategy.get_neighborhood(img, pos, distance)
    print("pos: ", pos)
    print("distance: ", distance)
    print("result: ", result)
    print("expected: ", expected)
    assert len(result) == len(expected)
    assert set(result) == set(expected)
