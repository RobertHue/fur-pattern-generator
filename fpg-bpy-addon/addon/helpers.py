import bpy
from fpg.generator import flatlist_to_numpy
from fpg.generator import numpy_to_flatlist
from loguru import logger


def get_active_image(context):
    # Get the active image in the Image Editor
    image_editor = next(
        area for area in context.screen.areas if area.type == "IMAGE_EDITOR"
    )
    active_image = image_editor.spaces.active.image
    if active_image is None:
        raise RuntimeError("No active image in the Image Editor.")
    logger.info("Active image:", active_image.name)
    return active_image


def read_image(context):
    """Reads an image into an numpy array"""
    active_image = get_active_image(context)

    # Make sure the image is packed or loaded
    active_image.use_fake_user = True

    # Get the image's width and height
    width = active_image.size[0]
    height = active_image.size[1]

    # Get the image's pixels as a flat list of (r, g, b, a) values
    pixels = active_image.pixels

    return flatlist_to_numpy(pixels, height, width)


def write_image(context, image):
    """Writes an nu an image into an numpy array"""
    active_image = get_active_image(context)

    # Make sure the image is packed or loaded
    active_image.use_fake_user = True

    # Write
    pixels = active_image.pixels
    flatlist = numpy_to_flatlist(image.data)
    pixels[:] = flatlist

    # Update the image data
    active_image.update()
