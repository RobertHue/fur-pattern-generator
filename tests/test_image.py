# from typing import Any
# from typing import SupportsFloat

import numpy as np

import pytest
from fpg.generator.colors import NP_RGBA_DTYPE
from fpg.generator.colors import RGB_Color
from fpg.generator.image import Image
from fpg.generator.image import export_pil
from fpg.generator.image import import_pil


####################
#       INIT       #
####################

values = [
    [
        (244, 222, 111, 255),
        (244, 222, 111, 255),
        (244, 222, 111, 255),
    ],
    [
        (244, 222, 111, 255),
        (244, 222, 111, 255),
        (244, 222, 111, 255),
    ],
    [
        (244, 222, 111, 255),
        (244, 222, 111, 255),
        (244, 222, 111, 255),
    ],
    [
        (244, 222, 111, 255),
        (244, 222, 111, 255),
        (244, 222, 111, 255),
    ],
    [
        (244, 222, 111, 255),
        (244, 222, 111, 255),
        (244, 222, 111, 255),
    ],
]

# create a 2D numpy array with defined values
array_2d = np.array(  # ndim: 5 x 3 x 4
    values,
    dtype=NP_RGBA_DTYPE,
)


def test_invalid_init() -> None:
    width = 100
    height = 100
    res = (width, height)
    with pytest.raises(ValueError):
        _ = Image()
    with pytest.raises(ValueError):
        _ = Image(ndarray=array_2d, res=res)


def test_constructor_wh() -> None:
    width = 100
    height = 100
    res = (width, height)
    img = Image(res=res)
    assert img.width == width
    assert img.height == height


def test_constructor_numpy() -> None:
    # Define the values for the array and create a 2D numpy array
    width = 3
    height = 5
    img = Image(ndarray=array_2d)
    assert img.width == width
    assert img.height == height


@pytest.mark.parametrize(
    ("coords"),
    (
        [-4, 5],
        [111, 5],
    ),
)
def test_invalid_coords(coords: list[int]) -> None:
    width = 100
    height = 100
    res = (width, height)
    img = Image(res=res)
    with pytest.raises(ValueError):
        img.validate_coords(*coords)


@pytest.mark.parametrize(
    ("coords"),
    (
        [0, 0],
        [99, 99],
    ),
)
def test_valid_coords(coords: list[int]) -> None:
    width = 100
    height = 100
    res = (width, height)
    img = Image(res=res)
    img.validate_coords(*coords)


######################
#       GETTER       #
######################


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, RGB_Color(244, 222, 111, 255)),
        (0, 1, RGB_Color(244, 222, 111, 255)),
        (1, 2, RGB_Color(244, 222, 111, 255)),
        (1, 3, RGB_Color(244, 222, 111, 255)),
        (2, 3, RGB_Color(244, 222, 111, 255)),
    ),
)
def test_get_color(x: int, y: int, expected: RGB_Color) -> None:
    img = Image(ndarray=array_2d)
    rgba_col = img.get_color(x, y)
    assert rgba_col[0] == expected.r
    assert rgba_col[1] == expected.g
    assert rgba_col[2] == expected.b
    assert rgba_col[3] == expected.a


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, RGB_Color(244, 222, 111, 255)),
        (0, 1, RGB_Color(244, 222, 111, 255)),
        (1, 2, RGB_Color(244, 222, 111, 255)),
        (1, 3, RGB_Color(244, 222, 111, 255)),
        (2, 3, RGB_Color(244, 222, 111, 255)),
    ),
)
def test_set_color(x: int, y: int, expected: RGB_Color) -> None:
    # Define the values for the array and create a 2D numpy array
    img = Image(ndarray=array_2d)
    img.set_color(x, y, expected)
    rgba_col = img.get_color(x, y)
    assert rgba_col[0] == expected.r
    assert rgba_col[1] == expected.g
    assert rgba_col[2] == expected.b
    assert rgba_col[3] == expected.a


def test_randomize() -> None:
    # Define the values for the array and create a 2D numpy array
    img = Image(ndarray=array_2d)

    img.randomize()
    for y in range(img.height):
        for x in range(img.width):
            origin_item = array_2d[y][x]
            rand_item = img.get_color(x, y)
            assert origin_item[0] == rand_item[0]
            assert origin_item[1] == rand_item[1]
            assert origin_item[2] == rand_item[2]
            assert origin_item[3] == rand_item[3]


def test_import_export_pil1() -> None:
    # Define the values for the array and create a 2D numpy array
    image_name = "tests/intermediate/test_image1.png"
    img1 = Image(res=(512, 512))
    img1.randomize()

    export_pil(img1, image_name)
    img2 = import_pil(image_name)

    # assert (img1.data == img2.data).all()
    for e, x in zip(img1.data, img2.data):
        assert e[0] == x[0]
        assert e[1] == x[1]
        assert e[2] == x[2]
        assert e[3] == x[3]


def test_import_export_pil2() -> None:
    image_name = "tests/intermediate/test_image2.png"
    img1 = Image(ndarray=array_2d)
    img1.randomize()

    export_pil(img1, image_name)
    img2 = import_pil(image_name)

    assert (img1.data == img2.data).all()
