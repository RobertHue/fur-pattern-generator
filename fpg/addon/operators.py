import bpy
import fpg.generator as fpg


print(
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
        image = fpg.Image(context.edit_image.name)
        imageData = bpy.data.materials[0]
        fpg.cellular_automata(
            image,
            imageData.my_settings.r_activator,
            imageData.my_settings.r_inhibitor,
            imageData.my_settings.w,
            imageData.my_settings.color_D,
            imageData.my_settings.color_U,
        )
        return {"FINISHED"}


class FPG_OT_generate_random(bpy.types.Operator):
    """generates random noise"""

    bl_idname = "fpg.generate_random"
    bl_label = "Random Noise"

    def execute(self, context):
        image = fpg.Image(context.edit_image.name)
        imageData = bpy.data.materials[0]
        print(
            "imageData.my_settings.color_D: ",
            imageData.my_settings.color_D[0],
            ", ",
            imageData.my_settings.color_D[1],
            ", ",
            imageData.my_settings.color_D[2],
            ", ",
        )
        print(
            "imageData.my_settings.color_U: ",
            imageData.my_settings.color_U[0],
            ", ",
            imageData.my_settings.color_U[1],
            ", ",
            imageData.my_settings.color_U[2],
            ", ",
        )
        fpg.generate_random(
            image, imageData.my_settings.color_D, imageData.my_settings.color_U
        )
        return {"FINISHED"}


# class FPG_OT_generate_random_mathutils(bpy.types.Operator):
# 	"""TBD"""
# 	bl_idname = "fpg.generate_random_mathutils"
# 	bl_label = "TBD"

# 	def execute(self, context):
# 		image = fpg.Image(context.edit_image.name)
# 		# create random image
# 		for u in range(image.height()):
# 			for v in range(image.width()):
# 				print("vec: ", Vector((u,v,0)))
# 				image.setPixel_HSV(u, v, Vector((u,v,0)))
# 		return {'FINISHED'}


classes = (FPG_OT_cellular_automata, FPG_OT_generate_random)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        unregister_class(cls)
