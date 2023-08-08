# from typing import Any
# from typing import SupportsFloat

import pytest
import numpy as np

from fpg.generator import Image
from fpg.generator.colors import RGB_Color

####################
#       INIT       #
####################

values = [
    [RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4)],
    [RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4)],
    [RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4)],
    [RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4), RGB_Color(1, 2, 3, 4)],
]


def test_invalid_init() -> None:
    width = 100
    height = 100
    shape = (width, height)
    array_2d = np.array(values)
    with pytest.raises(ValueError):
        _ = Image()
    with pytest.raises(ValueError):
        _ = Image(ndarray=array_2d, shape=shape)


def test_constructor_wh() -> None:
    width = 100
    height = 100
    shape = (width, height)
    img = Image(shape=shape)
    assert img.width == width
    assert img.height == height


def test_constructor_numpy() -> None:
    # Define the values for the array and create a 2D numpy array
    array_2d = np.array(values)
    print(f"{array_2d.shape=}")
    width = 3
    height = 4

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
    shape = (width, height)
    img = Image(shape=shape)
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
    shape = (width, height)
    img = Image(shape=shape)
    img.validate_coords(*coords)


######################
#       GETTER       #
######################


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, RGB_Color(1, 2, 3, 4)),
        (0, 1, RGB_Color(1, 2, 3, 4)),
        (1, 2, RGB_Color(1, 2, 3, 4)),
        (1, 3, RGB_Color(1, 2, 3, 4)),
        (2, 3, RGB_Color(1, 2, 3, 4)),
    ),
)
def test_get_color(x: int, y: int, expected: type[RGB_Color]) -> None:
    # Define the values for the array and create a 2D numpy array
    array_2d = np.array(values)
    img = Image(ndarray=array_2d)
    print("img: ", img)
    rgba_col = img.get_color(x, y)
    assert rgba_col.r == expected.r
    assert rgba_col.g == expected.g
    assert rgba_col.b == expected.b
    assert rgba_col.a == expected.a


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, RGB_Color(1, 2, 3, 4)),
        (0, 1, RGB_Color(1, 2, 3, 4)),
        (1, 2, RGB_Color(1, 2, 3, 4)),
        (1, 3, RGB_Color(1, 2, 3, 4)),
        (2, 3, RGB_Color(1, 2, 3, 4)),
    ),
)
def test_set_color(x: int, y: int, expected: type[RGB_Color]) -> None:
    # Define the values for the array and create a 2D numpy array
    array_2d = np.array(values)
    img = Image(ndarray=array_2d)
    img.set_color(x, y, expected)
    rgba_col = img.get_color(x, y)
    assert rgba_col.r == expected.r
    assert rgba_col.g == expected.g
    assert rgba_col.b == expected.b
    assert rgba_col.a == expected.a


def test_randomize() -> None:
    # Define the values for the array and create a 2D numpy array
    array_2d = np.array(values)
    img = Image(ndarray=array_2d)
    img.randomize_image()
    for y in range(img.height):
        for x in range(img.width):
            origin_item = values[y][x]
            rand_item = img.get_color(x, y)
            assert origin_item.r != rand_item.r
            assert origin_item.g != rand_item.g
            assert origin_item.b != rand_item.b
            assert origin_item.a != rand_item.a
