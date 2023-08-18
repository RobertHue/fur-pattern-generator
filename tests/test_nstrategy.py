import numpy as np

import pytest
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.colors import RGBA_COLOR_D
from fpg.generator.colors import RGBA_COLOR_U
from fpg.generator.image import Image
from fpg.generator.image import NumpyType
from fpg.generator.neighborhood import CenterType
from fpg.generator.neighborhood import CircularStrategy
from fpg.generator.neighborhood import MooreStrategy
from fpg.generator.neighborhood import NeumannStrategy
from fpg.generator.neighborhood import PosListType
from loguru import logger


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

################################################################################
# MOORE

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
moore_3_2_r2 = [
    *moore_3_2_r1,
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (4, 4),
    (3, 4),
    (2, 4),
    (1, 4),
    (1, 3),
    (1, 2),
    (1, 1),
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
        (array_2d, (3, 2), 2, moore_3_2_r2),
    ),
)
def test_moore_neighborhood(
    ndarray: NumpyType,
    pos: CenterType,
    distance: int,
    expected: PosListType,
) -> None:
    img = Image(ndarray=ndarray)
    nstrategy = MooreStrategy()
    result = nstrategy.get_neighborhood(img, pos, distance)
    logger.debug("pos: ", pos)
    logger.debug("distance: ", distance)
    logger.debug("result: ", result)
    logger.debug("expected: ", expected)
    assert len(result) == len(expected)
    assert set(result) == set(expected)


################################################################################
# NEUMANN

neumann_0_0_r0 = [(0, 0)]
neumann_0_0_r1 = [*neumann_0_0_r0, (1, 0), (0, 1)]
neumann_0_0_r2 = [*neumann_0_0_r1, (2, 0), (1, 1), (0, 2)]

neumann_3_2_r0 = [(3, 2)]
neumann_3_2_r1 = [*neumann_3_2_r0, (3, 1), (4, 2), (3, 3), (2, 2)]
neumann_3_2_r2 = [
    *neumann_3_2_r1,
    (4, 1),
    (5, 2),
    (4, 3),
    (3, 4),
    (2, 3),
    (1, 2),
    (2, 1),
    (3, 0),
]


@pytest.mark.parametrize(
    ("ndarray", "pos", "distance", "expected"),
    (
        (array_2d, (0, 0), 0, neumann_0_0_r0),
        (array_2d, (0, 0), 1, neumann_0_0_r1),
        (array_2d, (0, 0), 2, neumann_0_0_r2),
        #####
        (array_2d, (3, 2), 0, neumann_3_2_r0),
        (array_2d, (3, 2), 1, neumann_3_2_r1),
        (array_2d, (3, 2), 2, neumann_3_2_r2),
    ),
)
def test_neumann_neighborhood(
    ndarray: NumpyType,
    pos: CenterType,
    distance: int,
    expected: PosListType,
) -> None:
    img = Image(ndarray=ndarray)
    nstrategy = NeumannStrategy()
    result = nstrategy.get_neighborhood(img, pos, distance)
    logger.debug("pos: ", pos)
    logger.debug("distance: ", distance)
    logger.debug("result: ", result)
    logger.debug("expected: ", expected)
    assert len(result) == len(expected)
    assert set(result) == set(expected)


################################################################################
# Circular uses the same tests results as neumann but calculates it differently

neumann_0_0_r0 = [(0, 0)]
neumann_0_0_r1 = [*neumann_0_0_r0, (1, 0), (0, 1)]
neumann_0_0_r2 = [*neumann_0_0_r1, (2, 0), (1, 1), (0, 2)]

neumann_3_2_r0 = [(3, 2)]
neumann_3_2_r1 = [*neumann_3_2_r0, (3, 1), (4, 2), (3, 3), (2, 2)]
neumann_3_2_r2 = [
    *neumann_3_2_r1,
    (4, 1),
    (5, 2),
    (4, 3),
    (3, 4),
    (2, 3),
    (1, 2),
    (2, 1),
    (3, 0),
]


@pytest.mark.parametrize(
    ("ndarray", "pos", "distance", "expected"),
    (
        (array_2d, (0, 0), 0, neumann_0_0_r0),
        (array_2d, (0, 0), 1, neumann_0_0_r1),
        (array_2d, (0, 0), 2, neumann_0_0_r2),
        #####
        (array_2d, (3, 2), 0, neumann_3_2_r0),
        (array_2d, (3, 2), 1, neumann_3_2_r1),
        (array_2d, (3, 2), 2, neumann_3_2_r2),
    ),
)
def test_circular_neighborhood(
    ndarray: NumpyType,
    pos: CenterType,
    distance: int,
    expected: PosListType,
) -> None:
    img = Image(ndarray=ndarray)
    nstrategy = CircularStrategy()
    result = nstrategy.get_neighborhood(img, pos, distance)
    logger.debug("pos: ", pos)
    logger.debug("distance: ", distance)
    logger.debug("result: ", result)
    logger.debug("expected: ", expected)
    assert len(result) == len(expected)
    assert set(result) == set(expected)
