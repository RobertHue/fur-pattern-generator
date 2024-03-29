import bpy
from fpg.generator import Cells
from fpg.generator import RGB_Color
from loguru import logger

from .helpers import get_active_image
from .helpers import read_image
from .helpers import write_image


logger.info(
    "__file__={:<35} | __name__={:<20} | __package__={:<20}".format(
        __file__, __name__, str(__package__)
    )
)


# create a property group, this is REALLY needed so that operators
# AND the UI can access, display and expose it to the user to change
# #in here we will have all properties(variables) that is neccessary
# class CustomPropertyGroup(bpy.types.PropertyGroup):
# 	#NOTE: read documentation about 'props' to see them and their keyword
#          arguments
# 	       https://docs.blender.org/api/current/bpy.props.html
# 	float_slider: bpy.props.FloatProperty(name='float value', soft_min=0,
#                 soft_max=10)


class FPG_OT_cellular_automata(bpy.types.Operator):
    """generates a fur pattern through CA Young"""

    bl_idname = "fpg.cellular_automata"
    bl_label = "CA Young"
    bl_options = {"REGISTER", "UNDO"}  # noqa: RUF012

    def execute(self, context):
        # retrieve the material settings
        material = bpy.data.materials[0]
        d = tuple([int(x * 255) for x in material.my_settings.color_D[:]])
        u = tuple([int(x * 255) for x in material.my_settings.color_U[:]])
        logger.debug(f"color: {d=}")
        logger.debug(f"color: {u=}")
        color_D = RGB_Color(*d)
        color_U = RGB_Color(*u)

        # create image from context "texture paint" view
        image_array = read_image(context)
        cells = Cells(d_color=color_D, u_color=color_U, ndarray=image_array)

        # develop next generation
        RA = material.my_settings.r_activator
        RI = material.my_settings.r_inhibitor
        w = material.my_settings.w
        cells.develop(RA, RI, w)
        write_image(context, cells)
        logger.info("FINISHED o/")
        return {"FINISHED"}


class FPG_OT_generate_random(bpy.types.Operator):
    """generates random noise"""

    bl_idname = "fpg.generate_random"
    bl_label = "Random Noise"

    def execute(self, context):
        # retrieve the material settings
        material = bpy.data.materials[0]
        d = tuple([int(x * 255) for x in material.my_settings.color_D[:]])
        u = tuple([int(x * 255) for x in material.my_settings.color_U[:]])
        logger.debug(f"color: {d=}")
        logger.debug(f"color: {u=}")
        color_D = RGB_Color(*d)
        color_U = RGB_Color(*u)

        # randomize new image with given resolution
        active_image = get_active_image(context)
        width = active_image.size[0]
        height = active_image.size[1]
        cells = Cells(res=(width, height))
        cells = Cells(d_color=color_D, u_color=color_U, res=(width, height))
        cells.randomize()
        write_image(context, cells)
        logger.info("FINISHED o/")
        return {"FINISHED"}


classes = (FPG_OT_cellular_automata, FPG_OT_generate_random)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        unregister_class(cls)
