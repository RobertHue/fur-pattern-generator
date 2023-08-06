import bpy

from . import operators
from . import properties as props


class FPG_PT_ui(bpy.types.Panel):
    """Creates a Panel in the Image Editor window"""

    bl_idname = "FPG_PT_ui"
    #  this variable is a label/name that is displayed to the user
    bl_label = "Fur Generator Ui"
    # variable for determining which view this panel will be in
    bl_space_type = "IMAGE_EDITOR"
    # this variable tells us where in that view it will be drawn
    bl_region_type = "UI"
    # this context variable tells when it will be displayed, edit mode, object mode etc
    bl_context = ""
    # category is esentially the main UI element, the panels inside it are
    # collapsible dropdown menus drawn under a category
    # you can add your own name, or an existing one and it will be drawn accordingly
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        # obj = context.object

        layout.label(
            text="Active texture is:    " + context.edit_image.name,
            icon="IMAGE",
        )

        # place a buttons into the layout to call operators
        layout.separator()
        layout.label(text="generators:")
        layout.operator("fpg.ca_young")

        material = bpy.data.materials[0]
        layout.prop(material.my_settings, "r_activator")
        layout.prop(material.my_settings, "r_inhibitor")
        layout.prop(material.my_settings, "w")
        layout.prop(material.my_settings, "color_D")
        layout.prop(material.my_settings, "color_U")

        layout.operator("fpg.generate_random")

        # layout.operator("fpg.generate_random_mathutils")


def register():
    from bpy.utils import register_class

    register_class(FPG_PT_ui)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(FPG_PT_ui)
