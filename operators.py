from fur_pattern_generator import CA_young, generate_random, image



class FUR_PATTERN_GENERATOR_OT_ca_young(bpy.types.Operator):
		bl_idname = "fur_pattern_generator.ca_young"
		bl_label = "CA Young"

	def execute(self, context):
		image = Image("Image.png")
		CA_young(image)
		return {'FINISHED'}



class FUR_PATTERN_GENERATOR_OT_generate_random(bpy.types.Operator):
	bl_idname = "fur_pattern_generator.generate_random"
	bl_label = "Generate Random"

	def execute(self, context):
		image = Image("Image.png")
		generate_random(image)
		return {'FINISHED'}
