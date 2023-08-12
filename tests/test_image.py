# from typing import Any
# from typing import SupportsFloat

import pytest
import numpy as np

from fpg.generator.image import Image
from fpg.generator.image import export_pil
from fpg.generator.image import import_pil


from fpg.generator.colors import RGB_Color
from fpg.generator.colors import NP_RGBA_DTYPE

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
        (0, 0, (244, 222, 111, 255)),
        (0, 1, (244, 222, 111, 255)),
        (1, 2, (244, 222, 111, 255)),
        (1, 3, (244, 222, 111, 255)),
        (2, 3, (244, 222, 111, 255)),
    ),
)
def test_get_color(x: int, y: int, expected: RGB_Color) -> None:
    img = Image(ndarray=array_2d)
    print("img: ", img)
    rgba_col = img.get_color(x, y)
    assert rgba_col[0] == expected[0]
    assert rgba_col[1] == expected[1]
    assert rgba_col[2] == expected[2]
    assert rgba_col[3] == expected[3]


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, (244, 222, 111, 255)),
        (0, 1, (244, 222, 111, 255)),
        (1, 2, (244, 222, 111, 255)),
        (1, 3, (244, 222, 111, 255)),
        (2, 3, (244, 222, 111, 255)),
    ),
)
def test_set_color(x: int, y: int, expected: RGB_Color) -> None:
    # Define the values for the array and create a 2D numpy array
    img = Image(ndarray=array_2d)
    print("img: \n", img)
    img.set_color(x, y, expected)
    rgba_col = img.get_color(x, y)
    print("t array_2d: ", type(array_2d))
    print("t array_2d: ", array_2d[0, 0])
    print("t: ", img.data.dtype)
    print("rgba_col: ", rgba_col)
    print("t rgba_col: ", type(rgba_col))
    print("t rgba_col: ", type(rgba_col[0]))
    print("expected: ", expected)
    print("t expected: ", type(expected))
    print("t expected: ", type(expected[0]))
    assert rgba_col[0] == expected[0]
    assert rgba_col[1] == expected[1]
    assert rgba_col[2] == expected[2]
    assert rgba_col[3] == expected[3]


def test_randomize() -> None:
    # Define the values for the array and create a 2D numpy array
    img = Image(ndarray=array_2d)

    img.randomize_image()
    for y in range(img.height):
        for x in range(img.width):
            origin_item = array_2d[y][x]
            rand_item = img.get_color(x, y)
            assert origin_item[0] == rand_item[0]
            assert origin_item[1] == rand_item[1]
            assert origin_item[2] == rand_item[2]
            assert origin_item[3] == rand_item[3]


def test_import_export_pil() -> None:
    # Define the values for the array and create a 2D numpy array
    image_name = "tests/intermediate/test_image.png"
    img1 = Image(ndarray=array_2d)
    # img1.randomize_image()
    print(repr(img1))

    export_pil(img1, image_name)
    img2 = import_pil(image_name)
    print(repr(img2))

    # assert (img1.data == img2.data).all()
    for e, x in zip(img1.data, img2.data):
        print(f"\n{e=} \n\n {x=}\n")
        assert (e == x).all()
