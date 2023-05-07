# Python Module Index
import colorsys
import random

# Blender
import bpy

# 3rd Party
import cv2
import numpy as np


class Cells:
    """
    This class defines the cells of the Cellular Automata (CA).
    """

    def __init__(self, image, discriminator_color):
        self.width  = image.width()
        self.height = image.height()
        self.disc = [[0.0
            for i in range(self.width)]
            for j in range(self.height)]

        self.visited = [[0
            for i in range(self.width)]
            for j in range(self.height)]

        self.cells = [["D"
            if image.getPixel_HSV(i,j)[0] == discriminator_color[0] and
               image.getPixel_HSV(i,j)[1] == discriminator_color[1] and
               image.getPixel_HSV(i,j)[2] == discriminator_color[2]
            else 'U'
            for i in range(self.width)]
            for j in range(self.height)]

    def set_disc(self, u, v, disc):
        self.disc[v][u] = disc

    def get_disc(self, u, v):
        return self.disc[v][u]

    def increase_visits(self, u, v):
        self.visited[v][u] += 1

    def set_visited(self, u, v):
        self.visited[v][u] = 1

    def got_visited(self, u, v):
        if self.visited[v][u] > 0:
            return True
        else:
            return False

    def reset_visited(self):
        self.visited = [[0 for i in range(self.width)]
            for j in range(self.height)]

    def set(self, u, v, state):
        self.cells[v][u] = state

    def get(self, u, v):
        return self.cells[v][u]

    def reset(self):
        self.cells = [[0 for i in range(self.width)]
            for j in range(self.height)]

    def print(self):
        print()
        print("print: ")
        for row in self.cells[::-1]:
            print('[', end='')
            for val in row:
                print('{:1}'.format(val), end='')
            print(']')
        print()

    def print_visits(self):
        print()
        print("printVisits: ")
        for row in self.visited[::-1]:
            print('[', end='')
            for val in row:
                if (val >= 1):
                    print('{:2}'.format(val), end='')
                elif (val == 0):
                    print('{:2}'.format(' '), end='')
                else:
                    print('{:2}'.format('E'), end='')
            print(']')
        print()

    def print_discs(self):
        print()
        print("print discriminators: ")
        for row in self.disc[::-1]:
            print('[', end='')
            for d in row:
                if d > 0:
                    print('{:2}'.format('+'), end='')
                elif d < 0:
                    print('{:2}'.format('-'), end='')
                else:
                    print('{:2}'.format(' '), end='')
            print(']')
        print()


class Image:
    """
    Pass an image file loaded into Blender when creating an Image-object.
    """
    def __init__(self, image_file):
        self._img = bpy.data.images[image_file]

    def width(self):
        return self._img.size[0]

    def height(self):
        return self._img.size[1]

    def export_cv(self):
        pixel_list = list(self._img.pixels)
        rgb_pixels = [x for i, x in enumerate(pixel_list) if (i+1)%4 != 0]
        a = np.array(rgb_pixels)
        b = np.reshape(a, (self.height(), self.width(), 3))
        rgba = np.ones((self.height(), self.width(), 3), dtype=np.uint8)
        rgba[:,:,:] = np.uint8(b) * 255
        cv_image = np.flip(rgba, axis=[0, 2])
        return np.float32(cv_image)

    def import_cv(self, cv_image):
        rgb = np.flip(cv_image, axis=[0, 2])
        rgba = np.ones((self.height(), self.width(), 4), dtype=np.float32)
        rgba[:,:,:-1] = np.float32(rgb) / 255
        self._img.pixels = rgba.flatten()

    def is_coord_valid(self, x, y):
        """
        Returns 'True', if the supplied coordinates
        are in the Image. Otherwhise returns 'False'.
        """
        if x >= 0 and x < self._img.size[0] and \
           y >= 0 and y < self._img.size[1]:
            return True
        return False

    def get_pixel_rgba(self, x, y):
        """
        Gets the pixel's color at 'x' 'y' as RGBA.
        If no valid coords 'x' and 'y' are supplied, then [0,0,0,0] is returned.
        """
        if self.is_coord_valid(x, y):
            index = (y * self.width() + x) * 4
            cell = self._img.pixels[index:index+4]
            return cell
        return [0,0,0,0]

    def get_pixel_hsv(self, x, y):
        """
        Gets the pixel's color at 'x' 'y' as HSV.
        If no valid coords 'x' and 'y' are supplied, then [0,0,0,0] is returned.
        """
        if self.is_coord_valid(x, y):
            rgba = self.get_pixel_rgba(x, y)
            hsv  = colorsys.rgb_to_hsv(rgba[0], rgba[1], rgba[2])
            return hsv
        return [0,0,0,0]

    def set_pixel_rgba(self, x, y, rgba):
        """
        Sets the pixel's color at 'x' 'y' with RGBA.
        If no valid coords 'x' and 'y' are supplied, then only 'False' is returned.
        """
        if self.is_coord_valid(x, y):
            index = (y * self.width() + x) * 4
            self._img.pixels[index:index+4] = rgba
            return True
        return False

    def set_pixel_hsv(self, x, y, hsv):
        """
        Sets the pixel's color at 'x' 'y' with HSV.
        If no valid coords 'x' and 'y' are supplied, then only 'False' is returned.
        """
        if self.is_coord_valid(x, y):
            rgb  = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
            rgba = list(rgb)
            rgba.append(1)
            return self.set_pixel_rgba(x, y, rgba)
        return False


def draw_circle(image, color, x, y, radius):
    """
    Draws a circle into image.
    """
    # Reading an image in default mode
    cv_img = (image.export_CV())

    # draw a circle as mask
    center_coordinates = (x, y)
    thickness = 1
    new_img = cv2.circle(cv_img, center_coordinates, radius, color, thickness)

    # write back image with circle into image
    image.import_CV(new_img)


def get_circular_neighborhood(image, source_pixel, radius):
    """Gets the Circular neighborhood as a list of pixels including the source pixel."""
    # create mask with zeros
    mask = np.zeros((image.height(), image.width(), 3), dtype=np.uint8)

    # define a circle as mask
    x, y  = [source_pixel[i] for i in (0, 1)]
    center_coordinates = (x, y)
    color = (255,255,255)
    thickness = cv2.FILLED
    cv2.circle(mask, center_coordinates, radius, color, thickness)
    result_n = np.argwhere(mask == (255,255,255))
    return result_n


def get_moore_neighborhood(image, cells, source_pixel, radius):
    """Gets the Moore neighborhood as a list of pixels including the source pixel."""
    moore_lookup = [[1,0],[-1,0],[0,1],[0,-1], [1,1], [-1,-1], [1,-1], [1,-1]]
    result_n = []  # the neighboorhood result
    queue = []  # create a queue for BFS
    cells.resetVisited()  # to memorize that the cell has been visited once

    # Are coords inside the image; hence valid?
    x, y  = [source_pixel[i] for i in (0, 1)]
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
            # if a adjacent has not been visited, then mark it visited and enqueue it
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


def count_d_cells(image: Image, cells: Cells, pos, r):
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
        cell_info = cells.get(x, y)
        if cell_info == "D":
            cell_count += 1

    return cell_count


def rgb2hsv(rgb):
    hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    return list(hsv)


def generate_random(image, rgb_color_d, rgb_color_u):
    # create random image
    color_d = rgb2hsv(rgb_color_d)
    color_u = rgb2hsv(rgb_color_u)
    print("color_d: ", color_d)
    print("color_u: ", color_u)

    for u in range(image.height()):
        for v in range(image.width()):
            rand = random.randint(0,1)
            if rand == 0:
                image.set_pixel_hsv(u, v, color_d)
            else:
                image.set_pixel_hsv(u, v, color_u)


def cellular_automata(image, r_activator, r_inhibitor, w, rgb_color_d, rgb_color_u):
    """Cellular Automata (CA) by David Young

    Args:
        image (_type_): _description_
        r_activator (_type_): _description_
        r_inhibitor (_type_): _description_
        w (_type_): _description_
        rgb_color_D (_type_): _description_
        rgb_color_U (_type_): _description_
    """
    # we need to know the image dimensions
    width  = image.width()
    height = image.height()
    print("Image size: ", width, " x ", height)
    print("w: ", w)

    color_d = rgb2hsv(rgb_color_d)
    color_u = rgb2hsv(rgb_color_u)
    print("color_D: ", color_d)
    print("color_U: ", color_u)

    cells = Cells(image, color_d)
    # 1st pass : calculate cells Disc and apply cells-set
    print("1st pass start")
    for u in range(height):
        for v in range(width):
            cells.reset_visited()
            activators = count_d_cells(image, cells, [u, v], r_activator)
            # cells.printVisits()

            cells.reset_visited()
            inhibitors = count_d_cells(image, cells, [u, v], r_inhibitor) - activators
            # cells.printVisits()

            # This computation happens to all cells at the same time,
            # therefore we must defer the setting of the color to a 2nd step.
            disc = activators - w * inhibitors
            cells.set_disc(u, v, disc)
    cells.print_discs()
    cells.print()
    print("2nd pass start")
    # 2nd pass : apply cells to image:
    for u in range(height):
        for v in range(width):
            d = cells.get_disc(u, v)
            if d > 0:
                cells.set(u, v, "D")
                image.set_pixel_hsv(u, v, color_d)
            elif d < 0:
                cells.set(u, v, "U")
                image.set_pixel_hsv(u, v, color_u)
    cells.print_discs()
    cells.print()
    print("finished")
