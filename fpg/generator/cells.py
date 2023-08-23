import colorsys
import random
from io import StringIO

import numpy as np
import numpy.typing as npt

from loguru import logger
from PIL import Image as im

from .colors import D_THRESHOLD
from .colors import RGBA_COLOR_D
from .colors import RGBA_COLOR_U
from .colors import RGB_Color
from .image import Image


NumpyType = npt.NDArray
import fpg.generator.neighborhood as nh


class Cells(Image):
    """
    This class defines the cells of the Cellular Automata (CA).
    """

    def __init__(
        self,
        nstrategy: nh.NeighborStrategy = nh.NeumannStrategy(),
        d_color: RGB_Color = RGBA_COLOR_D,
        u_color: RGB_Color = RGBA_COLOR_U,
        ndarray: NumpyType | None = None,
        res: tuple[int, int] | None = None,
    ) -> None:
        super().__init__(ndarray, res)
        self._disc = np.zeros(self._img.shape, dtype=np.float32)
        self._nstrategy = nstrategy
        self._d_color = d_color
        self._u_color = u_color

    @property
    def d_color(self) -> RGB_Color:
        return self._d_color

    @property
    def u_color(self) -> RGB_Color:
        return self._u_color

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

    def show_cells(self) -> None:
        pil = im.fromarray(self.data, mode="RGBA")
        pil.show()

    def print_visits(self) -> None:
        logger.info("visited:\n", self._visited)

    def print_discs(self) -> None:
        result = StringIO()
        result.write("\n")
        result.write("print discriminators: ")
        for row in self._disc:
            result.write("[")
            for d in row:
                if d > 0:
                    result.write(" +")
                elif d < 0:
                    result.write(" -")
                else:
                    result.write("  ")
            result.write("]")
        result.write("\n")
        logger.info(result.read())

    ############################################################################

    def develop(self, RA: int, RI: int, w: float) -> None:
        """Develop the next generation of Cells.

        Note:
            Is done by using the Cellular Automata (CA) by David Young.

        Args:
            RA (int): the radius of the activator cells
            RI (int): the radius of the inhibitor cells
            w (float): the weight of the inhibitor RI. Whereas RA has a fixed
                weight of 1 for simplicity.
        """
        # plausibility check for radius
        if RA >= RI:
            raise ValueError(
                f"Activator radius {RA=} should be less than the inhibitor"
                f"radius {RI=}!"
            )

        # 1st pass : calculate cells Disc and apply cells-set
        logger.info("1st pass start - calculate cells Disc and apply cells-set")
        self.update_discs(RA, RI, w)

        # 2nd pass : apply cells to image:
        logger.info("2nd pass start - apply cells to image")
        for y in range(self.height):
            for x in range(self.width):
                pos = (x, y)
                d = self.get_disc(*pos)
                if d > 0:
                    self.set_color(*pos, self.d_color)
                elif d < 0:
                    self.set_color(*pos, self.u_color)

        logger.info("finished")

    def update_discs(self, RA: int, RI: int, w: float) -> None:
        for y in range(self.height):
            for x in range(self.width):
                pos = (x, y)
                AD = self.count_d_cells(pos, RA)  # radius/circle
                ID = self.count_d_cells(pos, RI) - AD  # ring

                # This computation happens to all cells at the same time,
                # therefore we must defer the setting of the color to a 2nd step
                disc = AD - (w * ID)
                # logger.debug("activators: ", AD)
                # logger.debug("inhibitors: ", ID)
                # logger.debug("disc: ", disc)
                self.set_disc(*pos, disc)

    def count_d_cells(self, pos: tuple[int, int], distance: int) -> int:
        """Counts the D cells at position pos in a given radius."""
        cell_count = 0
        region = self._nstrategy.get_neighborhood(self, pos, distance)

        for pos in region:
            cell_color = self.get_color(*pos)
            # D cell if the HSVA-colors value threshold is exceeded
            cell_color_adjusted = np.array(
                [*cell_color],
                dtype=np.float64,
            )
            cell_color_adjusted = np.divide(cell_color_adjusted, 255)
            rgb = cell_color_adjusted[:3]
            _, _, v = colorsys.rgb_to_hsv(*rgb)
            if v <= D_THRESHOLD:
                cell_count += 1
        return cell_count

    def randomize(self) -> None:
        """Randomizes the image with U & D pixels."""
        for y in range(self.height):
            for x in range(self.width):
                random_bool = random.choice([True, False])
                if random_bool is True:
                    self.set_color(x, y, self.d_color)
                else:
                    self.set_color(x, y, self.u_color)
