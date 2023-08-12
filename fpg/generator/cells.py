import numpy as np

import cv2

from .colors import HSV_COLOR_D
from .colors import RGB_Color
from .image import Image
from typing import Any
from typing import NamedTuple
from .colors import RGBA_COLOR_D
from .colors import RGBA_COLOR_U

from numpy.lib.stride_tricks import as_strided


class Cells(Image):
    """
    This class defines the cells of the Cellular Automata (CA).
    """

    def __init__(self, *args: str, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)
        self._disc = np.zeros(self._img.shape, dtype=np.float32)
        self._visited = np.zeros(self._img.shape, dtype=np.bool_)

    def update_disc(self):
        # for loop can be optimized (by using numpy functs or Cython or something else)
        update_all_cells(self, 3)

    ############################################################################

    def get_disc(self, x: int, y: int) -> float:
        return self._disc[y, x]

    def set_disc(self, x: int, y: int, disc: float) -> None:
        self._disc[y, x] = disc

    ############################################################################

    def get_visited(self, x: int, y: int) -> bool:
        return self._visited[y, x]

    def set_visited(self, x: int, y: int) -> None:
        self._visited[y, x] = True

    def reset_visited(self) -> None:
        self._visited = np.zeros((*self._shape, 1), dtype=np.bool_)

    ############################################################################

    # def print_cells(self) -> None:
    #     print()
    #     print("print: ")
    #     for row in self._cells[::-1]:
    #         print("[", end="")
    #         for val in row:
    #             print(f"{val:1}", end="")
    #         print("]")
    #     print()

    # def print_visits(self) -> None:
    #     print()
    #     print("printVisits: ")
    #     for row in self._visited[::-1]:
    #         print("[", end="")
    #         for val in row:
    #             if val >= 1:
    #                 print(f"{val:2}", end="")
    #             elif val == 0:
    #                 print("{:2}".format(" "), end="")
    #             else:
    #                 print("{:2}".format("E"), end="")
    #         print("]")
    #     print()

    # def print_discs(self) -> None:
    #     print()
    #     print("print discriminators: ")
    #     for row in self._disc[::-1]:
    #         print("[", end="")
    #         for d in row:
    #             if d > 0:
    #                 print("{:2}".format("+"), end="")
    #             elif d < 0:
    #                 print("{:2}".format("-"), end="")
    #             else:
    #                 print("{:2}".format(" "), end="")
    #         print("]")
    #     print()


def update_all_cells(cells: Cells, radius: float) -> int:
    """Counts the D cells at position pos in a given radius."""
    cell_count = 0

    # region_list = get_moore_neighborhood(cells, pos, radius)
    for i in range(cells.width):
        for j in range(cells.height):
            region_list = cell_neighbors(cells, i, j, distance=radius)
            print("region_list: ", region_list)
            print("t region_list: ", type(region_list))

            for region in region_list:
                # update coords:
                x = region[0]
                y = region[1]

                # get pixel
                cell_color = cells._img.get_color(x, y)
                print("cell col: ", cell_color)
                print("RGBA_COLOR_D: ", RGBA_COLOR_D)
                if cell_color == RGBA_COLOR_D:
                    cell_count += 1

    return cell_count


def sliding_window(arr, window_size):
    """Construct a sliding window view of the array"""
    print(arr)
    print(type(arr))
    arr = np.asarray(arr)
    print(arr)
    print(type(arr))
    window_size = int(window_size)
    if arr.ndim != 2:
        raise ValueError("need 2-D input")
    if not (window_size > 0):
        raise ValueError("need a positive window size")
    shape = (
        arr.shape[0] - window_size + 1,
        arr.shape[1] - window_size + 1,
        window_size,
        window_size,
    )
    if shape[0] <= 0:
        shape = (1, shape[1], arr.shape[0], shape[3])
    if shape[1] <= 0:
        shape = (shape[0], 1, shape[2], arr.shape[1])
    strides = (
        arr.shape[1] * arr.itemsize,
        arr.itemsize,
        arr.shape[1] * arr.itemsize,
        arr.itemsize,
    )
    return as_strided(arr, shape=shape, strides=strides)


def cell_neighbors(arr, i, j, distance):
    """Return d-th neighbors of cell (i, j)"""
    w = sliding_window(arr, 2 * distance + 1)

    ix = np.clip(i - distance, 0, w.shape[0] - 1)
    jx = np.clip(j - distance, 0, w.shape[1] - 1)

    i0 = max(0, i - distance - ix)
    j0 = max(0, j - distance - jx)
    i1 = w.shape[2] - max(0, distance - i + ix)
    j1 = w.shape[3] - max(0, distance - j + jx)

    return w[ix, jx][i0:i1, j0:j1].ravel()


# def draw_circle(
#     image: type[Image], color: RGB_Color, x: int, y: int, radius: float
# ) -> None:
#     """Draws a circle into image."""
#     Image.Image.getdata(image)
#     # Reading an image in default mode
#     cv_img = image.export_CV()

#     # draw a circle as mask
#     center_coordinates = (x, y)
#     thickness = 1
#     new_img = cv2.circle(cv_img, center_coordinates, radius, color, thickness)

#     # write back image with circle into image
#     image.import_CV(new_img)


# def get_circular_neighborhood(
#     image: type[Image], source_pixel: list[int, int], radius: float
# ) -> np.ndarray:
#     """Gets the Circular neighborhood as a list of pixels including the source
#     pixel."""
#     # create mask with zeros
#     mask = np.zeros((image.height(), image.width(), 3), dtype=np.uint8)

#     # define a circle as mask
#     x, y = (source_pixel[i] for i in (0, 1))
#     center_coordinates = (x, y)
#     color = (255, 255, 255)
#     thickness = cv2.FILLED
#     cv2.circle(mask, center_coordinates, radius, color, thickness)
#     return np.argwhere(mask == (255, 255, 255))


def get_moore_neighborhood(
    cells: Cells,
    pos: tuple[int, int],
    radius: float,
) -> np.ndarray:
    """Gets the Moore neighborhood as a list of pixels around pos."""
    moore_lookup = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [-1, -1],
        [1, -1],
        [1, -1],
    ]
    result_n = []  # the neighboorhood result
    queue = []  # create a queue for BFS
    cells.reset_visited()  # to memorize that the cell has been visited once

    # Are coords inside the image; hence valid?
    x, y = (pos[i] for i in (0, 1))
    if not cells._img.check_coords(x, y):
        return result_n

    # Mark the source_pixel as visited and enqueue it
    coords = pos
    result_n = [coords]
    cells.set_visited(x, y)
    queue.append(coords)

    while radius >= 0 and queue:
        level_size = len(queue)

        while level_size > 0:
            level_size -= 1

            # dequeue a pixel as src_pixel from queue
            src_pixel = queue.pop(0)
            result_n += [src_pixel]

            if not queue:
                radius -= 1

            # get all adjacent pixels of that dequeued src_pixel
            # if a adjacent has not been visited, then mark it visited and
            # enqueue it
            for lookup in moore_lookup:
                new_x = src_pixel[0] + lookup[0]
                new_y = src_pixel[1] + lookup[1]

                # Are valid coords inside the image:
                if not cells._img.check_coords(new_x, new_y):
                    continue

                # cell got already visited
                if cells.get_visited(new_x, new_y):
                    continue

                coords = [new_x, new_y]
                queue.append(coords)
                cells.set_visited(new_x, new_y)
        radius -= 1
    return result_n


def count_d_cells(cells: Cells, pos: tuple[int, int], radius: float) -> int:
    """Counts the D cells at position pos in a given radius."""
    cell_count = 0

    region_list = get_moore_neighborhood(cells, pos, radius)

    for region in region_list:
        # update coords:
        x = region[0]
        y = region[1]

        # get pixel
        cell_color = cells._img.get_color(x, y)
        print("cell col: ", cell_color)
        print("RGBA_COLOR_D: ", RGBA_COLOR_D)
        if cell_color == RGBA_COLOR_D:
            cell_count += 1

    return cell_count
