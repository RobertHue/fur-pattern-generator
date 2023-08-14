import numpy as np
import numpy.typing as npt
from numpy.lib.stride_tricks import as_strided

from PIL import Image as im

from .colors import RGBA_COLOR_D
from .colors import RGBA_COLOR_U
from .image import Image
import math

NumpyType = npt.NDArray


class Cells(Image):
    """
    This class defines the cells of the Cellular Automata (CA).
    """

    def __init__(self, *args: str, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)
        self._disc = np.zeros(self._img.shape, dtype=np.float32)
        self._visited = np.zeros(self._img.shape, dtype=np.uint8)

    @property
    def discs(self) -> NumpyType:
        return self._disc

    @property
    def visited(self) -> NumpyType:
        return self._visited

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
        self._visited = np.zeros(self._img.shape, dtype=np.uint8)

    ############################################################################

    def print_cells(self) -> None:
        pil = im.fromarray(self.data, mode="RGBA")
        pil.show()

    def print_visits(self) -> None:
        print("visited:\n", self._visited)

    def print_discs(self) -> None:
        print()
        print("print discriminators: ")
        for row in self._disc:
            print("[", end="")
            for d in row:
                if d > 0:
                    print(" +", end="")
                elif d < 0:
                    print(" -", end="")
                else:
                    print("  ", end="")
            print("]")
        print()

    ############################################################################

    def develop(self, r_activator: int, r_inhibitor: int, w: float) -> None:
        """Develop the next generation of Cells.

        Note:
            Is done by using the Cellular Automata (CA) by David Young.

        Args:
            r_activator (int): _description_
            r_inhibitor (int): _description_
            w (float): _description_
        """
        # 1st pass : calculate cells Disc and apply cells-set
        print("1st pass start - calculate cells Disc and apply cells-set")
        self.update_discs(r_activator, r_inhibitor, w)

        # 2nd pass : apply cells to image:
        print("2nd pass start - apply cells to image")
        for y in range(self.height):
            for x in range(self.width):
                pos = (x, y)
                d = self.get_disc(*pos)
                if d > 0:
                    self.set_color(*pos, RGBA_COLOR_D)
                elif d < 0:
                    self.set_color(*pos, RGBA_COLOR_U)

        print("finished")

    def update_discs(self, r_activator: int, r_inhibitor: int, w: float) -> int:
        for y in range(self.height):
            for x in range(self.width):
                pos = (x, y)
                AD = self.count_d_cells(pos, r_activator)  # radius/circle
                ID = self.count_d_cells(pos, r_inhibitor) - AD  # ring

                # This computation happens to all cells at the same time,
                # therefore we must defer the setting of the color to a 2nd step.
                disc = AD - w * ID
                # print("activators: ", AD)
                # print("inhibitors: ", ID)
                # print("disc: ", disc)
                self.set_disc(*pos, disc)

    ############################################################################

    def get_neighborhood(
        self,
        pos: tuple[int, int],
        distance: int,
    ) -> np.ndarray:
        """Gets the Moore neighborhood as a list of pixels around pos.

        Note:
            Also see https://mathworld.wolfram.com/CellularAutomaton.html
        """
        moore_lookup = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
        ]
        # neumann_lookup = [
        #     [0, -1],
        #     [1, 0],
        #     [0, 1],
        #     [-1, 0],
        # ]
        result_n = []  # the neighboorhood result
        queue = []  # create a queue for BFS
        self.reset_visited()  # to memorize that the cell has been visited once

        if not self.check_coords(*pos):
            return result_n

        # Mark the source_pixel as visited and enqueue it
        queue.append(pos)
        self.set_visited(*pos)

        while distance >= 0:
            distance -= 1

            level_size = len(queue)
            while level_size > 0:
                level_size -= 1

                # dequeue a pixel as src_pixel from queue
                src_pixel = queue.pop(0)
                result_n += [src_pixel]

                # get all adjacent pixels of that dequeued src_pixel
                # if a adjacent has not been visited, then mark it visited and
                # enqueue it
                for lookup in moore_lookup:
                    new_x = src_pixel[0] + lookup[0]
                    new_y = src_pixel[1] + lookup[1]
                    new_pos = (new_x, new_y)

                    # Are valid coords inside the image:
                    if not self.check_coords(*new_pos):
                        continue

                    # cell got already visited
                    if self.get_visited(*new_pos):
                        continue

                    queue.append(new_pos)
                    self.set_visited(*new_pos)
        return result_n

    def count_d_cells(self, pos: tuple[int, int], distance: int) -> int:
        """Counts the D cells at position pos in a given radius."""
        cell_count = 0
        # TODO - implement strategy or selector for the different neighborhood methods
        # region = self.get_neighborhood(pos, distance)
        region = get_circular_neighborhood(self, pos, distance)
        # print("region: ", type(region))
        # print("region: ", region)

        for pos in region:
            print("pos: ", type(pos))
            print("pos: ", pos)
            cell_color = self.get_color(*pos)
            is_equal = (
                cell_color[0] == RGBA_COLOR_D.r
                and cell_color[1] == RGBA_COLOR_D.g
                and cell_color[2] == RGBA_COLOR_D.b
                and cell_color[3] == RGBA_COLOR_D.a
            )
            if is_equal:
                cell_count += 1
        return cell_count


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


def get_circular_neighborhood(
    image: Image, center: list[int, int], radius: float
) -> np.ndarray:
    """Gets the Circular neighborhood as a list of pixels including the source
    pixel."""
    print("center: ", center)
    print("radius: ", radius)
    center_x, center_y = center
    return [
        (x, y)
        for x in range(center_x - radius, center_x + radius + 1)
        for y in range(center_y - radius, center_y + radius + 1)
        if math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= radius
        and image.check_coords(x, y)
    ]
