# 3rd Party
import numpy as np

# own libraries
from .colors import HSV_COLOR_D, HSV_COLOR_U
from .cells import Cells
from .cells import count_d_cells


def cellular_automata(
    image: type[np.array], r_activator: int, r_inhibitor: int, w: float
) -> None:
    """Cellular Automata (CA) by David Young.

    Args:
        image (list[COLOR]): _description_
        r_activator (int): _description_
        r_inhibitor (int): _description_
        w (float): _description_
    """
    # we need to know the image dimensions
    width = image.width()
    height = image.height()
    print("Image size: ", width, " x ", height)
    print("w: ", w)

    cells = Cells(image, HSV_COLOR_D)
    # 1st pass : calculate cells Disc and apply cells-set
    print("1st pass start")
    for u in range(height):
        for v in range(width):
            cells.reset_visited()
            activators = count_d_cells(image, cells, [u, v], r_activator)
            # cells.printVisits()

            cells.reset_visited()
            inhibitors = (
                count_d_cells(image, cells, [u, v], r_inhibitor) - activators
            )
            # cells.printVisits()

            # This computation happens to all cells at the same time,
            # therefore we must defer the setting of the color to a 2nd step.
            disc = activators - w * inhibitors
            cells.set_disc(u, v, disc)
    cells.print_discs()
    cells.print_cells()
    print("2nd pass start")
    # 2nd pass : apply cells to image:
    for u in range(height):
        for v in range(width):
            d = cells.get_disc(u, v)
            if d > 0:
                cells.set_cell(u, v, "D")
                image.set_pixel_hsv(u, v, HSV_COLOR_D)
            elif d < 0:
                cells.set_cell(u, v, "U")
                image.set_pixel_hsv(u, v, HSV_COLOR_U)
    cells.print_discs()
    cells.print_cells()
    print("finished")
