from .image import Image

import numpy as np

import cv2

from .colors import HSV_COLOR_D
from .colors import RGB_Color


class Cells:
    """
    This class defines the cells of the Cellular Automata (CA).
    """

    def __init__(self, image: Image) -> None:
        self._width = image.width
        self._height = image.height
        self._img = image
        self._disc = [
            [0.0 for i in range(self._width)] for j in range(self._height)
        ]

        self._visited = [
            [0 for i in range(self._width)] for j in range(self._height)
        ]

        self._cells = [
            [
                "D"
                if image.get_pixel_hsv(i, j).h == HSV_COLOR_D.h
                and image.get_pixel_hsv(i, j).s == HSV_COLOR_D.s
                and image.get_pixel_hsv(i, j).v == HSV_COLOR_D.v
                else "U"
                for i in range(self._width)
            ]
            for j in range(self._height)
        ]

    def set_disc(self, u: int, v: int, disc) -> None:
        self._disc[v][u] = disc

    def get_disc(self, u: int, v: int) -> float:
        return self._disc[v][u]

    def increase_visits(self, u: int, v: int) -> None:
        self._visited[v][u] += 1

    def set_visited(self, u: int, v: int) -> None:
        self._visited[v][u] = 1

    def got_visited(self, u: int, v: int) -> bool:
        return self._visited[v][u] > 0

    def reset_visited(self) -> None:
        self._visited = [
            [0 for i in range(self._width)] for j in range(self._height)
        ]

    def set_cell(self, u: int, v: int, state: True) -> None:
        self._cells[v][u] = state

    def get_cell(self, u: int, v: int) -> list[list[any]]:
        return self._cells[v][u]

    def reset(self) -> None:
        self._cells = [
            [0 for i in range(self._width)] for j in range(self._height)
        ]

    def print_cells(self) -> None:
        print()
        print("print: ")
        for row in self._cells[::-1]:
            print("[", end="")
            for val in row:
                print(f"{val:1}", end="")
            print("]")
        print()

    def print_visits(self) -> None:
        print()
        print("printVisits: ")
        for row in self._visited[::-1]:
            print("[", end="")
            for val in row:
                if val >= 1:
                    print(f"{val:2}", end="")
                elif val == 0:
                    print("{:2}".format(" "), end="")
                else:
                    print("{:2}".format("E"), end="")
            print("]")
        print()

    def print_discs(self) -> None:
        print()
        print("print discriminators: ")
        for row in self._disc[::-1]:
            print("[", end="")
            for d in row:
                if d > 0:
                    print("{:2}".format("+"), end="")
                elif d < 0:
                    print("{:2}".format("-"), end="")
                else:
                    print("{:2}".format(" "), end="")
            print("]")
        print()


def draw_circle(
    image: type[Image], color: RGB_Color, x: int, y: int, radius: float
) -> None:
    """Draws a circle into image."""
    Image.Image.getdata(image)
    # Reading an image in default mode
    cv_img = image.export_CV()

    # draw a circle as mask
    center_coordinates = (x, y)
    thickness = 1
    new_img = cv2.circle(cv_img, center_coordinates, radius, color, thickness)

    # write back image with circle into image
    image.import_CV(new_img)


def get_circular_neighborhood(
    image: type[Image], source_pixel: list[int, int], radius: float
) -> np.ndarray:
    """Gets the Circular neighborhood as a list of pixels including the source
    pixel."""
    # create mask with zeros
    mask = np.zeros((image.height(), image.width(), 3), dtype=np.uint8)

    # define a circle as mask
    x, y = (source_pixel[i] for i in (0, 1))
    center_coordinates = (x, y)
    color = (255, 255, 255)
    thickness = cv2.FILLED
    cv2.circle(mask, center_coordinates, radius, color, thickness)
    return np.argwhere(mask == (255, 255, 255))


def get_moore_neighborhood(
    image: type[Image],
    cells: Cells,
    source_pixel: list[int, int],
    radius: float,
) -> np.ndarray:
    """Gets the Moore neighborhood as a list of pixels including the source
    pixel."""
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
    cells.resetVisited()  # to memorize that the cell has been visited once

    # Are coords inside the image; hence valid?
    x, y = (source_pixel[i] for i in (0, 1))
    if not image.isValidCoord(x, y):
        return result_n

    # Mark the source_pixel as visited and enqueue it
    coords = source_pixel
    result_n = [coords]
    cells.increaseVisits(x, y)
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
                if not image.isValidCoord(new_x, new_y):
                    continue

                # cell got already visited
                if cells.gotVisited(new_x, new_y):
                    continue

                coords = [new_x, new_y]
                queue.append(coords)
                cells.setVisited(new_x, new_y)
        radius -= 1
    return result_n


def count_d_cells(
    image: type[Image], cells: Cells, pos: list[int, int], r: float
) -> int:
    """
    Counts the D cells at position pos in a given radius r.
    @param cells     empty cell-set that adds additional info to the image
    @param x         x pos of the center
    @param y         y pos of the center
    @param radius    radius
    """
    cell_count = 0

    region_list = get_moore_neighborhood(image, cells, pos, r)

    for region in region_list:
        # update coords:
        x = region[0]
        y = region[1]

        # get pixel
        cell_info = cells.get_cell(x, y)
        if cell_info == "D":
            cell_count += 1

    return cell_count
