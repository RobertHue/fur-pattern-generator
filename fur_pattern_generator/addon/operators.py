import bpy
from . import fur_pattern_generator as fpg

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
	__file__,__name__,str(__package__)))


class FUR_PATTERN_GENERATOR_OT_ca_young(bpy.types.Operator):
	bl_idname = "fur_pattern_generator.ca_young"
	bl_label = "Fur-Generator: CA Young"

	def execute(self, context):
		image = fpg.Image("Image.png")
		fpg.CA_young(image)
		return {'FINISHED'}



class FUR_PATTERN_GENERATOR_OT_generate_random(bpy.types.Operator):
	bl_idname = "fur_pattern_generator.generate_random"
	bl_label = "Fur-Generator: Random"

	def execute(self, context):
		image = fpg.Image("Image.png")
		fpg.generate_random(context.edit_image)
		return {'FINISHED'}
